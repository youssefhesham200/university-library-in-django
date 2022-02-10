from django.contrib import admin
from .models import User, Student, Owner, FormBook
# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Owner)
admin.site.register(FormBook)