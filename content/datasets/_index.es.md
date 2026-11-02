---
title: 'Datos'
slug: 'datasets'
type: landing

design:
  spacing: '5rem'

request:
  title: 'Cómo solicitarlos'
  text: >
    Una sola nota sirve para los tres: dime cuál te interesa y en qué estás
    trabajando, y te lo enviaré junto con el código y una explicación de cómo
    se construyó y de qué usos admite y cuáles no. Las únicas condiciones son
    que no se redistribuya y que se citen las fuentes originales. La única
    excepción es el censo escolar de Senegal, cuya cesión corresponde al
    Ministerio de Educación, por lo que las solicitudes de ese conjunto se
    remiten a sus responsables.
  url: 'mailto:daniel.perez-parra@ird.fr?subject=Dataset%20request'
  label: 'Solicitar datos'

sections:
  - block: markdown
    design:
      css_class: 'page-wide datasets-intro'
    content:
      title: 'Datos'
      text: |
        <p class="page-intro">Datos originales que he recopilado, obtenido
        mediante web scraping o conseguido de autoridades nacionales en el curso
        de mi investigación. La mayor parte no está publicada en abierto, así que
        la comparto como bien público con investigadores y estudiantes de máster,
        previa solicitud.</p>
        <p class="page-intro">Que la solicitud sea una conversación y no un
        enlace de descarga es deliberado: cada uno de estos conjuntos de datos
        descansa sobre supuestos acerca de cómo se construyó que determinan para
        qué puede utilizarse y para qué no, y prefiero explicarlos antes que ver
        los datos usados de formas que no admiten. Escríbeme con una breve nota
        sobre lo que tienes en mente; estaré encantado de ayudarte y
        orientarte :)</p>

  - block: collection
    design:
      view: dataset
      css_class: datasets-list
    content:
      filters:
        folders:
          - datasets
      count: 20
      sort_by: Weight
      sort_ascending: true
---
