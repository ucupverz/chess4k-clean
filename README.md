# chess4k_clean

[![tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/competitions/tiny-chess-01)

A chess engine that fits in 4,096 bytes of Python for the make.fun
`tiny-chess-01` bounty. `main.py` is the whole engine: one packed file,
Python 3.13 standard library only, deterministic, and it talks to nothing
but the contest env at `MAKEFUN_ENV_URL`.

## What it does

- **Board**: 0x88 mailbox with per-piece square lists, side to move,
  castling rights, en passant and the halfmove clock. Moves are generated
  pseudo-legally and filtered by a make/test/unmake legality check, so
  castling, en passant and promotion (queen by default, under-promotion
  kept for search) follow the rules.
- **Evaluation**: material plus the competition's piece-square tables,
  rank-mirrored for black, scored from the side to move, with a small
  bishop-pair bonus.
- **Search**: iterative deepening negamax alpha-beta. A persistent
  Zobrist transposition table (depth, exact/lower/upper flag, score and
  best move, mate scores normalised by ply) survives across moves. Move
  order: transposition move, then MVV-LVA captures and promotions, then
  quiets by a history table. Check extension at every node, late-move
  reductions for late quiet moves (reduced search re-run at full depth
  when it beats alpha), principal variation search, and a capture-only
  quiescence search with a stand-pat, full evasions when in check, and a
  depth cap.
- **Budget**: a node count, `BU = 300000`, never a clock. The same
  position gives the same move on every run, so a replayed trial matches.

## Files

| file | what |
| --- | --- |
| `main.py` | the packed entry point (<= 4,096 bytes), the whole engine |
| `engine.py` | the readable source it was packed from, not committed |

`main.py` is `makefun compress` output: an LZMA payload plus its
unpacker. Reproduce it with

    node <kit>/cli/makefun.mjs compress engine.py --out main.py

## Verification

Move generation is checked with perft on the standard suite; the search
was measured on the practice gauntlets (`practice/trial-0`) against the
house engines.

    perft start  d1 20  d2 400  d3 8902  d4 197281
    perft kiwipete d1 48 d2 2039 d3 97862 d4 4085603
    perft pos3  d1 14  d2 191  d3 2812  d4 43238
    perft pos4  d1 6   d2 264  d3 9467  d4 422333
    perft pos5  d1 44  d2 1486 d3 62379 d4 2103487
    perft pos6  d1 46  d2 2079 d3 89890 d4 3894594
    castling position d3 15206

## Grade it locally

    python run_trial.py --trial tiny-chess-01-kit/practice/trial-0 \
        --engine chess4k_clean/main.py --port 8190 --out res_clean_t0.json

It starts the kit's env server, plays the six-game practice gauntlet and
prints W/D/L and the Elo the scorer's anchors give it.

## License

MIT. See `LICENSE`.