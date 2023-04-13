import json
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout

from match.models import BetOdd, Market, Matche

from .models import Betting, ForgotPswd, Recharge,CustomUser,Withdrawal
# from serpapi import GoogleSearch
from django.contrib.auth.models import AbstractUser
from profiles.models import Profile

from .helper import send_forget_password_maill
import uuid






def index(request):
    # rand = random.randint(0,1000000)
    

    # print(rand)
   

    return render(request, 'screens/index.html')

def indexref(request, *args, **kwargs):
    code =str(kwargs.get('ref_code'))
    try:
        profile  = Profile.objects.get(code = code)
        request.session['ref_profile'] = profile.id
        print('id',profile.id,profile)
    except:
        pass
    print(request.session.get_expiry_date())
    return render(request, 'screens/ref.html',{
        'profile':profile
    })

def refferal(request):
    profile = Profile.objects.get(user=request.user)
    my_resc = profile.get_recommened_profiles()
    # my_code = get_object_or_404(Profile, pk=ref_id)
    # code =int(kwargs.get('ref_code'))
    # profile  = Profile.objects.get(code = code)
    return render(request, 'screens/refferal.html',{'my_resc':my_resc,
    # 'profile':profile
    })

def register(request):

    

    profile_id = request.session.get('ref_profile')
    print('profile_id',profile_id)
    
    if request.method =="POST":
    # Get from values
        nick_name = request.POST['nickname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if passwords match
        if password == password2:
           
            # check Username
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if CustomUser.objects.filter(email=email).exists():
                    messages.error(request, 'That email is been used')
                    return redirect('register')
                else:
                    # return
                    

       
                    user = CustomUser.objects.create_user(username=username, password=password, email=email,
                    first_name=nick_name)
                    # Login aftter

                    if profile_id is not None:
                        recommended_by_profile = Profile.objects.get(id=profile_id)

                        instance = user.save()
                        registered_user = CustomUser.objects.get(id=user.id)
                        registered_profile = Profile.objects.get(user=registered_user)
                        registered_profile.recommended_by = recommended_by_profile.user
                        registered_profile.save()
                        messages.success(request, 'you are now registered and can log in')
                        return redirect('login')
                    else:

                        user.save()
                        # token = Token.objects.get(user=user).key
                        # data['token'] = token
                        messages.success(request, 'you are now registered and can log in')
                        return redirect('login')

        else:
            messages.error(request, 'passwords do not match')
            return redirect('register') 
    return render(request, 'screens/register.html')

def login(request):
    if request.method == 'POST':
          # Login User
          username = request.POST['username']
          password = request.POST['password']

          user = auth.authenticate(username=username,password=password)

          if user is not None:
              auth.login(request, user)
              messages.success(request, 'you are now logged in')
              return redirect('index')
       
          else:
              messages.error(request, 'Invalid credentials')
              return redirect('login')
    return render(request, 'screens/home.html')

def logout(request):
    auth_logout(request)
    messages.info(request, 'you are now logged out...come back soon')
    return redirect('login')


def changePassword(request, token):
    context = {}
    try:
        profile_obj = ForgotPswd.objects.get(forgetpasswordtoken = token).first()
        context = {'user_id' : profile_obj.user.id}
        
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')
            
            if user_id is  None:
                messages.success(request, 'No user id found.')
                return redirect(f'changePassword/{token}')
                
            
            if  new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                return redirect(f'changePassword/{token}')
                         
            
            user_obj = CustomUser.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('login')

        print(profile_obj)
    except Exception as e:
        print(Exception)

    return render(request, 'screens/changePassword.html')

def forgotPassword(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')

            if not CustomUser.objects.filter(username=username).first():
                messages.error(request, "No username found")
                return redirect("forgotPassword")

            user_obj = CustomUser.objects.get(username=username)
            token = str(uuid.uuid4())
            # profile_obj = ForgotPswd.objects.get(user = user_obj)
            # profile_obj.forgetpasswordtoken = token
            # profile_obj.save()
            send_forget_password_maill(user_obj.email, token)
            messages.success(request, "An email is sent")
            return redirect("forgotPassword")
    
    except Exception as e:
        print(e)
    return render(request, 'screens/forgotPassword.html')
       



def market_place(request):
    # response=requests.get('https://livescore-api.com/api-client/scores/live.json&key=2vY6VuVQ1BsYpg9c&secret=4k3AcNxWrOScwllyRkFMOBDQc5PClZOq')
    # response = response.json()
    # response = response['data']['match'][:40]

    # params = {

    #     "q": "Premier League",
    #     "location": "austin, texas, united states",
    #     "api_key": "334b3e936a2f2a2368cb34fd9cd7f4fa65fa8d93f078d6810d6827e7cd427682"
    # }


    # search = GoogleSearch(params)
    # results = search.get_dict()
    # response = results["sports_results"]["games"]
    # print(response)

    import requests

    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

    querystring = {"next":"50"}

    headers = {
	    "X-RapidAPI-Key": "4ea9ec84bamsh1ef8a966d3bc3a1p16e7f0jsn79d9f9a1ca85",
	    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()["response"]

    # print(response.text)

    for item in response:
        Market.objects.create(
            league = item['league']['name'],
            home = item['teams']['home']['name'],
            away = item['teams']['away']['name'],
            homeLogo = item['teams']['home']['logo'],
            awaylogo = item['teams']['away']['logo'],
            homeGoal = item['goals']['home'],
            awayGoal = item['goals']['away'],
            matchTime = item['fixture']['date']
        )
        print('saved')

    data = Market.objects.all()

    return render(request, 'screens/market_place.html',{
        'data':data,
    })



def match_result(request):
   
    return render(request, 'screens/match_result.html')

   

def league(request):


    response = Matche.objects.all()[:10]

    # print(response.text)
    return render(request, 'screens/league.html',{

        'response':response
    })



def single_league(request):
    # response=requests.get('https://livescore-api.com/api-client/scores/live.json&key=2vY6VuVQ1BsYpg9c&secret=4k3AcNxWrOScwllyRkFMOBDQc5PClZOq')
    # response = response.json()
    # item = response['data']['match'][:12]
    # # item = [Response, single_id=single_id]

    

    return render(request, 'screens/single_league1.html')



def recharge(request):
    if request.method == "POST":
        
        recharge = Recharge()
        file = request.POST.get('file')
        user = request.POST.get('name')
        email = request.POST.get('email')
        transactionid = request.POST.get('transactionId')
        amount = request.POST.get('amount')
        chain = request.POST.get('chain')

        recharge.paymentProve=file
        recharge.transactionid = transactionid
        recharge.amount = amount
        recharge.name = user
        recharge.email = email
        recharge.chain = chain
        recharge.save()
        messages.success(request, "Your request has been submitted, You'll get an email shortly")
        return redirect('dashboard')

        
        
    return render(request, 'screens/recharge.html')

def dashboard(request):
    user = CustomUser()
    if request.method == "POST":
        phone = request.POST.get("phoneNo")


        user.phoneNo = phone
        user.save()
        messages.success(request,)

    # code =str(kwargs.get('ref_code'))
    # try:
    # profile  = Profile.objects.get(code = code)
    # request.session['ref_profile'] = profile.id
    # print('id',profile.id,profile)
    # except:
        # pass

    return render(request, 'screens/dashboard.html',{
        # 'profile':profile
    })

def prediction():

    import requests

    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

    querystring = {"next":"50"}

    headers = {
	    "X-RapidAPI-Key": "4ea9ec84bamsh1ef8a966d3bc3a1p16e7f0jsn79d9f9a1ca85",
	    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)
    data = response.json()["response"]

    print(data)

    for item in data:
        Matche.objects.create(
            league = item['league']['name'],
            leagueLogo = item['league']['logo'],
            leagueSeason = item['league']['season'],
            home = item['teams']['home']['name'],
            away = item['teams']['away']['name'],
            homeLogo = item['teams']['home']['logo'],
            awaylogo = item['teams']['away']['logo'],
            homeGoal = item['goals']['home'],
            awayGoal = item['goals']['away'],
            matchTime = item['fixture']['date']
        )
        print('saved')



    # return render(request,'screens/prediction.html',{'data':data})
def predict(request):

    data = Matche.objects.all().order_by("-id")
    return render(request,'screens/prediction.html',
    {'data':data}
    )


def singlepredict(request,key_id):
    data = get_object_or_404(Matche, pk=key_id)
    item = BetOdd.objects.all()


    return render(request,'screens/singlepredict.html',{'data':data,'item':item})


def singlegame(request):
    if request.method == "POST":
        
        betting = Betting()
        amount = request.POST.get('amount')
        user = request.POST.get('user')
        match= request.POST.get('match')
        prediction = request.POST.get('predict')

        betting.amount=amount
        betting.username = user
        betting.match = match
        betting.scores = prediction

    
        betting.save()
        messages.success(request, "Bet Received, stay in touch")
        return redirect('dashboard')

    return render(request, 'screens/single_league.html')

def betting(request):
    
    if request.method == 'POST':
        betting = Betting()

        user = request.POST.get('name')
        match = request.POST.get('match')
        amountbet = request.POST.get('betAmount')
        score = request.POST.get('score')
        profit = request.POST.get('profit')
        balance = request.POST.get('balance')

        betting.username = user
        betting.match = match
        betting.amount = amountbet
        betting.scores = score
        betting.profit = profit
        # balanceAmount = CustomUser.objects.get_or_create(username=request.user.username)
        # print(balanceAmount)
        print(balance)
        print(amountbet)

        if balance > amountbet:
            print("no no no")
            if Betting.objects.filter(username = user).exists():
                if Betting.objects.filter(match=match).exists():
                    messages.error(request, 'Already bet this match, you can bet just once')
                    return redirect('predict')

                else:
                    betting.save()
                    messages.success(request, 'Bet recieved, wait for approval')
                    return redirect('betting_history')
            else:
                betting.save()
                messages.success(request, 'Bet recieved, wait for approval')
                return redirect('betting_history')


        elif balance < amountbet:
            messages.error(request, 'Your balance is low, kindly recharge')
            return redirect('predict')

        # if Betting.objects.filter(username = user).exists():
        #     if Betting.objects.filter(match=match).exists():
        #         messages.error(request, 'Already bet this match, you can bet just once')
        #         return redirect('predict')


        #     else:
        #         if balance > amountbet:
        #             betting.save()
        #             messages.success(request, 'Bet recieved, wait for approval')
        #             return redirect('betting_history')

            

                # elif balance < amountbet:
                #     messages.error(request, 'Your balance is low, kindly recharge')
                #     return redirect('predict')
        # elif  not Betting.objects.filter(username = user).exists:
            
        #     # return redirect('betting_history')
           
        #     if balance < amountbet:
        #         betting.save()
        #         messages.success(request, 'Bet recieved, wait for approval')
        #         return redirect('betting_history')
                    
                
        #     elif balance > amountbet:
        #         messages.error(request, 'Your balance is low, kindly recharge')
        #         return redirect('predict')

                # if not response:
                #     pass
                    
                # else:
                #     print("Worked")
                #     balanceAmount = CustomUser.objects.get_or_create(amount=request.user.amount)
                #     amount = balance - amountbet
                    
                #     print(balanceAmount)


                # return redirect('dashboard')
                


    return render(request, 'screens/betting.html')

def transaction(request):
    return render(request, 'screens/transaction.html')

def withdrawal(request):
    if request.method == 'POST':
        withdraw = Withdrawal()
        user = request.POST.get('user')
        amount = request.POST.get('amount')
        chain = request.POST.get('chain')
        password = request.POST.get('password')
        balance = request.POST.get('balance')
        # print(f'{amount} and {balance}')

        withdraw.username = user
        withdraw.amountToWithdraw = amount
        withdraw.amountbalance = balance
        withdraw.chain = chain
        withdraw.password = password

        if amount < balance:
            messages.error(request, 'insufficient amount requested')
            print(f'{amount} and {balance}')
            
            return redirect('withdrawal')

        elif amount > balance:
            withdraw.save()
            messages.success(request, 'Your request has been received, an admin will confirm your request soon')
            print(f'{amount} and {balance}')
            return redirect('withdrawal')
        
    return render(request, 'screens/withdraw.html')

def betting_history(request):
    item = Betting.objects.filter(username=request.user.username).order_by("-id")


    return render(request, 'screens/bet_history.html',{
        'item':item
    })

def sample():

    from serpapi import GoogleSearch

    params = {
    "q": "premier league",
    "location": "austin, texas, united states",
    "api_key": "e772616fa6205b5953558f49c75b5a0a48d9c49bf2549c05ed29843d137ec039"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    sports_results = results["sports_results"]
    print(sports_results)