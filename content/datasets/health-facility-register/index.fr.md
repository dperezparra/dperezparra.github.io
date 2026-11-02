---
title: 'Registre des établissements de santé du Nigeria'
date: 2026-08-07
weight: 20

dataset:
  index: '02'
  nav_label: 'Établissements de santé'
  region: 'Nigeria — hôpitaux et soins de santé primaires'
  tile:
    theme: 'Santé'
    unit: 'établissements'
    countries: ['Nigeria']
    image: 'datasets/nigeria-health-facilities.png'
  stats:
    - value: '42 063'
      label: 'établissements répertoriés'
    - value: '41 323'
      label: 'points cartographiés'
    - value: '4 391'
      label: "coordonnées que j'ai ajoutées"
    - value: '1901–2024'
      label: "années d'ouverture"

  parts:
    - detail: >
        Tous les établissements du registre national, chacun avec un code
        unique, son État, sa zone de gouvernement local et sa circonscription
        (ward), son type de propriété, son niveau de soins et sa date
        d'ouverture — la couverture est complète : les 37 États et les 774 zones
        de gouvernement local, réparties en 9 566 circonscriptions. 30 773
        établissements sont publics et 11 290 privés ; 35 903 sont des centres de
        soins de santé primaires et 6 160 des hôpitaux, dont 6 002 secondaires et
        158 tertiaires. 40 021 étaient en activité au moment de l'établissement
        du registre, les autres étant fermés, temporairement fermés ou encore en
        construction, et chacun indique son statut d'enregistrement et de
        licence. 34 838 ont une date d'ouverture connue au jour près, ce qui
        permet d'utiliser le registre comme un panel plutôt que comme un
        instantané : 34 469 établissements disposent à la fois d'une année
        d'ouverture plausible et d'un point géolocalisé, et je conserve ce
        sous-ensemble dans un fichier distinct.
      panels:
        - image: 'datasets/nigeria-health-facilities.png'
          alt: 'Carte du Nigeria montrant les centres de soins de santé primaires sous forme de petits points vert clair et les hôpitaux sous forme de points vert foncé plus grands'
      legend:
        label: 'Établissements cartographiés'
        items:
          - {color: '#6ee7b7', shape: 'dot', size: '0.5rem', text: 'Soins de santé primaires (35 324)'}
          - {color: '#10b981', shape: 'triangle', size: '0.8rem', text: 'Hôpital (5 999)'}
      collection: >
        Téléchargé depuis le site du registre des établissements de santé
        (Health Facility Registry) du ministère fédéral de la Santé, aujourd'hui
        hors ligne. Environ un établissement sur huit n'avait pas de
        coordonnées ; je les ai géocodés moi-même dans R à l'aide de Google Maps
        et d'OpenStreetMap, et en ai ainsi récupéré 4 391. Un indicateur dans les
        données signale les points issus de cette étape.

  closing: "C'est la colonne vertébrale de mes travaux en cours sur l'expansion des établissements de santé et la fécondité au Nigeria."

abstract: >
  Le registre national des établissements de santé nigérians — tous les
  hôpitaux et centres de soins de santé primaires, publics et privés —
  nettoyé, daté et géocodé, y compris 4 391 établissements que j'ai moi-même
  placés sur la carte lorsque le registre ne donnait pas de coordonnées.

slug: 'health-facility-register'
share: false
---
