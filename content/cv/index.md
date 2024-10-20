---
title: Curriculum Vitae
date: 2023-09-29
type: landing

# todo: add a table of contents
sections:
  - block: markdown
    content:
      title: Curriculum Vitae
      subtitle: A PDF version of my CV is available to view or download [here](https://nredick.github.io/portfolio/resume.pdf).
      description: ""
    design:
      spacing:
        # Customize the section spacing. Order is top, right, bottom, left.
        padding: ["30px", "0", "30px", "0"]

  - block: experience
    content:
      title: Education
      # Date format for experience
      #   Refer to https://wowchemy.com/docs/customization/#date-format
      date_format: Jan 2006
      #   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
      items:
        - title: MSc in *Geophysics*
          company: University of California, Davis
          company_url: https://eps.ucdavis.edu
          #   company_logo: org-gc
          location: Davis, CA
          date_start: "2024-09-01"
        #   date_end: "2023-05-01"
        #   description: |2-
        #     * GPA: 3.75/4.0
        # todo: see if it's possible to color highlight the degrees
        # todo: add mcgill logo
        - title: BA in *Computer Science*, Minor in *Earth & Planetary Sciences*, Supplementary Minor in *Computer Science*
          company: McGill University
          company_url: https://www.mcgill.ca
          #   company_logo: org-gc
          location: Montreal, QC
          date_start: "2019-09-01"
          date_end: "2023-05-01"
          description: |2-
            * GPA: 3.75/4.0
    # design:
    #   spacing:
    #     # Customize the section spacing. Order is top, right, bottom, left.
    #     padding: ["30px", "0", "30px", "0"]

  # todo: make it pretty and add icons
  - block: markdown
    content:
      title: Skills
      text:
       "* **Programming Languages:** Python, Julia, C++, C, Java, DB2/SQL/MySQL, R, Bash, MATLAB, HTML/CSS, OCaml, MIPS Assembly
       * **Tools:** Git, Linux/Unix, LATEX, Jupyter, AWS EC2, VS Code, RESTful APIs, MongoDB, Jira, Jenkins"

    design:
      columns: "1"

  # todo: figure out how to add logos
  - block: experience
    content:
      title: Experience
      # Date format for experience
      #   Refer to https://wowchemy.com/docs/customization/#date-format
      date_format: Jan 2006
      # Experiences.
      #   Add/remove as many `experience` items below as you like.
      #   Required fields are `title`, `company`, and `date_start`.
      #   Leave `date_end` empty if it's your current employer.
      #   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
      items:
        - title: Technology Analyst
          company: Morgan Stanley
          company_url: https://www.morganstanley.com
          #   company_logo: org-gc
          location: Montreal, QC
          date_start: "2023-07-31"
          date_end: "2024-08-16"
        #   description: |2-
        #       * Worked collaboratively to provide agile metrics analysis for internal dev. teams globally, user support, & documentation.
        #       * Utilized DB2 SQL, MongoDB, & Python to process metrics and maintain project infrastructure.
        - title: Data Science Intern
          company: Esri Canada (Spot On Systems)
          company_url: https://www.esri.ca/en-ca/home
          # company_logo: org-x
          location: Remote
          date_start: "2022-05-17"
          date_end: "2022-08-05"
        #   description:
        - title: Software Engineering Intern
          company: Blue Spiral Interactive/Albany IT Group
          company_url: https://bluespiral.io
          # company_logo: org-x
          location: Saratoga Springs, NY
          date_start: "2019-08-31"
          date_end: "2019-06-01"
          # description:
        - title: Software Development Intern
          company: Garnet River
          company_url: https://www.esri.ca/en-ca/home
          # company_logo: org-x
          location: Saratoga Springs, NY
          date_start: "2019-02-01"
          date_end: "2019-06-01"
          # description:
    design:
      columns: "2"

  # todo: add personal projects
  - block: portfolio
    id: projects
    content:
      title: Projects
      filters:
        folders:
          - project
      # Default filter index (e.g. 0 corresponds to the first `filter_button` instance below).
      # default_button_index: 0
      # Filter toolbar (optional).
      # Add or remove as many filters (`filter_button` instances) as you like.
      # To show all items, set `tag` to "*".
      # To filter by a specific tag, set `tag` to an existing tag name.
      # To remove the toolbar, delete the entire `filter_button` block.
      # buttons:
      #   - name: All
      #     tag: "*"
      #   - name: Deep Learning
      #     tag: Deep Learning
      #   - name: Other
      #     tag: Demo
    design:
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: "1"
      view: 3
      # # For Showcase view, flip alternate rows?
      # flip_alt_rows: true

  - block: accomplishments
    content:
      # Note: `&shy;` is used to add a 'soft' hyphen in a long heading.
      title: "Awards"
      subtitle:
      # Date format: https://wowchemy.com/docs/customization/#date-format
      date_format: Jan 2006
      # Accomplishments.
      #   Add/remove as many `item` blocks below as you like.
      #   `title`, `organization`, and `date_start` are the required parameters.
      #   Leave other parameters empty if not required.
      #   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
      items:
        - date_start: "2022-10-01"
          description: |2-
            * Created a web app (`Python`, `HTML/CSS`, `Google Earth Engine`) that predicts the price & quality of a bottle of wine from climatological conditions of the year & region it was produced with sequential neural network.
          organization: McGill Artificial Intelligence Society (MAIS)
          organization_url: https://mcgillai.com
          title: Bogo Hack @ MAIS Hacks 2022
          url: https://devpost.com/software/read-between-the-wines

        - date_start: "2022-01-01"
          description: |2-
            * Led a team to create a COVID-19-themed Pac-Man webGL game using the Unity Game Engine (`C#`).
            * The game can be played at [this link](https://pacdemic-man-2vsjz.ondigitalocean.app/)!
          organization: McHacks
          organization_url: https://www.mchacks.ca
          title: Achievement Unlocked, Best Design @ McHacks9
          url: https://devpost.com/software/mcha-ck-fee-antivirus-2022-pan-demic-man

        - date_start: "2021-10-01"
          description: |2-
            * Led a team to create a web app, **MAISpeare** (`Python`, `HTML/CSS`) that generates a poem from an image using an LSTM.
          organization: McGill Artificial Intelligence Society (MAIS)
          organization_url: https://mcgillai.com
          title: Best AI Hack for Art @ MAIS Hacks 2021
          url: https://devpost.com/software/maispeare

        - date_start: "2020-10-01"
          description: |2-
            * Led a team to create a web app (`Python`, `HTML/CSS`) that predicts MBTI Personality Type based on Twitter data using a **XGBoost-driven neural network**.
          organization: McGill Artificial Intelligence Society (MAIS)
          organization_url: https://mcgillai.com
          title: Best Overall Hack @ MAIS Hacks 2020
          url: https://devpost.com/software/mbti-personality-classifier-2eho6w

        - date_start: "2021-05-01"
          description: |2-
            * Selected based on my research proposal to Use ML to Indentify Landslides & my academic performance.
          organization: Geotop
          organization_url: https://www.geotop.ca/index.php/en
          title: Geotop 2021 Scholarship Competition
          url: https://www.geotop.ca/en/formation/bourses/bourses-geotop

        - date_start: "2019-09-01"
          description: |2-
            * Entrance bursary to McGill University for academic excellence.
          organization: McGill University
          organization_url: https://www.mcgill.ca
          title: Alma Mater Scholarship

    design:
      columns: "1"

  - block: accomplishments
    content:
      # Note: `&shy;` is used to add a 'soft' hyphen in a long heading.
      title: "Extra-Curricular Activites"
      subtitle:
      # Date format: https://wowchemy.com/docs/customization/#date-format
      date_format: Jan 2006
      # Accomplishments.
      #   Add/remove as many `item` blocks below as you like.
      #   `title`, `organization`, and `date_start` are the required parameters.
      #   Leave other parameters empty if not required.
      #   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
      items:
        - date_end: "2023-04-30"
          date_start: "2020-09-01"
          description: |2-
            * Managed communications for the undergraduate student council for Earth & Planetary Sciences.
            * Designed & built the council’s website to host student resources, events, & other information.
          organization: The Monteregian Society (McGill University)
          organization_url: https://www.monteregiansociety.com
          title: Vice President Communications

        - date_end: "2021-05-30"
          date_start: "2021-01-01"
          description: |2-
            * Participated in an informal reading group with faculty and researchers to examine current papers in ML applications in the geosciences.
          organization: Machine Learning for Geoscience Reading Group (McGill University)
        #   organization_url: https://www.monteregiansociety.com
          title: Member
    design:
      columns: "2"

  - block: accomplishments
    content:
      # Note: `&shy;` is used to add a 'soft' hyphen in a long heading.
      title: "Professional Development"
      subtitle:
      # Date format: https://wowchemy.com/docs/customization/#date-format
      date_format: Jan 2006
      # Accomplishments.
      #   Add/remove as many `item` blocks below as you like.
      #   `title`, `organization`, and `date_start` are the required parameters.
      #   Leave other parameters empty if not required.
      #   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
      items:
        - date_start: "2020-12-01"
        #   description: |2-
        #     * Managed communications for the undergraduate student council for Earth & Planetary Sciences.
        #     * Designed & built the council’s website to host student resources, events, & other information.
          organization: American Geophysical Union (AGU)
          organization_url: https://www.agu.org
          title: SCIWS12 Tutorial on Machine Learning and Deep Learning for the environmental and geosciences
          url: https://www.agu.org/Events/FM20/SCIWS12-15-Tuesday-December

        - date_end: "2020-05-01"
          date_start: "2020-01-01"
          description: |2-
            * Selected through a technical interview to participate in a 12-week accelerated course on machine learning.
            * Webscraped data to train a CNN to classify geologic sample images into 4 classes; deployed as a webapp. Check out the repo [here](https://github.com/nredick/mais-202).
          organization: McGill Artificial Intelligence Society (MAIS)
          organization_url: https://mcgillai.com/mais202
          title: "MAIS 202: Accelerated Introduction to Machine Learning"
          url: https://github.com/nredick/mais-202
    design:
      columns: "1"

  # PUBLICATIONS
  - block: collection
    content:
      title: Publications
      filters:
        folders:
          - publication
        exclude_featured: false
    design:
      columns: "2"
      view: citation
---
