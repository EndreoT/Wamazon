from rest_framework import generics, permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .serializers import UserSerializer, DepartmentSerializer, ProductSerializer, GroupSerializer, ValidateIntegerSerializer
from .models import Department, Product
from .permissions import IsOwnerOrReadOnly

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.reverse import reverse

# Entry point on /api/
# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('customuser-list', request=request, format=format),
#         'departments': reverse('department-list', request=request, format=format),
#         'products': reverse('department-list', request=request, format=format),
#     })


# Viewsets combine both list and detail views into single view

class UserViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer
  permission_classes = (permissions.IsAdminUser,)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class DepartmentViewSet(viewsets.ModelViewSet):
  """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
  """
  queryset = Department.objects.all()
  serializer_class = DepartmentSerializer
  # Can only write if authenticated
  permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

  # Links user creater to created_by field
  def perform_create(self, serializer):
    serializer.save(created_by=self.request.user)


class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

  def get_serializer_class(self):
    if self.action == 'purchase_product':
        return ValidateIntegerSerializer
    else:
        return ProductSerializer
  
  @action(
    methods=['put'], detail=True, permission_classes=[permissions.IsAdminUser],
    url_path='purchase', url_name='purchase'
  )
  def purchase_product(self, request, pk=None): # route on api/products/<pk>/purchase
    product = Product.objects.get(pk=pk)
    stockToPurchase = request.data
    serializer = ValidateIntegerSerializer(data=stockToPurchase)
    if serializer.is_valid():
      totalCost = product.purchaseStock(serializer.validated_data)
      return Response(totalCost, status=status.HTTP_200_OK)
    return Response(serializer.errors)
  
  



# class UserList(generics.ListCreateAPIView):
#   queryset = get_user_model().objects.all()
#   serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#   queryset = get_user_model().objects.all()
#   serializer_class = UserSerializer


# class DepartmentList(generics.ListCreateAPIView):
#   queryset = Department.objects.all()
#   serializer_class = DepartmentSerializer
#   # Can only write if authenticated
#   permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

#   # Links user creater to created_by field
#   def perform_create(self, serializer):
#     serializer.save(created_by=self.request.user)


# class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
#   queryset = Department.objects.all()
#   serializer_class = DepartmentSerializer
#   permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


# class ProductList(generics.ListCreateAPIView):
#   queryset = Product.objects.all()
#   serializer_class = ProductSerializer


# class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
#   queryset = Product.objects.all()
#   serializer_class = ProductSerializer
