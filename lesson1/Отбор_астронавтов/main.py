from flask import Flask
from flask import url_for, request


app = Flask(__name__)


@app.route("/")
def main():
    return ""

@app.route("/astronaut_selection", methods=["POST", "GET"])
def astronaut_selection():
    if request.method == "GET":
        return f'''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
        crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
        <title>Отбор астронавтов</title>
    </head>
    <body>
        <h1 align="center"> Отбор астронавтов</h1>
        <div>
            <form class="astronaut_selection" method="post">
                <input class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                <input class="form-control" id="name" placeholder="Введите имя" name="name">
                <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                <div class="form-group">
                    <label for="educationSelect">Какое у вас образование?</label>
                    <select class="form-control" id="educationSelect" name="education">
                      <option>Общее образование</option>
                      <option>Профессиональное образование</option>
                      <option>Дополнительное образование</option>
                      <option>Профессиональное обучение</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="form-check">Выберите вашу профессию</label>
                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="profession" id="research_engineer" value="research_engineer" checked>
                        <label class="form-check-label" for="research_engineer">
                          Инженер-исследователь
                        </label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="profession" id="pilot" value="pilot" checked>
                        <label class="form-check-label" for="pilot">
                          Пилот
                        </label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="profession" id="builder" value="builder" checked>
                        <label class="form-check-label" for="builder">
                          Строитель
                        </label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="profession" id="exobiologist" value="exobiologist" checked>
                        <label class="form-check-label" for="exobiologist">
                          Экзобиолог
                        </label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="profession" id="doctor" value="doctor" checked>
                        <label class="form-check-label" for="male">
                          Врач
                        </label>
                    </div>
                </div>
                <div class="form-group">
                    <label for="form-check">Укажите пол</label>
                    <div class="form-check">
                      <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                      <label class="form-check-label" for="male">
                        Мужской
                      </label>
                    </div>
                    <div class="form-check">
                      <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                      <label class="form-check-label" for="female">
                        Женский
                      </label>
                    </div>
                </div>
                <div class="form-group">
                    <label for="about">Ваша мотивавция</label>
                    <textarea class="form-control" id="motivation" rows="3" name="motivation"></textarea>
                </div>
                <div class="form-group form-check">
                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                    <label class="form-check-label" for="acceptRules">Готов остаться на Марсе</label>
                </div>
                <button type="submit" class="btn btn-primary">Отправить</button>
            </form>
        </div>
    </body>
</html>
'''
    elif request.method == "POST":
        print(request.form.get('surname'))
        print(request.form.get('name'))
        print(request.form.get('email'))
        print(request.form.get('education'))
        print(request.form.get('profession'))
        print(request.form.get('sex'))
        print(request.form.get("motivation"))
        print(request.form.get('stay_on_mars'))
        return "Форма отправлена"

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
