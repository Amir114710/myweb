from django.shortcuts import redirect



class LoginRequirdMixins:
    def dispatch(self , request , *args , **kwargs):
        if self.request.user.is_authenticated == True:
            return redirect('home:main')
        return super().dispatch(request , *args , **kwargs)
class LogoutRequirdMixins:
    def dispatch(self , request , *args , **kwargs):
        if self.request.user.is_authenticated == False:
            return redirect('home:main')
        return super(LogoutRequirdMixins ,  self ).dispatch(request , *args , **kwargs)