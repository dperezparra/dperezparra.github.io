---
title: 'Données'
slug: 'datasets'
type: landing

design:
  spacing: '5rem'

request:
  title: 'Pour en obtenir un'
  text: >
    Une seule demande vaut pour les trois — dites-moi lequel vous intéresse et
    sur quoi vous travaillez, et je vous l'enverrai avec le code et une
    présentation de la manière dont il a été construit, de ce qu'il permet et
    de ce qu'il ne permet pas. Les seules conditions sont qu'il ne soit pas
    redistribué et que les sources d'origine soient citées. La seule exception
    est le recensement scolaire du Sénégal, dont l'accès relève du ministère de
    l'Éducation : une demande le concernant lui est donc transmise.
  url: 'mailto:daniel.perez-parra@ird.fr?subject=Dataset%20request'
  label: 'Demander un jeu de données'

sections:
  - block: markdown
    design:
      css_class: 'page-wide datasets-intro'
    content:
      title: 'Données'
      text: |
        <p class="page-intro">Des données originales que j'ai collectées,
        extraites du web ou obtenues auprès d'autorités nationales au fil de mes
        recherches. La plupart ne sont pas publiées en accès libre ; je les
        partage donc, comme un bien public, avec les chercheurs et les étudiants
        de master qui en font la demande.</p>
        <p class="page-intro">La demande prend délibérément la forme d'un échange
        plutôt que d'un lien de téléchargement : chacun de ces jeux de données
        repose sur des hypothèses de construction qui déterminent ce à quoi il
        peut servir et ce à quoi il ne peut pas servir, et je préfère les
        expliquer plutôt que de voir les données utilisées d'une manière qu'elles
        ne permettent pas. Écrivez-moi quelques lignes sur ce que vous avez en
        tête — je serai ravi de vous aider et de vous guider :)</p>

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
