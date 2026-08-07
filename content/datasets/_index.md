---
title: 'Datasets'
slug: 'datasets'
type: landing

design:
  spacing: '5rem'

sections:
  - block: markdown
    design:
      css_class: page-wide
    content:
      title: 'Datasets'
      text: |
        <p class="page-intro">Original data I have collected, web-scraped or
        obtained from national authorities in the course of my research. Most of
        it is not openly published, so I share it as a public good with
        researchers and master's students, on request.</p>
        <p class="page-intro">Requesting is deliberately a conversation rather
        than a download link: each of these datasets carries assumptions about
        how it was assembled that determine what it can and cannot be used for,
        and I would rather explain them than have the data used in ways it does
        not support. Write to me with a short note on what you have in mind.</p>

  - block: collection
    design:
      view: dataset
      css_class: datasets-list
    content:
      filters:
        folders:
          - datasets
      count: 20
      sort_by: Weight
      sort_ascending: true
---
