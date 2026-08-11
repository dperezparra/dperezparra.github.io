---
# The site used to live at /my-website/ as a GitHub Pages project site.
# Those URLs are still in Google; these aliases turn each one into a
# redirect to its replacement instead of a 404, which is what gets the
# old address out of the results and the ranking on to the new one.
aliases:
  - '/my-website/research/'
  - '/my-website/publication/'
  - '/my-website/ongoing-work/'
  - '/my-website/publication/public-debt-firm-performance/'

title: "Research"
slug: "research"
type: landing

sections:
  - block: collection
    content:
      title: "Working Papers"
      # This pulls from your publication section:
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
      # Scopes the card sizing in assets/css/custom.css to this block, so the
      # Fieldwork page's cards are left alone.
      css_class: research-papers
  - block: collection
    content:
      title: "Work in Progress"
      filters:
        folders:
          - ongoing-work
        exclude_featured: false
      # Order is set per entry via `weight` in content/ongoing-work/*/index.md
      # rather than by date - the dates are all identical.
      sort_by: Weight
      sort_ascending: true
    design:
      # Custom view added at layouts/_partials/views/wip.html - no year, no
      # trailing publication string, and a much tighter gap under the heading.
      view: wip
      css_class: research-wip
---
