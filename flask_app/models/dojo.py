from flask.globals import request
from flask_app.models.ninja import Ninja
from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name,created_at,updated_at) \
        VALUES (%(dojoname)s, NOW(), NOW());"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return cls(results[0])

    @classmethod
    def get_dojo_by_id_with_ninjas(cls,data):
        query = "SELECT * FROM dojos \
        JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(results)
        if results:
            dojo = cls(results[0])
            for row in results:
                data = {
                    "id": row['ninjas.id'],
                    "first_name": row['first_name'],
                    "last_name": row['last_name'],
                    "age" : row['age'],
                    "created_at": row['ninjas.created_at'],
                    "updated_at": row['ninjas.updated_at'],
                }
                dojo.ninjas.append(Ninja(data))
        else:
            dojo = Dojo.get_by_id(data)
        return dojo


    
        