---
title: 'School Censuses of Senegal and Nigeria'
date: 2026-08-07
weight: 10

# Display order and layout are driven by this block - see
# layouts/_partials/views/dataset.html
dataset:
  index: '01'
  region: 'Senegal · Nigeria — primary through secondary'
  stats:
    - value: '160,615'
      label: 'schools listed'
    - value: '133,428'
      label: 'geocoded points'
    - value: '~41.7m'
      label: 'pupil enrolments'
    - value: '1801–2024'
      label: 'founding years'
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
  panels_caption: >
    Every geocoded school in the Nigerian register, split by level. Each dot is
    one school; 133,428 of 141,663 records carry coordinates that fall inside
    the country. Primary provision reaches almost every settlement, while
    senior secondary schools concentrate in cities and along the main corridors
    — the spatial gap that motivates the education chapters of my thesis.
  components:
    - name: 'Nigeria — geocoded school register'
      detail: >
        141,663 schools with a unique code, name, state, LGA, level, sector and
        year of establishment. 133,428 carry usable point coordinates. Covers 39
        state entries and 670 local government areas. 77,774 private and 63,889
        public. Founding years run from 1801 to 2024, with a median of 2006.
    - name: 'Nigeria — enrolment tables'
      detail: >
        204,090 school records across four files, giving enrolment by grade and
        by sex: pre-primary (ECCD 1–2 and Nursery 1–3), primary (P1–P6), junior
        secondary (JSS 1–3) and senior secondary (SS 1–3), together roughly 41.7
        million pupil enrolments, each with state, LGA, sector and an
        urban/rural marker.
    - name: 'Senegal — Ministry of Education register'
      detail: >
        16,297 primary and 2,655 secondary establishments, each with its
        administrative code, region, department, inspectorate, commune, public /
        private / community status, teaching cycle, an urban/rural marker and a
        founding year (1822–2024 for primary, 1886–2024 for secondary). Located
        to commune level: 14 regions, 47 departments and roughly 550 communes.

  provenance: >
    The Senegalese register was obtained directly from officials at the Ministry
    of Education. The Nigerian data was web-scraped from
    [NEMIS](https://nemiserp.com), the national education management information
    system, with [Javier Martínez](https://x.com/javimartzs). That site is
    intermittently available; the scrape captured every school listed during a
    window when it was running reliably. Both are still in use in my PhD
    chapters.
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
  expansion in West Africa: a Ministry of Education census for Senegal, and a
  complete web-scrape of the Nigerian school management system, geocoded to
  the individual school.

slug: 'school-censuses'
share: false
---
