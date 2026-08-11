---
# The site used to live at /my-website/ as a GitHub Pages project site.
# Those URLs are still in Google; these aliases turn each one into a
# redirect to its replacement instead of a 404, which is what gets the
# old address out of the results and the ranking on to the new one.
aliases:
  - '/my-website/teaching/'

title: 'Teaching'
date: 2026-01-01
type: landing

design:
  spacing: '5rem'

sections:
  # The `markdown` block renders only `content.title` and `content.text`
  # (see blox/markdown/block.html) - other keys are ignored.
  # Raw HTML is allowed here (goldmark unsafe rendering is on in the theme);
  # `.teaching-courses` is styled in assets/css/custom.css.
  - block: markdown
    design:
      # Aligns this page's column and type size with /research/ and /fieldwork/
      # - see `.page-wide` in assets/css/custom.css.
      css_class: page-wide
    content:
      title: 'Teaching'
      text: |
        <p class="page-intro">I teach applied and quantitative economics at
        the <strong>Université Gustave Eiffel</strong>. Course materials are
        available on request — please
        <a href="mailto:daniel.perezparra@ird.fr">get in touch</a>.</p>

        <div class="teaching-courses">
          <div>
            <div class="course">
              <h3>Impact Evaluation Methods</h3>
              <p class="meta">Master's, year 2 · in English · since 2026</p>
            </div>
            <div class="course">
              <h3>Microeconomics II</h3>
              <p class="meta">Undergraduate, year 1 · in French · 2026 · Teaching Assistant</p>
            </div>
          </div>
          <div>
            <div class="course">
              <h3>Geospatial Analysis: Data and Inference</h3>
              <p class="meta">Master's, years 1–2 · in English · since 2026</p>
            </div>
            <div class="course">
              <h3>Development Economics Seminar</h3>
              <p class="meta">Master's, year 1 · in English · since 2026</p>
            </div>
          </div>
        </div>
---
