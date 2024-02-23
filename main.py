from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof.lower() or 'строитель' in prof.lower():
        pic = "../static/img/station_ns.jpg"
    else:
        pic = "../static/img/station_it.jpg"
    return render_template('training.html', picture=pic)


@app.route('/list_prof/<numerated>')
def list_prof(numerated):
    li = ["инженер-исследователь",
          "пилот",
          "экзобиолог",
          "врач",
          "инженер по терраформированию",
          "климатолог",
          "специалист по радиационной защите",
          "астрогеолог",
          "гляциолог",
          "инженер жизнеобеспечения",
          "метеоролог",
          "оператор марсохода",
          "киберинженер",
          "штурман",
          "пилот дронов"]
    params = {
        'professions': li,
        'num': numerated
    }
    return render_template('list_prof.html', **params)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    params = {
        'title': 'Анкета',
        'surname': 'Wathy',
        'name': "Mark",
        'education': "выше среднего",
        'profession': "штурман марсохода",
        'sex': 'male',
        'motivation': "Всегда мечтал застрять на Марсе!",
        'ready': True
    }
    return render_template('auto_answer.html', **params)


if __name__ == '__main__':
    app.run(port=8001, host='127.0.0.1')