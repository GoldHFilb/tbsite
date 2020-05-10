from django.db import models

class Article(models.Model):
    short_name = models.CharField(max_length=24)                    # коротке ім'я товару (артикулу)
    full_name = models.CharField(blank=True, max_length=255)        # повне найменування товару
    t_mass_per_gallon = models.FloatField(default=0, blank=True)            # вага галону (кг)
    t_expence = models.FloatField(default=0, blank=True)                    # витрати (м.кв./гал)
    t_binding = models.CharField(blank=True, max_length=24)                 # в'яжуче
    t_dry_remainder = models.CharField(blank=True, max_length=24)           # сухий залишок
    t_luster_degree = models.CharField(blank=True, max_length=24)           # ступінь блиску
    t_solvent = models.CharField(blank=True, max_length=24)                 # розчинник
    t_drying_time = models.CharField(blank=True, max_length=36)             # час висихання
    t_packaging = models.CharField(blank=True,max_length=36)                # упаковка
    t_price = models.FloatField(default=0, blank=True)                      # ціна
    content = models.TextField(blank=True)                                  # опис товару
    created_at = models.DateTimeField(auto_now_add=True)                    # дата створення запису
    updated_at = models.DateTimeField(auto_now=True)                        # дата останнього редагування
    small_photo = models.ImageField(blank=True, upload_to='images/%Y/%m/')  # маленьке зображення
    big_photo = models.ImageField(blank=True, upload_to='images/%Y/%m/')    # велике зображення
    publicate = models.BooleanField(auto_created=False)                     # публікувати чи ні?

    def __str__(self):
        return self.short_name
