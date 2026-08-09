---
title: 'Health Facility Register of Nigeria'
date: 2026-08-07
weight: 20

# Display order and layout are driven by this block - see
# layouts/_partials/views/dataset.html
dataset:
  index: '02'
  nav_label: 'Health facilities'
  region: 'Nigeria — hospitals and primary health care'
  stats:
    - value: '42,063'
      label: 'facilities listed'
    - value: '41,323'
      label: 'mapped points'
    - value: '4,391'
      label: 'coordinates I added'
    - value: '1901–2024'
      label: 'opening years'

  parts:
    - detail: >
        Every facility on the national register, each with a unique code, its
        state, local government area and ward, ownership, level of care and the
        date it opened — coverage is complete, all 37 states and all 774 local
        government areas, across 9,566 wards. 30,773 facilities are public and
        11,290 private; 35,903 are primary health care centres and 6,160 are
        hospitals, of which 6,002 are secondary and 158 tertiary. 40,021 were
        operational when the register was taken, the rest closed, temporarily
        closed or still under construction, and each carries its registration
        and licence status. 34,838 have an opening date recorded to the day,
        which is what makes the register usable as a panel rather than a
        snapshot: 34,469 facilities have both a plausible opening year and a
        point, and I keep that subset as a separate file.
      panels:
        - image: 'datasets/nigeria-health-facilities.png'
          alt: 'Map of Nigeria showing primary health care centres as small light green dots and hospitals as larger dark green dots'
      legend:
        label: 'Mapped facilities'
        items:
          - {color: '#6ee7b7', shape: 'dot', size: '0.5rem', text: 'Primary health care (35,324)'}
          - {color: '#10b981', shape: 'triangle', size: '0.8rem', text: 'Hospital (5,999)'}
      collection: >
        Downloaded from the Federal Ministry of Health's Health Facility
        Registry site, which has since gone offline. About one
        facility in eight came with no coordinate, and I geocoded those myself
        in R through Google Maps and OpenStreetMap, recovering 4,391 of them.
        A flag in the data marks which points came from that pass.

  closing: 'It is the backbone of my ongoing work on health facility expansion and fertility in Nigeria.'

abstract: >
  The national register of Nigerian health facilities — every hospital and
  primary health care centre, public and private — cleaned, dated and geocoded,
  including 4,391 facilities I placed on the map myself where the register gave
  no coordinates.

slug: 'health-facility-register'
share: false
---
