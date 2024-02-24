from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    id_astro = StringField('id астронавта', validators=[DataRequired()])
    pw_astro = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_cap = StringField('id капитана', validators=[DataRequired()])
    pw_cap = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Войти')


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


if __name__ == '__main__':
    app.run(port=8001, host='127.0.0.1')