from django.db import models

class AccessEvent(models.Model):
    class Decision(models.TextChoices):
        ALLOW = 'ALLOW', 'Разрешено'
        DENY = 'DENY', 'Запрещено'
        CLOSE = 'CLOSE', 'Закрыто'

    created_at = models.DateTimeField('Дата и время')
    username = models.CharField('Пользователь', max_length=60)
    ip_address = models.GenericIPAddressField('IP-адрес')
    vm_name = models.CharField('Виртуальная машина', max_length=50)
    device = models.CharField('Устройство', max_length=30)
    decision = models.CharField('Решение', max_length=10, choices=Decision.choices)
    reason = models.CharField('Причина', max_length=150)
    gateway = models.CharField('Шлюз', max_length=30, default='HV-01')

    class Meta:
        ordering = ['-created_at', '-id']
        verbose_name = 'Событие доступа'
        verbose_name_plural = 'События доступа'

    def __str__(self):
        return f'{self.username} — {self.vm_name}: {self.decision}'
