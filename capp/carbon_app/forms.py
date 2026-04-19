from flask_wtf import FlaskForm
from wtforms import  SubmitField,  SelectField,  FloatField
from wtforms.validators import InputRequired

class BusForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel'), ('CNG', 'CNG'), ('Petrol', 'Petrol'), ('Electric Europe', 'Electric Europe')])
  submit = SubmitField('Submit')

class CarForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric Nordic', 'Electric Nordic'), ('Electric Europe', 'Electric Europe')])
  submit = SubmitField('Submit')  

class TrainForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel'), ('Electric', 'Electric')])
  submit = SubmitField('Submit')  

class PlaneForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Flight class', [InputRequired()], 
    choices=[('Business', 'Business'), ('First class', 'First class'), ('Economy', 'Economy')])
  submit = SubmitField('Submit')
  
class FerryForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel'), ('CNG', 'CNG'), ('Petrol', 'Petrol')])
  submit = SubmitField('Submit')  

class MotorbikeForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Petrol', 'Petrol'), ('Electric', 'Electric')])
  submit = SubmitField('Submit')

class BicycleForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')  

class WalkForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')  


