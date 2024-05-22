from flask import render_template

def usuarios(patients):
    return render_template(
        "patients.html",
        patients=patients,
        title="Lista de usuarios",
    )

def create_patients():
    return render_template(
        "create_patients.html", title="Crear Paciente",
    )

def update_patients(patient):
    return render_template(
        "update_patient.html",
        title="Actualizar paciente",
        patient=patient,
    )
