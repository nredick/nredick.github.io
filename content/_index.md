---
# Leave the homepage title empty to use the site title
title:
date: 2024-10-16
type: landing

sections:
  - block: about.biography
    id: about
    content:
      title: About Me
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin

  # PUBLICATIONS
  - block: collection
    id: gallery
    content:
      title: Recent Publications
      #   text: |-
      #     {{% callout note %}}
      #     [Filter publications](./publication/).
      #     {{% /callout %}}
      filters:
        folders:
          - publication
        exclude_featured: false
    design:
      columns: "2"
      view: citation

  # TALKS
  #   - block: collection
  #     id: talks
  #     content:
  #       title: Recent & Upcoming Talks
  #       filters:
  #         folders:
  #           - event
  #     design:
  #       columns: "2"
  #       view: compact
  #   - block: tag_cloud
  #     content:
  #       title: Popular Topics
  #     design:
  #       columns: "2"

  #   - block: features
  #     content:
  #       title: Skills
  #       items:
  #         - name: R
  #           description: 90%
  #           icon: r-project
  #           icon_pack: fab
  #         - name: Statistics
  #           description: 100%
  #           icon: chart-line
  #           icon_pack: fas
  #         - name: **Photography**
  #           description: 10%
  #           icon: camera-retro
  #           icon_pack: fas

  #   - block: collection
  #     id: posts
  #     content:
  #       title: Recent Posts
  #       subtitle: ''
  #       text: ''
  #       # Choose how many pages you would like to display (0 = all pages)
  #       count: 5
  #       # Filter on criteria
  #       filters:
  #         folders:
  #           - post
  #         author: ""
  #         category: ""
  #         tag: ""
  #         exclude_featured: false
  #         exclude_future: false
  #         exclude_past: false
  #         publication_type: ""
  #       # Choose how many pages you would like to offset by
  #       offset: 0
  #       # Page order: descending (desc) or ascending (asc) date.
  #       order: desc
  #     design:
  #       # Choose a layout view
  #       view: compact
  #       columns: '2'

  # PHOTOS
  - block: markdown
    content:
      title: Gallery
      subtitle: "Some photos from the field and travels!"
      text: |-
        {{< gallery album="gallery" >}}
    design:
      columns: "1"

  - block: contact
    id: contact
    content:
      title: Contact
      subtitle:
    #   text: |-
    #     Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam mi diam, venenatis ut magna et, vehicula efficitur enim.
    #   # Contact (add or remove contact options as necessary)
      email: nathalie.redick@mail.mcgill.ca
    #   phone: 888 888 88 88
    #   appointment_url: 'https://calendly.com'
      address:
        # street: 450 Serra Mall
        city: Montréal
        region: QC
        # postcode: '94305'
        # country: Canada
        country_code: CA
    #   directions: Enter Building 1 and take the stairs to Office 200 on Floor 2
    #   office_hours:
    #     - 'Monday 10:00 to 13:00'
    #     - 'Wednesday 09:00 to 10:00'
      contact_links:
        - icon: linkedin
          icon_pack: fab
          name: Connect with me
          link: https://www.linkedin.com/in/nredick/

        # - icon: skype
        #   icon_pack: fab
        #   name: Skype Me
        #   link: 'skype:echo123?call'

        # - icon: video
        #   icon_pack: fas
        #   name: Zoom Me
        #   link: 'https://zoom.com'
      # Automatically link email and phone or display as text?
      autolink: true
    #   # Email form provider
    #   form:
    #     provider: netlify
    #     formspree:
    #       id:
    #     netlify:
    #       # Enable CAPTCHA challenge to reduce spam?
    #       captcha: false
    design:
      columns: '2'
---