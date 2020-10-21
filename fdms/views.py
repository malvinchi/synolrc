from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import Instform, BeneficiaryMF, InstitutionMF


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
        benef = BeneficiaryMF(request.POST)
        if form_mf.is_valid():
            form_mf.save()

        if benef.is_valid():
            benef.save()

        return HttpResponseRedirect("thanks/")
    else:
        form_mf = InstitutionMF()
        benef=BeneficiaryMF()

    title="CreateMF_Page"
    header="Create  Db Info"
    context={'title':title, 'header':header, "form":form_mf, "form1":benef} 
    return render(request, 'fdms/create.html', context)

def fdms_thanks(request):
    return render(request, 'fdms/thanks.html')

