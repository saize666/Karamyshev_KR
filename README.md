# VDAG Monitor — Django, Replit и GitHub

Учебная контрольная работа по дисциплине «Разработка и интеграция».
Автор: Карамышев Никита Евгеньевич, группа DevOps25-1М.

## Задача
Демонстрационный веб-компонент мониторинга обращений к виртуальным устройствам VNC и serial0. Связан с архитектурным паттерном Virtual Device Access Guard (VDAG). НЕТ реальных подключений к KVM/QEMU, Keycloak или OPA; используется синтетический журнал.

## Архитектура Django
- `vdag_site/settings.py` — конфигурация, регистрация приложения.
- `monitor/models.py` — модель события `AccessEvent`.
- `monitor/views.py` — логика трёх страниц.
- `monitor/urls.py` — маршруты.
- `monitor/templates/monitor/` — HTML-шаблоны.
- `monitor/static/monitor/css/site.css` — стили.
- `monitor/management/commands/load_demo_data.py` — генерация тестовых записей.
- `monitor/migrations/` — миграция SQLite.

