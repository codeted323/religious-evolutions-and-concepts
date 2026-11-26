# Religious evolutions and concepts

Two linked pages about the world's religions.

- **[The family tree of belief](index.html)** covers about 670 traditions, from Stone Age burials to modern movements. It has four views: a family tree, shared-trait maps, trait histories and tradition profiles. Each entry carries a fact-check status and its sources.
- **[Shared wisdom](wisdom.html)** gathers moral and practical guidance from eleven traditions. The passages are sorted into *matched* themes (shared by three or more traditions) and *unmatched* ones (distinctive teachings), each grouped by area of life. Every passage cites its translation.

## Files

- `index.html`, `data.json`: the family-tree site
- `wisdom.html`: the shared-wisdom page (self-contained)
- `source/`: the data and build scripts used to generate both pages
  - `source/family-tree/`: tradition data (`data*.txt`), trait taxonomy, audit notes and `build.py` (writes `data.json`)
  - `source/shared-wisdom/`: cited passages (`q.tsv`), theme groupings (`themes.py`), page template and `build.py` (writes `index.html`, published here as `wisdom.html`)

To view locally, serve the folder (for example `python3 -m http.server`) and open `index.html`. The family tree loads `data.json`, so it won't work when opened directly as a file.
