---
title: 'Health Facility Register of Nigeria'
date: 2026-08-07
weight: 20

# Display order and layout are driven by this block - see
# layouts/_partials/views/dataset.html
dataset:
  index: '02'
  region: 'Nigeria — hospitals and primary health care'
  stats:
    - value: '42,063'
      label: 'facilities listed'
    - value: '41,323'
      label: 'mapped points'
    - value: '4,391'
      label: 'geocoded by hand'
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
          alt: 'Map of Nigeria showing primary health care centres as small green dots, with public hospitals in blue and private hospitals in orange drawn on top'
      legend:
        label: 'Facility type'
        items:
          - {color: '#2a78d6', text: 'Public hospital (1,354)'}
          - {color: '#d95926', text: 'Private hospital (4,645)'}
          - {color: '#199e70', text: 'Primary health care (35,324)'}
      caption: >
        One dot per facility. The small green marks are the primary health care
        mesh, which reaches almost every ward in the country; the larger dots
        are hospitals, coloured by who runs them. The split is the striking
        part — private hospitals cluster hard in the south west and the
        south east, around Lagos, Ibadan, Onitsha and Aba, while public
        hospitals are spread thinly but evenly right across the north. Counts
        in the legend are the facilities that carry a usable point, 98.2% of the
        register; the primary health care mesh is itself 29,083 public and
        6,241 private, a split the map does not draw.
      collection: >
        Downloaded from the Federal Ministry of Health's Health Facility
        Registry at hfr.e4eweb.space while the portal was still up — it has
        since gone offline, so the register as it stood is now hard to come by.
        Roughly a tenth of the facilities arrived without usable coordinates,
        and I geocoded 4,391 of those myself in R from the facility name, ward,
        local government area and state, using the Google Maps geocoding API
        through `ggmap` and falling back on OpenStreetMap where Google returned
        nothing. Every result was checked against the administrative unit it was
        supposed to fall in, and the flag marking which points came from that
        pass travels with the data, so you can drop them if your design needs
        only the register's own coordinates.

  closing: 'It is the backbone of my ongoing work on health facility expansion and fertility in Nigeria.'
  access: >
    The register was public while the portal was running; what I add is the
    cleaning, the opening dates and the geocoding, and I am glad to pass all of
    it on. Send me a short note about what you are working on and I'll share it
    along with the code, explain how the geocoding was done and where it is
    weakest, and the only conditions are that it is not redistributed and that
    the source is credited. Always glad to hear what people are using it for :)
  request_url: 'mailto:daniel.perezparra@ird.fr?subject=Dataset%20request%3A%20Health%20Facility%20Register%20of%20Nigeria'
  request_label: 'Request access'

abstract: >
  The national register of Nigerian health facilities — every hospital and
  primary health care centre, public and private — cleaned, dated and geocoded,
  including 4,391 facilities I located by hand where the register gave no
  coordinates.

slug: 'health-facility-register'
share: false
---
