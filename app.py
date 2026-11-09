from flask import Flask, render_template, request
from google import genai

app = Flask(__name__)
client = genai.Client()


def summarize(text):
    try:
        response = client.models.generate_content(
           model="gemini-3.5-flash-lite",
           contents="Summarize this in 3 sentences:\n\n" + text,
        )
        if response.text is None:
            return "No summary came back. Try again."
        return response.text
    except Exception as error:
       return "Error: " + str(error)


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        user_text = request.form["user_text"]
        result = summarize(user_text)
    return render_template("index.html", result=result)


if __name__ == "__main__":
   app.run(debug=True)