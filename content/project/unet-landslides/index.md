---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Using U-Net to Detect Landslides"
summary: "During my undergraduate degree, I worked with Dr. James Kirkpatrick and the California Geological survey to develop a custom machine learning model based on U-Net architecture to detect landslides in satellite imagery."
# authors: [admin]
tags: [machine learning, geoscience, landslides, u-net]
categories: [Research]
date: 2023-09-29T12:06:36-04:00

# Optional external URL for project (replaces project detail page).
external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
# image:
#   caption: ""
#   focal_point: ""
#   preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_code: ""
url_pdf: ""
url_slides: "unet-landslides_slides.pdf"
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---

In Spring 2021, I began working with Dr. James Kirkpatrick at McGill University to implement a customized deep learning model for identifying landslides in geospatial imagery. Originally, our goal was to predict landslides in a spatiotemporal context. We very quickly learned there was a severe lack of open, well-labeled data available for this project. Instead, we decided to focus on building a model that could create the kind of data we lacked.

Based on the U-Net image segmentation model originally developed for biomedical image segmentation by [Ronneberger et al. (2015)](https://arxiv.org/abs/1505.04597), we developed a custom model that could identify landslides in satellite imagery. The California Geological Survey (CGS) was kind enough to provide us with a small portion of their beta dataset of landslide scarp and deposit data in Los Briones, CA. The most recent iteration of the model was able to identify landslides with 95.3% accuracy and a loss of 0.19, but we are still facing challenges with the F1 Score, recall, and precision. In the near future, we hope to improve our model by using a larger dataset and by implementing a more robust data augmentation pipeline.

The project has been on and off at times and is currently on hold while I work on a related project.