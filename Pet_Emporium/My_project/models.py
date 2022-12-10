from My_project import db,app,login_manager
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(user_id):
    return Login.query.get(int(user_id))

class Temple (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tempcode = db.Column(db.Integer,unique=True)
    tempname= db.Column(db.String)
    address= db.Column(db.String)
    location= db.Column(db.String)
    mobile=db.Column(db.Integer)
    board= db.Column(db.String)
    email= db.Column(db.String)
    username= db.Column(db.String)
    password = db.Column(db.String)
    status=db.Column(db.String)





class Login(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String,nullable=False)
    usertype = db.Column(db.String,nullable=False)
    email= db.Column(db.String,nullable=False,unique=True)
    password = db.Column(db.String,nullable=False)
    code = db.Column(db.String,nullable=False,unique=True)


class Addpetcage(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    productname= db.Column(db.String)
    price = db.Column(db.String)
    location= db.Column(db.String)
    contact = db.Column(db.String)
    image = db.Column(db.String)


class Addpetfood(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    productname= db.Column(db.String)
    price = db.Column(db.String)
    location= db.Column(db.String)
    contact = db.Column(db.String)
    image = db.Column(db.String)


class Addotheritem(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    productname= db.Column(db.String)
    price = db.Column(db.String)
    location= db.Column(db.String)
    contact = db.Column(db.String)
    image = db.Column(db.String)

class Brlogin(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String,nullable=False)
    usertype = db.Column(db.String,nullable=False)
    email= db.Column(db.String,nullable=False,unique=True)
    password = db.Column(db.String,nullable=False)
    code = db.Column(db.String,nullable=False,unique=True)

class Petshp_login(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String,nullable=False)
    usertype = db.Column(db.String,nullable=False)
    email= db.Column(db.String,nullable=False,unique=True)
    password = db.Column(db.String,nullable=False)
    code = db.Column(db.String,nullable=False,unique=True)

class Adoptlogin(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String,nullable=False)
    usertype = db.Column(db.String,nullable=False)
    email= db.Column(db.String,nullable=False,unique=True)
    password = db.Column(db.String,nullable=False)
    code = db.Column(db.String,nullable=False,unique=True)

class Userlogin(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String,nullable=False)
    usertype = db.Column(db.String,nullable=False)
    email= db.Column(db.String,nullable=False,unique=True)
    password = db.Column(db.String,nullable=False)
    code = db.Column(db.String,nullable=False,unique=True)

class Vlogin(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String,nullable=False)
    usertype = db.Column(db.String,nullable=False)
    email= db.Column(db.String,nullable=False,unique=True)
    password = db.Column(db.String,nullable=False)
    code = db.Column(db.String,nullable=False,unique=True)

class Add_pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    family = db.Column(db.String)
    category = db.Column(db.String)
    price = db.Column(db.Integer)
    location = db.Column(db.String)
    contact = db.Column(db.String)
    image = db.Column(db.String)

class Addadopt_pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String)
    location = db.Column(db.String)
    contact = db.Column(db.String)
    image = db.Column(db.String)

class Addbreed_pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    family = db.Column(db.String)
    category = db.Column(db.String)
    price = db.Column(db.Integer)
    location = db.Column(db.String)
    contact = db.Column(db.String)
    image = db.Column(db.String)

class Adopt_center(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    centername = db.Column(db.String)
    location = db.Column(db.String)
    contact = db.Column(db.String)
    image = db.Column(db.String)

class Adopt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adopt_center = db.Column(db.String)
    adoptpet = db.Column(db.String)
    adoptinfo = db.Column(db.String)


class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    confirm_password = db.Column(db.String)

class Vregister(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    experience = db.Column(db.String)
    location = db.Column(db.String)
    password = db.Column(db.String)
    confirm_password = db.Column(db.String)
    image = db.Column(db.String)

class Bregister(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    specialization = db.Column(db.String)
    location = db.Column(db.String)
    password = db.Column(db.String)
    confirm_password = db.Column(db.String)
    image = db.Column(db.String)

class Bcregister(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    specialization = db.Column(db.String)
    location = db.Column(db.String)
    password = db.Column(db.String)
    confirm_password = db.Column(db.String)
    image = db.Column(db.String)

class Petshp_register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    location = db.Column(db.String)
    password = db.Column(db.String)
    confirm_password = db.Column(db.String)
    image = db.Column(db.String)

class Adoptregister(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    experience = db.Column(db.String)
    location = db.Column(db.String)
    password = db.Column(db.String)
    confirm_password = db.Column(db.String)
    image = db.Column(db.String)


class Adopt_pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categories = db.Column(db.String)
    petname = db.Column(db.String)
    location = db.Column(db.String)
    contact = db.Column(db.String)
    image = db.Column(db.String)

class Adultexortic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    petname = db.Column(db.String)
    price = db.Column(db.Integer)
    contact = db.Column(db.String)
    location = db.Column(db.String)
    image = db.Column(db.String)

class Adultbird(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    petname = db.Column(db.String)
    price = db.Column(db.Integer)
    contact = db.Column(db.String)
    location = db.Column(db.String)
    image = db.Column(db.String)

class Adultcat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    petname = db.Column(db.String)
    price = db.Column(db.Integer)
    contact = db.Column(db.String)
    location = db.Column(db.String)
    image = db.Column(db.String)

class Adultdog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    petname = db.Column(db.String)
    price = db.Column(db.Integer)
    contact = db.Column(db.String)
    location = db.Column(db.String)
    image = db.Column(db.String)

class Adulthorse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    petname = db.Column(db.String)
    price = db.Column(db.Integer)
    contact = db.Column(db.String)
    location = db.Column(db.String)
    image = db.Column(db.String)

class Adultfish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    petname = db.Column(db.String)
    price = db.Column(db.Integer)
    contact = db.Column(db.String)
    location = db.Column(db.String)
    image = db.Column(db.String)

class Adultlivestock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    petname = db.Column(db.String)
    price = db.Column(db.Integer)
    contact = db.Column(db.String)
    location = db.Column(db.String)
    image = db.Column(db.String)

class Adultreptiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    petname = db.Column(db.String)
    price = db.Column(db.Integer)
    contact = db.Column(db.String)
    location = db.Column(db.String)
    image = db.Column(db.String)

class Babyexortic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    petname = db.Column(db.String)
    price = db.Column(db.Integer)
    contact = db.Column(db.String)
    location = db.Column(db.String)
    image = db.Column(db.String)

class Babybird(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    petname = db.Column(db.String)
    price = db.Column(db.Integer)
    contact = db.Column(db.String)
    location = db.Column(db.String)
    image = db.Column(db.String)

class Babycat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    petname = db.Column(db.String)
    price = db.Column(db.Integer)
    contact = db.Column(db.String)
    location = db.Column(db.String)
    image = db.Column(db.String)

class Babydog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    petname = db.Column(db.String)
    price = db.Column(db.Integer)
    contact = db.Column(db.String)
    location = db.Column(db.String)
    image = db.Column(db.String)

class Babyfish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    petname = db.Column(db.String)
    price = db.Column(db.Integer)
    contact = db.Column(db.String)
    location = db.Column(db.String)
    image = db.Column(db.String)

class Babyhorse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    petname = db.Column(db.String)
    price = db.Column(db.Integer)
    contact = db.Column(db.String)
    location = db.Column(db.String)
    image = db.Column(db.String)

class Babylivestock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    petname = db.Column(db.String)
    price = db.Column(db.Integer)
    contact = db.Column(db.String)
    location = db.Column(db.String)
    image = db.Column(db.String)

class Babyreptiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    petname = db.Column(db.String)
    price = db.Column(db.Integer)
    contact = db.Column(db.String)
    location = db.Column(db.String)
    image = db.Column(db.String)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    username = db.Column(db.String, unique=True)
    contact = db.Column(db.String)
    location = db.Column(db.String)

class Breedavailable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    petcategory = db.Column(db.String)
    petname = db.Column(db.String)
    location = db.Column(db.String)
    price = db.Column(db.Integer)
    contact = db.Column(db.String)
    image = db.Column(db.String)

class Breedbreeders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    specialization = db.Column(db.String)
    location = db.Column(db.String)
    contact = db.Column(db.String)
    image= db.Column(db.String)

class Breedclinic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clinicname = db.Column(db.String)
    location = db.Column(db.String)
    contact = db.Column(db.String)
    image = db.Column(db.String)

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    p_dog = db.Column(db.String)
    p_exortic = db.Column(db.String)
    p_fishes = db.Column(db.String)
    p_horses = db.Column(db.String)
    p_livestock = db.Column(db.String)
    p_reptiles = db.Column(db.String)
    p_bird = db.Column(db.String)
    p_cat = db.Column(db.String)

class P_bird(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adultbird = db.Column(db.String)
    babybird = db.Column(db.String)

class P_cat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adultbird = db.Column(db.String)
    babybird = db.Column(db.String)


class P_dog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adultbird = db.Column(db.String)
    babybird = db.Column(db.String)


class P_exortic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adultbird = db.Column(db.String)
    babybird = db.Column(db.String)

class P_reptiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adultbird = db.Column(db.String)
    babybird = db.Column(db.String)


class P_horse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adultbird = db.Column(db.String)
    babybird = db.Column(db.String)


class P_fish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adultbird = db.Column(db.String)
    babybird = db.Column(db.String)

class p_livestock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adultbird = db.Column(db.String)
    babybird = db.Column(db.String)


class Petgrooming(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    contact = db.Column(db.String)
    image = db.Column(db.String)

class Petcage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itemname = db.Column(db.String)
    price = db.Column(db.Integer)
    location = db.Column(db.String)
    image = db.Column(db.String)


class Petfood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    foodname = db.Column(db.String)
    price = db.Column(db.String)
    location = db.Column(db.String)
    category = db.Column(db.String)
    image = db.Column(db.String)

class Petshopaddaccesory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    petcage = db.Column(db.String)
    petfood = db.Column(db.String)
    otheritem = db.Column(db.String)


class Shp_addaccessory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String)
    itemname = db.Column(db.String)
    location = db.Column(db.String)
    contact = db.Column(db.String)
    price = db.Column(db.Integer)
    image= db.Column(db.String)


class Shp_addpet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String)
    petname = db.Column(db.String)
    location = db.Column(db.String)
    contact = db.Column(db.String)
    price = db.Column(db.Integer)
    image = db.Column(db.String)


class Useraddpet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String)
    itemname = db.Column(db.String)
    location = db.Column(db.String)
    contact = db.Column(db.String)
    price = db.Column(db.Integer)
    image = db.Column(db.String)

class Addtocart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String)
    name = db.Column(db.String)
    price = db.Column(db.String)
    image = db.Column(db.String)
