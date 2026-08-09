import structlog


structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.add_log_level,
        structlog.processors.JSONRenderer(),
    ]
)


logger = structlog.get_logger()


def log_job_start(job_id: str) -> None:
    logger.info(
        "job_start",
        job_id=job_id,
    )


def log_job_success(job_id: str, duration: float) -> None:
    logger.info(
        "job_success",
        job_id=job_id,
        duration=duration,
    )


def log_job_failure(job_id: str, duration: float, error: str) -> None:
    logger.error(
        "job_failure",
        job_id=job_id,
        duration=duration,
        error=error,
    )