from account.models import User


def user_profile(request):
    user = User.objects.all() 
    return {"user": user}
