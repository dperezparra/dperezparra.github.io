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
      tagline: 'Applied Microeconomist and Development Economist: Social Norms, Education and Crime'
      # Logo shown under the tagline (assets/media/).
      logo: {filename: 'ird-logo-full.png', url: 'https://en.ird.fr/', alt: 'Institut de Recherche pour le Développement (IRD)'}
      text: |
        I am an applied microeconomist working on development and security. My research studies how education, technology, institutions and public policy shape social norms, human capital and safety in West Africa and Latin America, combining original geospatial data with quasi-experimental methods.

        I hold a PhD in Economics from Université Gustave Eiffel (Érudite). Before joining IRD, I was a research consultant at the World Bank's Africa Gender Innovation Lab and at the University of Oxford's What Works Hub for Global Education, and a research assistant at Oxford's Centre for the Study of African Economies, where I was also a visiting PhD student. I have also worked as a research assistant at the Universidad Autónoma de Madrid and as an intern at the United Nations Economic Commission for Africa.
      # Newest first.
      news:
        - date: '2026'
          text: '**Boots in the Beat** conditionally accepted at *The Economic Journal*'
        - date: '2026'
          text: 'Postdoctoral researcher at the French National Research Institute for Sustainable Development (IRD)'
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
        # Where the entrance's routes start (home-map block).
        origin: {label: 'Paris', lon: 2.35, lat: 48.86}
        pins:
          - {country: 'Senegal', label: 'Senegal', lon: -14.8, lat: 14.6, side: 'left', dy: -4}
          - {country: 'Sierra Leone', label: 'Sierra Leone', lon: -11.8, lat: 8.5, side: 'left', dy: 12}
          - {country: 'Nigeria', label: 'Nigeria', lon: 8.0, lat: 9.6, side: 'right', dy: 5}
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
        - filename: dial-logo.png
          url: https://dial.ird.fr/
          alt: 'DIAL — Développement, Institutions et Mondialisation (LEDa-DIAL)'
          title: 'DIAL — Développement, Institutions et Mondialisation (LEDa-DIAL)'
        - filename: paris1-logo.png
          url: https://ces.pantheonsorbonne.fr/en
          alt: 'Université Paris 1 Panthéon-Sorbonne (CES)'
          title: 'Université Paris 1 Panthéon-Sorbonne (CES)'
        - filename: ces-logo.png
          url: https://ces.pantheonsorbonne.fr/en
          alt: 'Centre d’Économie de la Sorbonne (CES)'
          title: 'Centre d’Économie de la Sorbonne (CES)'
        - filename: uge-logo.png
          url: https://www.univ-gustave-eiffel.fr/en/
          alt: 'Université Gustave Eiffel'
          title: 'Université Gustave Eiffel'
        - filename: erudite-logo.png
          url: https://erudite.univ-paris-est.fr/
          alt: 'Érudite — Laboratoire d’économie, Université Gustave Eiffel'
          title: 'Érudite — Laboratoire d’économie, Université Gustave Eiffel'
---
