""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class CourseModel(Model):
    def __init__(self):
        super(WelcomeModel, self).__init__()

    def get_course(self):
        query = "SELECT * from courses"
        return self.db.query_db(query)

    def add_course(self):
        query = "INSERT into courses (course, description, created_at, updated_at) Values(: course, NOW()) where id = :id"
        data = {
            'course': ['course'],
            'description': ['discription']
        }
        return self.db.query_db(query, data)

    def get_course(self, id):
        query = "SELECT * FROM courses WHERE id=:id"
        values = {
            'id': id 
        }
        return self.db.query_db(query, values)
    
    def delete(self, id):
        query = "DELETE FROM courses WHERE id=:id"
        values = {
            'id': id
        }
        self.db.query_db(query, values)
        
