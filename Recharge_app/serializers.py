from rest_framework import serializers

from Recharge_app.models import Plans, Recharge

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plans
        fields = '__all__'

class RechargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recharge
        fields = '__all__'



    # def to_representation(self, instance):
    #     print('instance',instance)
    #     self.fields['plan'] = PlanSerializer(read_only=True)
    #     return super(RechargeSerializer,self).to_representation(instance)
