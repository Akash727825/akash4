from django.shortcuts import render, HttpResponse, redirect
from .models import Catagory,  Product, Customer, Order, Contact
from django.contrib.auth.hashers import make_password , check_password

# Create your views here.
def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        first_name= request.POST.get('first_name')
        email= request.POST.get('email')
        pass1= request.POST.get('pass1')
        pass2= request.POST.get('pass2')

        # validation
        error_massage = None
        if(not first_name):
            error_massage = "Full Name Required !!"
        elif first_name:
            if len(first_name)<5:
                error_massage = "Name Must Be more then five letters ! !" 




        if pass1!=pass2:
            return HttpResponse("Password not same")
        #saving 
        if not error_massage:      
            cust= Customer(first_name=first_name, email=email, pass1=pass1, pass2=pass2)
            cust.pass1 = make_password(cust.pass1)
            cust.pass2 = make_password(cust.pass2)
            cust.save()
            return redirect('signinpage')
        else:
            return render(request, 'signup.html')    
    return render(request, 'signup.html') 
        

   
def menu(request):
    products= Product.objects.all()
    context = {
        'products' : products
    }
    print(context)

    #cart section

    if request.method == 'POST':
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:    
                        cart[product] = quantity-1
                else:    
                    cart[product] = quantity+1
            else:
                cart[product] = 1  
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart   
        print(product)
        print('cart', request.session['cart'])

    return render(request,'menu.html',context)

def front(request):
    return render(request,'index.html')  

def signinpage(request):
    if request.method == 'POST':
        email= request.POST.get('email')
        pass3= request.POST.get('pass3')
        customer= Customer.get_customer(email)

        error_message = None
        if customer:
            flag = check_password(pass3 , customer.pass1)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['email'] = customer.email
                return redirect('front') 
            else:
                error_message = 'Email or Password Invalid'   
        else:
            error_message = 'Email or Password Invalid'
        return render (request, 'signin.html')
        
    return render(request,'signin.html')      

def logout(request):
    request.session.clear()
    return redirect('signinpage')


def cart1(request):
    ids=list(request.session.get('cart').keys())
    product = Product.get_product_by_id(ids)
    print(product)
    return render(request, 'cart.html' , {'product' : product})    

def checkout(request):
    if request.method == 'POST':
        address= request.POST.get('address')
        phone= request.POST.get('phone')
        customer = request.session.get('customer_id')
        cart = request.session.get('cart')
        products = Product.get_product_by_id(list(cart.keys()))
        print(address,phone,customer)

        for product in products:
            order = Order(customer = Customer(id=customer), product=product, price=product.price,
            address=address,  phone=phone, quantity=cart.get(str(product.id)))
            
            order.save()
        request.session['cart'] = {}
            
        
    return redirect('orderNow')

def orderNow(request):
    customer = request.session.get('customer_id')
    orders = Order.get_orders_by_customer(customer)
    print(customer,orders)

    return render(request, 'orders.html', {'orders' : orders})


def ContactUs(request):
    return render(request, 'contact.html')    
   