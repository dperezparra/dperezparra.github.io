---
title: "Recherche"
slug: "research"
type: landing

sections:
  - block: collection
    content:
      title: "Documents de travail"
      filters:
        folders:
          - publication
      count: 20
    design:
      view: article-grid
      fill_image: true
      columns: 2
      show_date: false
      show_read_time: true
      show_read_more: true
      css_class: research-papers
  - block: collection
    content:
      title: "Travaux en cours"
      filters:
        folders:
          - ongoing-work
        exclude_featured: false
      sort_by: Weight
      sort_ascending: true
    design:
      view: wip
      css_class: research-wip
---
