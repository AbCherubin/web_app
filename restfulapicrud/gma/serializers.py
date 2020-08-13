# api <-> mobile app / web app/etc .json
import rest_framework.serializers
from .models import tbl_user


class tbl_user_Serializer(serializers,ModelSerializer):
    class Meta:
        model = tbl_user
        field = '__all__'
        #field = ('id','username')