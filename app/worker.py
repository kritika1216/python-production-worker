import asyncio
import json
import signal
import time

from app.config import settings
from app.logger import log_job_failure, log_job_start, log_job_success
from app.redis_client import create_redis_client
from app.retry import retry


shutdown_requested = False


def handle_shutdown(signum, frame):
    global shutdown_requested
    shutdown_requested = True


@retry(
    max_attempts=settings.retry_count,
    delay=settings.retry_delay,
)
async def process_job(job: dict) -> str:
    await asyncio.sleep(1)

    return f"Processed job {job['id']}"


async def run_worker() -> None:
    global shutdown_requested

    client = create_redis_client()

    while not shutdown_requested:
        result = await client.blpop(settings.queue_name, timeout=1)

        if result is None:
            continue

        _, raw_job = result
        job = json.loads(raw_job)

        job_id = str(job["id"])
        start_time = time.perf_counter()

        log_job_start(job_id)

        try:
            result = await process_job(job)

            duration = time.perf_counter() - start_time
            log_job_success(job_id, duration)

            print(result)

        except Exception as exc:
            duration = time.perf_counter() - start_time
            log_job_failure(
                job_id,
                duration,
                str(exc),
            )

    await client.aclose()


def register_signal_handlers() -> None:
    signal.signal(signal.SIGTERM, handle_shutdown)
    signal.signal(signal.SIGINT, handle_shutdown)


async def main() -> None:
    register_signal_handlers()
    await run_worker()


if __name__ == "__main__":
    asyncio.run(main())