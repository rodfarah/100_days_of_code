
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, TimeField, SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Create ranking lists  >>>>>
dont_have = "✘"
coffee = "☕️"
wifi = "💪"
power = "🔌"

coffee_list = [dont_have]
wifi_list = [dont_have]
power_list = [dont_have]

for n in range(1, 6):
    coffee_list.append(coffee*n)
    wifi_list.append(wifi*n)
    power_list.append(power*n)

# <<<<<<


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = URLField(
        'Location URL', description='Enter a valid URL', validators=[DataRequired()])
    open_time = TimeField('Open Time', validators=[DataRequired()])
    closing_time = TimeField('Closing Time', validators=[DataRequired()])
    dropdown_coffee = SelectField('Coffee Rating', choices=coffee_list)
    dropdown_wifi = SelectField('Wifi Rating', choices=wifi_list)
    dropdown_power = SelectField('Power Outlet Rating', choices=power_list)
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe = form.cafe.data
        location_url = form.location_url.data
        open_time = form.open_time.data
        closing_time = form.closing_time.data
        dropdown_coffee = form.dropdown_coffee.data
        dropdown_wifi = form.dropdown_wifi.data
        dropdown_power = form.dropdown_power.data

        # Make the form write a new row into cafe-data.csv
        new_data = [cafe, location_url, open_time, closing_time,
                    dropdown_coffee, dropdown_wifi, dropdown_power]
        with open("cafe-data.csv", mode="r", newline='') as add_data:
            lines = add_data.readlines()
            if not lines[-1].endswith("\n"):
                lines += "\n"
        with open("cafe-data.csv", mode="a", newline='') as add_data:
            csv_writer = csv.writer(add_data)
            csv_writer.writerow(new_data)
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
