from datetime import timedelta


def format_time(time: timedelta) -> str:
    """
    Formats delta time (current time - whatever time has passed) to
    readable time

    :param time: Requires a timedelta type
    :return: A string with a readable time format D HH:MM:SS
    :raises TypeError: If the time parameter is not of type timedelta
    """
    if not isinstance(time, timedelta):
        raise TypeError("Invalid input type. Param 'time' must be a timedelta.")  # NOQA

    SECS_IN_DAYS = 86400

    _dm_days, _dm_seconds = divmod(time.total_seconds(), SECS_IN_DAYS)

    d = f"{int(_dm_days)} days" if _dm_days != 1 else f"{int(_dm_days)} day"
    h, remainder = divmod(_dm_seconds, 3600)
    m, s = divmod(remainder, 60)

    h, m, s = map(lambda v: str(v).zfill(2), map(int, (h, m, s)))

    return f"{d} {h}:{m}:{s}"
