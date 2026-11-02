---
title: 'Recensements scolaires du Nigeria et du Sénégal'
date: 2026-08-07
weight: 10

dataset:
  index: '01'
  nav_label: 'Recensements scolaires'
  region: 'Nigeria · Sénégal — du préprimaire au secondaire'
  tile:
    theme: 'Éducation'
    unit: 'écoles'
    countries: ['Nigeria', 'Sénégal']
    image: 'datasets/nigeria-primary.png'
  stats:
    - value: '160 615'
      label: 'écoles répertoriées'
    - value: '133 428'
      label: 'points géocodés'
    - value: '~41,7 M'
      label: "inscriptions d'élèves"
    - value: '1801–2024'
      label: 'années de création'

  parts:
    - name: 'Nigeria'
      subtitle: '141 663 écoles, géocodées à l''échelle de chaque établissement'
      detail: >
        Toutes les écoles inscrites au registre national, chacune avec un code
        unique, son nom, son État, sa LGA, son niveau, son secteur et son année
        de création. 133 428 disposent de coordonnées ponctuelles situées à
        l'intérieur du pays. Le registre couvre 39 entrées d'État et 670 zones de
        gouvernement local, et se répartit entre 77 774 écoles privées et 63 889
        publiques ; les années de création vont de 1801 à 2024, avec une médiane
        en 2006. S'y ajoutent quatre tables d'effectifs — 204 090 enregistrements
        d'écoles et environ 41,7 millions d'inscriptions d'élèves, ventilées par
        niveau et par sexe, de l'ECCD et de la maternelle jusqu'au SS3, chacune
        avec le secteur et un indicateur urbain/rural.
      panels:
        - image: 'datasets/nigeria-pre-primary.png'
          label: 'Préprimaire'
          value: '1 106'
          alt: 'Carte du Nigeria montrant la localisation des écoles préprimaires'
        - image: 'datasets/nigeria-primary.png'
          label: 'Primaire'
          value: '105 894'
          alt: 'Carte du Nigeria montrant la localisation des écoles primaires'
        - image: 'datasets/nigeria-junior-secondary.png'
          label: 'Premier cycle du secondaire'
          value: '31 421'
          alt: 'Carte du Nigeria montrant la localisation des écoles du premier cycle du secondaire'
        - image: 'datasets/nigeria-senior-secondary.png'
          label: 'Second cycle du secondaire'
          value: '3 242'
          alt: 'Carte du Nigeria montrant la localisation des écoles du second cycle du secondaire'
      collection: >
        Extrait du web à partir de [NEMIS](https://nemiserp.com), le système
        national d'information pour la gestion de l'éducation, avec
        [Javier Martínez](https://x.com/javimartzs). Ce site n'est accessible que
        par intermittence ; l'extraction a recueilli toutes les écoles
        répertoriées pendant une période où il fonctionnait de manière fiable.

    - name: 'Sénégal'
      subtitle: '18 952 établissements issus du registre du ministère de l''Éducation'
      detail: >
        16 297 établissements primaires et 2 655 établissements secondaires,
        chacun avec son code administratif, sa région, son département, son
        inspection et sa commune, son statut public / privé / communautaire, son
        cycle d'enseignement, un indicateur urbain/rural et son année de
        création — de 1822 à 2024 pour le primaire, de 1886 à 2024 pour le
        secondaire. La couverture est nationale : 14 régions, 47 départements et
        environ 550 communes.
      panels:
        - image: 'datasets/senegal-petite-enfance.png'
          label: 'Petite enfance'
          value: '5 116'
          alt: 'Carte du Sénégal colorée selon le nombre d''établissements préscolaires par commune'
        - image: 'datasets/senegal-primaire.png'
          label: 'Primaire'
          value: '11 181'
          alt: 'Carte du Sénégal colorée selon le nombre d''écoles primaires par commune'
        - image: 'datasets/senegal-moyen-secondaire.png'
          label: 'Moyen & secondaire'
          value: '2 655'
          alt: 'Carte du Sénégal colorée selon le nombre d''établissements moyens et secondaires par commune'
      legend:
        label: 'Écoles par commune'
        items:
          - {color: '#cde2fb', text: '1–9'}
          - {color: '#9ec5f4', text: '10–19'}
          - {color: '#6da7ec', text: '20–39'}
          - {color: '#3987e5', text: '40–79'}
          - {color: '#256abf', text: '80+'}
      collection: >
        Obtenu directement auprès de responsables du ministère de l'Éducation.
        **L'accès au recensement sénégalais est soumis à leur accord** : une
        demande le concernant est donc transmise au ministère plutôt
        qu'accordée directement. Limites communales issues
        d'[OpenStreetMap](https://www.openstreetmap.org/copyright) (ODbL).

  closing: 'Les deux sont encore utilisés dans certains de mes travaux en cours.'

abstract: >
  Deux registres scolaires nationaux constitués pour mes travaux sur
  l'expansion de l'enseignement secondaire en Afrique de l'Ouest : une
  extraction web complète du système de gestion scolaire nigérian, géocodée à
  l'échelle de chaque école, et un recensement du ministère de l'Éducation
  pour le Sénégal.

slug: 'school-censuses'
share: false
---
