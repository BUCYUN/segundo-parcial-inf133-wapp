from flask import render_template
from flask_login import current_user

def register():
    return render_template(
        "register.html", title="Registrar Usuario", current_user=current_user
    )

def login():
    return render_template(
        "login.html", title="Iniciar Sesión", current_user=current_user
    )
