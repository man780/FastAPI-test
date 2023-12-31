# Ax Technology `test` task
A `RESTfull API` service in Python that will provide CRUD operations for working with a database containing user information.

### To launch the application, run the command
```bash
docker-compose up --build
```
<details>
  <summary>OR</summary>

  ```bash
  python3.10 -m venv venv
  source venv/bin/activate
  ```
  install all libs dependencies
  ```bash
  pip install -r requirements.txt
  ```
  ##### then run
  ```bash
  python main.py
  pytest
  ```
</details>


### Go to link in localhost
[http://127.0.0.1:8009/docs#/](http://127.0.0.1:8009/docs#/)


### Tests
I used pytest with `conftest.py` for testing API routers

```commandline
python main.py
pytest
```
Run command above to run testing routers

---

### Сделанные работы
- [x] Docker. Dockerfile и docker-compose

### CRUD
- [x] Создание пользователя
- [x] Получение пользователя по id
- [x] Получение всех пользователей
- [x] Обновление пользователя по id
- [x] Удаление пользователя по id
- [x] Поиск пользователя по имени

---
#### Дополнительные требования:
- [x] Добавьте возможность фильтрации и сортировки пользователей.
- [ ] Реализуйте аутентификацию пользователей с использованием JWT.
- [x] Реализуйте механизм логирования для отслеживания ошибок.

#### Оценка:
- [x] Качество исходного кода `pylint`
- [x] Соответствие требованиям
- [x] Полнота и корректность тестов. `pytest`
- [x] Стиль кодирования и соблюдение стандартов: `DONE` with `black`
- [x] Опыт использования: 
  - [ ] SQL: 
    _Тут не сделал_: но есть пример [тут](https://github.com/man780/compose-django-postgres-celery-redis/blob/main/app/education/views.py) 57-строка
  - [x] Git
- [x] Умение разрабатывать RESTful API
