from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '3e01c1650be861b686cebac5f0713365'

from windOnline import routes   
