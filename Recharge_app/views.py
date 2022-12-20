from django.shortcuts import render
from datetime import date,datetime,timedelta

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Recharge_app.models import Plans, Recharge
from Recharge_app.serializers import PlanSerializer, RechargeSerializer

class Home(APIView):
    def get(self,request):
        print(request,request)
        return Response({'message':'hello home'})

class PlanView(APIView):
    '''
    to get all the plans irrespective of operator and circle
    '''
    def get(self,request):
        all_plans = Plans.objects.all()
        print('all_plans',all_plans)
        serializer = PlanSerializer(all_plans,many=True)
        print('serializer',serializer.data)
        return Response({'All Plans':serializer.data})
    '''
    to post a plan, it can be used by admin to display plans to the user
    '''
    def post(self,request):
        print('request',request.data)
        serializer = PlanSerializer(data=request.data)
        if serializer.is_valid():
            print('in valid')
            serializer.save()
        else:
            print('errors',serializer.errors)
        return Response({'message':'plan added successfull...'})


class SelectPlan(APIView):
    '''
    to view plans by giving operator and circle as inputs

    {
    "Operator":"jio",
    "Circle":"Telangana"
    }
    '''
    def post(self,request):
        print(request,request.data)
        operator = request.data['Operator'].capitalize()
        circle = request.data['Circle'].capitalize()
        plan = Plans.objects.filter(operator=operator,circle=circle)
        print('plan',plan)
        serializer = PlanSerializer(plan,many=True)
        print('serializer',serializer.data)
        return Response({'Plan':serializer.data})

class RechargeView(APIView):
    '''
    after viewing plans by entering price and number recharge will be done to that particular number
    inputs in this way {
    "Number":"9849314733",
    "Operator":"jio",
    "Circle":"telangana",
    "Price":"129"
    }
    '''
    def post(self,request):
        print('request',request.data)
        operator = request.data['Operator'].capitalize()
        circle = request.data['Circle'].capitalize()
        price = request.data['Price']
        plan = Plans.objects.filter(operator=operator,circle=circle,price=price)
        serializer = PlanSerializer(plan,many=True)
        plan_id = serializer.data[0]['id']
        validity = serializer.data[0]['validity']
        expiry = date.today()+timedelta(days=int(validity))
        data ={}
        data['number'] = request.data['Number']
        data['plan'] = int(plan_id)
        data['is_active'] = True
        data['validity_expire'] = expiry
        recharge_serializer = RechargeSerializer(data=data)
        if recharge_serializer.is_valid():
            print('in serializer...')
            recharge_serializer.save()
        else:
            print('recharge_serializer',recharge_serializer.errors)
            return Response({'message':'Recharge failed','status':status.HTTP_500_INTERNAL_SERVER_ERROR})
        return Response({'message':'Recharge successfull...'})


class RechargeCheck(APIView):
    '''
    this api should run daily so that expiring recharges will be deactivated
    im having is_active to each recharge, when a user recharges im giving him a plan and making is_active to TRUe
    and this recharge have expiry date so based on this expiry date we make is_active to False to understand that
    that particular user is not having any active recharge
    '''
    def get(self,request):
        all_recharges = Recharge.objects.all()
        serializer = RechargeSerializer(all_recharges,many=True)
        month_formate = {
            '01': 1,
            '02': 2,
            '03': 3,
            '04': 4,
            '05': 5,
            '06': 6,
            '07': 7,
            '08': 8,
            '09': 9,
            '10': 10,
            '11': 11,
            '12': 12
        }
        for r in serializer.data:
            expiry_date = r['validity_expire']
            fyear = expiry_date[0:4]
            fmonth = expiry_date[5:7]
            fdate = expiry_date[-2:]
            present = datetime.now()
            future = datetime(int(fyear), month_formate[fmonth], int(fdate))
            if present > future:
                print(r['id'])
                Recharge.objects.filter(id=r['id']).update(is_active=False)
            else:
                print('still in validity')
        return Response({'message':'done...'})



