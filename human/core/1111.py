
class AllVenues(models.Model):
    name = models.CharField(default = '', verbose_name = 'Место проведения', blank=False, max_length=100)
    href = models.CharField(max_length=100, verbose_name="Короткое название для ссылки", blank=True, default='')
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name_plural = "Заведения"
        verbose_name = "Заведение"

class CurrentVenue(models.Model):
    date = models.DateTimeField(null=True, auto_now=False, blank=True, verbose_name="Дата и время")
    place = models.ForeignKey(AllVenues, on_delete=models.CASCADE, blank=False, null=True, verbose_name="Место")
    def __str__(self):
        return str(self.date)[0:16] + "_" + str(self.place.name)

    class Meta:
        verbose_name_plural = "События"
        verbose_name = "Событие"

class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории", blank=False, default='')
    img = models.ImageField(validators=[validate_image], blank=True, default='', verbose_name="Иконка",upload_to='Categories/')
    href = models.CharField(max_length=100, verbose_name="Ссылка", blank=False, default='')
    has_subcategories = models.BooleanField(default=False, verbose_name="Имеются подкатегории", blank=False)
    place = models.ForeignKey(AllVenues, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Место")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "Категорию"

class Subcategories(models.Model):
    href = models.CharField(max_length=100, verbose_name="Ссылка", blank=False, default='')

    name = models.CharField(max_length=100, verbose_name="Название подкатегории", blank=False, default='')
    img = models.ImageField(validators=[validate_image], blank=True, default='', verbose_name="Иконка",upload_to='Subcategories/')
    category_name = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=False, verbose_name="Название категории")
    prefix = models.CharField(max_length=100, verbose_name="Префикс в корзине", blank=True, default='')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Подкатегории"
        verbose_name = "Подкатегорию"

class Goods(models.Model):
    name = models.CharField(default="", verbose_name="Название товара", blank=False, max_length=100)
    subcategory_name = models.ForeignKey(Subcategories, on_delete=models.CASCADE, blank=False, verbose_name="Название подкатегории")
    href = models.CharField(max_length=100, verbose_name="Ссылка", blank=False, default='')
    img = models.ImageField(validators=[validate_image], default='', verbose_name="Картинка", blank=False,upload_to='Goods/')
    price = models.PositiveIntegerField(default=0, verbose_name="Цена товара", blank=False)
    info = models.TextField(verbose_name="Информация", blank=True, default='')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Товары"
        verbose_name = "Товар"





admin.site.register(Team, teamsAdmin)

class FilterForGoods(admin.SimpleListFilter):
    title = u'Подкатегории'
    parameter_name = 'subcategory_name'

    def lookups(self, request, model_admin):
        subcat_id = [subcat.id for subcat in Subcategories.objects.all()]
        subcat_name = [subcat.name for subcat in Subcategories.objects.all()]
        return_all = []
        for f in map(lambda x, y: (x, y), iter(subcat_id), iter(subcat_name)):
            return_all.append(f)
        return tuple(return_all)

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(subcategory_name=self.value())
        else:
            return queryset

class goodsAdmin(admin.ModelAdmin):
    model = Goods
    list_display = ['name', 'subcategory_name', 'price', 'info']
    fields = ['name', 'subcategory_name', 'img', 'price', 'info']
    actions = ['change_hrefs']

    def change_hrefs(self, request, queryset):
        for item in queryset:
            item.href += "_" + item.subcategory_name.category_name.place.href
            item.save()

    change_hrefs.short_description = "Изменить ссылки v2.0"

    def save_model(self, request, obj, form, change):
        obj.href = obj.name.replace(' ', '')
        obj.save()

    list_filter = (FilterForGoods,)

admin.site.register(Goods, goodsAdmin)
