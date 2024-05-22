from flask import Blueprint, request, redirect, url_for
from views import patients_view
from utils.decorator import role_required
from flask_login import login_user, logout_user, login_required, current_user
from models.patients_model import Patient

patient_bp = Blueprint("patient", __name__)

@patient_bp.route("/patients")
def list_users():
    patients = Patient.get_all()
    return patients_view.patients(patients)

@patient_bp.route("/patients/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
def create_user():
    if request.method == "POST":
        name = request.form["name"]
        last_name = request.form["last_name"]
        ci = request.form["ci"]
        birth_date = request.form["birth_date"]
        patient = Patient(name, last_name, ci, birth_date)
        patient.save()
        return redirect(url_for("user.list_users"))
    return patients_view.create_patients()

@patient_bp.route("/patients/<int:id>/update", methods=["GET", "POST"])
@login_required
@role_required("admin")
def update_user(id):
    patient = Patient.get_by_id(id)
    if not patient:
        return "Usuario no encontrado", 404
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        ci = request.form["ci"]
        birth_date = request.form["birth_date"]
        patient.first_name = first_name
        patient.last_name = last_name
        patient.ci = ci
        patient.birth_date = birth_date
        patient.update()
        return redirect(url_for("user.list_users"))
    return patients_view.update_patients(patient)


@patient_bp.route("/patients/<int:id>/delete")
@login_required
@role_required("admin")
def delete_user(id):
    patient = Patient.get_by_id(id)
    if not patient:
        return "Usuario no encontrado", 404
    patient.delete()
    return redirect(url_for("user.list_users"))