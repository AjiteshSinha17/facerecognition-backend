from flask import Blueprint, request, jsonify
from app.face_utils import register_face, recognize_face

attendance = Blueprint('attendance', __name__)

@attendance.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    file = request.files['image']
    response = register_face(name, file)
    return jsonify(response), response.get("status", 400)

@attendance.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    file = request.files['image']
    response = recognize_face(file)
    return jsonify(response), response.get("status", 400)
