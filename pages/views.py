from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse("ສະບາຍດີ ປະເທດລາວ")
# view :
    # 1. FBV : Function-based view
    # 2. CBV : Class-based view
    # 3. GCBV  : Generic Class-based view