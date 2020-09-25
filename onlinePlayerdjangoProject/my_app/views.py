import json
from django.http import HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from django.http import JsonResponse

from my_app.music_api.kugou_api import *
from my_app.music_api.kuwo_api import *
from my_app.music_api.migu_api import *
from my_app.music_api.qq_api import *
from my_app.music_api.xiami_api import *


@csrf_exempt
def search_song(request):
    song_name = request.GET['name']
    song_type = request.GET['type']

    if song_type == 'kugou':
        content = kugou_search_song(song_name)
    elif song_type == 'kuwo':
        content = kuwo_search_song(song_name)
    elif song_type == 'migu':
        content = migu_search_song(song_name)
    elif song_type == 'qq':
        content = qq_search_song(song_name)
    elif song_type == 'xiami':
        content = xiami_search_song(song_name)
    else:
        content = 'no music'

    return HttpResponse(json.dumps(content))


def kugou_search_song(name):
    kugou_song_list = []
    kugou_song_list_meesage = kugou_search_api(name)
    for index in range(len(kugou_song_list_meesage)):
        song_url = kugou_song_list_meesage[index]["song_url"]
        song_name = kugou_song_list_meesage[index]["song_name"]
        song_user = kugou_song_list_meesage[index]["song_user"]
        song_time = kugou_song_list_meesage[index]["song_time"]
        song_img = kugou_song_list_meesage[index]["song_img"]
        song_lyr = kugou_song_list_meesage[index]["song_lyr"]
        song_album = kugou_song_list_meesage[index]["song_album"]
        kugou_song_list.append(
            {'song_url': song_url, 'song_name': song_name, 'song_user': song_user, 'song_time': song_time,
             'song_img': song_img, 'song_lyr': song_lyr, 'song_album': song_album})
    return kugou_song_list


def kuwo_search_song(name):
    kuwo_song_list = []
    kuwo_song_list_message = kuwo_search_api(name)
    for index in range(len(kuwo_song_list_message)):
        song_url = kuwo_song_list_message[index]["song_url"]
        song_name = kuwo_song_list_message[index]["song_name"]
        song_user = kuwo_song_list_message[index]["song_user"]
        song_time = kuwo_song_list_message[index]['song_time']
        song_img = kuwo_song_list_message[index]["song_img"]
        song_lyr = kuwo_song_list_message[index]["song_lyr"]
        song_album = kuwo_song_list_message[index]["song_album"]
        kuwo_song_list.append(
            {'song_url': song_url, 'song_name': song_name, 'song_user': song_user, 'song_time': song_time,
             'song_img': song_img, 'song_lyr': song_lyr, 'song_album': song_album})
    return kuwo_song_list


# 无时间
def migu_search_song(name):
    miqu_song_list = []
    migu_song_list_message = migu_search_api(name)
    for index in range(len(migu_song_list_message)):
        song_url = migu_song_list_message[index]["song_url"]
        song_name = migu_song_list_message[index]["song_name"]
        song_user = migu_song_list_message[index]["song_user"]
        song_time = migu_song_list_message[index]['song_time']
        song_img = migu_song_list_message[index]["song_img"]
        song_lyr = migu_song_list_message[index]["song_lyr"]
        song_album = migu_song_list_message[index]["song_album"]
        miqu_song_list.append(
            {'song_url': song_url, 'song_name': song_name, 'song_user': song_user, 'song_time': song_time,
             'song_img': song_img, 'song_lyr': song_lyr, 'song_album': song_album})
    return miqu_song_list


def qq_search_song(name):
    qq_song_list = []
    qq_song_list_message = qq_search_api(name)
    for index in range(len(qq_song_list_message)):
        song_url = qq_song_list_message[index]["song_url"]
        song_name = qq_song_list_message[index]["song_name"]
        song_user = qq_song_list_message[index]["song_user"]
        song_time = qq_song_list_message[index]['song_time']
        song_img = qq_song_list_message[index]["song_img"]
        song_lyr = qq_song_list_message[index]["song_lyr"]
        song_album = qq_song_list_message[index]["song_album"]
        qq_song_list.append(
            {'song_url': song_url, 'song_name': song_name, 'song_user': song_user, 'song_time': song_time,
             'song_img': song_img, 'song_lyr': song_lyr, 'song_album': song_album})
    return qq_song_list


# 无时间
def xiami_search_song(name):
    xiami_song_list = []
    xiami_song_list_message = xiami_search_api(name)
    for index in range(len(xiami_song_list_message)):
        song_url = xiami_song_list_message[index]["song_url"]
        song_name = xiami_song_list_message[index]["song_name"]
        song_user = xiami_song_list_message[index]["song_user"]
        song_time = xiami_song_list_message[index]['song_time']
        song_img = xiami_song_list_message[index]["song_img"]
        song_lyr = xiami_song_list_message[index]["song_lyr"]
        song_album = xiami_song_list_message[index]["song_album"]
        xiami_song_list.append(
            {'song_url': song_url, 'song_name': song_name, 'song_user': song_user, 'song_time': song_time,
             'song_img': song_img, 'song_lyr': song_lyr, 'song_album': song_album})
    return xiami_song_list
