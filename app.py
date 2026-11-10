from flask import Flask, render_template, request
from google import genai

app = Flask(__name__)
client = genai.Client()


def summarize(text, length):
    try:
        response = client.models.generate_content(
           model="gemini-3.5-flash-lite",
           contents="Summarize this in " + length + ":\n\n" + text,
        )
        if response.text is None:
            return "No summary came back. Try again."
        return response.text
    except Exception as error:
       return "Error: " + str(error)


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    user_text = ""
    length = "3 sentence"
    if request.method == "POST":
        user_text = request.form["user_text"].strip()
        length = request.form.get("length", "3 sentence")
        if user_text == "":
            result = "Please paste some text."
        else:
            result = summarize(user_text, length)
    return render_template("index.html", result=result, user_text=user_text, length=length)


if __name__ == "__main__":
   app.run(debug=True)