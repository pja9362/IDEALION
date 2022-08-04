from django.shortcuts import render, get_object_or_404, redirect
from .models import contents, categoryList #db 불러오기
from django.utils import timezone
from .forms import ContentsForm, categoryForm
from django.core.paginator import Paginator

#홈 화면이 호출될 때 실행되는 함수입니다
def home(request):
    lists = categoryList.objects.all() #나만의 지도 버튼 눌렀을 때 모든 카테고리를 띄워주기 위해 데이터베이스에서 카테고리 리스트를 뽑아옵니다 
    return render(request, "home.html", {'lists':lists} ) #home.html을 렌더링합니다

#하나하나의 마커의 상세 내용을 띄어줄 때 실행되는 함수입니다.
def detailPlace(request, content_id):
    Contents = get_object_or_404(contents, pk = content_id) #모든 마커 중에 선택된 마커를 반환해줍니다
    return render(request, "detailPlace.html", {"content":Contents}) #detailPlace.html을 띄워줍니다

# myMap.html에서 마커를 추가하기 위해 "해당 장소를 추가하겠습니다" 버튼을 눌렀을 때 실행되는 함수입니다
def addPlace(request):
    form = ContentsForm()  #forms.py에 있는 새로운 콘텐츠 입력 폼을 가져옵니다
    lat = request.POST['lat'] #마커의 위도 ,경도 값을 저장합니다
    lng = request.POST['lng']
    category= request.POST.get('category')  #카테고리 값을 저장합니다
    return render(request, "addPlace.html",{'form':form, 'lat':lat, 'lng':lng, 'category':category}) #addPlace.html을 띄워줍니다

#addPlace.html에서 submit 버튼을 눌렀을 때 실행되는 함수입니다
def create(request):

    #컨텐츠 입력 폼에 담긴 값을 가져옵니다
    form = ContentsForm(request.POST, request.FILES)
    
    #폼에 입력된 값이 유효할 때 실행됩니다
    if form.is_valid():

        #폼에 작성된 값을 임시적으로 저장
        new_content = form.save(commit=False)

        # 마커의 작성날짜를 현재 시간으로 설정
        new_content.pub_date = timezone.now() 
        
        #폼에 입력된 값을 가져와서 새로운 마커의 속성값으로 저장합니다
        new_content.writer = request.user.username
        new_content.category = request.POST['category']
        new_content.lat = request.POST['lat']
        new_content.lng = request.POST['lng']
 
        #마커를 최종적으로 저장합니다
        new_content.save()

        #모든 마커를 데이터베이스에서 작성일자 순으로 가져옵니다
        Contents = contents.objects.order_by('-pub_date')

        #모든 카테고리들 중 새 마커의 카테고리와 이름이 같은 카테고리만 가져옵니다
        lists = categoryList.objects.get(name = new_content.category)
        return render(request, 'myMap.html', {'contents': Contents, 'list':lists}) #mymap.html을 화면에 띄워줍니다

    #폼에 입력된 값이 유효하지 않을 때 create() 함수를 다시 호출해줍니다.
    return redirect('create')


# 마커에 대한 정보를 수정하기 위한 함수입니다.
def editPlace(request, content_id): 
    edit_content = contents.objects.get(id = content_id)  #모든 마커 중 선택한 마커만을 가져옵니다
    return render(request, 'editPlace.html', {'content': edit_content}) #editPlace.html을 화면에 띄워줍니다


# editPlace.html에서 마커에 대한 정보를 수정하고 submit 버튼을 눌렀을 때 실행되는 함수입니다
def updatePlace(request, content_id):

    #모든 마커 중 선택한 마커만을 가져옵니다
    update_content = contents.objects.get(id=content_id)

    #editPlace.html의 폼에 입력한 정보들을 가져와 수정할 마커에 저장합니다.
    update_content.title = request.POST['title']
    update_content.writer = request.POST['writer']    
    update_content.body = request.POST['body']
    update_content.pub_date = timezone.now() #작성일자를 현재 시간으로 변경해줍니다
    Category = update_content.category
    
    #수정한 마커의 내용들을 데이터베이스에 저장합니다
    update_content.save()
    return redirect('myMap', Category) #mymap.html로 다시 돌아가기 위해 mymap() 함수를 호출합니다.


#마커를 삭제하기 위한 함수입니다
def deletePlace(request, content_id):

    #모든 마커 중 선택한 마커만을 가져옵니다
    delete_content = contents.objects.get(id = content_id)
    
    #해당 마커를 데이터베이스에서 삭제합니다
    delete_content.delete()
    Category = delete_content.category
    return redirect('myMap', Category) #mymap.html로 다시 돌아가기 위해 mymap() 함수를 호출합니다.


# 나만의 지도 (myMap.html)을 띄워주기 위한 함수입니다.
def myMap(request, Category):
    Contents = contents.objects.order_by('-pub_date')  #모든 마커들을 가져옵니다
    lists = categoryList.objects.get(name = Category)  #데이터베이스 상의 모든 카테고리들 중 현재 카테고리만을 가져옵니다 
    return render(request, 'myMap.html', {'contents': Contents, 'list':lists}) # myMap.html을 띄워줍니다

def ourMap(request):
       return render(request, 'ourMap.html') 

def showtoilets(request):
       return render(request, 'showtoilets.html')  

def showsmokings(request):
       return render(request, 'showsmokings.html')     



# 새로운 카테고리를 만들기 위한 함수입니다
def newCategory(request):

    #home.html에서 나만의 지도 버튼을 누르고 전송 버튼을 눌렀을 때 실행됨
    if request.method == "GET":
        Category = request.GET.get('newCategory')

        #사용자가 "새로운 지도 추가하기" 메뉴를 선택했다면 실행됨
        if(Category == 'add'):
            form = categoryForm()
            return render(request, 'newCategory.html', {'form': form}) #새로운 카테고리를 만들기 위한 newCategory.html을 화면에 띄워줌
        
        #사용자가 이미 존재하는 카테고리의 지도를 선택하였을 때, 해당 카테고리를 매개변수로 주면서 myMap.html을 화면에 띄워줍니다
        return redirect('myMap', Category)

    #newCategory.html에서 새로운 카테고리의 내용들을 모두 작성한 후 submit 버튼을 눌렀을 때 실행됨
    if request.method == "POST":
        tempForm = categoryForm(request.POST, request.FILES) #폼에 작성된 내용들을 가져옴
        
        #폼에 작성된 내용들을 모두 유효할 때
        if tempForm.is_valid():

            #내용들을 임시적으로 저장
            new_Category = tempForm.save(commit=False)
            
            #카테고리를 생성한 사람을 현재 사용자로 저장
            new_Category.author = request.user.username

            #내용들을 최종적으로 저장함
            new_Category.save()

            Category = request.POST['name']
            return redirect('myMap', Category) #myMap함수를 다시 호출함 => 아래줄의  return render(request, 'newCategory.html', {'form': tempForm})가 실행됩니다
        return render(request, 'newCategory.html', {'form': tempForm}) #newCategory.html이 실행됩니다

    
