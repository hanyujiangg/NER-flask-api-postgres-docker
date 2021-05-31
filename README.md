# NER-flask-api-docker-postgres
A docker containerised REST API that takes in news in json format and return the top 10 most frequent named entity and store the input data and predicted data in local Postgres database. 

This serves as a proof-of-concept for further development in the future.

## Potential Business Use Cases 
1. Store the important named entity in the database from news channels so that all news related to a company of interest can be retrieved. 
2. Produce keywords for the news articles for tagging.  
3. Help analysts have a rough idea of the news articles by skimming through the key named entities.

## Named Entity Recognition Models 
Literature review and testing were carried out to determine the best NER model for the data given the sample input news data as file sample_news_10.json for this project. For this POC, Stanford NER model and Spacy NER models were chosen and compared. 

Please refer to this [README.md for model comparison](https://github.com/hanyujiangg/NER-flask-api-postgres-docker/blob/master/model-comparison/README.md) for further details.

Spacy model is able to capture more named entities and more occurrence of the entities. Thus, for this project **Spacy en_core_web_sm** is used. 

## Named Entity Labels in Spacy
|   |   |
|---|---|
|  ![image](https://user-images.githubusercontent.com/35590255/120158172-68ef6f80-c226-11eb-8a0c-a6c80a9fe16c.png) | ![image](https://user-images.githubusercontent.com/35590255/120158189-6d1b8d00-c226-11eb-971f-242168fcd596.png)  |




## API Introduction
The application is a REST API development with Flask. It serves three functions: 
1. Receives news input and responds with the top 10 most frequent named entity in each news input, and store the news and predicted entities in the Postgres database if any. 
2. Retrieve news in the Postgres database
3. Retrieve named entities and frequencies for a particular piece of news and/or category(ORG DATE etc.) in the database

## API Documentation 
The API is designed to return various HTTP status codes in the response header

| HTTP Status Code | Remarks                 |
|------------------|-------------------------|
| 200              | OK                      |
| 206              | Partial Success Request |
| 400              | Bad Request             |
| 404              | Request URLNot Found    |
| 500              | Internal Server Error   |

Please change the URL according to the usage. 
flask: http://127.0.0.1:5000/ (If it is run directly after git clone the code without the Docker image)
localhost: localhost:5000/ (This is the default URL after pull and run the docker image)


### Send News -/POST
Send news articles to get back predicted named entities for each article. 

http://127.0.0.1:5000/news <br/>
localhost:5000/news

#### JSON Body 
see sample_news_10.json

#### Response

```json

{
    "7": {
        "Ethereum": {
            "frequency": 7,
            "category": "ORG"
        },
        "ETH": {
            "frequency": 4,
            "category": "ORG"
        }
    },
    "8": {
        "Trump": {
            "frequency": 20,
            "category": "ORG"
        },
        "House": {
            "frequency": 6,
            "category": "ORG"
        }
    },
    "error_message": {
        "news_database": "news is not inserted successfully",
        "entity_database": "entities are not inserted successfully"
    }
}

```

It returns the top 10 most frequent entities in each news article along with error_message if any. If the database connection fails or news or entity already exists in the database, the respective error message will appear in the JSON response and status code 206 will be returned. 

### Retrieve News -/GET
Retriveves all news articles in the database

http://127.0.0.1:5000/news <br/>
localhost:5000/news

#### Response 

```json
[
    {
        "id": 1,
        "content": "The stock market rises"
    },
    {
        "id": 2,
        "content": "The stock market falls"
    },
    {
        "id": 3,
        "content": "The moon is full"
    }
]
```

It returns the news articles stored in the database from previous injection from send news operation. 

### Retrieve Entity -/GET
Retrieve all entity based on the user inputs

http://127.0.0.1:5000/<news_id>/<Category-optional> <br/>
localhost:5000/<news_id>/<Category-optional>
    
This GET method has two formats for different use cases.      
For example, http://127.0.0.1:5000/entity/7/ORG or http://127.0.0.1:5000/entity/7

#### Response 
For http://127.0.0.1:5000/entity/7/ORG
    
```json
[
    {
        "id": 7,
        "entity_category": "ORG",
        "entity_name": "Ethereum",
        "count": 7
    },
    {
        "id": 7,
        "entity_category": "ORG",
        "entity_name": "ATH",
        "count": 3
    },
    {
        "id": 7,
        "entity_category": "ORG",
        "entity_name": "Polkadot",
        "count": 1
    }
]
    
```

It returns the all the named entities stored in the database for the news with the input news id and input category.
    
For http://127.0.0.1:5000/entity/7
    
```json
[
    {
        "id": 7,
        "entity_category": "DATE",
        "entity_name": "the summer of June 2020",
        "count": 1
    },
    {
        "id": 7,
        "entity_category": "CARDINAL",
        "entity_name": "between 500k-600k",
        "count": 1
    },
    {
        "id": 7,
        "entity_category": "MONEY",
        "entity_name": "$3.74 million",
        "count": 1
    }

]
    
```
    
It returns all the named entities of all categories stored in the databse with the input news id.
    
## Installation 
### Docker
The application is containerised in a docker image.
    
To start running, in the terminal input the following,
    
```
    
    docker pull docker.pkg.github.com/hanyujiangg/ner-flask-api-postgres-docker/python-docker:1.1
    
```
<br/>
    Run the pulled docker image and publish a port for our container
  <br/>  
    
```
    docker run --publish 5000:5000 docker.pkg.github.com/hanyujiangg/ner-flask-api-postgres-docker/python-docker:1.1
```
    
This should be the output after executing the above command:
    
```
 $ docker run --publish 5000:5000 docker.pkg.github.com/hanyujiangg/ner-flask-api-postgres-docker/python-docker:1.1
 * Serving Flask app 'flask_api' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://172.17.0.2:5000/ (Press CTRL+C to quit)
```
And use send news API through Postman to start off. Please note that the default URL is **localhost:5000**.
    
### Postgres database configuration 
The application is supposed to connect with a local Postgres database. 
Create a local postgres database and change the connection.py accordingly.
    
```
DB_NAME = "mrosbzup"
DB_USER = "mrosbzup"
DB_PASS = "aqNEI7Y05XCIS7GQYdgqc9ksMNxqlhwj"
DB_HOST = "batyr.db.elephantsql.com"
DB_PORT = "5432"
    
```
Then run the following command line to create the tables for News and Entity
    ```
    python createtable.py
    ```
The news retrival, entity retrival and news and entity storing functions should work after this step. 
    
However, the send news function should work even without a database. 

## Reference
1. https://docs.docker.com/language/python/build-images/
2. https://towardsdatascience.com/the-right-way-to-build-an-api-with-python-cd08ab285f8f
3. https://flask.palletsprojects.com/en/2.0.x/

    


