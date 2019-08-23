from django.db import models

# Create your models here.
class Question(models.Model):
    def __str__(self):
        return self.question_text
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Post1(models.Model):
    def __str__(self):
        return self.question_text
    def recently(self):
        return self.id >= 3
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    cvs_path = models.FileField(upload_to='static/taswira/dataset')

class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now()- datetime.timedelta(days=1)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Dataset(models.Model):
    def __str__(self):
        return self.title
    SCOPE_COVERAGE = (
        ('D', 'Dunia'),
        ('T', 'Tanzania'),
        ('M', 'Mkoa'),
        ('W', 'Wilaya'),
        ('K', 'Kata')
        )
    title = models.CharField(max_length=20)
    description= models.TextField()
    scope = models.CharField(max_length=1, choices=SCOPE_COVERAGE)
    source = models.CharField(max_length=20)
    sector = models.CharField(max_length=20)
    published_date = models.DateField()
    start_date= models.PositiveSmallIntegerField()
    end_date= models.PositiveSmallIntegerField()
    cvs_filePath=models.FileField("data file")
    #user uploaded, when uploaded

class Post(models.Model):
    title = models.CharField(max_length=20)
    time_posted=models.DateTimeField(auto_now=True)
    description= models.TextField()
    scope = models.SmallIntegerField()
    sector = models.CharField(max_length=20)
    dataset_id= models.SmallIntegerField()
    user_id= models.SmallIntegerField()
    post_evaluation=models.TextField()
    active =models.BooleanField()


class Comment(models.Model):
    post_id=models.SmallIntegerField()
    user_id=models.SmallIntegerField()
    comment=models.TextField(max_length=100)
    time_posted=models.DateTimeField(auto_now_add=True)

class User(models.Model):
    name=models.CharField(max_length=10);
    password=models.CharField(max_length=10);
    role=models.CharField(max_length=10);
#this will be modified depending on the required changes


