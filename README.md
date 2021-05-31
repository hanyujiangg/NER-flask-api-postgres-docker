# NER-flask-api-docker-postgres
A docker containerised REST API that takes in news in json format and return the top 10 most frequent named entity and store the input data and predicted data in local Postgres database. 

This serves as a proof-of-concept for further development in the future.

## Potential Business Use Cases 
1. Store the important named entity in the database from news channels so that all news related to a company of interest can be retrieved. 
2. Produce keywords for the news articles for tagging.  
3. Help analysts have a rough idea of the news articles by skimming through the key named entities.

## Named Entity Recognition Models
Literature review and testing were carried out to determine the best NER model for the data given the sample input news data as file sample_news_10.json for this project. For this POC, Stanford NER model and Spacy NER models were chosen and compared. Since Stanford NER model produces NER prediction in a different format than Spacy, functions are created to standardise the output in the desired format. 

#### Stanford NER en_core_web_sm output before modification: 
[('Meyer', 'ORGANIZATION'), ('Handelman', 'ORGANIZATION'), ('Co.', 'ORGANIZATION'), ('Increases', 'ORGANIZATION'), ('Position', 'ORGANIZATION'), ('in', 'O'), ('TE', 'ORGANIZATION'), ('Connectivity', 'ORGANIZATION'), ('Ltd.', 'ORGANIZATION'), ('(', 'O'), ('NYSE', 'O'),...]



#### Spacy NER en_core_web_sm output before modification: 
Meyer Handelman Co. Increases Position 0 38 ORG
TE Connectivity Ltd. 42 62 ORG
NYSE 64 68 ORG
TEL 69 72 ORG
Meyer Handelman Co. Increases Position 75 113 ORG
TE Connectivity Ltd. 117 137 ORG
NYSE 139 143 ORG
...

#### Spacy NER en_core_web_lg output before modification: 
Meyer Handelman Co. Increases Position 0 38 ORG
TE Connectivity Ltd. 42 62 ORG
NYSE 64 68 ORG
TEL 69 72 ORG
Meyer Handelman Co. Increases Position 75 113 ORG
TE Connectivity Ltd. 117 137 ORG
NYSE 139 143 ORG
...

From here we see that Spacy en_core_web_sm and en_core_web_lg does not produce a significant difference for our data so en_core_web_sm were chosen for its smaller size. 
NER output format standardisation was carried out to compare the prediction results for Stanford NER and Spacy en_core_web_sm.

![Screenshot 2021-05-31 at 2 07 05 PM](https://user-images.githubusercontent.com/35590255/120147622-82d68580-c219-11eb-9d8d-6734323edb4e.jpg)

As we can see from the results above, Spacy model is able to capture more named entities and more occurrence of the entities. Thus, for this project Spacy en_core_web_sm is used. 

## API Introduction
The application is a REST API development with Flask. It serves three functions: 
1. Receives news input and responds with the top 10 most frequent named entity in each news input 
2. Retrieve news in the Postgres database
3. Retrieve named entities and frequencies for a particular piece of news and/or category(ORG DATE etc.) in the database

## API Documentation 
### Send News -/POST
http://127.0.0.1:5000/news

#### JSON Body 
see sample_news_10.json

#### Response
{
    "7": {
        "Ethereum": {
            "frequency": 7,
            "category": "ORG"
        },
        "ETH": {
            "frequency": 4,
            "category": "ORG"
        },
        "ATH": {
            "frequency": 3,
            "category": "ORG"
        },
        "Bitcoin Ethereum News\n": {
            "frequency": 1,
            "category": "ORG"
        },
        "1,800": {
            "frequency": 1,
            "category": "MONEY"
        },
        "2,000": {
            "frequency": 1,
            "category": "MONEY"
        },
        "CoinMetrics": {
            "frequency": 1,
            "category": "ORG"
        },
        "the summer of June 2020": {
            "frequency": 1,
            "category": "DATE"
        },
        "between 500k-600k": {
            "frequency": 1,
            "category": "CARDINAL"
        },
        "January 2021": {
            "frequency": 1,
            "category": "DATE"
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
        },
        "Republicans": {
            "frequency": 6,
            "category": "NORP"
        },
        "Capitol": {
            "frequency": 5,
            "category": "ORG"
        },
        "Joe Neguse": {
            "frequency": 5,
            "category": "PERSON"
        },
        "Democrats": {
            "frequency": 4,
            "category": "NORP"
        },
        "Senate": {
            "frequency": 4,
            "category": "ORG"
        },
        "February 10, 2021": {
            "frequency": 3,
            "category": "DATE"
        },
        "Lopatic": {
            "frequency": 3,
            "category": "NORP"
        },
        "Republican": {
            "frequency": 3,
            "category": "NORP"
        }
    },
    "error_message": {
        "news_database": "news is not inserted successfully",
        "entity_database": "entities are not inserted successfully"
    }
}

It returns the top 10 most frequent entities in each news article along with error_message if any. If the database connection fails or news or entity already exists in the database, the respective error message will appear in the JSON response. 

### Send News -/POST
http://127.0.0.1:5000/news

#### JSON Body 
see sample_news_10.json
