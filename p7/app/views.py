from django.shortcuts import render, redirect
from .models import Customer, Order, Product
from .forms import OrderForm, CustomerForm, CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def registerUser(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login_user')
    context = {'form': form}
    return render(request, 'app/register_user.html', context)

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('order')
        else:
            messages.info(request, 'Username or Password is incorrect! ')
            return render(request, 'app/login_user.html')
    return render(request, 'app/login_user.html')

def logoutUser(request):
    logout(request)
    return redirect('login_url')


@login_required(login_url='login_user')
def home(request):
    return render(request, 'app/home.html')

@login_required(login_url='login_user')
def product(request):
    product = Product.objects.all()
    context = {"product":product}
    return render(request, 'app/product.html', context)

@login_required(login_url='login_user')
def customer(request):
    customer = Customer.objects.all()
    context = {'customers':customer}
    return render(request, 'app/customer/customer.html', context)

@login_required(login_url='login_user')
def createCustomer(request):
    form = CustomerForm()
    if request.method=="POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer')
    context = {'form': form}
    return render(request, 'app/customer/create_customer.html',context)

@login_required(login_url='login_user')
def updateCustomer(request, pk):
    customer = Customer.objects.get(id = pk)
    form = CustomerForm(instance=customer)
    if request.method=="POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer')
    context = {'form':form}
    return render(request, 'app/customer/create_customer.html', context)

@login_required(login_url='login_user')
def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method=="POST":
        customer.delete()
        return redirect('customer')

    context = {'customer':customer}
    return render(request, 'app/customer/delete_customer.html', context)

@login_required(login_url='login_user')
def order(request):
    order = Order.objects.all()
    context = {'orders':order}
    return render(request, 'app/order/order.html', context)

@login_required(login_url='login_user')
def createOrder(request):
    form = OrderForm()
    if request.method=="POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order')
    context = {'form': form}
    return render(request, 'app/order/create_order.html',context)

@login_required(login_url='login_user')
def updateOrder(request, vidur):
    order = Order.objects.get(id = vidur)
    form = OrderForm(instance=order)
    if request.method=="POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order')
    context = {'form':form}
    return render(request, 'app/order/create_order.html', context)

@login_required(login_url='login_user')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method=="POST":
        order.delete()
        return redirect('order')

    context = {'order':order}
    return render(request, 'app/order/delete.html', context)


from .serializers import CustomerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
class GetOrder(APIView):
    def post(self, request, format=None):
        name = request.data.get('name')
        phoneno = request.data.get('phoneno')
        address = request.data.get('address')
        if name and phoneno and address:
            a = Customer.objects.create(name=name, phoneno=phoneno, address=address)
            serializer = CustomerSerializer(a)
            
            a.save()
            return Response({"result": "User created Successfully!" })
        else:
            return ResourceWarning({"result": "invalid params"})

