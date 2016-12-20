from pyramid.response import Response
import io
import os

THIS_DIR = os.path.dirname(__file__)

def list_page(request):
    """View list page."""
    file_path = os.path.join(THIS_DIR, 'templates', 'home.html').read()
    file_data = io.open(file_path).read()
    return Response(file_data)


def detail_page(request):
    """View detail page."""
    file_path = os.path.join(THIS_DIR, 'data', 'sample.html').read()
    file_data = io.open(file_path).read()
    return Response(file_data)


def create_page(request):
    """View create page."""
    file_path = os.path.join(THIS_DIR, 'templates', 'new_entry.html').read()
    file_data = io.open(file_path).read()
    return Response(file_data)


def update_page(request):
        """View update page."""
    file_path = os.path.join(THIS_DIR, 'templates', 'edit_entry.html').read()
    file_data = io.open(file_path).read()
    return Response(file_data)


def includeme(config):
    """Add routes."""
    config.add_view(list_page, route_name='list')
    config.add_view(detail_page, route_name='detail')
    config.add_view(create_page, route_name='create')
    config.add_view(update_page, route_name='update')
