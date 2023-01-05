from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView
from rest_framework.generics import DestroyAPIView, UpdateAPIView

from .serializer import ProductSerializer

from .models import Product

class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
        
upload_product = ProductCreateAPIView.as_view()

class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
    
index = ProductListAPIView.as_view()   


class ProductRetriveAPIView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all() 
    
    
single = ProductRetriveAPIView.as_view()    

# @api_view(['GET'])
# def index(request, *args, **kwargs):
#     products = Product.objects.all()
#     serialisers = ProductSerializer(products, many=True)
    
#     return Response(serialisers.data, status=status.HTTP_200_OK)

class ProductDestroyAPIView(DestroyAPIView):
    serializer_class = ProductSerializer
    queryset =  Product.objects.all()
    

delete = ProductDestroyAPIView.as_view()    

class ProductUpdateAPIView(UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    

update = ProductUpdateAPIView.as_view()


# @api_view(["POST"])
# def upload_product(request, *args, **kwargs):
#     serializer = ProductSerializer(data=request.data, files=request.FILE)
    
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def index (request, *args, **kwargs) -> JsonResponse:
#     product_objects = Product.objects.all()
#     products = [
#         {
#             "id": product.id,
#             "name":product.name,
#             "content":product.content,
#             "price":product.price,
#             "discount":product.discount,
#             "date_created":product.date_created,
#             "date_updated":product.data_updated
#         }for product in product_objects
#     ]
    # data = [
    #     {
    #     "name":"Mariam",
    #     "school":"Futminna",
    #     "sex":"Female",
    #     "age":18
    # }]
    
    # name = "Mariam"    
    # return JsonResponse(data=products, safe=False)