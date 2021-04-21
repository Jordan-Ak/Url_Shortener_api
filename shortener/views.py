from django.shortcuts import reverse
from rest_framework import viewsets

from .models import Link
from .serializers import LinkSerializer
# Create your views here.


class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer

    def get_queryset(self):

        if self.request.user.is_staff:
            queryset = Link.objects.all()
        
        else:
            pass
        
        return queryset
