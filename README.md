# dperezparra.github.io

Personal academic website of **Daniel Pérez-Parra** — PhD candidate in Economics
at Érudite, Université Gustave Eiffel. Research, teaching and fieldwork on
education, gender and social norms in West Africa.

Built with [Hugo](https://gohugo.io/) and the
[Hugo Blox](https://hugoblox.com/) *Academic CV* template.
Deployed to GitHub Pages on every push to `main`.

---

## Local development

The theme is a **Hugo module**, so you need Go as well as Hugo, and Node for the
Tailwind CSS pipeline. Versions are pinned in `netlify.toml` and
`.github/workflows/deploy.yml` — keep them in sync.

| Tool | Version |
|---|---|
| Hugo **extended** | 0.152.1 |
| Go | 1.21.5 |
| Node | 22 |
| pnpm | 10.14.0 (via `corepack`) |

```bash
pnpm install          # Tailwind CLI + Pagefind
pnpm dev              # hugo server --disableFastRender  ->  http://localhost:1313/
```

To reproduce a production build, including the search index:

```bash
pnpm build:full       # hugo --minify && pagefind --site public
```

Search is **not** available under `pnpm dev` — Pagefind indexes `public/` after
the fact, so you need the full build to test it.

---

## Repository layout

| Path | Purpose |
|---|---|
| `config/_default/` | All site config: `hugo.yaml`, `params.yaml`, `menus.yaml`, `module.yaml`, `languages.yaml` |
| `content/authors/admin/_index.md` | **Profile data.** Role, affiliations, social links. Drives the homepage biography block and the author byline on papers |
| `content/publication/` | Working papers (one folder per paper) |
| `content/ongoing-work/` | Work in progress |
| `content/missions/` | Fieldwork write-ups |
| `content/teaching.md` | Teaching page |
| `content/datasets/_index.md` | Datasets page — a placeholder until there are entries; the file explains how to switch it to a `collection` block |
| `assets/css/custom.css` | Style overrides. **This exact path** — the theme looks for it here |
| `assets/media/icon.png` | Favicon and social-share fallback image (IRD symbol) |
| `assets/media/{ird-mark,dauphine-logo,paris1-logo}.png` | Affiliation logos. All three appear below the CV button on the homepage; IRD alone sits in the navbar |
| `static/uploads/` | PDFs (CV, papers) |
| `layouts/` | **Shadowed theme templates** — see below |

The theme itself lives in the Go module cache and is **not** in this repo.
Never edit it: `hugo mod clean` will wipe your changes. Customise via, in order
of preference — config → front matter → a hook partial in
`layouts/_partials/hooks/{head-start,head-end,body-end,footer-start}/` →
shadowing a theme template by recreating its exact path under `layouts/`.

### Shadowed templates

Four theme files are shadowed. Each is a **verbatim** copy of upstream apart
from changes marked `CUSTOMISED`, and each carries a header comment saying so.

| File | Changes | If you delete it |
|---|---|---|
| `layouts/partials/hbx/blocks/resume-biography/block.html` | **(1)** an `organizations` entry may carry a `group:` list, rendered on one line separated by a dot — this puts the two host labs on a single line under IRD; **(2)** `design.institution_logos` renders a centred logo row below the CV button | Affiliations go back to one per line, and the homepage logo row disappears |
| `layouts/partials/components/headers/navbar.html` | Institution logos just before the search button, from the `header.navbar.institution_logos` list | The navbar logo disappears |
| `layouts/_partials/views/card.html` | **(1)** co-authors listed under the summary, linked via `data/author_links.yaml`; **(2)** the single-author avatar byline removed from the footer | Paper cards show the old first-author-with-avatar byline and no co-author links |
| `layouts/single.html` | **(1)** one dot separator between all authors; **(2)** read time floored at 1, so pages never say "0 minute read" | Authors separate inconsistently and pages read "0 minute read" |

The card changes affect `/research/` only in practice — `/fieldwork/` uses the
same view, but its entries have no `authors`, so both are no-ops there.

Logos are configured in two places, deliberately: `params.yaml` holds the
single IRD mark for the navbar (all three would not fit), while
`content/_index.md` holds all three for the homepage row.

### Added templates (not overrides)

These add to the theme rather than replacing anything, so they carry no upgrade
cost:

| File | Purpose |
|---|---|
| `layouts/_partials/views/wip{,--start,--end}.html` | A `wip` collection view, selected with `design.view: wip`. Used for Work in Progress on `/research/`: title, co-authors, optional status, and an expandable abstract. The built-in `citation` view hard-codes the year and opens with a large gap under the heading. |
| `layouts/_partials/views/mission{,--start,--end}.html` | A `mission` collection view, selected with `design.view: mission`. Used for `/fieldwork/`: a map of the country with a pin per site, beside the dates, headline figures and narrative, with the photograph full width beneath. |
| `layouts/_partials/hooks/head-end/person-jsonld.html` | `schema.org/Person` structured data on the homepage (see the SEO note above). |

Work in Progress ordering comes from `weight` in each
`content/ongoing-work/*/index.md`, with `sort_by: Weight` on the block — the
entries all share one date, so date sorting was arbitrary. An entry with no
`abstract` field shows "Abstract not available yet." — add the field to publish
a real one.

### Adding a fieldwork mission

Create `content/missions/<slug>/index.md` with a `featured.jpg` and this block:

```yaml
fieldwork:
  map: nigeria              # key in data/maps.yaml
  dates: 'November – December 2024'
  sites:
    - {name: 'Abuja',   lat: 9.0765, lon: 7.3986}
    - {name: 'Calabar', lat: 4.9757, lon: 8.3417}
  stats:
    - {value: '10', label: 'focus groups'}
```

Pins are plotted from real coordinates, so they land where the places actually
are. **For a new country**, add its outline to `data/maps.yaml` — that file
documents the exact projection to use, and the outlines come from Natural Earth
(public domain). The map is inline SVG: no mapping library, no JavaScript, and
nothing fetched at run time.

Blocks are mounted from the theme's `blox/<id>/block.html` to
`layouts/partials/hbx/blocks/<id>/block.html`, and `biography` is an alias for
`resume-biography` — hence that path.

The theme's own `header.navbar.logo` is *not* used: it renders at the far left
of the navbar and links to the site home, not to an external institution.

**On upgrading `blox-tailwind`**, diff each file against its new upstream
version and re-apply the one marked change. Deleting either is always safe.

---

## Adding content

Each entry is a **page bundle**: a folder containing `index.md` plus its images.

**A working paper** — create `content/publication/<slug>/index.md`:

```yaml
---
title: >
  Your paper title
summary: >
  * Submitted
authors:
  - Coauthor Name      # display name; add their homepage to data/author_links.yaml
  - admin              # = you, resolves to content/authors/admin
date: "2026-01-01"
hide_date: true        # papers show authors and read time, not a date
publication_types: ["Working Paper"]
publication: Submitted # or e.g. "R&R at The Economic Journal"
slug: "<slug>"
abstract: >
  ...
tags: [Economics of Crime]   # one topic; the card chip shows the first tag
links:
  - type: pdf
    url: "uploads/<file>.pdf"
image:
  filename: "featured.png"
  preview_only: true
share: false
---
```

Work in progress and fieldwork entries follow the same shape under
`content/ongoing-work/` and `content/missions/`.

Notes:

- **Co-authors** are plain display names. A slug (`jane-doe`) only works if
  `content/authors/jane-doe/` exists — otherwise the raw slug is rendered.
- **`author_notes`** (e.g. `["Corresponding author", "", ""]`) renders a tooltip
  next to the matching author. Add it only when at least one entry is non-empty:
  an all-empty array renders nothing but still makes the theme emit a debug
  `console.log` on the page.
- **Featured images** are matched by the glob `*featured*`, which takes priority
  over `image.filename`. Keep exactly one per folder, and set `image.filename`
  to match so the two never disagree.
- **PDF filenames** should be lowercase with hyphens, no spaces.
- **Image format**: photographs → JPEG, ~2000 px on the long edge. Charts, maps
  and other flat-colour figures → PNG (a 256-colour palette PNG is usually far
  smaller than JPEG *and* avoids compression artefacts around text and borders).

---

## Deployment

`.github/workflows/deploy.yml` runs on every push to `main`: build with Hugo,
generate the Pagefind index, publish to GitHub Pages.

`netlify.toml` configures an equivalent Netlify build. `enableGitInfo` is set in
`config/_default/hugo.yaml` and deliberately **not** duplicated as
`HUGO_ENABLEGITINFO` in `netlify.toml` — the two used to disagree.

`.github/workflows/import-publications.yml` converts a root-level
`publications.bib` into `content/publication/` and opens a PR. It is dormant
until such a file is added.

---

## Licence

Site content (text, images, PDFs) © Daniel Pérez-Parra, licensed
[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) — as
configured under `footer.copyright.license` in `config/_default/params.yaml`.
The underlying Hugo Blox template is MIT licensed — see `LICENSE.md`.
