# Ax Technology `test` task
A `RESTfull API` service in Python that will provide CRUD operations for working with a database containing user information.

### To launch the application, run the command
```bash
docker-compose up --build
```
or

---
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
```
----

### Go to link in localhost
[http://127.0.0.1:8009/docs#/](http://127.0.0.1:8009/docs#/)


### Tests
I used pytest with `conftest.py` for testing API routers

```commandline
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
- [ ] Поиск пользователя по имени

---
#### Дополнительные требования:
- [ ] Добавьте возможность фильтрации и сортировки пользователей.
- [ ] Реализуйте аутентификацию пользователей с использованием JWT.
- [x] Реализуйте механизм логирования для отслеживания ошибок.

#### Оценка:
- [x] Качество исходного кода
- [x] Соответствие требованиям
- [x] Полнота и корректность тестов. `pytest`
- [x] Стиль кодирования и соблюдение стандартов: `DONE` with `black`
- [x] Опыт использования: 
  - [ ] SQL
  - [x] Git
- [x] Умение разрабатывать RESTful API
