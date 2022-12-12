from dataclasses import dataclass
from datetime import datetime


@dataclass
class CrontabScheduler:
    """A scheduler based on cron expressions.

    The scheduler can be used to get the next scheduled datetime based on a reference datetime now.

    Attributes:
        expr (str): A valid cron expression (with four parts only, we dont use the fifth part in this bite).
        now (datetime): The reference datetime for which the next datetime should be determined.
        ... hopefully more attributes added by you!

    Raises:
        ValueError: Whenever a value for a cron expression part is not valid.
    """

    expr: str
    now: datetime

    def __iter__(self):
        return self

    def __next__(self) -> datetime:
        # Right now this returns the input datetime now, so you can run all tests and see how it works.
        # However, you are supposed to implement your own logic here to return the next
        # datetime according to the bite description. 
        return self.now