from flask import Flask,request,json,make_response
from flask_restful import Resource, Api, reqparse
import ast
import psycopg2
import connection
from psycopg2.extras import RealDictCursor
import spacy
from nltk import FreqDist

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
api = Api(app)

class NewsInput(Resource):
    def get(self):
        conn = connection.get_connection()
        cur = conn.cursor(cursor_factory = RealDictCursor)
        query_sql = "select * from News"
        cur.execute(query_sql)
        # row_headers=[x[0] for x in cur.description] #this will extract row headers
        rows = cur.fetchall()

        print("data selected successfully")
        conn.close()
        return json.jsonify(rows)


    def post(self):

        data = request.get_json()
        try:
            error_msg = {}
            # generate json response 
            to_return_json = {}
            for key,value in data.items(): 
                to_return_json[key] = {}
                doc = nlp(value['news'])
                dic = {}
                output = []
                for ent in doc.ents:
                    dic[ent.text] = ent.label_
                    output.append(ent.text)

                fdist = FreqDist(output)
                for ele in fdist.most_common(10):
                    to_return_json[key][ele[0]] = {}
                    to_return_json[key][ele[0]]["frequency"] = ele[1]
                    to_return_json[key][ele[0]]["category"] = dic[ele[0]]

            # inject news into database 
            try:
                conn = connection.get_connection()
                cur = conn.cursor()
                for key,value in data.items():
                    print(key)
                    print(value['news'])
                    cur.execute('''INSERT INTO News (ID,CONTENT) values( %s, %s)''', (int(key) ,value['news']))
                    
                conn.commit()
                print("news data inserted successfully")
            except Exception as error:
                error_msg['news_database'] = "news is not inserted successfully"
                print(error)
                # return json.jsonify({"message":"news is not inserted successfully"})

            # inject entity into database
            try:
                for key,value in data.items(): 
                    doc = nlp(value['news'])
                    dic = {}
                    output = []
                    for ent in doc.ents:
                        dic[ent.text] = ent.label_
                        output.append(ent.text)

                    fdist = FreqDist(output)
                    for ele in fdist.most_common():
                        cur.execute('''INSERT INTO Entity (ID,entity_category,entity_name,count) values( %s,%s,%s,%s)''', (int(key) ,dic[ele[0]],ele[0],ele[1]))
                conn.commit()
                conn.close()
                print("entity data inserted successfully")
            except Exception as error:
                error_msg['entity_database'] = "entities are not inserted successfully"
                print(error)
            
            to_return_json["error_message"] = error_msg
            if error_msg == {}:
                return make_response(json.jsonify(to_return_json),200)
            return make_response(json.jsonify(to_return_json),206)
        except Exception as error: 
            print(error)
            return json.jsonify({"message":"entities are not predicted"})



class Entity(Resource):
    def get(self,id,category=None):
        conn = connection.get_connection()
        cur = conn.cursor(cursor_factory = RealDictCursor)
        if category:
            cur.execute('''select * from entity where id = %s and entity_category = %s''',(id,category))
        else: 
            cur.execute('''select * from entity where id = %s ''',(id,))
        
        rows = cur.fetchall()
        conn.close()
        print("data selected successfully")
        return json.jsonify(rows)



api.add_resource(NewsInput, '/news')  
api.add_resource(Entity, '/entity/<string:id>','/entity/<string:id>/<string:category>')  



if __name__ == '__main__':
    nlp = spacy.load("en_core_web_sm")  

    app.run(host='0.0.0.0')  # run our Flask app