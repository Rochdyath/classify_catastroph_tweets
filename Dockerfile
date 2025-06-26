FROM python:3.10-slim

WORKDIR /app

ENV PYTHONPATH="${PYTHONPATH}:/app"

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN python -m nltk.downloader punkt punkt_tab stopwords wordnet averaged_perceptron_tagger_eng

COPY . .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
CMD ["run-main"]
