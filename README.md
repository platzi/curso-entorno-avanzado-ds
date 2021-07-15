# Cookiecuter Personal Platzi

<!-- badges: start -->
[![@jvelzmagic](https://img.shields.io/badge/@jvelezmagic-Sitio_personal-blue?&logoColor=white)](https://jvelezmagic.com/) 
[![Platzi](https://img.shields.io/badge/Curso_Platzi-Configuración_Avanzada_...-green&logoColor=white)](https://platzi.com/datos/)
<!-- badges: end -->

Aprende a crear tu propia plantilla personalizada utilizando cookiecutter.

## Requiremientos

- [Anaconda](https://www.anaconda.com/download/) >= 4.x
- [git](https://git-scm.com/) >= 2.x
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0:
    Esto puede ser instalado con `pip` o `conda` dependiendo cómo tú manejas tus paquetes de Python:

``` bash
pip install cookiecutter
```

o

``` bash
conda install -c conda-forge cookiecutter
```

## Crear un nuevo proyecto

En el directorio en el que quieras guardar tu proyecto generado:

```bash
cookiecutter https://github.com/platzi/curso-entorno-avanzado-ds --checkout cookiecutter-personal-platzi
```


## Estructura de directorios y archivos resultantes

    {{ cookiecutter.project_slug }}
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
Proyecto creado con fines demostrativos para el curso "[Configuración avanzada...]()" de [Platzi](https://platzi.com/) por [@jvelezmagic](https://twitter.com/jvelezmagic).
