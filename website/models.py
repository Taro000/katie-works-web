from django.db import models

# Create your models here.


class Work(models.Model):
    name = models.CharField('仕事名', max_length=63)
    thumbnail = models.ImageField('サムネイル', upload_to="work")
    text = models.TextField('テキスト')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class WorkImage(models.Model):
    works = models.ForeignKey(Work, on_delete=models.PROTECT)
    name = models.CharField('画像名', max_length=63)
    img = models.ImageField('画像',  upload_to="work")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Craft(models.Model):
    name = models.CharField('クラフト名', max_length=63)
    thumbnail = models.ImageField('サムネイル', upload_to="craft")
    text = models.TextField('テキスト')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CraftImage(models.Model):
    works = models.ForeignKey(Craft, on_delete=models.PROTECT)
    name = models.CharField('画像名', max_length=63)
    img = models.ImageField('画像', upload_to="craft")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Company(models.Model):
    name = models.CharField('社名', max_length=31)
    owner = models.CharField('代表者', max_length=15)
    business = models.CharField('事業内容', max_length=63)
    tel = models.CharField('TEL', max_length=31)
    fax = models.CharField('FAX', max_length=31)
    email = models.EmailField('メール')
    address = models.TextField('所在地')
