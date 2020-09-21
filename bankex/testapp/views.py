from django.shortcuts import render
from django.contrib.auth import logout, login
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect
from datetime import datetime, date
from .models import mastercustomernumber, masteraccountnumber, cusm, invm, glif

# Create your views here.

def main(request):
    return render(request, 'main.html')


def signup(request):
    fname = request.POST['fname']
    sname = request.POST['sname']
    user = request.POST['user']
    pass1 = request.POST['pass1']
    pass2 = request.POST['pass2']
    emailaddress = request.POST['emailaddress']
    userexist = User.objects.filter(username=user)
    print(userexist)
    if pass1 != pass2:
        messages.info(request, 'Passwords not matching')
        return render(request, 'main.html')
    elif User.objects.filter(username=user).exists():
        messages.info(request, 'User already exist')
        return render(request, 'main.html')
    else:
        user = User.objects.create_user(username=user, password=pass1, email=emailaddress, first_name=fname,
                                        last_name=sname)
        user.save()
        return render(request, 'main.html')


def login(request):
    id = request.POST['usernamelolgin']
    password = request.POST['passsed']

    user = auth.authenticate(username=id, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        messages.info(request, 'Invalid login details')
        return render(request, 'main.html')
def index(request):
  if not request.user.is_authenticated:
        return render(request, 'main.html')
  else:
      user = request.user
      details = cusm.objects.filter(loginid = user)
      acdetails = invm.objects.filter(loginid = user)
      myDate = datetime.now()
      formatedDate = myDate.strftime("%Y-%m-%d %H:%M:%S")

      context={'details_cust' : details,
               'details_acct' : acdetails,
               'date': formatedDate}
      return render(request, 'index.html', context)


def createcust(request):
  user = request.user
  if not request.user.is_authenticated:
        return render(request, 'main.html')
  elif cusm.objects.filter(loginid = user).exists():
      messages.info(request,'Customer number already exist, try logging using new account ')
      return HttpResponseRedirect('/index/')
  else:
      return render(request, 'createcusm.html')

def addcust(request):
  user = request.user
  if not request.user.is_authenticated:
        return render(request, 'main.html')
  else:
    name420 = request.POST['fullname']
    email = request.POST['email']
    phone = request.POST['phone']
    nationality = request.POST['nationality']
    satate = request.POST['state']
    city = request.POST['city']
    occupancyname = request.POST['occupancy']
    dob = request.POST['dob']
    idtype = request.POST['idtype']
    idnumber = request.POST['idnumber']
    address = request.POST['address']
    #user = request.user
    print(name420)
    print(phone)
    print(email)
    if cusm.objects.filter(loginid = user).exists():
      return HttpResponseRedirect('/index/')
    else:
       print("coming till here")
       # a = mastercustomernumber.objects.filter(id = 0)
       # custnumber = a[0].customernumber
       # customernumbers = custnumber
       z = cusm(loginid = user, name = name420 ,   email = email, phone = phone , nationality = nationality, state = satate, district = city , occupency = occupancyname, address = address, idtype = idtype , idnumber = idnumber )
       z.save()
       # custnumber = int(custnumber)
       # custnumber = custnumber + 1
       # mastercustomernumber.objects.filter(id = 1).update(customernumber = custnumber )
       return HttpResponseRedirect('/index/')

def opsavings(request):
  user = request.user
  if not request.user.is_authenticated:
        return render(request, 'main.html')
  elif cusm.objects.filter(loginid = user).exists():
      return render(request, 'opsavings.html')
  else:
      messages.info(request,'Customer number Does not exist, try creating customer number first ')
      return HttpResponseRedirect('/index/')

def addsb(request):
  if not request.user.is_authenticated:
        return render(request, 'main.html')
  else:
    currency = request.POST['currency']
    opbal = request.POST['opbal']
    acname = request.POST['acname']
    nar = request.POST['nar']
    print(currency)
    print(opbal)
    print(acname)
    user = request.user
    # a = masteraccountnumber.objects.filter(id = 1)
    # accountnumber = a[0].accountnumber
    z = invm(loginid = user,  acctype = 'SB', opendate = date.today(), status = '00', curency = currency, balance = opbal, accname = acname, intrest = '2', narration = nar  )
    z.save()
    # accountnumber = int(accountnumber)
    # accountnumber = accountnumber + 1
    # accountnumber = str(accountnumber)
    #masteraccountnumber.objects.filter(id = 1).update(accountnumber = accountnumber )
    return HttpResponseRedirect('/index/')
