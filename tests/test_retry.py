import asyncio

from app.retry import retry


attempts = 0


@retry(max_retries=3, delay=1)
async def test_job():
    global attempts
    attempts += 1

    print(f"Attempt {attempts}")

    if attempts < 3:
        raise ValueError("Job failed")

    return "Job succeeded"


async def main():
    result = await test_job()
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
