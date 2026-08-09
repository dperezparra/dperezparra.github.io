---
title: 'Crime-Reduction Policing in Chile'
date: 2026-08-09
weight: 30

# Display order and layout are driven by this block - see
# layouts/_partials/views/dataset.html
dataset:
  index: '03'
  region: 'Chile — municipality (comuna) level, 1994–2022'
  stats:
    - value: '345'
      label: 'municipalities covered'
    - value: '150'
      label: 'under Plan Cuadrante'
    - value: '189'
      label: 'with their own patrols'
    - value: '1994–2022'
      label: 'years covered'

  # A record-wide figure: both programmes on one axis, which is the comparison
  # neither part can make on its own.
  panels:
    - image: 'datasets/chile-policing-rollout.png'
      alt: 'Step chart of the cumulative number of Chilean municipalities covered by each programme between 1994 and 2022, showing Plan Cuadrante rising from 2000 to 2013 and municipal patrol corps rising from 2016'
  legend:
    label: 'Municipalities covered'
    items:
      - {color: '#7c3aed', shape: 'line', text: 'Plan Cuadrante (150 by 2013)'}
      - {color: '#d95926', shape: 'line', text: 'Seguridad Ciudadana (183 by 2022)'}

  parts:
    - name: 'Plan Cuadrante'
      subtitle: '150 municipalities, staggered entry 2000–2013'
      detail: >
        Plan Cuadrante de Seguridad Preventiva is a beat-policing reform run by
        Carabineros de Chile: urban municipalities are cut into small quadrants
        and officers are assigned permanently to one of them rather than
        rotating across the whole municipality, the aim being to reduce both
        crime and the fear of it. Begun in 1998, it reached municipalities in
        waves — 44 in the first year of this record, then a steady spread until
        the last 13 arrived in 2013. That staggered entry is what makes the file
        useful: it is the treatment timing behind
        [Boots in the Beat](/publication/plan-cuadrante/), where we use it to
        estimate the reform's effects on victimisation and crime perception.
        Alongside the entry dates sits a companion workbook flagging which
        municipalities appear in the national victimisation survey and which
        untreated municipalities border a treated one.
      collection: >
        The entry dates were provided directly by Carabineros de Chile, whose
        own records are the only authoritative source for them.

    - name: 'Seguridad Ciudadana'
      subtitle: '345 municipalities × 20 years of municipal patrol programmes'
      detail: >
        Where Plan Cuadrante changed how national police officers were
        deployed, Seguridad Ciudadana programmes are the municipalities' own:
        locally funded patrol corps that attack crime by adding policing
        resources on the ground. The panel runs 2003 to 2022 for all 345
        municipalities and records whether each one runs such a corps and from
        what year — 189 do, with start years from 1994 to 2022 that cluster
        heavily after 2016 — along with the same questions asked about Plan
        Cuadrante, 2021 population and density, and a reliability grade for
        each municipality's answers, of which 261 are complete. It also carries
        patrol staffing year by year: 530 municipality-years with officers on
        the books across 179 municipalities, a median corps of 6 and a largest
        of 141. The wider workbook behind it holds the same for municipal
        inspectors in 127 municipalities.
      collection: >
        Collected municipality by municipality through the Chilean Transparency
        Portal, which obliges public bodies to answer requests for their own
        records — 340 of the 345 came that way, the rest from municipal
        websites. Every figure is self-reported by the municipality that
        answered, which is why a reliability grade travels with each one.

  closing: 'Together they cover two very different eras of Chilean crime policy, and both are in use in my ongoing work.'
  access: >
    Happy to share both. Send me a short note about what you are working on and
    I'll pass them on with the code, flag which municipalities have shakier
    answers and why, and put you straight on what the Transparency Portal
    responses can and cannot support. The only conditions are that they are not
    redistributed and that Carabineros de Chile and the responding
    municipalities are credited as the sources. Always glad to hear what people
    are using it for :)
  request_url: 'mailto:daniel.perezparra@ird.fr?subject=Dataset%20request%3A%20Crime-Reduction%20Policing%20in%20Chile'
  request_label: 'Request access'

abstract: >
  Municipality-level records of the two policing programmes Chile used against
  crime: Plan Cuadrante, the beat-policing reform Carabineros rolled out from
  2000, and the patrol corps municipalities set up themselves, assembled one
  Transparency Portal request at a time.

slug: 'chile-policing'
share: false
---
