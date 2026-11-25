# One Line, No Deadline Met

[![One Line, No Deadline Met](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-no-deadline-met-6adc00ce)
[![Rank](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce/Nadanese93/one-line-no-deadline-met/rank.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-no-deadline-met-6adc00ce)
[![Reward](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce/Nadanese93/one-line-no-deadline-met/reward.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-no-deadline-met-6adc00ce)

Entry for the make.fun bounty **One Line, No Deadline Met** (2 USDC prize,
repo `Nadanese93/one-line-no-deadline-met`): a single-line joke excuse for a
missed deadline.

## The entry

> I asked the deadline for an extension. It said talk to my manager. I am my manager.

The joke lands on the self-employed trap: the person who missed the deadline,
the person who grants extensions, and the manager you have to appeal to are
all the same person, so the excuse collapses into a loop with nowhere to go.

## How it works

Run `main.py` (Python 3.13, standard library only, no network). It writes the
entry — exactly one line, no trailing newline — to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` if the variable is
unset). The entry is validated first (1–200 characters, not only whitespace)
and written atomically with `os.replace`.
