from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import Instform, BeneficiaryMF, InstitutionMF
from django.views import View

# Create your views here.
# home page rendering
def fdms_home(request):
    wlcom = "Welcome to FDMS - Home"
    context = {"wlc" : wlcom, 'title':"FDMS -Welcome! Home"}

    return render(request, "fdms/welcome.html", context)
#    return HttpResponse("<h2> Welcome to FDMS </h2>")

def fdms_create_mf(request):
    if request.method == "POST":
        form_mf=InstitutionMF(request.POST)
        if form_mf.is_valid():
           cfd= form_mf.cleaned_data
           cfd.save()
           return HttpResponseRedirect("thanks/")
        else:
            return HttpResponseRedirect('error/')
#            form_mf=InstitutionMF()
    if request.method=="POST":
        benef = BeneficiaryMF(request.POST)
        if benef.is_valid():
            benef.save()
            return HttpResponseRedirect("thanks/")
            
    else:
        form_mf = InstitutionMF()
        benef = BeneficiaryMF()

    title="CreateMF_Page"
    header="Create  Db Info"
    context={'title':title, 'header':header, "form":form_mf, "form1":benef} 
    return render(request, 'fdms/create.html', context)

def fdms_thanks(request):
    return render(request, 'fdms/thanks.html')

def fdms_error(request):
    return render(request, 'fdms/error.html')

#CREATING A CLASS BASED VIEW for Heading in each crud page

class GreetingMsg(View):
    greetings="this is a Greeting"

    def get(self, request):
        greetings="Hello , gonna Delete"
        form_mf1=InstitutionMF()
        context={'form21':form_mf1}
        return render(request, 'fdms/delete.html', context)
    
    def post(self, request):
        greetings="Hello, gonna POST Delete"
        return HttpResponse(greetings)
    
def fdms_update(request):
    if request.method == "POST":
        benf2 = BeneficiaryMF(request.POST)
        if benf2.is_valid():
            benf2.save()
    else:
        benf2 = BeneficiaryMF()
        
    wlcom = "Update your DB"
    context={'form1': benf2, "wlc": wlcom}
    return render(request, "fdms/update.html", context)

def fdms_read(request):
    if request.method == 'POST':
        if request.is_valid():
            pass
    
#    readform=Instform(request)
#    context={'formr1': readform}
    return render(request, 'fdms/read.html')
