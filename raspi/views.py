from django.http.response import JsonResponse
from django.shortcuts import redirect, render,HttpResponse
from .models import LedStat,UserDevices
from django.contrib.auth import login,logout,authenticate
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def AppLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            userdevice = UserDevices.objects.get(user=user)
            return HttpResponse(userdevice.device_id.device_id)
        else:
            return HttpResponse("can't login now please check username or password")
        


def getLED1stat(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.led1_status==0:
        return HttpResponse("LED is off")
    else:
        return HttpResponse("LED is On")

def getLED2stat(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.led2_status==0:
        return HttpResponse("LED is off")
    else:
        return HttpResponse("LED is On")

def getLED3stat(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.led3_status==0:
        return HttpResponse("LED is off")
    else:
        return HttpResponse("LED is On")

def getimp1stat(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.imp_1==0:
        return HttpResponse("input1 is low")
    else:
        return HttpResponse("input1 is high")

def getimp2stat(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.imp_2==0:
        return HttpResponse("input2 is low")
    else:
        return HttpResponse("input2 is high")

def getimp3stat(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.imp_3==0:
        return HttpResponse("input3 is low")
    else:
        return HttpResponse("input3 is high")

def getLED4stat(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.led4_status==0:
        return HttpResponse("LED is off")
    else:
        return HttpResponse("LED is On")

def getLED5stat(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.led5_status==0:
        return HttpResponse("LED is off")
    else:
        return HttpResponse("LED is On")

def getLED6stat(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.led6_status==0:
        return HttpResponse("LED is off")
    else:
        return HttpResponse("LED is On")

def getLED7stat(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.led7_status==0:
        return HttpResponse("LED is off")
    else:
        return HttpResponse("LED is On")

def ToggleLED1(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.led1_status==0:
        ledstat.led1_status=1
        ledstat.save()
        return redirect('getstat1',pk)
    else:
        ledstat.led1_status=0
        ledstat.save()
        return redirect('getstat1',pk)      

def ToggleLED2(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.led2_status==0:
        ledstat.led2_status=1
        ledstat.save()
        return redirect('getstat2',pk)
    else:
        ledstat.led2_status=0
        ledstat.save()
        return redirect('getstat2',pk) 

def ToggleLED3(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.led3_status==0:
        ledstat.led3_status=1
        ledstat.save()
        return redirect('getstat3',pk)
    else:
        ledstat.led3_status=0
        ledstat.save()
        return redirect('getstat3',pk)

def Toggleimp1(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.imp_1==0:
        ledstat.imp_1=1
        ledstat.save()
        return redirect('getip1',pk)
    else:
        ledstat.imp_1=0
        ledstat.save()
        return redirect('getip1',pk)
   

def Toggleimp2(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.imp_2==0:
        ledstat.imp_2=1
        ledstat.save()
        return redirect('getip2',pk)
    else:
        ledstat.imp_2=0
        ledstat.save()
        return redirect('getip2',pk)


def Toggleimp3(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.imp_3==0:
        ledstat.imp_3=1
        ledstat.save()
        return redirect('getip3',pk)
    else:
        ledstat.imp_3=0
        ledstat.save()
        return redirect('getip3',pk)

def ToggleLED4(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.led4_status==0:
        ledstat.led4_status=1
        ledstat.save()
        return redirect('getstat4',pk)
    else:
        ledstat.led4_status=0
        ledstat.save()
        return redirect('getstat4',pk)

def ToggleLED5(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.led5_status==0:
        ledstat.led5_status=1
        ledstat.save()
        return redirect('getstat5',pk)
    else:
        ledstat.led5_status=0
        ledstat.save()
        return redirect('getstat5',pk)

def ToggleLED6(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.led6_status==0:
        ledstat.led6_status=1
        ledstat.save()
        return redirect('getstat6',pk)
    else:
        ledstat.led6_status=0
        ledstat.save()
        return redirect('getstat6',pk)

def ToggleLED7(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.led7_status==0:
        ledstat.led7_status=1
        ledstat.save()
        return redirect('getstat7',pk)
    else:
        ledstat.led7_status=0
        ledstat.save()
        return redirect('getstat7',pk)

def sendControl(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    return JsonResponse({'led1':str(ledstat.led1_status),
    'led2':str(ledstat.led2_status),
    'led3':str(ledstat.led3_status),
    'input1':str(ledstat.imp_1),
    'input2':str(ledstat.imp_2),
    'input3':str(ledstat.imp_3),
    'led7':str(ledstat.led4_status),
    'led8':str(ledstat.led5_status),
    'led9':str(ledstat.led6_status),
    'led10':str(ledstat.led7_status),})


def getTemp(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    return HttpResponse(str(ledstat.temprature))

def setTemp(request,pk,temp):
    ledstat = LedStat.objects.get(device_id=pk)
    ledstat.temprature = float(temp)
    ledstat.save()
    return redirect('gettemp',pk)

def led1control(request,pk,state):
    ledstat = LedStat.objects.get(device_id=pk)
    ledstat.led1_status = state
    ledstat.save()
    return redirect('getstat1',pk)

def led2control(request,pk,state):
    ledstat = LedStat.objects.get(device_id=pk)
    ledstat.led2_status = state
    ledstat.save()
    return redirect('getstat2',pk)

def led3control(request,pk,state):
    ledstat = LedStat.objects.get(device_id=pk)
    ledstat.led3_status = state
    ledstat.save()
    return redirect('getstat3',pk)

def imp1control(request,pk,state):
    ledstat = LedStat.objects.get(device_id=pk)
    ledstat.imp_1 = state
    ledstat.save()
    return redirect('getip1',pk)

def imp2control(request,pk,state):
    ledstat = LedStat.objects.get(device_id=pk)
    ledstat.imp_2 = state
    ledstat.save()
    return redirect('getip2',pk)

def imp3control(request,pk,state):
    ledstat = LedStat.objects.get(device_id=pk)
    ledstat.imp_3 = state
    ledstat.save()
    return redirect('getip3',pk)


def dashboard(request,pk):
    context={}
    ledstat = LedStat.objects.get(device_id=pk)
    context['Stats']=ledstat
    return render(request,'index.html',context)
