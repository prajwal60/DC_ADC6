from django.http import HttpResponse
from django.shortcuts import render
from Rooms.models import Owner
from Rooms.models import Buyer
from Rooms.models import Room
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from django.db.models import Q


def homepage(request):
    if request.method == "GET":
        Room_list = Room.objects.all()
        context_variable = {
            'detail': Room_list
        }
        print(context_variable)
        return render(request, 'homepage.html', context_variable)
        


def login_form(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user is not None:
            login(request, user)
            return render(request, 'homepage.html')
        else:
            return render(request, 'login.html')


def registration_form_of_buyer(request):
    if request.method == "GET":
        return render(request, 'buyerregistration.html')
    else:
        # pass1=request.POST('buyer_password1')
        # pass2=request.POST('buyer_password2')
        # if(pass1==pass2):

        buyerobj = User.objects.create_user(first_name=request.POST['buyer_firstname'],
                                            last_name=request.POST['buyer_lastname'],
                                            username=request.POST['buyer_username'],
                                            password=['buyer_password1'],
                                            email=request.POST['buyer_email'])

        buy = Buyer(B_First_Name=request.POST['buyer_firstname'],
                    B_Last_Name=request.POST['buyer_lastname'],
                    B_Username=request.POST['buyer_username'],
                    B_Password=request.POST['buyer_password1'],
                    B_Gender=request.POST['buyer_gender'],
                    B_Phone_number=request.POST['buyer_phonenumber'],
                    B_E_mail=request.POST['buyer_email'])

        buy.save()
        buyerobj.save()
        return render(request, "login.html")
    # else:

    #     return HttpResponse("Your password is not matching")


def registration_form_of_owner(request):
    if request.method == "GET":
        return render(request, 'ownerregistration.html')
    else:
        Ownerobj = User.objects.create_user(first_name=request.POST['owner_firstname'],
                                            last_name=request.POST['owner_lastname'],
                                            username=request.POST['owner_username'],
                                            password=['owner_password1'],
                                            email=request.POST['owner_email'])

        own = Owner(O_First_Name=request.POST['owner_firstname'],
                    O_Last_Name=request.POST['owner_lastname'],
                    O_Username=request.POST['owner_username'],
                    O_Password=request.POST['owner_password1'],
                    O_Gender=request.POST['owner_gender'],
                    O_Phone_number=request.POST['owner_phonenumber'],
                    O_E_mail=request.POST['owner_email'])

        own.save()
        Ownerobj.save()
        return render(request, "login.html")


# def updating_for_buyer(request, id):
#     Buyer_list = Buyer.objects.get(id=id)

#     context_variable = {
#         'table': Buyer_list
#     }

#     print(context_variable)
#     return render(request, 'update_form_of_buyer.html', context_variable)

def uploadphoto(request):
    if request.method=="GET":
        return render(request,'photoupload.html')
    else:

        uploaded_image = request.FILES['image']
        fssobj = FileSystemStorage()
        filename = fssobj.save(uploaded_image.name, uploaded_image)
        uploaded_image_url = fssobj.url(filename)

        roomobj = Room(file=uploaded_image_url,
                    location=request.POST['location'],
                    phone_number=request.POST['phonenumber'],
                    price=request.POST['price'],
                    pub_date=request.POST['pubdate'],
                    desc=request.POST['description'],
        )
        roomobj.save()
    #  return render(request, 'temp.html', { 'uploaded_image_url': uploaded_image_url})

        return HttpResponse('<a href="/">Return back to homepage</a><br> <h1>You have successfully uploaded an image</h1>')



    

def delete(request, pk):
    room=Room.objects.get(pk=pk)
    room.delete()
    return redirect("/")

def update_form(request, pk):

    room=Room.objects.get(pk=pk)
    return render(request,'edit.html',{'room':room})



def update(request, pk):
    room = Room.objects.get(pk=pk)
    if request.method == "POST":
        room.image = request.FILES['image']
        room.location = request.POST['location']
        room.desc = request.POST['desc']
        room.price = request.POST['price']
        room.save()
        return redirect("/")

    else:
        return HttpResponse("record not updated")

def search(request):
    if request.method == "GET":
        src=request.GET['search']
        match=Room.objects.filter(Q(location__startswith=src))
        if match:
            return render(request,'search_result.html',{'source':match})
        else:
            return HttpResponse('<a href="/">Return back to homepage</a><br> <h1>Room not found</h1>')

def seephoto(request,pk):
    if request.method =="GET":
        room = Room.object.get(pk=pk)
        return render(request,'seephoto.html' )
