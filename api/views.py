from unicodedata import name
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Commands, Articles, Bots, BotTokens
from .serializers import CommandsSerializer, ArticlesSerializer
from django.utils.crypto import get_random_string
from mylo.settings import SECRET_KEY
# import jwt


# Create your views here.
@api_view()
def commands(request):
    queryset = Commands.objects.all()
    serializer = CommandsSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def commandsid(request, id):
    command = get_object_or_404(Commands, pk=id)
    serializer = CommandsSerializer(command)

    return Response(serializer.data)



@api_view()
def articles(request):
    queryset = Articles.objects.all()
    serializer = ArticlesSerializer(queryset, many=True)
    return Response(serializer.data)

def dashboard_view(request):
    return render(request,"dashboard.html")

# @api_view()
# def register_bot(request):
#     if request.method == 'POST':
#         data = request.POST
#         if data['name'] is None:
#             return JsonResponse({"message", "name field should not be empty"}, status=400)
#         if data['password'] is None:
#             return JsonResponse({"message", "password field should not be empty"}, status=400)
#         bot = Bots.objects.filter(name=data['name']).first()
#         if bot is not None:
#             return JsonResponse({"message": "there is already a bot with this name"}, status=400)

#         if(data['passowrd'] != data['repassword']):
#             JsonResponse({"message": "Password and repassword are different"}, status=400)
#         hashed_password = jwt.encode({'password': data['password']}, SECRET_KEY, algorithm='HS256')
#         bot = Bots(name=data['name'], password=hashed_password)
#         bot.save()
#         return JsonResponse({"message": "bot was created successfuly"}, status=201)
            
# @api_view()
# def bot_login(request):
#     if request.method == 'POST':
#         data = request.POST
#         try:
#             bot = Bots.objects.get(name=data['name'])
#             hashed_password = jwt.encode({'password': data['password']}, SECRET_KEY, algorithm='HS256')
#             if bot.password != hashed_password:
#                 return JsonResponse({"messgae": "password or username is wrong"}, status=400) 
#             generated_token_text = get_random_string(256)
#             token = BotTokens(bot=bot, token=generated_token_text)
#             token.save()
#             return JsonResponse({"token": generated_token_text}, 200)

#         except Bots.DoesNotExist:
#             return JsonResponse({"message": "password or username is wrong"}, status=400) 



