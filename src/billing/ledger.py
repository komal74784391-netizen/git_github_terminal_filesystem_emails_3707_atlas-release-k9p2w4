"""Ledger helpers for dispatch invoices."""


def reconcile(entries, settled_ids):
    """Return the entries that have not settled yet."""
    return [e for e in entries if e["id"] not in settled_ids]
