from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Item
from account.models import User, Order

# Create your views here.
def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items' : items})

def create(request):
    if request.method == 'POST':
        new_item = Item()
        new_item.name = request.POST['name']
        new_item.price = request.POST['price']
        new_item.image = request.FILES['image']
        new_item.body = request.POST['body']
        new_item.save() 
        return redirect('home')
    else:
        return render(request, 'new.html')


def detail(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'detail.html', {'item' : item})


def update(request, id):
    if request.method == 'POST':
        update_item = Item.objects.get(id = id)
        update_item.name = request.POST['name']
        update_item.price = request.POST['price']
        update_item.image = request.FILES['image']
        update_item.body = request.POST['body']
        update_item.save()
        return redirect('detail', update_item.id)
    else:
        item = Item.objects.get(id = id)
    return render(request, 'edit.html', {'item':item})
        
def delete(request, id):
    delete_item = Item.objects.get(id = id)
    delete_item.delete()
    return redirect('home')

# 주문 목록에 넣기 
def order(request, id) : 
    item = get_object_or_404(Item, id = id)
    # 새로운 order 
    new_order = Order()
    # 현재 user 정보 가져오기 
    user_id = request.user.id
    user = User.objects.get(id = user_id)
    # 새로운 order 채우기 
    new_order.order_user = user
    new_order.order_item = item
    # order 객체 저장 
    new_order.save() 
    return redirect('order_finished')

# 내 주문 내역 
def order_list(request) : 
    # Order 객체 전부 가져오기 
    list = Order.objects.all()
    # product 객체 전부 가져오기
    item = Item.objects.all()

    ### 해당 유저의 주문 내역을 반환하는 과정 ###
    
    # 이 유저에 해당하는 객체만 list 에 저장. 
    list = list.filter(order_user = request.user.id)

    # for 문을 돌면서 이 유저가 가지고 있는 상품 result 에 저장 후 return
    # 이렇게 해야 order_list 에서 product 의 상세정보로 연결됨. 
    result = []

    for i in list : 
        for j in item : 
            # 상품명으로 비교
            if str(i) == str(j) : 
                result.append(j)
                
    return render(request, 'order_list.html', {'result':result})

# 주문 완료 페이지 
def order_finished(request) : 
    return render(request, 'order_finished.html')
