from django.conf import settings

def app_config(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {
        'APP_NAME': settings.APP_NAME,
        'HIDE_ADMIN_IN_NAVBAR': settings.HIDE_ADMIN_IN_NAVBAR
        }