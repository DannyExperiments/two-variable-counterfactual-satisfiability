# Reproducibility

Run from the repository root with Python 3.11 or later.

    python3 -I scripts/verify_repository.py
    python3 -I verification/src/replay.py

The standard-library replay checks all 16 response valuation types at dimension four, 65,536 Boolean truth tables, 64 four-vertex coloring systems and all eight vertices of the worked response cube. [Recorded replay](verification/results/replay.txt).

Extract the [offline explorer](visualization/response-cube-explorer.zip) and open index.html. The [GIF renderer](visualization/render.py) uses Python and Pillow with supplied font paths. [Build the paper](paper/BUILD.md).
