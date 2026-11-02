---
title: 'Registro de establecimientos de salud de Nigeria'
date: 2026-08-07
weight: 20

dataset:
  index: '02'
  nav_label: 'Establecimientos de salud'
  region: 'Nigeria — hospitales y atención primaria de salud'
  tile:
    theme: 'Salud'
    unit: 'establecimientos'
    countries: ['Nigeria']
    image: 'datasets/nigeria-health-facilities.png'
  stats:
    - value: '42.063'
      label: 'establecimientos registrados'
    - value: '41.323'
      label: 'puntos cartografiados'
    - value: '4.391'
      label: 'coordenadas añadidas por mí'
    - value: '1901–2024'
      label: 'años de apertura'

  parts:
    - detail: >
        Todos los establecimientos del registro nacional, cada uno con un código
        único, su estado, área de gobierno local y circunscripción (ward),
        titularidad, nivel de atención y fecha de apertura. La cobertura es
        completa: los 37 estados y las 774 áreas de gobierno local, repartidos en
        9.566 circunscripciones. 30.773 establecimientos son públicos y 11.290
        privados; 35.903 son centros de atención primaria y 6.160 son hospitales,
        de los cuales 6.002 son de nivel secundario y 158 de nivel terciario.
        40.021 estaban en funcionamiento cuando se elaboró el registro; el resto
        estaban cerrados, cerrados temporalmente o aún en construcción, y cada
        uno incluye su situación de registro y de licencia. 34.838 tienen la
        fecha de apertura consignada al día, lo que permite usar el registro como
        un panel y no como una simple instantánea: 34.469 establecimientos tienen
        a la vez un año de apertura verosímil y coordenadas, y conservo ese
        subconjunto en un archivo aparte.
      panels:
        - image: 'datasets/nigeria-health-facilities.png'
          alt: 'Mapa de Nigeria con los centros de atención primaria como pequeños puntos verde claro y los hospitales como puntos más grandes verde oscuro'
      legend:
        label: 'Establecimientos cartografiados'
        items:
          - {color: '#6ee7b7', shape: 'dot', size: '0.5rem', text: 'Atención primaria (35.324)'}
          - {color: '#10b981', shape: 'triangle', size: '0.8rem', text: 'Hospital (5.999)'}
      collection: >
        Descargado del sitio del Registro de Establecimientos de Salud (Health
        Facility Registry) del Ministerio Federal de Salud, que ya no está en
        línea. Aproximadamente uno de cada ocho establecimientos carecía de
        coordenadas, y los georreferencié yo mismo en R mediante Google Maps y
        OpenStreetMap, recuperando 4.391 de ellos. Una variable indicadora en
        los datos señala qué puntos proceden de ese proceso.

  closing: 'Es la columna vertebral de mi trabajo en curso sobre la expansión de los establecimientos de salud y la fecundidad en Nigeria.'

abstract: >
  El registro nacional de establecimientos de salud de Nigeria —todos los
  hospitales y centros de atención primaria, públicos y privados—, depurado,
  fechado y georreferenciado, incluidos 4.391 establecimientos que situé yo
  mismo en el mapa cuando el registro no daba coordenadas.

slug: 'health-facility-register'
share: false
---
