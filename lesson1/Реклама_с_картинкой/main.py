from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route("/promotion_image")
def promotion_image():
    return f"""
            <!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <h1>Жди нас, Марс!</h1>
                    <p><img src="{url_for('static', filename='img/mars.png')}" width="500" height="500"
                    alt="здесь должна была быть картинка, но не нашлась"></p>
                    <div class="alert alert-primary" role="alert">
                      Человечество вырастает из детства.</br>
                        Человечеству мала одна планета.</br>
                        Мы сделаем обитаемыми безжизненные пока планеты.</br>
                        И начнем с Марса!</br>
                        Присоединяйся!
                    </div>
                  </body>
                </html>
            """


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
