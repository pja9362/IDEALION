from django.db import models

# Create your models here.

#하나하나의 마커에 대한 데이터들입니다
class contents(models.Model): #id에 대한 column 안써도됨 
    lat = models.FloatField(max_length=50, default='0')
    lng = models.FloatField(max_length=50, default='0')
    title = models.CharField(max_length = 200)
    writer = models.CharField(max_length = 100)
    category = models.CharField(max_length = 100, default = "none")
    pub_date = models.DateTimeField()
    detail = models.TextField()
    image = models.ImageField(upload_to = "blog/", blank = True, null = True)
    
    def __str__(self):  #객체가 호출될 때 실행됨
        return self.title #제목을 title로 띄우기  

    def summary(self): #본문 간단히 나타내기
        return self.detail[:100]


#하나하나의 카테고리에 대한 데이터들입니다
class categoryList(models.Model):
    name = models.CharField(max_length = 200, default="", unique=True)
    share = models.BooleanField(default='true')  
    icon = models.ImageField(upload_to = "idea/", blank = True, null = True)
    author = models.CharField(max_length = 200, default="")

    def __str__(self):  #객체가 호출될 때 실행됨
        return self.name #제목을 title로 띄우기  
