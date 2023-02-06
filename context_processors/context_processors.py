from account.models import User , Profile


def profile(request):
    profile = Profile.objects.all() 
    return {"user": profile}
