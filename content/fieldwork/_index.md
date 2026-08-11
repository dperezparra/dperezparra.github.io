---
# The site used to live at /my-website/ as a GitHub Pages project site.
# Those URLs are still in Google; these aliases turn each one into a
# redirect to its replacement instead of a 404, which is what gets the
# old address out of the results and the ranking on to the new one.
aliases:
  - '/my-website/fieldwork/'
  - '/my-website/missions/'

title: "Fieldwork"
slug: "fieldwork"
type: landing

sections:
  - block: collection
    content:
      title: "Fieldwork"
      filters:
        folders:
          - missions
      count: 20
      sort_by: Date
      sort_ascending: false
    design:
      # Custom view added at layouts/_partials/views/mission.html: a map of the
      # country with a pin per site, beside the mission details.
      view: mission
---
