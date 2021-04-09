# LegalNLP-API

NLP Web API for Legal Text

## Get Started
You will need Docker installed on your machine and access to the internet.

To start this project simply run:

docker-compose up -d

Running the above command starts the underlying Blackstone project as well as the API layer, which by default is running on port 80 at http://localhost/.

## Running precompiled image
You can also pull and run this docker image from Docker Hub:

docker pull openlegal/legalnlp-api
followed by

docker run -p 80:80 openlegal/legal-nlp-api

## Documentation

Documentation is available on /docs when you run the docker image.

Example is available: https://openlegal-legal-nlp-api.westeurope.azurecontainer.io/docs
