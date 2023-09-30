---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Building an Accessible Machine Learning Workflow for Geospatial Analysis"
summary: ""
# authors: [admin]
tags: [research, deep learning, geospatial, no-code, satellite imagery, u-net]
categories: [Research]
date: 2023-09-29T19:30:05-04:00

# Optional external URL for project (replaces project detail page).
external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_code: "https://github.com/nredick/geospatial-unet"
url_pdf: ""
url_slides: "geospatial-dl_slides.pdf"
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---

Starting in Fall 2022, I began working with Dr. Matthew Tarling and Dr. Jamie Kirkpatrick at McGill University to develop a deep learning (DL) workflow for geospatial analysis. Inspired by challenges we faced developing a DL model for landslide identification, we decided to create a free, open-source workflow for processing geospatial data and training DL models on the processed data. The workflow is designed to be accessible to researchers with little to no coding experience. The workflow is currently in development and we hope to publish a paper in the near future.

The workflow is distributed in Jupyter notebook format (available on Github) and designed to be run on Google Colab, requiring no environment set up from the user. Alongside the notebook, we intend to provide a step-by-step guide and a demo dataset.

In order to make the workflow customizable for different datasets, we have designed it to be incredibly modular through the use of widgets: drop-down buttons, radio buttons, text boxes, and more. The Jupyter notebook format allows basic instructions to be provided alongside the code as well.

Notably, the model can take any number of geospatial parameters as input, including satellite imagery, elevation data, and more. Data is stacked along the channel dimension and fed into a customized DL model based on U-Net. For more details on the implementation and the model architecture, check out linked code repository and the slides from my presentation at the Dept. of Earth and Planetary Sciences Undergraduate Research Symposium (2023).

This project is still in development. Check back soon for updates!