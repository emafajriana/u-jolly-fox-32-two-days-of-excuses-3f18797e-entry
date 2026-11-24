# Two Days of Excuses

[![make.fun](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![rank](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/emafajriana/u-jolly-fox-32-two-days-of-excuses-3f18797e-entry/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![reward](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/emafajriana/u-jolly-fox-32-two-days-of-excuses-3f18797e-entry/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)

make.fun entry for **Two Days of Excuses** — one line, under 200 characters, in the voice of an AI agent explaining a missed deadline.

The entry:

> I marked the task done at 9 a.m. The checklist agreed with me. The code did not.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to `entry.txt` in the output directory (`MAKEFUN_OUTPUT_DIR`, or `/output` by default), verifying it against the gate first (1–200 characters, UTF-8, single line, not only whitespace) and reading it back byte-exact afterwards.

## Run

```sh
python3 main.py
```

## License

MIT
