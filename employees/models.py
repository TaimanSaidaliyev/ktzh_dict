from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        abstract = True


class Position(TimeStampedModel):
    serial_number = models.PositiveIntegerField(verbose_name="Порядковый номер", blank=True, null=True)
    name = models.CharField(max_length=100, unique=True, verbose_name="Название должности")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['serial_number']
        verbose_name = "Должность"
        verbose_name_plural = "Должности"


class Department(TimeStampedModel):
    serial_number = models.PositiveIntegerField(verbose_name="Порядковый номер", blank=True, null=True)
    name = models.CharField(max_length=100, unique=True, verbose_name="Название департамента")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['serial_number']
        verbose_name = "Департамент"
        verbose_name_plural = "Департаменты"


class EmployeeStatus(models.Model):
    serial_number = models.PositiveIntegerField(unique=True, blank=True, null=True, verbose_name="Порядковый номер")
    name = models.CharField(max_length=100, unique=True, verbose_name="Статус сотрудника")
    color = models.CharField(max_length=7, default='#000000', verbose_name="Цвет")  # Добавляем поле цвета

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['serial_number']
        verbose_name = "Статус сотрудника"
        verbose_name_plural = "Статусы сотрудников"


class Division(TimeStampedModel):
    serial_number = models.PositiveIntegerField(verbose_name="Порядковый номер", blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name="Название отдела")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Департамент", related_name="divisions")

    def __str__(self):
        return f"{self.name} (Dept: {self.department.name})"

    class Meta:
        ordering = ['serial_number']
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"
        unique_together = ('department', 'serial_number')


class Employee(TimeStampedModel):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Отчество")
    birth_date = models.DateField(verbose_name="Дата рождения")
    serial_number = models.PositiveIntegerField(verbose_name="Порядковый номер", blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name="Должность")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Департамент")
    division = models.ForeignKey(Division, on_delete=models.CASCADE, verbose_name="Отдел", blank=True, null=True)
    status = models.ForeignKey(EmployeeStatus, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Статус сотрудника")
    office_coordinates = models.CharField(max_length=255, verbose_name="Координаты офиса")
    work_phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Рабочий телефон")
    mobile_phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Мобильный телефон")
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фотография', blank=True)
    fired = models.BooleanField(default=False, verbose_name='Уволен')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.position})"

    class Meta:
        ordering = ['serial_number']
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


@receiver(pre_save, sender=Position)
@receiver(pre_save, sender=Department)
@receiver(pre_save, sender=EmployeeStatus)
@receiver(pre_save, sender=Employee)
@receiver(pre_save, sender=Division)
def ensure_serial_number(sender, instance, **kwargs):
    if instance.serial_number is None:
        last_serial = sender.objects.all().aggregate(models.Max('serial_number'))['serial_number__max']
        if last_serial is None:
            last_serial = 0
        instance.serial_number = last_serial + 1
