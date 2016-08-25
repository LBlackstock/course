"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from datetime import time 

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('Course')
        self.db = self._app.codingdojo
   
    def index(self):
        courses = self.models['Course'].get_courses()
        print "all courses", courses
        return self.load_view('index.html', courses=courses)

    def add_course(self):
        course_id = self.models['Course'].add_course(request.form)
        print "new course id", course_id
        return redirect('/')

    def confirm_delete(self, id):
        print id
        course = self.models['Course'].get_course(id)
        print course
        return self.load_view('delete.html', course=course)

    def delete(self, course_id):
        print id
        self.models['Course'].delete(id)
        return redirect('/')