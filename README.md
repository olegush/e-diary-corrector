# Корректор школьного электронного дневника

Данный скрипт иллюстрирует возможности работы с [Django ORM](https://tutorial.djangogirls.org/en/django_orm/) и содержит три функции, корректирующие [данный](https://github.com/devmanorg/e-diary/) электронный дневник для конкретного ученика. Первая функция исправляет оценки, вторая - удаляет замечания, третья - добавляет похвалу учителя по указанному предмету.


# Запуск
1. Скачайте [репозиторий](https://github.com/devmanorg/e-diary/) с электронным дневником.

2. Установите виртуальное окружение:
```bash
virtualenv virtualenv_folder_name
```

активируйте его:
```bash
source virtualenv_folder_name/bin/activate
```

и установите зависимости из **requirements.txt**:
```bash
python -m pip install -r requirements.txt
```

3. Создайте базу данных:
```bash
python3 manage.py migrate
```

4. Запустите сервер:
```bash
python3 manage.py runserver
```
и откройте сайт в браузере сайт дневника http://127.0.0.1:8000

5. Скачайте архив БД и распакуйте его рядом с файлом **manage.py**.

6. Там же создайте файл **.env** и добавьте в него переменные окружения: `DEBUG` — дебаг-режим, `SECRET_KEY` — секретный ключ проекта, `DATABASE_NAME` — путь до базы данных, например: `schoolbase.sqlite3`.

7. Обновите сайт http://127.0.0.1:8000 и убедитесь, что данные отображаются.

8. Cкачайте файл **fix_scripts.py** и отредактируйте константы:
```python
MARKS_TO_FIX = [1, 2, 3] # Оценки на исправление (одна или несколько)
NEW_MARKS = [4, 5] # Новые оценки (одна или несколько, выбираются случайным образом)
FULL_NAME = 'Имя Фамилия' # Для кого вносить исправления
SUBJECT_FOR_COMMENDATION = 'Предмет' # Предмет для добавления похвалы от учителя, дата урока выбирается случайным образом
COMMENDATIONS = ['Похвала1', 'Похвала2'...] # Список из которого случайным образом выбирается похвала
```

9. Получите ID ученика: Зайдите на сайт дневника, и найдите страницу нужного ученика. Число в конце адресной строки браузера это и есть ID.

10. Запустите терминал и консоль `python3 manage.py shell`. Скопируйте весь код из **fix_scripts.py**, вставьте в консоль и нажмите Enter.

11. Найдите учетную запись ученика в базе данных по имеющемуся ID:
```python
>>> schoolkid = Schoolkid.objects.filter(id=ID)[0]
```
Вы можете искать по другим критериям, например ФИО. Главное - получить одну единственную учетную запись. Для полной уверенности распечатайте ее:
```python
>>> print(schoolkid)
```

12. Вызовите нужные функции:
```python
>>> fix_marks(schoolkid, MARKS_TO_FIX, NEW_MARKS)
>>> remove_chastisements(schoolkid)
>>> create_commendation(schoolkid, SUBJECT_FOR_COMMENDATION)
```


# Цели проекта

Код создан в учебных целях в рамках учебного курса по веб-разработке - [dvmn.org](https://dvmn.org)
