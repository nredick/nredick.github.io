---
title: Code-Free Deep Learning for Geospatial Applications
authors:
- Nathalie R. Redick
- Matthew S. Tarling
- James D. Kirkpatrick
date: '2024-01-23'
publishDate: '2025-09-03T18:12:24.241945Z'
publication_types:
- talk
abstract: In the geosciences, deep learning (DL) has been used to develop state-of-the-art
  methods for weather and climate prediction, seismic signal processing, and remote
  sensing analysis, among other tasks. However, developing a DL model demands an understanding
  of advanced programming and statistical techniques as well as domain knowledge of
  the desired task. Additionally, popular DL libraries do not currently have sufficient
  functionality for use in geoscience, which often works with large volumes of high-dimensional
  data in nonstandard file types, such as vector files or hyperspectral images. We
  have developed a novel, no-code DL workflow for geoscience applications that guides
  users in training a custom model and using it to produce classified geospatial data
  ready for input into any GIS software. It is completely open-source and distributed
  freely via Google Colaboratory. Our model is based on the UNet architecture, a deep
  convolutional neural network proficient at geospatial pixel-wise classification
  tasks due to the ability to maintain relative spatial information about the input
  data. Customization of the provided model is handled by interactive widgets. Geospatial
  inputs are stacked as image channels, allowing a model to learn from a variable
  number of inputs instead of only RGB color bands. For example, a trained model could
  analyze hyperspectral imagery alongside LiDAR to learn identifying features from
  both inputs. The workflow addresses the class imbalance problem prevalent in geospatial
  datasets through optional oversampling during data preprocessing and the use of
  focal loss during training. We demonstrate the utility of the workflow by implementing
  it on three different satellite and airborne LiDAR datasets. Due to the workflow's
  modularity, custom geospatial functionality, and open-source format, it has the
  potential to assist with a broad range of geospatial classification tasks.
tags:
- Deep learning
- Geospatial analysis
- Low-code
- Machine learning
- Open science
links:
- name: URL
  url: https://agu.confex.com/agu/fm23/meetingapp.cgi/Paper/1366363
- name: iPoster
  type: slides
  url: https://agu23.ipostersessions.com/Default.aspx?s=50-20-C0-E2-80-0B-ED-73-CC-3E-1D-A0-DA-35-98-9F
---
