---
title: 'Censos escolares de Nigeria y Senegal'
date: 2026-08-07
weight: 10

dataset:
  index: '01'
  nav_label: 'Censos escolares'
  region: 'Nigeria · Senegal — de preescolar a secundaria'
  tile:
    theme: 'Educación'
    unit: 'escuelas'
    countries: ['Nigeria', 'Senegal']
    image: 'datasets/nigeria-primary.png'
  stats:
    - value: '160.615'
      label: 'escuelas registradas'
    - value: '133.428'
      label: 'puntos georreferenciados'
    - value: '~41,7 M'
      label: 'matrículas de alumnos'
    - value: '1801–2024'
      label: 'años de fundación'

  parts:
    - name: 'Nigeria'
      subtitle: '141.663 escuelas, georreferenciadas una a una'
      detail: >
        Todas las escuelas que figuran en el registro nacional, cada una con un
        código único, nombre, estado, LGA (área de gobierno local), nivel, sector
        y año de creación. 133.428 tienen coordenadas puntuales situadas dentro
        del país. El registro abarca 39 entradas de estado y 670 áreas de
        gobierno local, y se reparte entre 77.774 escuelas privadas y 63.889
        públicas; los años de fundación van de 1801 a 2024, con una mediana de
        2006. Lo acompañan cuatro tablas de matrícula —204.090 registros de
        escuelas y unos 41,7 millones de matrículas de alumnos—, desglosadas por
        curso y por sexo desde ECCD y nursery (educación infantil) hasta SS3,
        cada una con el sector y un indicador urbano/rural.
      panels:
        - image: 'datasets/nigeria-pre-primary.png'
          label: 'Preescolar'
          value: '1.106'
          alt: 'Mapa de Nigeria con la ubicación de las escuelas de preescolar'
        - image: 'datasets/nigeria-primary.png'
          label: 'Primaria'
          value: '105.894'
          alt: 'Mapa de Nigeria con la ubicación de las escuelas primarias'
        - image: 'datasets/nigeria-junior-secondary.png'
          label: 'Secundaria inferior'
          value: '31.421'
          alt: 'Mapa de Nigeria con la ubicación de las escuelas de secundaria inferior'
        - image: 'datasets/nigeria-senior-secondary.png'
          label: 'Secundaria superior'
          value: '3.242'
          alt: 'Mapa de Nigeria con la ubicación de las escuelas de secundaria superior'
      collection: >
        Obtenido mediante web scraping de [NEMIS](https://nemiserp.com), el
        sistema nacional de información para la gestión educativa, junto con
        [Javier Martínez](https://x.com/javimartzs). Ese sitio solo está
        disponible de forma intermitente; la extracción recogió todas las
        escuelas registradas durante un periodo en que funcionaba de manera
        fiable.

    - name: 'Senegal'
      subtitle: '18.952 establecimientos del registro del Ministerio de Educación'
      detail: >
        16.297 establecimientos de primaria y 2.655 de secundaria, cada uno con
        su código administrativo, región, departamento, inspección y comuna, su
        carácter público, privado o comunitario, el ciclo de enseñanza, un
        indicador urbano/rural y el año de fundación: de 1822 a 2024 en primaria
        y de 1886 a 2024 en secundaria. La cobertura es nacional: 14 regiones,
        47 departamentos y unas 550 comunas.
      panels:
        - image: 'datasets/senegal-petite-enfance.png'
          label: 'Primera infancia'
          value: '5.116'
          alt: 'Mapa de Senegal sombreado según el número de centros de educación preescolar por comuna'
        - image: 'datasets/senegal-primaire.png'
          label: 'Primaria'
          value: '11.181'
          alt: 'Mapa de Senegal sombreado según el número de escuelas primarias por comuna'
        - image: 'datasets/senegal-moyen-secondaire.png'
          label: 'Media y secundaria'
          value: '2.655'
          alt: 'Mapa de Senegal sombreado según el número de centros de enseñanza media y secundaria por comuna'
      legend:
        label: 'Escuelas por comuna'
        items:
          - {color: '#cde2fb', text: '1–9'}
          - {color: '#9ec5f4', text: '10–19'}
          - {color: '#6da7ec', text: '20–39'}
          - {color: '#3987e5', text: '40–79'}
          - {color: '#256abf', text: '80+'}
      collection: >
        Obtenido directamente de responsables del Ministerio de Educación. **El
        acceso al censo senegalés está sujeto a su autorización**, por lo que
        las solicitudes se remiten al Ministerio en lugar de concederse
        directamente. Límites comunales de
        [OpenStreetMap](https://www.openstreetmap.org/copyright) (ODbL).

  closing: 'Ambos se siguen utilizando en algunos de mis trabajos en curso.'

abstract: >
  Dos registros escolares nacionales reunidos para mi trabajo sobre la
  expansión de la educación secundaria en África Occidental: una extracción
  completa del sistema de gestión escolar de Nigeria, georreferenciada escuela
  por escuela, y un censo del Ministerio de Educación de Senegal.

slug: 'school-censuses'
share: false
---
