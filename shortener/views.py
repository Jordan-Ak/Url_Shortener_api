from django.shortcuts import reverse
from rest_framework import viewsets

from .models import Link
from .serializers import LinkSerializer

# Create your views here.


class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer
    
    def get_queryset(self):

        if self.request.user.is_staff or self.action != 'list':
            queryset = Link.objects.all()
        
        else:
            return None
        
        return queryset

    #def create(self, request, *args, **kwargs):
 
        #if "input_link" in request.POST:
            #try:
             #   instance = Link.objects.get(input_link = request.POST['input_link'])
                #reverse()