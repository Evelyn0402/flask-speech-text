
from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    ## upload files 
    transcript = ""
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        ## import model
        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            try:
                transcript = recognizer.recognize_google(data, key=None)
            except sr.UnknownValueError:
                transcript = "Can not idenfity the audio"
            except sr.RequestError as e:
                transcript = f"wrong require{e}"

    ## interface 
    # index.html定义UI的内容（如文字、按钮）, index.css定义样式（如颜色、布局）, index.html通过<link>加载index.css
    return render_template('index.html', transcript=transcript)

if __name__ == "__main__":
    app.run(debug=False, threaded=True, host='0.0.0.0', port=5000)

