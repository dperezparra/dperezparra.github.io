---
title: 'School Censuses of Senegal and Nigeria'
date: 2026-08-07
weight: 10

# Display order and layout are driven by this block - see
# layouts/_partials/views/dataset.html
dataset:
  index: '01'
  region: 'Nigeria · Senegal — pre-primary through secondary'
  stats:
    - value: '160,615'
      label: 'schools listed'
    - value: '133,428'
      label: 'geocoded points'
    - value: '~41.7m'
      label: 'pupil enrolments'
    - value: '1801–2024'
      label: 'founding years'

  parts:
    - name: 'Nigeria'
      subtitle: '141,663 schools, geocoded to the individual school'
      detail: >
        Every school listed in the national register, each with a unique code,
        name, state, LGA, level, sector and year of establishment. 133,428 carry
        point coordinates that fall inside the country. The register spans 39
        state entries and 670 local government areas, and splits 77,774 private
        against 63,889 public; founding years run from 1801 to 2024, with a
        median of 2006. Alongside it sit four enrolment tables — 204,090 school
        records and roughly 41.7 million pupil enrolments, broken down by grade
        and by sex from ECCD and nursery through to SS3, each with sector and an
        urban/rural marker.
      panels:
        - image: 'datasets/nigeria-pre-primary.png'
          label: 'Pre-Primary'
          value: '1,106'
          alt: 'Map of Nigeria showing the location of pre-primary schools'
        - image: 'datasets/nigeria-primary.png'
          label: 'Primary'
          value: '105,894'
          alt: 'Map of Nigeria showing the location of primary schools'
        - image: 'datasets/nigeria-junior-secondary.png'
          label: 'Junior Secondary'
          value: '31,421'
          alt: 'Map of Nigeria showing the location of junior secondary schools'
        - image: 'datasets/nigeria-senior-secondary.png'
          label: 'Senior Secondary'
          value: '3,242'
          alt: 'Map of Nigeria showing the location of senior secondary schools'
      caption: >
        Each dot is one school. Primary provision reaches almost every
        settlement, while senior secondary schools concentrate in the cities and
        along the main corridors — the spatial gap that motivates the education
        chapters of my thesis.
      collection: >
        Web-scraped from [NEMIS](https://nemiserp.com), the national education
        management information system, with
        [Javier Martínez](https://x.com/javimartzs). That site is only
        intermittently available; the scrape captured every school listed during
        a window when it was running reliably.

    - name: 'Senegal'
      subtitle: '18,952 establishments from the Ministry of Education register'
      detail: >
        16,297 primary and 2,655 secondary establishments, each with its
        administrative code, region, department, inspectorate and commune,
        public / private / community status, teaching cycle, an urban/rural
        marker and a founding year — 1822 to 2024 for primary, 1886 to 2024 for
        secondary. Coverage is national: 14 regions, 47 departments and roughly
        550 communes.
      panels:
        - image: 'datasets/senegal-petite-enfance.png'
          label: 'Petite enfance'
          value: '5,116'
          alt: 'Map of Senegal shaded by the number of pre-school establishments per department'
        - image: 'datasets/senegal-primaire.png'
          label: 'Primaire'
          value: '11,181'
          alt: 'Map of Senegal shaded by the number of primary schools per department'
        - image: 'datasets/senegal-moyen-secondaire.png'
          label: 'Moyen & secondaire'
          value: '2,655'
          alt: 'Map of Senegal shaded by the number of middle and secondary schools per department'
      legend:
        label: 'Schools per department'
        items:
          - {color: '#ede9fe', text: '1–49'}
          - {color: '#c4b5fd', text: '50–99'}
          - {color: '#a78bfa', text: '100–199'}
          - {color: '#7c3aed', text: '200–349'}
          - {color: '#5b21b6', text: '350+'}
      caption: >
        All three panels share one absolute scale, so they can be read against
        each other: middle and secondary schools are scarce almost everywhere,
        while primary provision is dense across the country. Mapped by
        department rather than commune — the census locates schools to commune,
        but no available boundary layer matches those names well enough (62.7%
        against GADM's communes, 78% even with fuzzy matching), whereas
        department covers 100% of the 18,952 establishments.
      collection: >
        Obtained directly from officials at the Ministry of Education.
        Department boundaries from
        [geoBoundaries](https://www.geoboundaries.org) (CC BY 3.0 IGO).

  closing: 'Both are still in use in some of my ongoing papers.'
  access: >
    Neither dataset is openly published, and both are shared as a public good
    with researchers and master's students. I ask for a short note on the
    intended use so I can explain how each was assembled, what it does and does
    not support, and the conditions attached — in particular that it is not
    redistributed and that the source is credited.
  request_url: 'mailto:daniel.perezparra@ird.fr?subject=Dataset%20request%3A%20School%20Censuses%20of%20Senegal%20and%20Nigeria'
  request_label: 'Request access'

abstract: >
  Two national school registers assembled for my work on secondary school
  expansion in West Africa: a complete web-scrape of the Nigerian school
  management system, geocoded to the individual school, and a Ministry of
  Education census for Senegal.

slug: 'school-censuses'
share: false
---
