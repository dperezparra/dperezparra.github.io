---
title: 'Programmes policiers de lutte contre la criminalité au Chili'
date: 2026-08-09
weight: 30

dataset:
  index: '03'
  nav_label: 'Programmes policiers'
  region: 'Chili — niveau municipal (comuna), 1994–2022'
  tile:
    theme: 'Sécurité'
    unit: 'municipalités'
    countries: ['Chili']
    image: 'datasets/chile-policing-rollout.png'
  stats:
    - value: '345'
      label: 'municipalités couvertes'
    - value: '150'
      label: 'sous Plan Cuadrante'
    - value: '189'
      label: 'avec leurs propres patrouilles'
    - value: '1994–2022'
      label: 'années couvertes'

  panels:
    - image: 'datasets/chile-policing-rollout.png'
      alt: 'Graphique en escalier du nombre cumulé de municipalités chiliennes couvertes par chaque programme entre 1994 et 2022, montrant la progression du Plan Cuadrante de 2000 à 2013 et celle des corps de patrouille municipaux à partir de 2016'
  legend:
    label: 'Municipalités couvertes'
    items:
      - {color: '#7c3aed', shape: 'line', text: 'Plan Cuadrante (150 en 2013)'}
      - {color: '#d95926', shape: 'line', text: 'Seguridad Ciudadana (183 en 2022)'}

  parts:
    - name: 'Plan Cuadrante'
      subtitle: '150 municipalités, entrée échelonnée 2000–2013'
      detail: >
        Le Plan Cuadrante de Seguridad Preventiva est une réforme de police de
        proximité menée par les Carabineros de Chile : les municipalités
        urbaines sont découpées en petits quadrants et les agents sont affectés
        de façon permanente à l'un d'eux au lieu de tourner sur l'ensemble de la
        municipalité, l'objectif étant de réduire à la fois la criminalité et le
        sentiment d'insécurité. Lancé en 1998, il a atteint les municipalités par
        vagues — 44 la première année couverte par ces données, puis une
        extension régulière jusqu'à l'arrivée des 13 dernières en 2013. C'est
        cette entrée échelonnée qui fait l'intérêt du fichier : elle fournit le
        calendrier du traitement de
        [Boots in the Beat](/fr/publication/plan-cuadrante/), où nous l'utilisons
        pour estimer les effets de la réforme sur la victimisation et la
        perception de la criminalité. Les dates d'entrée sont accompagnées d'un
        classeur complémentaire indiquant quelles municipalités figurent dans
        l'enquête nationale de victimisation et quelles municipalités non
        traitées sont limitrophes d'une municipalité traitée.
      collection: >
        Les dates d'entrée ont été fournies directement par les Carabineros de
        Chile, dont les propres archives sont la seule source faisant autorité
        en la matière.

    - name: 'Seguridad Ciudadana'
      subtitle: '345 municipalités × 20 ans de programmes de patrouille municipale'
      detail: >
        Là où le Plan Cuadrante a modifié le déploiement des agents de la police
        nationale, les programmes de Seguridad Ciudadana relèvent des
        municipalités elles-mêmes : des corps de patrouille financés localement
        qui luttent contre la criminalité en renforçant les moyens policiers sur
        le terrain. Le panel couvre la période 2003–2022 pour les 345
        municipalités et indique si chacune dispose d'un tel corps et depuis
        quelle année — c'est le cas de 189 d'entre elles, avec des années de
        création allant de 1994 à 2022 et fortement concentrées après 2016 —
        ainsi que les mêmes questions posées au sujet du Plan Cuadrante, la
        population et la densité en 2021, et une note de fiabilité des réponses
        de chaque municipalité, dont 261 sont complètes. Il renseigne également
        les effectifs de patrouille année par année : 530 municipalités-années
        avec des agents en poste dans 179 municipalités, un corps médian de 6
        agents et un maximum de 141. Le classeur plus large dont il est issu
        contient les mêmes informations pour les inspecteurs municipaux de 127
        municipalités.
      collection: >
        Collectées municipalité par municipalité via le Portail de la
        transparence chilien, qui oblige les organismes publics à répondre aux
        demandes portant sur leurs propres archives — 340 des 345 réponses ont
        été obtenues ainsi, les autres provenant des sites web municipaux. Chaque
        chiffre est déclaré par la municipalité qui a répondu, d'où la note de
        fiabilité associée à chacun.

  closing: "Ensemble, ils couvrent deux époques très différentes de la politique chilienne de lutte contre la criminalité, et tous deux sont utilisés dans mes travaux en cours."

abstract: >
  Des données au niveau municipal sur les deux programmes policiers mis en
  œuvre par le Chili contre la criminalité : le Plan Cuadrante, la réforme de
  police de proximité déployée par les Carabineros à partir de 2000, et les
  corps de patrouille créés par les municipalités elles-mêmes, reconstitués
  une demande au Portail de la transparence après l'autre.

slug: 'chile-policing'
share: false
---
