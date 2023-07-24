FROM python:3.9-alpine
WORKDIR /app
COPY requirements.txt ./
RUN pip install -U pip setuptools wheel
RUN python -m spacy download pt_core_news_lg
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["gunicorn", "-c gunicorn.config.py" "wsgi:app"]