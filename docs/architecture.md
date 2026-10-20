# Dispatch architecture

The scheduler feeds the billing ledger through a replay buffer. Vendor shims
live under `vendor/` and mirror upstream packages so builds work offline.
