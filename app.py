from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Liste for å lagre input
text_list = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Hent tekst fra input-feltet
        text = request.form.get("text_input")
        if text:
            text_list.append(text)  # Legg til teksten i listen
        return redirect(url_for("index"))  # Oppdater siden
    return render_template("index.html", text_list=text_list)

if __name__ == "__main__":
    app.run(debug=True)