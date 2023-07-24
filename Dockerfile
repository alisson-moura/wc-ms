FROM python:3.9-alpine
RUN apk add --no-cache gcc musl-dev g++
WORKDIR /app
COPY requirements.txt ./
RUN pip install -U pip setuptools wheel
RUN pip install -r requirements.txt
RUN python -m nltk.downloader all
COPY . .
EXPOSE 8080
CMD ["gunicorn", "-c", "gunicorn.config.py", "wsgi:app"]