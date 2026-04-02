from flask import Flask, render_template, request

app = Flask(__name__)

def check_url(url):
    score = 0

    if "https" not in url:
        score += 1

    suspicious_words = ["login", "verify", "bank", "free", "win"]
    for word in suspicious_words:
        if word in url:
            score += 1

    if len(url) > 50:
        score += 1

    if score >= 2:
        return "⚠️ Suspicious URL"
    else:
        return "✅ Safe URL"

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        url = request.form["url"]
        result = check_url(url)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run()