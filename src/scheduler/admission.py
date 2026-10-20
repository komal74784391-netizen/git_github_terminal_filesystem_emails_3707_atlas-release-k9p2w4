"""Admission control for bursty dispatch traffic."""

MAX_INFLIGHT = 48


def admit(queue_depth):
    if queue_depth >= MAX_INFLIGHT:
        return False
    return True
