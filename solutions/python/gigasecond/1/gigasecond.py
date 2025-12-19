from datetime import datetime, timedelta


def add(moment: datetime) -> datetime:
    """Add a gigasecond (1,000,000,000 seconds) to a datetime."""
    return moment + timedelta(seconds=1_000_000_000)
