import pytest

from app.retry import retry


attempts = 0


@retry(max_attempts=3, delay=1)
async def run_job():
    global attempts
    attempts += 1

    print(f"Attempt {attempts}")

    if attempts < 3:
        raise ValueError("Job failed")

    return "Job succeeded"


@pytest.mark.asyncio
async def test_retry():
    result = await run_job()

    assert result == "Job succeeded"
    assert attempts == 3

