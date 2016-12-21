"""View file for learning journal."""

from pyramid.view import view_config
import io
import os

THIS_DIR = os.path.dirname(__file__)

JOURNAL = {
    1: {'id': 1, 'title': 'Joey DeRosa Learning Journal Day12', 'date': '12/20/16', 'body': 'Today was a long day, after chasing errors and refactoring math formulas our heap was finally compleat. I wouldn\'t have thought two simple methods to be so time consuming. By the time I got to my Journal app the TAs had already left. Luckilly with the help of some class-mates the app you see before you has life.'},
    2: {'id': 2, 'title': 'Joey DeRosa Learning Journal Day11', 'date': '12/19/16', 'body': 'Today was The day we pitched our project ideas, A lot of good ones there but I think it is obvious that TrollPy is the way to go. The data structure today was called Deque and was basically a renamed doubly linked list. Really glad that pyramid was introduced and I no longer have to trouble shoot errors that seem to just create themselves in code that was previously working.'},
    3: {'id': 3, 'title': 'Joey DeRosa Learning Journal Day10', 'date': '12/16/16', 'body': 'Today\'s white boarding challenge proved frustrating due to the limitations of what we could use, however with most things in coding the answer seemed obvious after we solved it. As for the server the new addition s weren\'t difficult to implement and gevent is a handy new feature. Our server also has some nice new response codes to throw out.'},
    4: {'id': 4, 'title': 'Joey DeRosa Learning Journal Day9', 'date': '12/15/16', 'body': 'Today had a lot of data structure trouble. We were on a wild goose chase trying to fix errors for functionality that wasn\'t needed. I did learn a lot about requesting files from a server and how to return them. All in all an tiring but good day.'},
    5: {'id': 5, 'title': 'Joey DeRosa Learning Journal Day8', 'date': '12/14/16', 'body': 'Today\'s data structure assignment wasn\'t much of a challenge with the single link list to work from. The server was fairly easy too because we had accidentally worked ahead the day before, however we did run into an infinite loop error that appeared for seemingly no reason. The PuPPy meetup was awesome, unfortunately I had to leave early in order to get home at a decent hour. the Kit AI was totally a Knight Rider reference.'},
}


@view_config(route_name='list', renderer='templates/home.jinja2')
def list_page(request):
    """View list page."""
    return {'title_list': JOURNAL}


@view_config(route_name='detail', renderer='templates/entry.jinja2')
def detail_page(request):
    """View detail page."""
    return {'title_list': JOURNAL[int(request.matchdict['id'])]}


@view_config(route_name='create', renderer='templates/new_entry.jinja2')
def create_page(request):
    """View create page."""
    return {'title_list': JOURNAL}


@view_config(route_name='update', renderer='templates/edit_entry.jinja2')
def update_page(request):
    """View update page."""
    return {'title_list': JOURNAL[int(request.matchdict['id'])]}
