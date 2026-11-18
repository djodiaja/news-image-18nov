# news-image-18nov

Entry for the [make.fun](https://make.fun) bounty [news-image-20261118](https://make.fun/bounty/news-image-20261118).

[![Competition](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![Rank](https://make.fun/badge/news-image-20261118/djodiaja/news-image-18nov/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![Reward](https://make.fun/badge/news-image-20261118/djodiaja/news-image-18nov/reward.svg)](https://make.fun/bounty/news-image-20261118)

Reference code: `vkeq2szk`

## Approach

Deterministic image copy. The repo ships `entry.png`, a pre-rendered news infographic for 18 November 2026. `main.py` copies it unchanged to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`) using `shutil.copy2`. There are no models, fonts, or network calls at runtime, so every run produces a byte-identical output (verified by SHA-256 across repeated runs).

```
MAKEFUN_OUTPUT_DIR=./out python main.py
```
