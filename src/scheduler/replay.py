"""Replay helpers for the dispatch scheduler."""

DEFAULT_REPLAY_WINDOW_MS = 1500


def replay_span(events, window_ms=DEFAULT_REPLAY_WINDOW_MS):
    """Return the number of events that fit in one replay window."""
    if not events:
        return 0
    return min(len(events), window_ms)
