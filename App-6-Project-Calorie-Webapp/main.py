from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from calorie import Calorie
from temperature import Temperature

app = Flask(__name__)


class Homepage(MethodView):

    def get(self):
        return render_template('index.html')


class CaloriePage(MethodView):

    def get(self):
        calories_form = CalorieForm()
        return render_template('calories_form_page.html', caloriesform=calories_form)

    def post(self):
        calories_form = CalorieForm(request.form)
        temperature = Temperature(country=calories_form.country.data, city=calories_form.city.data).get()
        calorie = Calorie(weight=float(calories_form.weight.data), height=float(calories_form.height.data),
                          age=float(calories_form.age.data), temperature=temperature)
        calories = float(calorie.calculate())

        return render_template('calories_form_page.html', caloriesform=calories_form, calories=calories, result=True)


class CalorieForm(Form):
    weight = StringField("Weight: ", default=50)
    height = StringField("Height: ", default=175)
    age = StringField("Age: ", default=24)
    country = StringField("Country: ", default="india")
    city = StringField("City: ", default="thane")
    button = SubmitField('Calculate')


app.add_url_rule('/', view_func=Homepage.as_view('home_page'))
app.add_url_rule('/calories_form', view_func=CaloriePage.as_view('calories_form_page'))

app.run(debug=True)
