
# Named Entity Recognition Models
Literature review and testing were carried out to determine the best NER model for the data given the sample input news data as file sample_news_10.json for this project. For this POC, Stanford NER model and Spacy NER models were chosen and compared. 

### Stanford NER Model
This model is implemented in Java and is based on linear chain CRF (Conditional Random Field) sequence models. For various applications, custom models can be trained with labeled data sets.

It has three models:
1. 3-class : Location, person, organization
2. 4-class : Location, person, organization, misc.
3. 7-class : Location, person, organization, money, percent, date, time

The 7 class model is used in the comparison. 
Since Stanford NER model produces NER prediction in a different format than Spacy, functions are created to standardise the output in the desired format. 

#### Stanford NER en_core_web_sm output before modification: 

```
[('Meyer', 'ORGANIZATION'), ('Handelman', 'ORGANIZATION'), ('Co.', 'ORGANIZATION'), ('Increases', 'ORGANIZATION'), ('Position', 'ORGANIZATION'), ('in', 'O'), ('TE', 'ORGANIZATION'), ('Connectivity', 'ORGANIZATION'), ('Ltd.', 'ORGANIZATION'), ('(', 'O'), ('NYSE', 'O'),...]
```

### Spacy NER Model
The Spacy NER system contains a word embedding strategy using sub word features and "Bloom" embed, and a deep convolution neural network with residual connections. The system is designed to give a good balance of efficiency, accuracy and adaptability.

#### Spacy NER en_core_web_sm output before modification: 
```
Meyer Handelman Co. Increases Position 0 38 ORG
TE Connectivity Ltd. 42 62 ORG
NYSE 64 68 ORG
TEL 69 72 ORG
Meyer Handelman Co. Increases Position 75 113 ORG
TE Connectivity Ltd. 117 137 ORG
NYSE 139 143 ORG
...
```

#### Spacy NER en_core_web_lg output before modification: 
```
Meyer Handelman Co. Increases Position 0 38 ORG
TE Connectivity Ltd. 42 62 ORG
NYSE 64 68 ORG
TEL 69 72 ORG
Meyer Handelman Co. Increases Position 75 113 ORG
TE Connectivity Ltd. 117 137 ORG
NYSE 139 143 ORG
...
```

From here we see that Spacy en_core_web_sm and en_core_web_lg does not produce a significant difference for our data so en_core_web_sm were chosen for its smaller size. 
NER output format standardisation was carried out to compare the prediction results for Stanford NER and Spacy en_core_web_sm.

![Screenshot 2021-05-31 at 2 07 05 PM](https://user-images.githubusercontent.com/35590255/120147622-82d68580-c219-11eb-9d8d-6734323edb4e.jpg)

As we can see from the results above, Spacy model is able to capture more named entities and more occurrence of the entities. Thus, for this project **Spacy en_core_web_sm** is used. 

## Named Entity Labels in Spacy
|   |   |
|---|---|
|  ![image](https://user-images.githubusercontent.com/35590255/120158172-68ef6f80-c226-11eb-8a0c-a6c80a9fe16c.png) | ![image](https://user-images.githubusercontent.com/35590255/120158189-6d1b8d00-c226-11eb-971f-242168fcd596.png)  |



## Reference
1. https://spacy.io/usage/spacy-101
2. https://nlp.stanford.edu/software/CRF-NER.html
3. https://blog.vsoftconsulting.com/blog/understanding-named-entity-recognition-pre-trained-models#:~:text=Model%20Architecture,-The%20current%20architecture&text=The%20Spacy%20NER%20system%20contains,of%20efficiency%2C%20accuracy%20and%20adaptability.
    
    
    


