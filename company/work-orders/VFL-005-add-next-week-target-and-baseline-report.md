# VFL-005 - Add Next-Week Target And Baseline Report

## Status

Ready

## Objective

Add a next-week realized-volatility target and simple baseline evaluation without weakening the existing next-day validation contract.

## Scope

- Use the generic forward realized-volatility target with `horizon = 5`.
- Label overlapping five-trading-day windows explicitly.
- Generate a separate next-week baseline report.
- Keep next-day and next-week metrics separate.

## Acceptance Criteria

- Tests cover the five-day target alignment.
- Report names and docs make the horizon clear.
- Metrics compare models only within the same horizon.
- Claim boundary remains forecasting-methodology only.
