from flask import Flask, render_template
from windOnline import app
from windOnline.forms import windForm




@app.route("/", methods=['GET', 'POST'])
def wind():
    form = windForm()
    if form.validate_on_submit():
        pass
    return render_template('windForm.html', title = 'Wind Pressure Calc Form', form=form)

