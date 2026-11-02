---
# The site used to live at /my-website/ as a GitHub Pages project site.
# Those URLs are still in Google; these aliases turn each one into a
# redirect to its replacement instead of a 404, which is what gets the
# old address out of the results and the ranking on to the new one.
aliases:
  - '/my-website/'
  - '/my-website/curriculum/'

# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: '4rem'

# The Spanish and French home pages are _index.es.md and _index.fr.md: keep the
# three in step when editing the text or the news.
sections:
  # Custom block - layouts/_partials/hbx/blocks/home-map/block.html. Name,
  # photo, role, affiliations and profile links come from the author page
  # (content/authors/admin/); everything below is this page's own.
  - block: home-map
    content:
      username: admin
      eyebrow: 'Nigeria · Senegal · Sierra Leone · Chile'
      tagline: 'Development and security economics: norms, schooling and crime.'
      text: |
        I am an applied microeconomist working on development and security. One strand of my research studies how education, technology and institutions change harmful social norms in West Africa, including female genital cutting and child marriage.

        A second strand studies how policing and peacekeeping shape safety and human capital, from beat policing in Chile to UN peacekeeping in Sierra Leone. Across both, I build original geospatial datasets and use quasi-experimental methods to identify causal effects.
      # Newest first.
      news:
        - date: '2026'
          text: '**Boots in the Beat** conditionally accepted at *The Economic Journal*'
        - date: '2026'
          text: 'Postdoctoral researcher at IRD, based at LEDa-DIAL and CES'
        - date: '2026'
          text: 'PhD in Economics, Université Gustave Eiffel (Érudite)'
      button:
        text: Download my CV
        url: uploads/daniel-perez-parra-cv.pdf
      # Countries filled on the map, each with a pulsing point. `country` must
      # match a name in data/world_map.json; `label` is what is printed;
      # `side` puts the label left or right of the point and `dy` nudges it
      # down (negative: up).
      map:
        label: 'Map of the Americas and Africa marking Nigeria, Senegal, Sierra Leone and Chile'
        pins:
          - {country: 'Nigeria', label: 'Nigeria', lon: 8.0, lat: 9.6, side: 'right', dy: 5}
          - {country: 'Senegal', label: 'Senegal', lon: -14.8, lat: 14.6, side: 'left', dy: -4}
          - {country: 'Sierra Leone', label: 'Sierra Leone', lon: -11.8, lat: 8.5, side: 'left', dy: 12}
          - {country: 'Chile', label: 'Chile', lon: -70.8, lat: -33.4, side: 'right', dy: 5}
    design:
      # Sets the section's padding - see `.home-map-section` in custom.css.
      css_class: home-map-section
      # Affiliation logos, in a row under the news.
      institution_logos:
        - filename: ird-mark.png
          url: https://en.ird.fr/
          alt: 'Institut de Recherche pour le Développement (IRD)'
          title: 'Institut de Recherche pour le Développement (IRD)'
        - filename: dauphine-logo.png
          url: https://leda.dauphine.fr/
          alt: 'Université Paris-Dauphine — PSL (LEDa-DIAL)'
          title: 'Université Paris-Dauphine — PSL (LEDa-DIAL)'
        - filename: paris1-logo.png
          url: https://ces.pantheonsorbonne.fr/en
          alt: 'Université Paris 1 Panthéon-Sorbonne (CES)'
          title: 'Université Paris 1 Panthéon-Sorbonne (CES)'
---
