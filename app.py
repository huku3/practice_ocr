from flask import Flask
from flask import render_template
from flask import request
from PIL import Image
import pyocr

app = Flask(__name__)


# tools = pyocr.get_available_tools()
# tool = tools[0]

# imag = Image.open("")

# txt = tool.image_to_string(imag, lang="eng+jpn", builder=pyocr.builders.TextBuilder())


@app.route("/")
def index():
    return render_template("index.html")


# @app.route("/upload")
# def upload_form():
#     return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():
    # リクエストファイルの読み込み
    ocr_file = request.files["ocrFile"]
    img = Image.open(ocr_file)

    # ocr 準備
    tools = pyocr.get_available_tools()
    tool = tools[0]
    # OCR
    txt = tool.image_to_string(
        img, lang="eng+jpn", builder=pyocr.builders.TextBuilder()
    )

    if txt == "":
        txt = "読み取りエラー"
        return render_template("index.html", txt=txt)


if __name__ == "__main__":
    app.run(debug=True)
