# Tweet Disaster Classification

Ce projet classe les tweets selon qu’ils décrivent une catastrophe réelle (1) ou non (0).

## Structure du projet

tweet_project/
├── data/ # Contient les données CSV
├── notebooks/ # EDA et modélisation
├── src/ # Code source
├── tests/ # Tests unitaires
├── main.py # Script principal
├── requirements.txt
├── Dockerfile
└── README.md

## Exécution

```bash
docker build -t tweet-project .
docker run --rm tweet-project
```

## Lancer les tests
```bash
docker run --rm tweet-project run-tests
```
