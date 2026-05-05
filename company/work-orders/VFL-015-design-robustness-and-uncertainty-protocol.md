# VFL-015 - Design Robustness And Uncertainty Protocol

## Status

Done

## Lifecycle State

Done

## Risk Lane

Normal

## Objective

Design the Milestone 3 protocol for robustness and uncertainty diagnostics before implementing new analysis code.

## Scope

- Define rolling-window ranking diagnostics.
- Define block-bootstrap error-difference diagnostics.
- Specify input artifacts and generated outputs.
- Preserve the no-overclaim boundary.

## Acceptance Criteria

- Add a protocol document under `docs/`.
- Create implementation work orders for the first diagnostics.
- Do not add new model families in this work order.
- Tests/lint pass after docs/state updates.

## Claim Boundary

This work designs robustness diagnostics. It does not produce new model-performance evidence.

## Canonical Artifact

- `docs/robustness-uncertainty-protocol.md`

## Verification Evidence

- Protocol defines rolling-window ranking diagnostics.
- Protocol defines block-bootstrap error-difference diagnostics.
- Protocol specifies forecast-error panel inputs and generated output columns.
- Protocol preserves the no-trading/no-model-superiority claim boundary.
- `uv run pytest` passed.
- `uv run ruff check .` passed.

## Closeout State

Done. Next work order is `VFL-016 - Implement rolling-window ranking diagnostics`.
