from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FloatField
from wtforms.validators import DataRequired, NumberRange

class windForm(FlaskForm):
    region = SelectField(
        'Region',choices=[('A', 'A'),('B', 'B'),('C', 'C'),('D', 'D')]
    )
    importance = SelectField(
        'Importance Level',choices=[('1N', '1 Non Cyclonic'),('1C', '1 Cyclonic'),('2', '2'),('3', '3'),('4', '4')]
    )
    terrain = SelectField(
        'Terrain Category',choices=[('TerrainCat1','1'),('TerrainCat1_5','1.5'),('TerrainCat2','2'),('TerrainCat2_5','2.5'),('TerrainCat3','3'),
                                    ('TerrainCat3_5','3.5'),('TerrainCat4','4')]
    ) 
    md = SelectField(
        'Md = ', choices=[('1','1'),('0.95', '0.95')]
    )
    kc = SelectField(
        'Kc = ', choices=[('1','1'),('0.95','0.95'),('0.9','0.9'),('0.8','0.8')]
    )
    ridgeHeight = FloatField('Ridge Height', validators=[DataRequired(), NumberRange(min = 1, max = 200)])
    eavesHeight = FloatField('Eaves Height',validators=[DataRequired(), NumberRange(min = 1, max = 200)])
    submit = SubmitField('Calculate')