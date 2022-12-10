from flask import Flask,redirect,render_template,request,url_for
from My_project import app,db,crypt,mail
from My_project.models import *
from My_project.forms import *
from flask import Markup
import os
from PIL import Image
from random import randint
import smtplib
from flask_mail import Mail, Message
from flask import Markup


@app.route('/quickview',methods=['POST','GET'])
def quickview():
    w=Addpetcage.query.all()
    print(w)
    r=Addpetfood.query.all()
    print(r)
    x=Addotheritem.query.all()
    print(x)
    y=Bregister.query.all()
    print(y)
    n=Adoptregister.query.all()
    print(n)
    return render_template('quickview.html',w=w,r=r,x=x,y=y,n=n)

@app.route('/addtocart',methods=['POST','GET'])
def addtocart():
    p=Addpetcage.query.all()
    print(p)
    l=Addpetfood.query.all()
    print(l)
    m=Addotheritem.query.all()
    print(m)
    j=Bregister.query.all()
    print(j)

    return render_template('addtocart.html',p=p,l=l,m=m,j=j)

@app.route('/addbreedpet',methods=['POST','GET'])
def addbreedpet():
     view= "default.jpg"
     form =AddBreedPet()
     try:
          if form.validate_on_submit():
               if form.image.data:
                    file= save_picture(form.image.data)
                    view = file
               addb= Addbreed_pet(family=form.a_family.data,category=form.a_category.data,location=form.a_location.data,price=form.a_price.data,
                         contact=form.a_contact.data,image=view)
               db.session.add(addb)
               print(addb)
               db.session.commit()
               flash("Registration Succes ! You account wille verified soon, Thank you",'success')
               return redirect('/addbreedpet')
     except Exception as e:
          print(e)
     return render_template('addbreedpet.html',form=form)


@app.route('/temp_reg',methods=['POST','GET'])
def temp_reg():
     view= "default.jpg"
     form =TempleRegistration()
     try:
          if form.validate_on_submit():
               if form.image.data:
                    file= save_picture(form.image.data)
                    view = file
               temp= Temple(tempname=form.name.data,address=form.address.data,location=form.location.data,mobile=form.mobile.data,
                         board=form.devasom.data,email=form.email.data,password=form.password.data,username=view)
               db.session.add(temp)
               print(temp)
               db.session.commit()
               flash("Registration Succes ! You account wille verified soon, Thank you",'success')
               return redirect('/temp_reg')
     except Exception as e:
          print(e)
     return render_template('temp_reg.html',form=form)



@app.route('/admin', methods=['POST','GET'])
def admin():
    return render_template("admin.html")



@app.route('/ad_login', methods=['POST','GET'])
def ad_login():
    if request.method == 'post':
       uname = request.form['uname']
       email = request.form['email']
       psw = request.form['psw']

       al = Login(username=uname,email=email,password=psw)
       db.session.add(al)
       db.session.commit()
       flash('login successfull!!')  
    return render_template("ad_login.html")



@app.route('/adminindex')
def adminindex():
    return render_template("adminindex.html")


   
@app.route('/add_pet',methods=['POST','GET'])
def add_pet():
    return render_template("add_pet.html")


@app.route('/adminview')
def adminview():
   return render_template("adminview.html")

@app.route('/viewbooking')
def viewbooking():
    return render_template("viewbooking.html")


@app.route('/delete')
def delete():
    return render_template("delete.html")


@app.route('/userlogin',methods=['POST','GET'])
def userlogin():
    if request.method == 'post':
        uname = request.form['uname']
        email = request.form['email']
        psw = request.form['psw']

        user = Userlogin(username=uname,email=email,password=psw)
        db.session.add(user)
        db.session.commit()
    return render_template("userlogin.html")

@app.route('/userindex')
def userindex():
    return render_template("userindex.html")

@app.route('/userlayout')
def userlayout():
    return render_template("userlayout.html")

@app.route('/user_registration',methods=['POST','GET'])
def user_registration():
    if request.method == 'post' :
        name = request.form['name']
        email = request.form['email']
        uname = request.form['username']
        password = request.form['password']
        cpassword = request.form['confirm']

        ur = Register(name=name,email=email,username=uname,password=password,confirm_password=cpassword)
        db.session.add(ur)
        db.session.commit()
    return render_template("user_registration.html")

@app.route('/user_addpet')
def user_addpet():
    return render_template("user_addpet.html")

@app.route('/buy_pet')
def buy_pet():
    return render_template("buy_pet.html")

@app.route('/viewbreeders')
def viewbreeders():
    return render_template("viewbreeders.html")

@app.route('/viewpetshp')
def viewpetshp():
    return render_template("viewpetshp.html")

