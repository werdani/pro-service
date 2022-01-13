from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated



#Function to view all products.
@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def all_product(request):
    all_produc = Product.objects.all()
    data = ProductSerializer(all_produc, many=True).data
    return Response({'data':data})


@api_view(['GET'])
def product_filter(request,user):
    all_produc = Product.objects.filter(fieldname='user')
    data = ProductSerializer(all_produc, many=True).data
    return Response({'data':data})



#Function to arrange products by price. 
@api_view(['GET'])
def price_order(request):
    product = Product.objects.all().order_by('price')
    data = ProductSerializer(product, many=True).data
    return Response({'data':data})
