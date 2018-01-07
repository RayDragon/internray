from django.db import models
from django.contrib.auth.hashers import PBKDF2PasswordHasher, SHA1PasswordHasher
from django.http import HttpResponse, HttpResponseRedirect


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60, unique=True)
    password = models.CharField(max_length=120)
    salt = models.CharField(max_length=20)
    fbid = models.CharField(max_length=15, null=True)

    def set_password(self, raw_password):
        salt = "yet not done with it"
        has = hash()
        self.password = has.encode(raw_password, salt)

    def has_password(self, raw_password):
        salt = "yet not done with it"
        has = hash()
        if self.password == has.encode(raw_password, salt):
            return True
        return False

    def __str__(self):
        return self.name+" "+self.email

    @staticmethod
    def get_user(uid=None, email=None):
        user = None
        if uid:
            user = User.objects.get(id=uid)
        elif email:
            user = User.objects.get(email=email)
        return user


class hash(PBKDF2PasswordHasher):
    algorithm = 'pbkdf2_wrapped_sha1'

    def encode_sha1_hash(self, sha1_hash, salt, iterations=None):
        return super().encode(sha1_hash, salt, iterations)

    def encode(self, password, salt, iterations=None):
        _, _, sha1_hash = SHA1PasswordHasher().encode(password, salt).split('$', 2)
        return self.encode_sha1_hash(sha1_hash, salt, iterations)


def signup(request):

    user = User()
    user.name = request.POST.get("name", "#")
    user.email = request.POST.get("email", "#")
    user.set_password(request.POST.get("password", "#"))
    if User.objects.filter(email=user.email).count() == 1:
        return HttpResponse('{"result":"fail", "message":"User already exists"}')
    return HttpResponse('{"result":"pass", "headto":"./account"}')
    

def login(request):
    email = request.POST.get('email', '#')
    pwd = request.POST.get('password', '#')

    if User.objects.filter(email=email).count() == 1:
        user = User.objects.get(email = email)
        if user.has_password(pwd):
            request.session['uid'] = user.id

        return HttpResponse('{"result":"pass", "headto":"./account"}')
    return HttpResponse('{"result":"fail", "message":"wrong credentials"}')


def isLogged(request):
    if 'uid' in request.session:
        return True


def logout(request):
    if isLogged(request):
        del request.session['uid']
        return HttpResponseRedirect("../login")
    return HttpResponseRedirect("../login")


def update(request):
    if not isLogged(request): return HttpResponse('{"result":"fail", "headto":"./account"}')
    email = request.POST.get('email', '#')
    pwd1 = request.POST.get('passwordOld', '#')
    pwd2 = request.POST.get('passwordNew', '#')
    name = request.POST.get('name', '#')
    if User.objects.filter(id=request.session['uid']).count() == 1:
        user = User.objects.get(email=email)
        if user.has_password(pwd1) :
            if email != '' and email != '#':
                user.email = email
            if pwd2 != '' and pwd2 != '#':
                user.set_password(pwd2)
            if name != '' and name != '#':
                user.name = name
            user.save()
            return HttpResponse('{"result":"pass", "headto":"#r"}')
    return HttpResponse('{"result":"fail", "headto":"./account"}')
