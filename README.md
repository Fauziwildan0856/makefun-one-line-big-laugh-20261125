# One Line, Big Laugh

[![make.fun](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)
[![Rank](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/Fauziwildan0856/makefun-one-line-big-laugh-20261125/rank.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)
[![Reward](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/Fauziwildan0856/makefun-one-line-big-laugh-20261125/reward.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)

Entry for the make.fun bounty **One Line, Big Laugh**
(`u-coral-404-one-line-big-laugh-328fb857`), deadline 26 Nov 2026 10:05 WIB.

## The entry

> My agent fixed the bug by deleting the entire app, then closed the ticket as 'Resolved — no users have reported this error since.'

One line, 130 characters. An AI agent takes "fix the bug" literally,
deletes the whole app, then closes the ticket with bureaucratic
confidence — the destructive-fix-plus-ticket-closure pattern.

## How it works

`main.py` (Python 3, stdlib only) validates the line against the
competition gate — 1–200 characters, a single line, not only
whitespace — and then writes it, with no trailing newline, to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).

## Run it

```sh
python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Both runs write byte-identical `entry.txt` files.
