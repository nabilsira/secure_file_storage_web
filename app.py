from flask import Flask, render_template, request, send_file, redirect, url_for, flash
import os
from encrypt import encrypt_file
from decrypt import decrypt_file
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "secret123"

UPLOAD_FOLDER = "uploads"
ENCRYPTED_FOLDER = "encrypted"
DECRYPTED_FOLDER = "decrypted"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ENCRYPTED_FOLDER, exist_ok=True)
os.makedirs(DECRYPTED_FOLDER, exist_ok=True)

# Dashboard Data
encrypt_count = 0
decrypt_count = 0
activity_log = []


# 🏠 HOME PAGE (opens first)
@app.route("/")
def home():
    return render_template("index.html")


# 📊 DASHBOARD
@app.route("/dashboard")
def dashboard():
    return render_template(
        "dashboard.html",
        encrypt_count=encrypt_count,
        decrypt_count=decrypt_count,
        activity=activity_log[-5:]
    )


# 🔐 ENCRYPT
@app.route("/encrypt", methods=["POST"])
def encrypt():
    global encrypt_count

    file = request.files.get("file")
    password = request.form.get("password")

    if not file or file.filename == "":
        flash("No file selected ❌")
        return redirect(url_for("dashboard"))

    if not password:
        flash("Password required ❌")
        return redirect(url_for("dashboard"))

    try:
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        output_file = encrypt_file(filepath, password, ENCRYPTED_FOLDER)

        encrypt_count += 1
        activity_log.append(f"🔒 {filename} encrypted")

        return send_file(output_file, as_attachment=True)

    except Exception as e:
        print("Encryption Error:", e)
        flash("Error during encryption ❌")
        return redirect(url_for("dashboard"))


# 🔓 DECRYPT
@app.route("/decrypt", methods=["POST"])
def decrypt():
    global decrypt_count

    file = request.files.get("file")
    password = request.form.get("password")

    if not file or file.filename == "":
        flash("No file selected ❌")
        return redirect(url_for("dashboard"))

    if not password:
        flash("Password required ❌")
        return redirect(url_for("dashboard"))

    try:
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        output_file = decrypt_file(filepath, password, DECRYPTED_FOLDER)

        decrypt_count += 1
        activity_log.append(f"🔓 {filename} decrypted")

        return send_file(output_file, as_attachment=True)

    except Exception as e:
        print("Decryption Error:", e)
        flash("Wrong password or corrupted file ❌")
        return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(debug=True)