import datetime
from rest_framework import filters
from rest_framework import generics
from .models import Role
from .serializers import LoginSerializer, Updateserializer, UserSerializer, RoleSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from django.db.models import Q
from .serializers import LoginSerializer
from .models import User 



class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserDisplayView(generics.ListAPIView):
    search_fields = ["username", "first_name", "last_name","email"]
    filter_backends = (filters.SearchFilter,)
    def get_serializer_class(self):
        return UserSerializer
    
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
    
    def get(self, request, *args, **kwargs):  
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)  
        serializer = self.get_serializer(queryset, many=True) 
        return Response(serializer.data)

    

class RoleCreateView(generics.CreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class RoleDisplayView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer



class UserById(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    lookup_field = "pk"

    def get(self, request,pk,format=None):
        instance = self.get_object()
        serializers=UserSerializer(instance)

        return Response(serializers.data)
    
    def put(self, request,pk,format=None):
        instance = self.get_object()
        serializers =Updateserializer(instance,data=request.data)

        if serializers.is_valid():
            serializers.save()

            return Response(
                {
                    "Message": "Successfully Updated",
                    "Body": serializers.data
                }
            )
        
        return Response( serializers.errors )
    
    def delete(self, request,pk,format=None):
        user=self.get_object()
        try:
            user.delete()
            return Response({"Message": "Successfully Deleted"})
        except:
            return Response({"Message": "Failed to Delete"})





class LoginView(generics.GenericAPIView):  
    
    serializer_class = LoginSerializer  

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            try:
                user_obj = User.objects.get(
                    Q(username__iexact=data["username"]) | Q(email__iexact=data["username"])
                )
                if check_password(data["password"], user_obj.password):
                    user_obj.last_login = datetime.datetime.now()
                    user_obj.save()
                    resp_serializer = LoginSerializer(instance=user_obj)
                    return Response(resp_serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({"Message": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                return Response({"Message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
