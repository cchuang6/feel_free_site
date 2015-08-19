from django.shortcuts import render
from parse_rest.datatypes import Object, Pointer, GeoPoint, Function
import datetime
from .models import Space, History, User

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
    getSpaceDetail = Function('getSpaceDetail')
    spaceDetail = getSpaceDetail(spaceId=spaceId, version=version, deviceType=deviceType)
    num_users = len(spaceDetail['result']['users'])

    context = {'num_visits': num_visits, 'num_users': num_users, 'title': 'SIP Test'}
    return render(request, 'index.html', context)


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