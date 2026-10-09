from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import AccessEvent

class MonitorTests(TestCase):
    def setUp(self):
        AccessEvent.objects.create(
            created_at=timezone.now(), username='admin.vdag', ip_address='192.168.69.10',
            vm_name='pay-01', device='VNC', decision='ALLOW',
            reason='Доступ разрешён политикой', gateway='HV-01',
        )

    def test_dashboard(self):
        result = self.client.get(reverse('monitor:dashboard'))
        self.assertEqual(result.status_code, 200)
        self.assertContains(result, 'VDAG')
        self.assertContains(result, 'pay-01')

    def test_stats(self):
        result = self.client.get(reverse('monitor:statistics'))
        self.assertEqual(result.status_code, 200)
        self.assertContains(result, 'Статистика')

    def test_filter_denied(self):
        result = self.client.get('/?decision=DENY')
        self.assertNotContains(result, 'admin.vdag')

    def test_requirements(self):
        self.assertEqual(self.client.get('/requirements/').status_code, 200)
