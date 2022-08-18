from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

students = []


class Student(Resource):

    def get(self, name):
        """
        for student in students:
            if student["name"] == name:
                return student
        """
        student = next(filter(lambda x: x["name"] == name, students), None)
        return {'student': student}, 200 if student else 404

    def post(self, name):
        if next(filter(lambda x: x["name"] == name, students), None):
            return {"message": f"Student with same name exists"}, 400

        data = request.get_json();
        student = {"name": name,
                   "id": data["id"]}
        students.append(student)
        return student


class StudentList(Resource):
    def get(self):
        return {"students": students}, 200


api.add_resource(Student, '/student/<string:name>')  # http://127.0.0.1:5000/student/Dheeren
api.add_resource(StudentList, "/students/")  # http://127.0.0.1:5000/students

app.run(port=5000)
