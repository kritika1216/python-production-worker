import pytest

from app.worker import process_job


@pytest.mark.asyncio
async def test_process_job():
    job = {
        "id": "test-001",
        "task": "hello",
    }

    result = await process_job(job)

    assert result == "Processed job test-001"
