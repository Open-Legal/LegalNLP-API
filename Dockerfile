FROM python:3.6.8

ENV SPACY_MODEL=en_core_web_sm

RUN pip install https://blackstone-model.s3-eu-west-1.amazonaws.com/en_blackstone_proto-0.0.1.tar.gz

RUN pip install nltk==3.6.2 lexnlp==2.2.1.0 fastapi-cloudauth==0.4.0 fastapi==0.68.1 blackstone uvicorn==0.15.0 regex==2022.3.15

RUN python -m nltk.downloader all

EXPOSE 80

COPY ./app /app

CMD ["python", "/app/main.py"]
