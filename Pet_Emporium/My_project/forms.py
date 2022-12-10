from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import validators, ValidationError
from wtforms import Form,StringField, PasswordField,validators, SubmitField,SelectField, BooleanField, TextAreaField,IntegerField,FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from wtforms import SelectField






class AddBreedPet(FlaskForm):
    a_family= StringField('Family',
                           validators=[DataRequired(), Length(min=1, max=40)])
    a_category = StringField('Category', validators=[DataRequired(),Length(min=1, max=99)])
    a_price = StringField('Price', validators=[DataRequired(),Length(min=1, max=99)])
    a_location = StringField('Location', validators=[DataRequired(),Length(min=3, max=50)])
    a_contact  = StringField('Contact', validators=[DataRequired(),Length(min=10, max=10)])
    image = FileField('Add Breed Pet', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('proceed') 


class TempleRegistration(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=5, max=40)])
    email = StringField('Email', validators=[DataRequired(),Length(min=5, max=99)])
    address = StringField('Address', validators=[DataRequired(),Length(min=1, max=99)])
    location = SelectField('Location', choices = [('Thiruvananthapuram', 'Thiruvananthapuram'), ('Kollam', 'Kollam'),('Kottayam', 'Kottayam'),
                                                   ('Ernamkulam', 'Ernamkulam'),('idukki', 'idukki'),('Thrissur', 'Thrissur'),
                                                   ('Wayanad', 'Wayanad'),('kozhikode', 'Kozhikode'),('Palakkad', 'Palakkad'),
                                                   ('Pathanamthitta', 'Pathanamthitta'),('Alapuzha','Alapuzha'),('Wayanad','Wayanad'),
                                                   ('Malappuram','Malappuram'),('Alapuzha','Alapuzha'),('Kasargode','Kasargode')
                                                   ])
    devasom = SelectField('Devasom',choices = [('Cochin', 'Cochin'), ('Guruvayoor', 'Guruvayoor'),('Malabar', 'Malabar'),('Travancore', 'Travancore')])
    mobile = StringField('Mobile', validators=[DataRequired(),Length(min=10, max=10)])
    password  = PasswordField('Password', validators=[DataRequired(),Length(min=3, max=99)])
    image = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('proceed') 


class AddAdoptPet(FlaskForm):
    loc = StringField('Location',
                           validators=[DataRequired(), Length(min=2, max=40)])
    ctct = StringField('Contact', validators=[DataRequired(),Length(min=10, max=10)])
    ctgry = SelectField('Category', choices = [('Cat', 'Cat'), ('Dog', 'Dog'),('Livestock', 'Livestock'),
                                                   ('Horse', 'Horse'),('Fish', 'Fish'),('Exortics', 'Exortics'),
                                                   ('Reptiles', 'Reptiles')])
    image = FileField('Add Adopting Pet', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('proceed') 

class AdoptCent(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=3, max=40)])
    email = StringField('Email', validators=[DataRequired(),Length(min=5, max=99)])
    exp = StringField('Experience', validators=[DataRequired(),Length(min=1, max=2)])
    loc = StringField('Location',validators= [DataRequired(),Length(min=3, max=30)])
    usname = StringField('Username', validators=[DataRequired(),Length(min=2, max=30)])
    password  = PasswordField('Password', validators=[DataRequired(),Length(min=3, max=99)])
    image = FileField('Add AdoptCenter', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('proceed') 



class BrReg(FlaskForm):
    pctgry = SelectField('PetCategory',
                           choices=[('Dog','Dog'),('Cat','Cat'),('Exoric','Exortic'),('Horse','Horse'),('Bird','Bird'),('Reptile','Reptile'),('Others','Others')])
    con = StringField('Contact', validators=[DataRequired(),Length(min=10, max=10)])
    price = StringField('price', validators=[DataRequired(),Length(min=1, max=99)])
    fam = StringField('Family', validators = [DataRequired(),Length(min=2,max=44)])
    loc = StringField('Location', validators=[DataRequired(),Length(min=1, max=30)])
    age  = StringField('Age', validators=[DataRequired(),Length(min=1, max=5)])
    image = FileField('Add Pet Pic', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('proceed') 


class AddPetCage(FlaskForm):
    name = StringField('Product Name',
                           validators=[DataRequired(), Length(min=2, max=40)])
    cont = StringField('Contact', validators=[DataRequired(),Length(min=10, max=10)])
    price = StringField('Price', validators=[DataRequired(),Length(min=1, max=99)])
    loc = StringField('Quantity', validators=[DataRequired(),Length(min=2, max=40)])
    image = FileField('Add product pic', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('proceed')


class AddPetFood(FlaskForm):
    name = StringField('Product Name',
                           validators=[DataRequired(), Length(min=2, max=40)])
    cont = StringField('Contact', validators=[DataRequired(),Length(min=10, max=10)])
    price = StringField('Price', validators=[DataRequired(),Length(min=1, max=99)])
    loc = StringField('Quantity', validators=[DataRequired(),Length(min=2, max=40)])
    image = FileField('Add product pic', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('proceed') 


class AddOtheritem(FlaskForm):
    name = StringField('Product Name',
                           validators=[DataRequired(), Length(min=2, max=40)])
    cont = StringField('Contact', validators=[DataRequired(),Length(min=10, max=10)])
    price = StringField('Price', validators=[DataRequired(),Length(min=1, max=99)])
    loc = StringField('Quantity', validators=[DataRequired(),Length(min=2, max=40)])
    image = FileField('Add product pic', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('proceed')


class BcReg(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=3, max=40)])
    email = StringField('Email', validators=[DataRequired(),Length(min=5, max=99)])
    uname = StringField('Address', validators=[DataRequired(),Length(min=1, max=99)])
    loc = StringField('Location', validators = [DataRequired(),Length(min=3,max=33)])
    password  = PasswordField('Password', validators=[DataRequired(),Length(min=3, max=99)])
    image = FileField('Add BreedClincs', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('proceed') 


class PetShop(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=40)])
    email = StringField('Email', validators=[DataRequired(),Length(min=5, max=99)])
    usname = StringField('Username', validators=[DataRequired(),Length(min=1, max=99)])
    loc = StringField('Location', validators = [DataRequired(),Length(min=1, max=99)])
    password  = PasswordField('Password', validators=[DataRequired(),Length(min=3, max=99)])
    image = FileField('Add Your PetShop image', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('proceed')

class VeteneryReg(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=40)])
    email = StringField('Email', validators=[DataRequired(),Length(min=5, max=99)])
    usname = StringField('Username', validators=[DataRequired(),Length(min=1, max=99)])
    loc = StringField('Location',validators=[DataRequired(),Length(min=1, max=99)])
    exp = StringField('Experience', validators=[DataRequired(),Length(min=1, max=99)])
    password  = PasswordField('Password', validators=[DataRequired(),Length(min=3, max=99)])
    image = FileField('Add Your Clinic', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('proceed') 

