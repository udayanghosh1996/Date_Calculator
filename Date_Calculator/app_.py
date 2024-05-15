from flask import Flask, render_template, request
from Realtive_Date_Calculator import *
from Date_Calcualtor import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def add_date():
    if request.method == 'POST':
        # Fetch data from form
        try:
            years = int(request.form.get('years', 0))
            months = int(request.form.get('months', 0))
            weeks = int(request.form.get('weeks', 0))
            days = int(request.form.get('days', 0))
            hours = int(request.form.get('hours', 0))
            minutes = int(request.form.get('minutes', 0))
            seconds = int(request.form.get('seconds', 0))

            current_date, resultant_date = add_time_to_date(years, months, weeks, days, hours, minutes, seconds)

            return render_template('index.html', result=str(resultant_date), original=str(current_date))
        except ValueError:
            return render_template('index.html', error="Please enter valid integers.")
    else:
        # GET request
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
