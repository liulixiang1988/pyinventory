from django.http import HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from inventory_app.models import Inventory
from inventory_app.serializers import InventorySerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def inventory_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        inv = Inventory.objects.all()
        serializer = InventorySerializer(inv, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = InventorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def inventory_detail(request, pk):
    try:
        inv = Inventory.objects.get(pk=pk)
    except Inventory.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = InventorySerializer(inv)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = InventorySerializer(inv, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        inv.delete()
        return HttpResponse(status=204)