@app.route('/adopt')
def adopt():
    return render_template("adopt.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/categories')
def categories():
    return render_template("categories.html")

@app.route('/pet')
def pet():
    return render_template("pet.html")

@app.route('/petshp_a_accessories')
def petshp_accessories():
    c = Petshp_register.query.all()
    print(c)
    return render_template("petshp_a_accessories.html",c=c)

@app.route('/pe_addproduct')
def pe_addproduct():
    return render_template("pe_addproduct.html")

@app.route('/pe_addpetfood',methods=['POST','GET'])
def pe_addpetfood():
     view= "default.jpg"
     form =AddPetFood()
     try:
          if form.validate_on_submit():
               if form.image.data:
                    file= save_picture(form.image.data)
                    view = file
               adpf= Addpetfood(productname=form.name.data,price=form.price.data,location=form.loc.data,contact=form.cont.data,
                         image=view)
               db.session.add(adpf)
               print(adpf)
               db.session.commit()
               flash("Registration Succes ! You account wille verified soon, Thank you",'success')
               return redirect('/pe_addpetfood')
     except Exception as e:
          print(e)
     return render_template('pe_addpetfood.html',form=form)


@app.route('/pe_addpetcage',methods=['POST','GET'])
def pe_addpetcage():
     view= "default.jpg"
     form =AddPetCage()
     try:
          if form.validate_on_submit():
               if form.image.data:
                    file= save_picture(form.image.data)
                    view = file
               adpc= Addpetcage(productname=form.name.data,price=form.price.data,location=form.loc.data,contact=form.cont.data,
                         image=view)
               db.session.add(adpc)
               print(adpc)
               db.session.commit()
               flash("Registration Succes ! You account wille verified soon, Thank you",'success')
               return redirect('/pe_addpetcage')
     except Exception as e:
          print(e)
     return render_template('pe_addpetcage.html',form=form)



@app.route('/pe_addotheritems',methods=['POST','GET'])
def pe_addotheritems():
     view= "default.jpg"
     form =AddOtheritem()
     try:
          if form.validate_on_submit():
               if form.image.data:
                    file= save_picture(form.image.data)
                    view = file
               adot= Addotheritem(productname=form.name.data,price=form.price.data,location=form.loc.data,contact=form.cont.data,
                         image=view)
               db.session.add(adot)
               print(adot)
               db.session.commit()
               flash("Registration Succes ! You account wille verified soon, Thank you",'success')
               return redirect('/pe_addotheritems')
     except Exception as e:
          print(e)
     return render_template('pe_addotheritems.html',form=form)


@app.route('/adopt_center')
def adopt_center():
    r = Adoptregister.query.all()
    print(r)
    return render_template('adopt_center.html',r=r)

@app.route('/vetenerian')
def vetenerian():
    v=Vregister.query.all()
    print(v)
    return render_template("vetenerian.html",v=v)

@app.route('/blog')
def blog():
    return render_template("blog.html")


@app.route('/b_addpet',methods=['POST','GET'])
def b_addpet():
     view= "default.jpg"
     form =BrReg()
     try:
          if form.validate_on_submit():
               if form.image.data:
                    file= save_picture(form.image.data)
                    view = file
               brrg= Bregister(name=form.pctgry.data,username=form.price.data,location=form.loc.data,specialization=form.fam.data,
                         email=form.con.data,password=form.age.data,image=view)
               db.session.add(brrg)
               print(brrg)
               db.session.commit()
               flash("Registration Succes ! You account wille verified soon, Thank you",'success')
               return redirect('/b_addpet')
     except Exception as e:
          print(e)
     return render_template('b_addpet.html',form=form)


    

@app.route('/aaa')
def aaa():
    x = Bregister.query.all()
    print(x)
    return render_template("aaa.html",x=x)
@app.route('/br_login',methods=['POST','GET'])
def br_login():
    if request.method == 'POST':
        uname = request.form['uname']
        email = request.form['email']
        psw = request.form['psw']
        breed = Brlogin(username=uname,email=email,password=psw)
        db.session.add(breed)
        db.session.commit()
    return render_template("br_login.html")

def save_image(picture_file):
    picture_name = picture_file.filename
    picture_path = os.path.join(app.root_path,'static/pics',image)
    picture_file.save(picture_path)
    return picture_name

# @app.route('/addbreedpet', methods=['POST','GET'])
# def addbreedpet():
#     view= "default.jpg"
#     form =AddBreedPet()
#     try:
#         if form.validate_on_submit():
#             if form.image.data:
#                 file= save_picture(form.image.data)
#                 view = file
#                 add= Addbreed_pet(family=form.a_family.data,category=form.a_category.data,price=form.a_price.data,location=form.a_location.data,contact=form.a_contact.data,image=view)
#                 db.session.add(add)
#                 print(add)
#                 db.session.commit()
#                 flash("Registration Succes ! You account wille verified soon, Thank you",'success')
#                 return redirect('/breeed_available')
#     except Exception as e:
#         print(e)
#     return render_template('addbreedpet.html',form=form)
    
            



@app.route('/petshp_login',methods=['POST','GET'])
def petshp_login():
    if request.method == 'post':
        uname = request.form['uname']
        email = request.form['email']
        psw = request.form['psw']

        pl = Petshp_login(username=uname,email=email,password=psw)
        db.session.add(pl)
        db.session.commit()
        flash('login successfull!!')
    return render_template("petshp_login.html")


@app.route('/petshp_reg',methods=['POST','GET'])
def petshp_reg():
     view= "default.jpg"
     form =PetShop()
     try:
          if form.validate_on_submit():
               if form.image.data:
                    file= save_picture(form.image.data)
                    view = file
               pesh= Petshp_register(name=form.name.data,username=form.usname.data,location=form.loc.data,email=form.email.data,password=form.password.data,image=view)
               db.session.add(pesh)
               print(pesh)
               db.session.commit()
               flash("Registration Succes ! You account wille verified soon, Thank you",'success')
               return redirect('/petshp_reg')
     except Exception as e:
          print(e)
     return render_template('petshp_reg.html',form=form)


@app.route('/shp_addpet')
def shp_addpet():
    return render_template("shp_addpet.html")

@app.route('/shp_addaccessory')
def shp_addaccessory():
    a = Temple.query.all()
    print(a)

    return render_template("shp_addaccessory.html",a=a)

@app.route('/adopt_login',methods=['POST','GET'])
def adopt_login():
    if request.method == 'post':
        uname = request.form['uname']
        email = request.form['email']
        psw = request.form['psw']

        adl = Adoptlogin(username=uname,email=email,password=psw)
        db.session.add(adl)
        db.session.commit()
        flash('login successfull!!')

    return render_template("adopt_login.html")

@app.route('/adopt_reg',methods=['POST','GET'])
def adopt_reg():
     view= "default.jpg"
     form =AdoptCent()
     try:
          if form.validate_on_submit():
               if form.image.data:
                    file= save_picture(form.image.data)
                    view = file
               adpc= Adoptregister(name=form.name.data,username=form.usname.data,experience=form.exp.data,email=form.email.data,
                         location=form.loc.data,password=form.password.data,image=view)
               db.session.add(adpc)
               print(adpc)
               db.session.commit()
               flash("Registration Succes ! You account wille verified soon, Thank you",'success')
               return redirect('/adopt_center')
     except Exception as e:
          print(e)
     return render_template('adopt_reg.html',form=form)


@app.route('/vetenerian_login',methods=['POST','GET'])
def vetenerian_login():
    if request.method == 'post':
        uname = request.form['uname']
        email = request.form['email']
        psw = request.form['psw']

        vl = Vlogin(username=uname,email=email,password=psw)
        db.session.add(vl)
        db.session.commit()
        flash('login successfull!!')
    return render_template("vetenerian_login.html")

@app.route('/vetenerian_reg',methods=['POST','GET'])
def vetenerian_reg():
     view= "default.jpg"
     form =VeteneryReg()
     try:
          if form.validate_on_submit():
               if form.image.data:
                    file= save_picture(form.image.data)
                    view = file
               vttt= Vregister(name=form.name.data,username=form.usname.data,location=form.loc.data,experience=form.exp.data,
                         email=form.email.data,password=form.password.data,image=view)
               db.session.add(vttt)
               print(vttt)
               db.session.commit()
               flash("Registration Succes ! You account wille verified soon, Thank you",'success')
               return redirect('/vetenerian_reg')
     except Exception as e:
          print(e)
     return render_template('vetenerian_reg.html',form=form)


@app.route('/dog')
def dog():
    return render_template("p_dog.html")


@app.route('/cat')
def cat():
    return render_template("p_cat.html")


@app.route('/birds')
def birds():
    return render_template("p_bird.html")

@app.route('/exortic')
def exortic():
    return render_template("p_exortic.html")

@app.route('/fishes')
def fishes():
    return render_template("p_fishes.html")

@app.route('/livestock')
def livestock():
    return render_template("p_livestock.html")

@app.route('/horses')
def hoerses():
    return render_template("p_horses.html")

@app.route('/reptiles')
def reptiles():
    return render_template("p_reptiles.html")

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/register_login')
def register_login():
    return render_template("register_login.html")


@app.route('/addadoptpet',methods=['POST','GET'])
def addadoptpet():
     view= "default.jpg"
     form =AddAdoptPet()
     try:
          if form.validate_on_submit():
               if form.image.data:
                    file= save_picture(form.image.data)
                    view = file
               adpt= Addadopt_pet(category=form.ctgry.data,location=form.loc.data,contact=form.ctct.data,image=view)
               db.session.add(adpt)
               print(adpt)
               db.session.commit()
               flash("Registration Succes ! You account wille verified soon, Thank you",'success')
               return redirect('/adoptpet')
     except Exception as e:
          print(e)
     return render_template('addadoptpet.html',form=form)



@app.route('/adoptpet')
def adoptpet():
    p = Addadopt_pet.query.all()
    print(p)
    return render_template('adoptpet.html',p=p)



@app.route('/adoptinfo')
def adoptinfo():
    return render_template("adoptinfo.html")

@app.route('/adultdog')
def adultdog():
    return render_template("adultdog.html")

@app.route('/adultcat')
def adultcat():
    return render_template("adultcat.html")

@app.route('/adulthorse')
def adulthorse():
    return render_template("adulthorse.html")

@app.route('/babydog')
def babydog():
    return render_template("babydog.html")

@app.route('/babycat')
def babycat():
    return render_template("babycat.html")

@app.route('/babyhorse')
def babyhorse():
    return render_template("babyhorse.html")

@app.route('/petfood')
def petfood():
    t=Addpetfood.query.all()
    print(t)
    return render_template("petfood.html",t=t)

@app.route('/petcage')
def petcage():
    k=Addpetcage.query.all()
    print(k)
    return render_template("petcage.html",k=k)

@app.route('/otheritem')
def otheritem():
    h=Addotheritem.query.all()
    print(h)
    return render_template("otheritem.html",h=h)

@app.route('/adultbird')
def adultbird():
    return render_template("adultbird.html")

@app.route('/adultreptiles')
def adultreptiles():
    return render_template("adultreptiles.html")

@app.route('/adultfish')
def adultfish():
    return render_template("adultfish.html")

@app.route('/babyfish')
def babyfish():
    return render_template("babyfish.html")

@app.route('/babybird')
def babybird():
    return render_template("babybird.html")

@app.route('/babyreptiles')
def babyreptiles():
    return render_template("babyreptiles.html")

@app.route('/babylivestock')
def babylivestock():
    return render_template('babylivestocks.html')

@app.route('/adultlivestock')
def adultlivestock():
    return render_template('/adultlivestocks.html')

@app.route('/adultexortic')
def adultexortic():
    return render_template('/adult_exortic.html')

@app.route('/babyexortic')
def babyexortic():
    return render_template('/baby_exortic.html')


@app.route('/breedregister')
def breedregister():
    return render_template("breedregister.html")




@app.route('/brclinic_reg',methods=['POST','GET'])
def brclinic_reg():
     view= "default.jpg"
     form =BcReg()
     try:
          if form.validate_on_submit():
               if form.image.data:
                    file= save_picture(form.image.data)
                    view = file
               brrc= Bcregister(name=form.name.data,username=form.uname.data,location=form.loc.data,email=form.email.data,password=form.password.data,image=view)
               db.session.add(brrc)
               print(brrc)
               db.session.commit()
               flash("Registration Succes ! You account wille verified soon, Thank you",'success')
               return redirect('/brclinic_reg')
     except Exception as e:
          print(e)
     return render_template('brclinic_reg.html',form=form)


@app.route('/breed_clinic')
def bree_clinic():
    f = Addbreed_pet.query.all()
    print(f)
    return render_template('breed_clinic.html',f=f)

@app.route('/breed_available')
def breed_available():
    x = Addbreed_pet.query.all()
    print(x)
    return render_template('breed_available.html',x=x)

@app.route('/b_viewpets')
def b_viewpets():
    i = Bregister.query.all()
    print(i)

    return render_template("b_viewpets.html",i=i)



@app.route('/breed_info')
def breed_info():
    return render_template('/breed_info.html')

@app.route('/forms', methods=['POST','GET'])
def forms():
    if request.method == 'post':
        un = request.form('uname')
        pas = request.form('email')
        em = request.form('psw')

        fo = Brlogin(username=un,email=em,password=pas)
        db.session.add(fo)
        db.session.commit()
        flash('sucessful!!')

    return render_template('/forms.html')

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def save_picture(form_picture):
    random_hex = random_with_N_digits(14)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = str(random_hex) + f_ext
    picture_path = os.path.join(app.root_path, 'static/pics', picture_fn)

    output_size = (1080, 720)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)


    return picture_fn


