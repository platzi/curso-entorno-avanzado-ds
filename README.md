# Paths Management Platzi 

<!-- badges: start -->
[![@jvelzmagic](https://img.shields.io/badge/@jvelezmagic-Sitio_personal-blue?&logoColor=white)](https://jvelezmagic.com/) 
[![Platzi](https://img.shields.io/badge/Curso_Platzi-Configuración_Avanzada_...-green&logoColor=white)](https://platzi.com/datos/)
<!-- badges: end -->

By: jvelezmagic.

Version: 0.1.0

Learn how to manage routes in your data science project.

## Prerequisites

- [Anaconda](https://www.anaconda.com/download/) >=4.x
- Optional [Mamba](https://mamba.readthedocs.io/en/latest/)

## Create environment

```bash
conda env create -f environment.yml
activate paths_management_platzi
```

or 

```bash
mamba env create -f environment.yml
activate paths_management_platzi
```

## Project organization

    paths_management_platzi
        ├── data
        │   ├── processed      <- The final, canonical data sets for modeling.
        │   └── raw            <- The original, immutable data dump.
        │
        ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
        │                         the creator's initials, and a short `-` delimited description, e.g.
        │                         `1.0-jvelezmagic-initial-data-exploration`.
        │
        ├── .gitignore         <- Files to ignore by `git`.
        │
        ├── environment.yml    <- The requirements file for reproducing the analysis environment.
        │
        └── README.md          <- The top-level README for developers using this project.

---
Project created for demonstration purposes for the course "[Configuración Avanzada...]()" by [Platzi](https://platzi.com/) - [@jvelezmagic](https://jvelezmagic.com/).
