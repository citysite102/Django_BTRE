from django.contrib import admin

from .models import Listing


# 讓 listing 裡面顯示底下這些欄位
class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
  # 讓 id、 title 這個項目變得可以連結過去
  list_display_links = ('id', 'title')
  # 在admin 右側會跑出一個 Filter
  list_filter = ('realtor',)
  # 讓某個欄位可以直接可編輯，然後再按儲存
  list_editable = ('is_published',)
  search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
  list_per_page = 25

admin.site.register(Listing, ListingAdmin)
