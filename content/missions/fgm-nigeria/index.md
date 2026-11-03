---
# The site used to live at /my-website/ as a GitHub Pages project site.
# Those URLs are still in Google; these aliases turn each one into a
# redirect to its replacement instead of a 404, which is what gets the
# old address out of the results and the ranking on to the new one.
aliases:
  - '/my-website/missions/fgm-nigeria/'

title: Qualitative Surveys in Central and Southern Nigeria
# Mission ran November-December 2024; dated at its close.
date: 2024-12-01

# Drives the carousel layout on /fieldwork/ - see layouts/_partials/views/mission.html.
#   sites    - pins on the map (approximate coordinates)
#   regions  - the locations grouped by state
#   sections - the three short headed blocks under the summary
#   gallery  - carousel photos, in order; `focus` is the CSS object-position
#              that keeps the faces in frame in the 16:7 slide
fieldwork:
  map: nigeria
  dates: 'November – December 2024'
  sites:
    - {name: 'Abuja', lat: 9.0765, lon: 7.3986}
    - {name: 'Dakwa', lat: 9.1700, lon: 7.3600}
    - {name: 'Deidei', lat: 9.1100, lon: 7.2800}
    - {name: 'Mpape', lat: 9.1220, lon: 7.4970}
    - {name: 'Akpabuyo', lat: 4.9550, lon: 8.4500}
    - {name: 'Ikom', lat: 5.9600, lon: 8.7100}
    - {name: 'Odukpani', lat: 5.1300, lon: 8.3300}
  stats:
    - {value: '7', label: 'locations'}
    - {value: '10', label: 'focus groups'}
    - {value: '68', label: 'participants'}
    - {value: '6', label: 'religious leaders'}
  regions:
    - name: 'Federal Capital Territory'
      places: ['Abuja', 'Dakwa', 'Deidei', 'Mpape']
      note: 'Igbo, Yoruba and Hausa communities, many of them internal migrants from other regions of Nigeria.'
    - name: 'Cross River State'
      places: ['Akpabuyo', 'Ikom', 'Odukpani']
      note: 'Predominantly Christian communities, mainly Efik, Ekoi and Ibibio.'
  sections:
    - title: 'Who we met'
      text: 'Women living in areas where female genital cutting is prevalent: 10 focus groups across 8 rural communities, with 65 women and 3 men. We also held in-depth interviews with 6 Christian and Muslim religious and traditional authorities.'
    - title: 'How'
      text: 'Each focus group lasted about an hour and a half and was run with a local translator. The interviews with religious authorities were held one to one.'
    - title: 'What we asked'
      text: 'How people use the internet, and how they see its effects on social norms, particularly sexual behaviour and the stigma around it.'
  gallery:
    - {file: 'gallery/01.jpg', caption: 'Focus group in a rural community', focus: '50% 0%'}
    - {file: 'gallery/02.jpg', caption: 'Focus group by the roadside', focus: '50% 80%'}
    - {file: 'gallery/03.jpg', caption: 'Discussion in the shade', focus: '50% 0%'}
    - {file: 'gallery/04.jpg', caption: 'One-to-one interview', focus: '50% 0%'}
    - {file: 'gallery/05.jpg', caption: 'Meeting at a health facility', focus: '50% 38%'}
    - {file: 'gallery/06.jpg', caption: 'The field team', focus: '50% 43%'}
    - {file: 'gallery/07.jpg', caption: 'Talking with residents by the road', focus: '50% 2%'}
    - {file: 'gallery/08.jpg', caption: 'Evening interview', focus: '50% 0%'}
    - {file: 'gallery/09.jpg', caption: 'Evening interview', focus: '50% 0%'}
    - {file: 'gallery/10.jpg', caption: 'Focus group under the trees', focus: '50% 74%'}
  paper: '/publication/fgm-3g'
  funding: 'Érudite, Université Gustave Eiffel'
  collaborators: 'Hadiza Kande Jidda, Anthony Ekere, Stephen Adibe and Susan Michael'

abstract: >
  With my coauthor [Jorge García-Hombrados](https://sites.google.com/view/jgarciahombrados/home), we spent November and December 2024 in the Federal Capital Territory and Cross River State, talking with women in communities where female genital cutting is practised and with Christian and Muslim religious authorities about the internet and changing social norms.

image:
  filename: "featured.jpg"
  focal_point: "middle"
  preview_only: true
  
tags:
  - Female Genital Cutting
  - Pre-marital sex

share: false
  
---