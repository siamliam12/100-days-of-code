from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
@api_view(['GET', 'POST'])
def secured_app_view(request):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    if request.method == 'GET':
        content = {'message': 'Hello, World!'}
        return Response(content)