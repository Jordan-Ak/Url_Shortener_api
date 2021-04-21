from django.shortcuts import reverse, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.response import Response

from .admin_variables import HOST_URL
from .models import Link
from .serializers import LinkSerializer
from .permissions import IsAdminOrReadOnly
# Create your views here.


class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):

        if self.request.user.is_staff or self.action != 'list':
            queryset = Link.objects.all()
        
        else:
            return None
        
        return queryset

    def create(self, request, *args, **kwargs):
 
        if "input_link" in request.POST:
            try:
                instance = Link.objects.get(input_link = request.POST['input_link'])
                return HttpResponseRedirect(reverse('LinkView-detail', args = [instance.UUID]))
            
            except Link.DoesNotExist:
                serializer = LinkSerializer(data = request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data)


class Link_Redirector(View):

    def get(self, request, short_link, *args, **kwargs):
        short_link = HOST_URL + '/' + self.kwargs['short_link']
        link_query = get_object_or_404(Link, short_link = short_link)
        redirect_link = link_query.input_link 
        return HttpResponseRedirect(redirect_link)
