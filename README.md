# chess4k-clean

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/ucupverz/chess4k-clean/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/ucupverz/chess4k-clean/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine that fits in 4,096 bytes of Python 3.13 for the make.fun
`tiny-chess-01` bounty. `main.py` is the whole engine: one packed file,
standard library only, deterministic, talking to nothing but the contest
env at `MAKEFUN_ENV_URL`.

0x88 mailbox board with full rules (castling, en passant, promotion),
piece-square evaluation, and iterative-deepening negamax alpha-beta: a
persistent Zobrist transposition table, MVV-LVA ordering, check extension,
late-move reductions, PVS and quiescence. A fixed node budget
(`BU = 300000`), never a clock, so every replay matches move for move.

## Run it

```sh
python run_trial.py --trial tiny-chess-01-kit/practice/trial-0 \
    --engine chess4k_clean/main.py --port 8190 --out res_clean_t0.json
```

Verified: perft startpos d4 = 197281, castling d3 = 15206; trial-0 gauntlet
W W W W D L (4.5 / 6, Elo 1545), slowest move 4551 ms.

`main.py` is `makefun compress` output (LZMA payload + unpacker); the
readable source `engine.py` is git-ignored. Reproduce it with
`node <kit>/cli/makefun.mjs compress engine.py --out main.py`.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
