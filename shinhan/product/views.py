from django.shortcuts import render,redirect
from .models import Product
from django.http.response import JsonResponse

def main(request):
    products=Product.objects.all().order_by('-id')
    # 키 값 products가 html에 쓰이는 부분 
    return  render(request,'product.html', {'products':products})


def detail(request,pk):
    product= Product.objects.get(pk=pk)

    ret={
        'username':product.user.username,
        'title':product.title,
        'content':product.content,
        'price':product.price,
        'location':product.location,
        'image':'/static/prod1.jpg' 
    }

    if product.image:
        ret['image']=product.image.url
   
    # JsonResponse
    # 문자열이나 숫자로 이루어진 데이터를 담게 됨
    # 이미지는 파일을 다루기 때문에 
    # 
    return JsonResponse(ret)

def write(request):
    # 1. 페이지 접속 조차 막고 싶을 때  이쪽
    if not request.user.is_authenticated:
        return redirect('/member/login/')

    # 주소가 동일하므로
    # 어떤 요청으로 들어왔는지 확인하기 위한 code
    # 주소에 들어가는 건 GET

    
    if request.method=='POST':
        # 2. 여기에 작성하면 
        # 등록 버튼 누를시 로그인 페이지로 이동
        # if not request.session.get('user_id'):
        #     return redirect('/member/login/')


        # 아래와 같이 작성해도 무방
        # product=Product()
        # product.content=request.POST.get('content')

        # request.POST
        # print(request.method)
        # print(equest.POST)

        # .POST.get('price') = .POST['price'] 
        # 값이 없을 수도 있으니까 get으로 호출해서 가져옴
        product= Product( 
            user=request.user,
            title=request.POST.get('title'),
            content=request.POST.get('content'),
            price=request.POST.get('price'),
            location=request.POST.get('location'),
            image=request.FILES.get('image')
            )
        product.save()
        return redirect('/')
        # 현재 상황에서는 id 값을 사용할 수 없음
        #return redirect(f'/product/{product.id}')

    
    return  render(request,'product_write.html')
