# Build the manuscript

The TeX source carries the bibliography inline, with the accompanying `references.bib` providing reusable records. With TeX Live use

```sh
cd paper
latexmk -g -pdf -interaction=nonstopmode -halt-on-error -file-line-error manuscript.tex
```

The distributed PDF was built with Tectonic 0.17.0, seeded TeX resources, and the following fixed source epoch.

```sh
cd paper
env TZ=UTC SOURCE_DATE_EPOCH=1795737600 FORCE_SOURCE_DATE=1 tectonic -C --keep-logs manuscript.tex
```

The `-C` option uses cached resources. Builds that use a different PDF engine may differ in file bytes.
