import rest_framework.viewsets
from . import models
from . import serializers

class tbl_user_Viewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.tbl_user_Serializer

    #list(),retrieve(),create(),update(),destroy()