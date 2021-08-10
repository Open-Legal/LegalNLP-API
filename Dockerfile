FROM python:3.6.8

RUN pip install nltk fastapi uvicorn lexnlp fastapi-cloudauth 

RUN python -m nltk.downloader all

EXPOSE 80

COPY ./app /app

CMD ["python", "/app/main.py"]
