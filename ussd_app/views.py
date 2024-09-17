from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import redis

redis_client = redis.Redis(host = "localhost", port = 6379, db=0)

@csrf_exempt
def index(request):
    if request.method == "POST":
        session_id = request.POST.get("sessionId")
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        user_data = redis_client.get(session_id)
        if user_data:
            user_data = user_data.decode('utf-8')
        else:
            user_data=None

        response = ""

        if text == "":

            redis_client.delete(session_id)
            response = "CON Welcome to our news service subscription \n"
            response += "1. Sport \n"
            response += "2. political \n"
            response += "3. Local  \n"
            response += "4. International"

        elif text == "1":
            redis_client.set(session_id, "sports", ex=600)
            response = "CON Select your prefered sport plan \n"
            response += "1. Daily @ N100 \n"
            response += "2. Weekly @ N50 \n"
            response += "3. Monthly @ N25 "

        elif text == "1*1":
            redis_client.set(f"{session_id}_plan", "daily", ex=600)
            response = "CON You will be charged N100 for your Daily Sports news subscription \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"

        elif text == "1*1*1":
            redis_client.set(f"{session_id}_subscription", "auto", ex=600)
            response = "END thank you for subscribing to our daily sport news plan \n"
        elif text == "1*1*2":
            redis_client.set(f"{session_id}_subscription", "oneoff", ex=600)
            response = "END thank you for your one-off daily sport news plan \n"

        elif text == "1*2":
            redis_client.set(f"{session_id}_plan", "weekly", ex=600)
            response = "CON You will be charged N50 for our weekly Sports news plan \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"
        
        elif text == "1*2*1":
            redis_client.set(f"{session_id}_subscription", "auto", ex=600)
            response = "END thank you for subscribing to our weekly sport news plan \n"
        elif text == "1*2*2":
            redis_client.set(f"{session_id}_subscription", "oneoff", ex=600)
            response = "END thank you for your one-off weekly sport news plan \n"

        elif text == "1*3":
            redis_client.set(f"{session_id}_plan", "monthly", ex=600)
            response = "CON You will be charged N25 for our monthly Sports news plan \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"
            
        elif text == "1*3*1":
            redis_client.set(f"{session_id}_subscription", "auto", ex=600)
            response = "END thank you for subscribing to our monthly sport news plan \n"
        elif text == "1*3*2":
            redis_client.set(f"{session_id}_subscription", "oneoff", ex=600)
            # Retrieve stored Redis data
            category = redis_client.get(session_id).decode('utf-8')
            plan = redis_client.get(f"{session_id}_plan").decode('utf-8')
            subscription = redis_client.get(f"{session_id}_subscription").decode('utf-8')
            
            print(f"Category: {category}")
            print(f"Plan: {plan}")
            print(f"Subscription: {subscription}")
            response = "END thank you for your one-off monthly sport news plan \n"

        return HttpResponse(response)

            

    # Create your views here.
