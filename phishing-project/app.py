from flask import Flask, request, render_template_string

app = Flask(__name__)

with open("index.html", "r", encoding="utf-8") as f:
    HTML = f.read()

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML)

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email", "")
    password = request.form.get("password", "")

    print("\n=== DEMO CREDENTIAL SUBMISSION ===")
    print(f"Email: {email}")
    print(f"Password: {password}")
    print("==================================\n")
    print("SIEM ALERT")
    print("Suspicious login activity detected")
    return """
    <html>
      <body style="font-family:Arial; text-align:center; margin-top:80px;">
        <h2>Login failed</h2>
        <p>Please contact customer support.</p>
        <p style="color:#777;">This is a controlled classroom demonstration.</p>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False, ssl_context=('cert.pem', 'key.pem'))

