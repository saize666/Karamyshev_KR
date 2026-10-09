"""Populate a reproducible set of synthetic events for the educational demo."""
from datetime import timedelta
from random import Random
from django.core.management.base import BaseCommand
from django.utils import timezone
from monitor.models import AccessEvent

class Command(BaseCommand):
    help = 'Загрузить 60 демонстрационных событий (не реальные данные)'

    def handle(self, *args, **options):
        if AccessEvent.objects.exists():
            self.stdout.write('Данные уже существуют — повторная загрузка не требуется.')
            return
        rng = Random(25)
        start = timezone.now()
        actors = ['admin.vdag', 'operator01', 'security01', 'unknown', 'guest']
        rules = {
            'ALLOW': ['Доступ разрешён политикой', 'MFA подтверждена', 'Плановое обслуживание'],
            'DENY': ['Нет прав на ВМ', 'Не пройдена MFA', 'Недопустимое время доступа', 'Недействительный билет'],
            'CLOSE': ['Истекло время сеанса', 'Пользователь завершил сеанс', 'Права отозваны'],
        }
        rows = []
        for i in range(60):
            decision = rng.choices(['ALLOW', 'DENY', 'CLOSE'], [0.51, 0.31, 0.18])[0]
            vm = rng.choice(['pay-01', 'test-01'])
            rows.append(AccessEvent(
                created_at=start - timedelta(minutes=18 * i + rng.randint(0, 12)),
                username=rng.choice(actors),
                ip_address=f'192.168.69.{rng.randint(10, 210)}',
                vm_name=vm,
                device=rng.choice(['VNC', 'serial0']),
                decision=decision,
                reason=rng.choice(rules[decision]),
                gateway='HV-01' if vm == 'pay-01' else 'HV-02',
            ))
        AccessEvent.objects.bulk_create(rows)
        self.stdout.write(self.style.SUCCESS(f'Загружено {len(rows)} тестовых событий.'))
