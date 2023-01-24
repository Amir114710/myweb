from account.models import User


def profile(request):
    user = User.objects.all() 
    return {"user": user}
