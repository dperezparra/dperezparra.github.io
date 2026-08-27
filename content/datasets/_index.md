---
title: 'Datasets'
slug: 'datasets'
type: landing

design:
  spacing: '5rem'

# One request covers all three - the terms are the same for every record, and
# the couple of exceptions are noted next to the datasets they apply to. It is
# rendered under the catalog by layouts/_partials/views/dataset--start.html,
# which has to reach it from here because that spot is inside the collection
# block.
request:
  title: 'Asking for any of them'
  text: >
    One note covers all three — tell me which you are after and what you are
    working on, and I'll send it over with the code and a walk-through of how
    it was built and what it will and will not support. The only conditions are
    that it is not redistributed and that the original sources are credited.
    The one exception is the Senegalese school census, which is the Ministry of
    Education's to grant, so a request for that one is passed on to them.
  url: 'mailto:daniel.perez-parra@ird.fr?subject=Dataset%20request'
  label: 'Request a dataset'

sections:
  - block: markdown
    design:
      # `datasets-intro` pulls the first record up towards this paragraph.
      css_class: 'page-wide datasets-intro'
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
        not support. Write to me with a short note on what you have in mind —
        I'd be happy to help and guide :)</p>

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
