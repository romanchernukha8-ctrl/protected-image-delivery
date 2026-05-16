from flask import Flask, send_file, abort

app = Flask(__name__)


def get_current_user():

    return {
        "username": "admin",
        "can_view_images": True
    }


@app.route("/")
def home():

    return """
    <html>
        <body>

            <h1>Protected Image</h1>

            <img src="/image/linux">

        </body>
    </html>
    """


@app.route("/image/<image_id>")
def get_image(image_id):

    user = get_current_user()

    if not user:
        return abort(403)

    if not user["can_view_images"]:
        return abort(403)

    path = f"/data/images/{image_id}.jpg"

    return send_file(path, mimetype='image/jpeg')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
