from django.contrib import admin
from . import models

class EmployeeAdmin(admin.ModelAdmin):
    list_per_page =6
    list_max_show_all =6
    list_display=('FUllname','Role','Email','Department')
admin.site.register(models.Employee,EmployeeAdmin)

 
class DepartmentAdmin(admin.ModelAdmin):
    list_per_page =6
    list_max_show_all =6
    list_display=('Department',)
admin.site.register(models.Department,DepartmentAdmin)      

class AdministrationAdmin(admin.ModelAdmin):
    list_per_page =6
    list_max_show_all =6
    list_display=('Role','Passport','Message')
admin.site.register(models.Administration,AdministrationAdmin)      


class AnnouncementAdmin(admin.ModelAdmin):
    list_per_page =6
    list_max_show_all =6
    list_display=('Heading','Document','DateRegistered')
admin.site.register(models.Announcements,AnnouncementAdmin)   


class CustomerAdmin(admin.ModelAdmin):
    list_per_page =6
    list_max_show_all =6
    list_display=('Fullname','Email','Resident','NationalID','State','License','Construction','BusinessType','Earthquake','Flood','TINnumber',)
admin.site.register(models.Customer,CustomerAdmin)  

class CompansationAdmin(admin.ModelAdmin):
    list_per_page =6
    list_max_show_all =6
    list_display=('amount','CustomerID','RegisteredDate','BankReceipt')
admin.site.register(models.compansation,CompansationAdmin)   

class MonthlyInstallmentAdmin(admin.ModelAdmin):
    list_per_page =6
    list_max_show_all =6
    list_display=('amount','CustomerID','RegisteredDate','BankReceipt')
admin.site.register(models.MonthlyInstallment,MonthlyInstallmentAdmin)   



