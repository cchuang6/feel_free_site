from django.shortcuts import render
from parse_rest.datatypes import Object, Pointer, GeoPoint
import datetime
from .models import Space, History, User

# Create your views here.

def index(request):
    # This is for test only
    # Who is here
    # How many people came in one day
    # How long they have stayed
    # Sex, Age, Occoupation
    today = datetime.datetime.today()
    today = today.replace(hour=0, minute=0, second=0, microsecond=0)

    # make to one day
    today = today - datetime.timedelta(days=1)
    tomorrow = today + datetime.timedelta(days=1)
    #SIP ID: LjIgPxR6Bt
    targetId = 'LjIgPxR6Bt'
    space = Pointer(Space(objectId=targetId))
    checkin_today = History.Query.filter(createdAt__gte=today, createdAt__lt=tomorrow,
                                         action='CHECK IN', space=space)


    # TODO: use parse function
    # my_loc = GeoPoint(latitude=33.489626, longitude=-111.926755)
    #### Use geo location to determine check in or not
    #space = Space.Query.filter(objectId=targetId)
    #user 1: xjX6jBZbbB, bktH2uYB4K, qZUSq5LMIF
    # user1 = User.Query.filter(objectId='xjX6jBZbbB')
    # user2 = User.Query.filter(objectId='bktH2uYB4K')
    # user3 = User.Query.filter(objectId='qZUSq5LMIF')

    # if space.count() != 0:
    #     users = User.Query.filter(alreadyCheckedIn=True, coordniate__nearSphere=space[0].coordinate)



    # maps_for_mode = GameMap.Query.filter(maps__relatedTo=mode)



    context = {'checkin_num': checkin_today.count()}




    # locations = [item.coordinate for item in query]
    # print locations
    return render(request, 'index.html', context)