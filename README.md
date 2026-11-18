# make.fun news-image (Nov 18, 2026)

`main.py` embeds a base64 PNG and writes it to `/output/entry.png`
(override the directory with `MAKEFUN_OUTPUT_DIR`). No dependencies, no network,
output is byte-identical on every run (SHA-256 asserted in the script).

```
python main.py
```

<!-- TODO: paste the official make.fun badge markdown for this bounty here.
     I don't know the exact badge URLs, so none are invented. -->
