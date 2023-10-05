---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "MAISpeare"
summary: "Hackathon Project created at MAIS Hacks 2021, winner of the Best AI Hack for Art."
# authors: []
tags: [hackathon, poetry, xgboost, neural networks, nlp, art]
categories: [Hackathons, "Personal Projects"]
date: 2023-09-30T12:21:08-04:00

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

url_code: "https://github.com/nredick/mais-hacks-2021"
url_pdf: ""
url_slides: "MAISpeare_slides.pdf"
url_video: "https://youtu.be/-NJtXdIWoH8"

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---

Alongside some of my classmates at McGill University, I worked to create a web application based on a machine learning model that generates a 30-word poem based on an image prompt. Our project was created for the MAIS Hacks 2021, where it won the Best AI Hack for Art award.

We trained an LSTM neural network trained on 20,000k lines of poetry from the [Poems Dataset (NLP)](https://www.kaggle.com/datasets/michaelarman/poemsdataset) with Tensorflow Keras and used the Google Vision API for image analysis.

![MAISpeare](demo.png)