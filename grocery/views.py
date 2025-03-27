from django.shortcuts import render, redirect, HttpResponse
from  . models import *
import random as r
import razorpay
from django.conf import settings

def home(request):
    allcategory = Category.objects.filter(status='Active')
    allproduct = Product.objects.filter(status = 'Active')
    trending=Product.objects.filter(status = 'Active', trending="Y")[0:5]
    latest= Product.objects.filter(status = 'Active')[0:5]
    if request.user.is_authenticated:
        counter= Cart.objects.filter(user=request.user).values().count()
    else:
        counter=0
    
    return render(request, 'index.html', {'category': allcategory, 'product': allproduct, 'trending': trending, 'latest': latest, 'counter':counter})

def categorypage(request, id):
    products= Product.objects.filter(category=id, status="Active")
    allcategory = Category.objects.filter(status='Active')
    latest= Product.objects.filter(status = 'Active')[0:5]
    counter= Cart.objects.filter(user=request.user).values().count()
    return render(request, 'category.html', {'category': allcategory, 'products': products, 'latest': latest, 'counter':counter})

    
def productDetails(request, id):
    allcategory = Category.objects.filter(status='Active')
    product= Product.objects.get(id=id)
    category= product.category
    related= Product.objects.filter(category=category, status="Active")
    counter= Cart.objects.filter(user=request.user).values().count()
    
    return render(request, 'product-details.html', {'category': allcategory, 'product': product, 'related': related, 'counter': counter})

def addtocart(request):
    product= request.GET.get('product')
    pid= Product.objects.get(id=product)   
    user= request.user
    qt= request.GET.get('qty') 
    cart, created= Cart.objects.get_or_create(product=pid, user=user)
    if not created:
        cart.qty+=int(qt)  
    else:
        cart.qty= qt
    cart.save()
    return HttpResponse('Added To Cart')

def viewCart(request):
    cart= Cart.objects.filter(user= request.user)
    counter= Cart.objects.filter(user=request.user).values().count()
    return render(request, 'cart.html' , {'cart':cart, 'counter': counter})

def deleteCart(request):
    id= request.GET.get('id')
    cart= Cart.objects.get(id=id)
    cart.delete()
    return HttpResponse("Item Deleted From Cart")


def updateCart(request):
    id= request.GET.get('id')
    newqty= request.GET.get('qty')
    cart= Cart.objects.get(id=id)
    cart.qty=newqty
    cart.save()
    return HttpResponse("Cart Updated")

def checkout(request):
    
    allcategory = Category.objects.filter(status='Active')
    counter= Cart.objects.filter(user=request.user).values().count()
    orderid= 'ORD'+str(r.randint(1000, 9999))
    uid= request.user
    cart= Cart.objects.filter(user=uid)
    total=0
    for c in cart:
          total+=int(c.qty)*int(c.product.mrp)
    
    if total>=1000:
        shipping=0
    else:
        shipping=100

    gst=18
    netamount= total+shipping
    gstval= netamount*gst//100
    netamount+=gstval 
          
    

    if request.POST.get('sendorder'):
        for x in cart:
            order= Order.objects.create(product=x.product, user=uid, qty=x.qty, orderid=orderid, status='Success')
            order.save()
            product= Product.objects.get(id=x.product.id)
            product.stock=int(product.stock)-int(x.qty)
            product.save()


        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email= request.POST.get('email')
        contact=request.POST.get('contact')
        street= request.POST.get('street')
        landmark= request.POST.get('landmark')
        address=street+','+landmark
        state=request.POST.get('state')
        city= request.POST.get('city')
        country= request.POST.get('country')
        pincode=request.POST.get('pincode')
        amount= request.POST.get('amount')
        paymode= request.POST.get('paymode')
        order= Order.objects.filter(orderid=orderid).first()
        
        

        bill= Billing.objects.create(user=request.user, orderid=order, first_name=first_name, last_name=last_name, email=email, contact=contact, address=address, state=state, city=city, pincode=pincode, amount=amount, payment_mode=paymode)
        
        bill.save()
        cart.delete()
        if paymode=='Online':
            return render(request, 'payment.html', {'amount': int(netamount)*100})
        else:
            pass


     
    return render(request, 'checkout.html', {'orderid':orderid,'cart':cart, 'category':allcategory, 'counter':counter, 'total':total, 'shipping':shipping, 'netamount': netamount,'gst': gstval })

def success(request):
 if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        razorpay_order = client.order.create(
            {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"}
        )
        return render(request,"success.html", {'amount': amount*100 })
 
def orderlist(request):
    user=request.user
    order=Order.objects.filter(user=user)
    return render(request,'my-orders.html',{'order':order})

def loginUser(request):
    pass