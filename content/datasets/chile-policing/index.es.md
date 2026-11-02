---
title: 'Programas policiales contra la delincuencia en Chile'
date: 2026-08-09
weight: 30

dataset:
  index: '03'
  nav_label: 'Programas policiales'
  region: 'Chile — nivel comunal, 1994–2022'
  tile:
    theme: 'Seguridad'
    unit: 'comunas'
    countries: ['Chile']
    image: 'datasets/chile-policing-rollout.png'
  stats:
    - value: '345'
      label: 'comunas cubiertas'
    - value: '150'
      label: 'con Plan Cuadrante'
    - value: '189'
      label: 'con patrullaje propio'
    - value: '1994–2022'
      label: 'años cubiertos'

  panels:
    - image: 'datasets/chile-policing-rollout.png'
      alt: 'Gráfico escalonado del número acumulado de comunas chilenas cubiertas por cada programa entre 1994 y 2022, en el que el Plan Cuadrante crece de 2000 a 2013 y los cuerpos de patrullaje municipal crecen a partir de 2016'
  legend:
    label: 'Comunas cubiertas'
    items:
      - {color: '#7c3aed', shape: 'line', text: 'Plan Cuadrante (150 en 2013)'}
      - {color: '#d95926', shape: 'line', text: 'Seguridad Ciudadana (183 en 2022)'}

  parts:
    - name: 'Plan Cuadrante'
      subtitle: '150 comunas, entrada escalonada 2000–2013'
      detail: >
        El Plan Cuadrante de Seguridad Preventiva es una reforma de policía por
        cuadrantes (beat policing) gestionada por Carabineros de Chile: las
        comunas urbanas se dividen en pequeños cuadrantes y los agentes se
        asignan de forma permanente a uno de ellos, en lugar de rotar por toda
        la comuna, con el objetivo de reducir tanto la delincuencia como el
        temor a ella. Iniciado en 1998, llegó a las comunas por oleadas: 44 en
        el primer año de este registro y, después, una expansión continua hasta
        que las últimas 13 se incorporaron en 2013. Esa entrada escalonada es lo
        que hace útil el archivo: es el calendario de tratamiento en el que se
        basa [Boots in the Beat](/es/publication/plan-cuadrante/), donde lo usamos
        para estimar los efectos de la reforma sobre la victimización y la
        percepción de la delincuencia. Junto a las fechas de entrada hay un
        libro de cálculo complementario que indica qué comunas aparecen en la
        encuesta nacional de victimización y qué comunas no tratadas limitan con
        una tratada.
      collection: >
        Las fechas de entrada fueron proporcionadas directamente por Carabineros
        de Chile, cuyos propios registros son la única fuente autorizada al
        respecto.

    - name: 'Seguridad Ciudadana'
      subtitle: '345 comunas × 20 años de programas municipales de patrullaje'
      detail: >
        Mientras que el Plan Cuadrante cambió la forma de desplegar a los
        agentes de la policía nacional, los programas de Seguridad Ciudadana son
        propios de los municipios: cuerpos de patrullaje financiados localmente
        que combaten la delincuencia sumando recursos de vigilancia sobre el
        terreno. El panel abarca de 2003 a 2022 para las 345 comunas y registra
        si cada una cuenta con uno de estos cuerpos y desde qué año —189 lo
        tienen, con años de inicio entre 1994 y 2022 muy concentrados a partir
        de 2016—, junto con las mismas preguntas formuladas sobre el Plan
        Cuadrante, la población y la densidad de 2021, y una calificación de
        fiabilidad de las respuestas de cada municipio, de las cuales 261 están
        completas. También incluye la dotación de patrullaje año a año: 530
        observaciones comuna-año con efectivos en plantilla en 179 comunas, con
        un cuerpo mediano de 6 efectivos y uno máximo de 141. El libro de
        cálculo más amplio del que procede recoge la misma información sobre los
        inspectores municipales de 127 comunas.
      collection: >
        Recopilado comuna por comuna a través del Portal de Transparencia de
        Chile, que obliga a los organismos públicos a responder a las
        solicitudes sobre sus propios registros: 340 de las 345 respuestas se
        obtuvieron así y el resto, de los sitios web municipales. Todas las
        cifras son autodeclaradas por el municipio que respondió, por lo que
        cada una va acompañada de una calificación de fiabilidad.

  closing: 'En conjunto, abarcan dos etapas muy distintas de la política chilena contra la delincuencia, y ambos se utilizan en mis trabajos en curso.'

abstract: >
  Registros a nivel comunal de los dos programas policiales con los que Chile
  combatió la delincuencia: el Plan Cuadrante, la reforma de policía por
  cuadrantes que Carabineros desplegó a partir de 2000, y los cuerpos de
  patrullaje creados por los propios municipios, reunidos solicitud a
  solicitud a través del Portal de Transparencia.

slug: 'chile-policing'
share: false
---
