from django.db import models
import uuid
from stdimage.models import StdImageField
from django_cleanup import cleanup

# Create your models here.
WORK_CATEGORIES = [
    ('LG', 'Logo'),
    ('CL', 'Catalogue'),
    ('AD', 'Advertisement'),
    ('OT', 'Others'),
]


def set_work_img_name(instance, filename):
    return f"work/{str(uuid.uuid4())}.{filename.split('.')[-1]}"


def set_craft_img_name(instance, filename):
    return f"craft/{str(uuid.uuid4())}.{filename.split('.')[-1]}"


class Work(models.Model):
    name = models.CharField('仕事名', max_length=63)
    thumbnail = StdImageField('サムネイル', upload_to=set_work_img_name, max_length=32, variations={
        'large': (1920, 1080, True),
        'thumbnail': (608, 342, True),
    })
    text = models.TextField('テキスト')
    category = models.CharField('カテゴリー', max_length=2, choices=WORK_CATEGORIES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Work'
        verbose_name_plural = 'Work'

    def __str__(self):
        return self.name


class WorkImage(models.Model):
    works = models.ForeignKey(Work, on_delete=models.PROTECT)
    name = models.CharField('画像名', max_length=63)
    img = StdImageField('画像', upload_to=set_work_img_name, max_length=32, variations={
        'large': (1920, 1080, True),
        'thumbnail': (608, 342, True),
    })
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Work画像'
        verbose_name_plural = 'Work画像'

    def __str__(self):
        return self.works.name + '-' + self.name


class Craft(models.Model):
    name = models.CharField('クラフト名', max_length=63)
    thumbnail = StdImageField('サムネイル', upload_to=set_craft_img_name, max_length=32, variations={
        'large': (1920, 1080, True),
        'thumbnail': (608, 342, True),
    })
    text = models.TextField('テキスト')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Craft'
        verbose_name_plural = 'Craft'

    def __str__(self):
        return self.name


class CraftImage(models.Model):
    crafts = models.ForeignKey(Craft, on_delete=models.PROTECT)
    name = models.CharField('画像名', max_length=63)
    img = StdImageField('画像', upload_to=set_craft_img_name, max_length=32, variations={
        'large': (1920, 1080, True),
        'thumbnail': (608, 342, True),
    })
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Craft画像'
        verbose_name_plural = 'Craft画像'

    def __str__(self):
        return self.crafts.name + '-' + self.name


class Company(models.Model):
    name = models.CharField('社名', max_length=31)
    owner = models.CharField('代表者', max_length=15)
    business = models.CharField('事業内容', max_length=63)
    tel = models.CharField('TEL', max_length=31)
    fax = models.CharField('FAX', max_length=31)
    email = models.EmailField('メール')
    address = models.TextField('所在地')

    class Meta:
        verbose_name = '会社情報'
        verbose_name_plural = '会社情報'

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField('お名前', max_length=127)
    send_by = models.EmailField('メールアドレス')
    tel = models.CharField('TEL', max_length=31)
    content = models.TextField('お問い合わせ内容')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'お問い合わせ'
        verbose_name_plural = 'お問い合わせ'

    def __str__(self):
        return self.name + 'さま - ' + self.created_at.astimezone().strftime('%Y/%m/%d %H:%M:%S')
