# Python Production Worker

A production-style asynchronous Python job worker using Redis.

## Features

- Async job processing with asyncio
- Redis-backed job queue
- Automatic retry with configurable attempts and delay
- Structured JSON logging
- Graceful shutdown using SIGTERM and SIGINT
- Automated tests with pytest and pytest-asyncio
- Environment-based configuration

## Project Structure

```text
python-production-worker/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── logger.py
│   ├── main.py
│   ├── redis_client.py
│   ├── retry.py
│   └── worker.py
├── tests/
│   ├── __init__.py
│   ├── test_config.py
│   ├── test_retry.py
│   └── test_worker.py
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
