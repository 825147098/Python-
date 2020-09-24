import json
from django.http import HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from django.http import JsonResponse

from my_app.music_api.kugou_api import *
from my_app.music_api.wangyi_api import *
from my_app.music_api.kuwo_api import *
from my_app.music_api.migu_api import *
from my_app.music_api.qq_api import *
from my_app.music_api.qianqian_api import *
from my_app.music_api.xiami_api import *


@csrf_exempt
def search_song(request):
    song_name = request.GET['name']
    song_type = request.GET['type']

    dic = []
