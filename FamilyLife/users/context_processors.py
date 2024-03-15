from main_site.views import menu

def get_context(request):
    return {'mainmenu': menu}