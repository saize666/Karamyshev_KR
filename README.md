# VDAG Monitor — Django, Replit и GitHub

Учебная контрольная работа по дисциплине «Разработка и интеграция».
Автор: Карамышев Никита Евгеньевич, группа DevOps25-1М.

## Задача
Демонстрационный веб-компонент мониторинга обращений к виртуальным устройствам VNC и serial0. Связан с архитектурным паттерном Virtual Device Access Guard (VDAG). НЕТ реальных подключений к KVM/QEMU, Keycloak или OPA; используется синтетический журнал.

## Запуск в Replit
1. Импортируйте ZIP-архив проекта с помощью `https://replit.com/import` (импорт ZIP).
2. Откройте редактор проекта, убедитесь, что есть `manage.py`, `.replit`, `start.sh`.
3. Нажмите Run. Команда `bash start.sh` создаст `.venv`, установит Django, выполнит миграции и загрузит 60 тестовых событий.
4. Откройте вкладку Webview.

## Команды для Shell
```bash
bash start.sh
```

### Проверить тесты
```bash
.venv/bin/python manage.py test monitor
```

### Наполнить данными вручную
```bash
.venv/bin/python manage.py load_demo_data
```

## Маршруты
- `/` — панель событий, фильтр по решению и ВМ.
- `/stats/` — статистика.
- `/requirements/` — требования R1–R5.

## GitHub: обязательные пункты 10–12
1. Создайте **публичный** пустой репозиторий `Karamyshev_KR` (без README и .gitignore).
2. Выполните в Shell (заменив YOUR_GITHUB_USERNAME):
```bash
git init
git branch -M main
git add .
git commit -m "Первоначальная версия VDAG Monitor"
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/Karamyshev_KR.git
git push -u origin main
```
3. Внести первое реальное изменение HTML и отправить в `main`:
```bash
# Поменяйте строку на главном шаблоне вручную или используйте команду ниже:
python3 -c "from pathlib import Path; p=Path('monitor/templates/monitor/index.html'); s=p.read_text(); s=s.replace('Панель мониторинга</h1>', 'Панель мониторинга VDAG</h1>'); p.write_text(s)"
git add monitor/templates/monitor/index.html
git commit -m "Изменение 1_Карамышев"
git push origin main
```
4. Создайте отдельную ветку и второе изменение HTML:
```bash
git switch -c vetka_Karamyshev
python3 -c "from pathlib import Path; p=Path('monitor/templates/monitor/stats.html'); s=p.read_text(); s=s.replace('Статистика доступа</h1>', 'Статистика доступа VDAG</h1>'); p.write_text(s)"
git add monitor/templates/monitor/stats.html
git commit -m "Изменение 2_Карамышев"
git push -u origin vetka_Karamyshev
```
Обязательно соедините GitHub в настройках Replit, иначе `git push` может запросить учётные данные. Для HTTPS используется токен/авторизация приложения, НЕ пароль Google.

## Архитектура Django
- `vdag_site/settings.py` — конфигурация, регистрация приложения.
- `monitor/models.py` — модель события `AccessEvent`.
- `monitor/views.py` — логика трёх страниц.
- `monitor/urls.py` — маршруты.
- `monitor/templates/monitor/` — HTML-шаблоны.
- `monitor/static/monitor/css/site.css` — стили.
- `monitor/management/commands/load_demo_data.py` — генерация тестовых записей.
- `monitor/migrations/` — миграция SQLite.

## Ограничение
Приложение является учебным макетом веб-интерфейса и не реализует настоящий Access Gateway, авторизацию OIDC/MFA, соединения с устройствами ВМ или реальные механизмы безопасности. Для реальной эксплуатации нужны отдельные требования и защитные настройки.
