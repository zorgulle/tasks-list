import enum


class Status(enum.Enum):
    TODO = 1
    IN_PROGRESS = 2
    BLOCKED = 3
    DONE = 4


def get_status_name(status):
    match_status = list(filter(lambda s: s == status, Status))
    return match_status.name