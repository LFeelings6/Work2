from django.Contrib import admin
from models import EquipmentCategory
#Equipment Admin view
class EquipmentCategoryAdmin(admin.modelAdmin):
      list_display=('category_name','date_created',)#Display Data in
      list_filter=('date_created',)
      search_fields=('category_name',)#Add A search Field






      
      #Register Models
      admin.site.register(EquipmentCategory,EquipmentCategoryAdmin)