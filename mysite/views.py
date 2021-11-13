from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from MyModels import models
from django.shortcuts import redirect
from django.template import loader
import json, time

lvls={'firework':['firework by Trick', '<iframe width="1349" height="480" src="https://www.youtube.com/embed/QBe5x2o9v2w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'], 'slaughterhouse':['Slaughterhouse by SpaceUK','<iframe width="1349" height="480" src="https://www.youtube.com/embed/pKzzz6LQfUk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>']}

def register(request, name='', password='', password2=''):
  if password == password2 and len(password) > 7:
    if name not in models.jsondb and '' not in [name, password]:
      models.jsondb=models.jsondb[name]={'password': password}
      return redirect(f'https://BlajeTenBackEnd.timtaran.repl.co/sr/{name}')
    else:
      if name in models.jsondb:
        return HttpResponse('Account with this username are already created')
      return HttpResponse('Empty name or password')
  else:
    if password != password2:
      return HttpResponse("Passwords don't match")
    return HttpResponse('Password is =< 7 symbols')
def login(request, name='', password=''):
  if name in models.jsondb:
    return HttpResponse('Uhm....')
  return HttpResponse('._.')
def sr(request, name):
  return HttpResponse(f'Sucsefully registred with username {name}')
def er(request):
  return HttpResponse(f'This username is registred or password/username is empty<br><br><br><br><br><br><br><br><br>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Maybe you have not match passwords')
def gd(request, name=''):
  if name in lvls:
    lvl=lvls[name]
    return HttpResponse(f'<h3>{lvl[0]}<h3><br><br>{lvl[1]}')
  else:
    text=''
    for i in lvls:
      text+=f"{i}<br>"
    return HttpResponse(f'Level is not added at this site.<br>All levels:<br>{text}')
def register_page(request):
  template = loader.get_template('mysite/register_page.html')
  context = {}
  return HttpResponse(template.render(context, request))

@csrf_exempt
def index(request):
  if request.method=="POST":
    return HttpResponse("Why you trying to do it...")
  return HttpResponse("""
  Hello, world
  """)
@csrf_exempt
def api_login(request):
  if request.method=="POST":
    return HttpResponse('Сори, итс донт ворк')
    #token = request.POST.get('token', False)
    #return HttpResponse(f'Your token is {token}')
    #return HttpResponse('{"result:"}')
  else:
    token = request.GET.get("token", "")
    if len(token)==45:
      #checks
      data={'result':'true', 'other_data':{'user_message':'Успешный вход в аккаунт [имя аккаунта]', 'userdata':'[имя аккаунта]'}}
      return HttpResponse(json.dumps(data))
    else:
      data={'result':'false', 'other_data':{'user_message':'Неверный токен для входа'}}
      return HttpResponse(json.dumps(data))
@csrf_exempt
def api_data(request):
  if request.method=="POST":
    return HttpResponse('Сори, итс донт ворк')
    #token = request.POST.get('token', False)
    #return HttpResponse(f'Your token is {token}')
    #return HttpResponse('{"result:"}')
  else:
    token = request.GET.get("token", "")
    if len(token)==45:
      #checks
      data={'result':'true', 'other_data':{'user_message':f'Профиль:\nБаланс: [Баланс пользователя]\nЛокация: [Локация пользователя]\nРоль: [Роль пользователя]\nВремя: {time.time()}'}}
      return HttpResponse(json.dumps(data))
    else:
      data={'result':'false', 'other_data':{'user_message':'Неверный токен для входа'}}
      return HttpResponse(json.dumps(data))