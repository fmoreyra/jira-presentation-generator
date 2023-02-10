# jira-presentation-generator

## Setup:

- Create virtual environment

```
python3 -m venv .venv
```

- Activate virtual environment

```
source .venv/bin/activate
```

- Install packages

```
pip install -r requirements.txt
```

- Run script and get tickets of current Sprint

```
python main.py
```

- Docker setup locally  (with docker installed and .env fully configured)

```
docker build -t jira-presentation-generator .
```

- Run docker image

```
docker run -v $(pwd):/usr/src/app jira-presentation-generator
```


## TODO:

- Eliminar slides innecesarias del template
- Limpiar código de generación de slides
- FEATURE: Subir imágenes relacionadas a una issue
- Upload de presentación a una carpeta de google drive