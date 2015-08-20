from django.shortcuts import render
from parse_rest.datatypes import Object, Pointer, GeoPoint, Function
import datetime
from .models import Space, History, User
from sets import Set

# Create your views here.

# TODO: average time users checked in the space
# TODO: Demographic

def index(request):
    """Return a index page

    Args:
        request (HttpRequest): The request object used to generate this response.

    Returns:
        HttpResponse object: An HttpResponse with rendered text
    """

    #SIP ID: LjIgPxR6Bt
    spaceId = 'LjIgPxR6Bt'
    date = datetime.datetime.today()
    version = '1.2.1'
    deviceType = 'ios'

    # number of check in per day
    num_visits = __getNumVisitsOneDay(spaceId, date)

    # number of current users
    # getSpaceDetail = Function('getSpaceDetail')
    # spaceDetail = getSpaceDetail(spaceId=spaceId, version=version, deviceType=deviceType)
    # num_users = len(spaceDetail['result']['users'])

    # This is for testing
    endDate = datetime.datetime.today()
    startDate = endDate - datetime.timedelta(days=30)
    num_newUsers = __getNumNewCustomers(spaceId, startDate, endDate)

    # number of new customers


    # context = {'title': 'SIP Test', 'num_visits': num_visits, 'num_users': 0,
    #            'num_newUsers': num_newUsers}
    context = {'title': 'SIP Test', 'num_visits': 0, 'num_users': 0,
               'num_newUsers': 0}
    return render(request, 'index.html', context)


def __getNumNewCustomers(spaceId, startDate, endDate):
    """Get number of new customers in date range

    Args:
        spaceId (str): Space Object ID
        startDate (datetime.datetime): The query start date
        endDate (datetime.datetime): The query end date

    Returns:
        int: Number of visits
    """

    if endDate == None:
        endDate = datetime.datetime.today()
    endDate = endDate.replace(hour=0, minute=0, second=0, microsecond=0)
    endDate = endDate + datetime.timedelta(days=1)
    startDate = startDate.replace(hour=0, minute=0, second=0, microsecond=0)

    space = Pointer(Space(objectId=spaceId))
    currentLogs = History.Query.filter(createdAt__lt=endDate, action='CHECK IN', space=space)
    prevLogs = History.Query.filter(createdAt__lt=startDate, action='CHECK IN', space=space)

    sNow = Set()
    sPrev = Set()
    for item in currentLogs:
        sNow.add(item.user.objectId)
    for item in prevLogs:
        sPrev.add(item.user.objectId)
    sNow -= sPrev
    return len(sNow)

def __getNumVisitsOneDay(spaceId, date):
    """Get number of visits in one day

    Args:
        spaceId (str): Space Object ID
        date (datetime.datetime): The query date

    Returns:
        int: Number of visits
    """

    if date == None:
        date = datetime.datetime.today()
    date = date.replace(hour=0, minute=0, second=0, microsecond=0)
    tomorrow = date + datetime.timedelta(days=1)

    space = Pointer(Space(objectId=spaceId))
    result = History.Query.filter(createdAt__gte=date, createdAt__lt=tomorrow,
                                  action='CHECK IN', space=space)
    return result.count()