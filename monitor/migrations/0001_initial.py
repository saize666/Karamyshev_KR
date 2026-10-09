from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='AccessEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name='Дата и время')),
                ('username', models.CharField(max_length=60, verbose_name='Пользователь')),
                ('ip_address', models.GenericIPAddressField(verbose_name='IP-адрес')),
                ('vm_name', models.CharField(max_length=50, verbose_name='Виртуальная машина')),
                ('device', models.CharField(max_length=30, verbose_name='Устройство')),
                ('decision', models.CharField(choices=[('ALLOW', 'Разрешено'), ('DENY', 'Запрещено'), ('CLOSE', 'Закрыто')], max_length=10, verbose_name='Решение')),
                ('reason', models.CharField(max_length=150, verbose_name='Причина')),
                ('gateway', models.CharField(default='HV-01', max_length=30, verbose_name='Шлюз')),
            ],
            options={'verbose_name': 'Событие доступа', 'verbose_name_plural': 'События доступа', 'ordering': ['-created_at', '-id']},
        ),
    ]
