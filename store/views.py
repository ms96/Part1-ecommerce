from django.shortcuts import render
from .models import *
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from django.http import JsonResponse
import json, datetime
from .serializers import *


def profile(request):
    context = {}
    return render(request, 'profile.html',context)

# def account_login(request):
#     context = {}
#     return render(request, 'login.html',context)

# def account_signup(request):
#     context = {}
#     return render(request, 'signup.html',context)

def home(request):
    context = {'cartItems':0}
    return render(request, 'store/main.html',context)





class StoreAPIView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            customer = request.user.customer
            orders = Order.objects.filter(customer=customer, complete=False)
            order = orders.first()
            items = order.orderitem_set.all() if order else []
            cartItems = order.get_cart_items if order else 0
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}
            cartItems = order['get_cart_items']

        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        if request.accepted_renderer.format == 'json':
            # If the request accepts JSON response, return JSON data
            data = {
                'products': serializer.data,
                'cartItems': cartItems
            }
            return Response(data)
        else:
            # If the request is from a browser, render HTML template
            context = {'products': products, 'cartItems': cartItems}
            return render(request, 'store/store.html', context)
        
class CartAPIView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            customer = request.user.customer
            orders = Order.objects.filter(customer=customer, complete=False)
            order = orders.first()
            items = order.orderitem_set.all() if order else []
            cartItems = order.get_cart_items if order else 0
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}
            cartItems = order['get_cart_items']

        if request.accepted_renderer.format == 'json':
            # If the request accepts JSON response, return JSON data
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        else:
            # If the request is from a browser, render HTML template
            context = {'items': items, 'order': order, 'cartItems': cartItems}
            return render(request, 'store/cart.html', context)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckoutAPIView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items if order else 0
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}
            cartItems = order['get_cart_items']

        if request.accepted_renderer.format == 'json':
            # If the request accepts JSON response, return JSON data
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        else:
            # If the request is from a browser, render HTML template
            context = {'items': items, 'order': order, 'cartItems': cartItems}
            return render(request, 'store/checkout.html', context)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UpdateItemAPIView(APIView):
    def post(self, request):
        productId = request.data.get('productId')
        action = request.data.get('action')

        customer = request.user.customer
        product = Product.objects.get(id=productId)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

        if action == 'add':
            orderItem.quantity += 1
        elif action == 'remove':
            orderItem.quantity -= 1

        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()

        serializer = OrderItemSerializer(orderItem)
        print(serializer.data)
        return Response(serializer.data)
    

class ProcessOrderAPIView(APIView):
    def post(self, request):
        transaction_id = datetime.datetime.now().timestamp()
        data = request.data
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            total = data.get('total')
            order.transaction_id = transaction_id

            if total == order.get_cart_total and total > 0:
                order.complete = True
                order.total_price = total
            order.save()

            # After saving the order, reduce the stock quantity of all the products in the order
            order_items = order.orderitem_set.all()
            for item in order_items:
                product = item.product
                product.stock_quantity -= item.quantity
                product.save()
        else:
            print("User is not logged in")

        # if request.accepted_renderer.format == 'json':
        #     # serializer = OrderSerializer(order, many=True)
        #     return Response({"id":order.id, "total":order.total_price, "ordered_date":order.date_ordered})
        # else:
        return Response({'message': 'Order processed','id':order.id})
        
class OrderHistoryAPIView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            customer = request.user.customer
            orders = customer.order_set.filter(complete=True).order_by('-id')
            serializer = OrderSerializer(orders, many=True)
            if request.accepted_renderer.format == 'json':
                return Response(serializer.data)
            else:
                context = {'orders': orders, 'cartItems':0}
                return render(request, 'store/orderhistory.html', context)
        else:
            return Response({'error': 'User is not authenticated'}, status=403)