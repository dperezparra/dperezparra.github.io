---
title: 'Datasets'
slug: 'datasets'
type: landing

design:
  spacing: '5rem'

sections:
  # Placeholder until there are entries to list. Deliberately NOT a `collection`
  # block yet: with no entries, that renders a heading above an empty grid.
  #
  # To switch over once the first dataset exists, replace the block below with:
  #
  #   - block: collection
  #     content:
  #       title: 'Datasets'
  #       filters:
  #         folders:
  #           - datasets
  #       count: 20
  #     design:
  #       view: card
  #       columns: 2
  #
  # ...and add each dataset as its own page bundle, e.g.
  # content/datasets/<slug>/index.md (plus an optional featured.png), following
  # the same front-matter shape as content/publication/<slug>/index.md.
  - block: markdown
    design:
      # Aligns this page's column and type size with /research/ and /fieldwork/
      # - see `.page-wide` in assets/css/custom.css.
      css_class: page-wide
    content:
      title: 'Datasets'
      text: |
        <p class="page-intro">Data and replication material from my research
        will be posted here. In the meantime, please
        <a href="mailto:daniel.perezparra@ird.fr">get in touch</a> if you would
        like access to a particular dataset.</p>
---
