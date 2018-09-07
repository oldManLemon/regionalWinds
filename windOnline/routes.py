from flask import Flask, render_template,flash,redirect,url_for
from windOnline import app
from windOnline.forms import windForm
from windOnline.wind import windCalcs
import pdfkit




@app.route("/", methods=['GET', 'POST'])
@app.route("/wind",methods=['GET', 'POST'])
def wind():
    #print("outsideForm")
    form = windForm()
    if form.validate_on_submit():
        print("inside the form")
        region = form.region.data
        importance = form.importance.data
        terrain = form.terrain.data
        md = form.md.data
        kc = form.kc.data
        ridgeHeight = form.ridgeHeight.data
        eavesheight = form.eavesHeight.data
        calc = windCalcs(ridgeHeight, eavesheight, region, importance, terrain, md, kc)
        #print(calc)

        #flash("hey")
        #return redirect(url_for('tab'))
        render = render_template('table.html', title = "Results", rHeight=ridgeHeight, eHeight=eavesheight, mcatRidge = calc[2], vServiceR = calc[4], vUltimateR = calc[6], mcatEaves = calc[3], vServiceE= calc[5],vUltimateE = calc[7] )
        return render, pdfkit.from_string(render, 'output.pdf')
    else:
        print(form.errors)
    return render_template('windForm.html', title = 'Wind Pressure Calc Form', form=form)

@app.route("/tab")
def tab():
    return render_template('table.html', title = "Results", rHeight=ridgeHeight, eHeight=eavesheight, mcatRidge = calc[2], vServiceR = calc[4], vUltimateR = calc[6], mcatEaves = calc[3], vServiceE= calc[5],vUltimateE = calc[7])    

