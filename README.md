## saber-build-system
### Тестовое задание:
[ТЗ Python.docx](https://github.com/valeriyaduran/saber-build-system/files/13406893/Python.docx)

### Установка и запуск сервиса:
Предварительные условия:
Должен быть запущен docker daemon
1) Cклонировать репозиторий: git clone https://github.com/valeriyaduran/saber-build-system.git
2) Поднять сервис: из рабочей директории проекта необходимо в терминале ввести следующую команду: docker compose up или sudo docker compose up (в зависимости от наличия соответствующих permissions)


### Работа с сервисом:
Билды и таски расположены в директории "builds".

Для получения по названию билда списка задач, отсортированных с учетом их зависимостей, необходимо отправить POST запрос, содержащий имя билда.

**Пример запроса**:
```
curl --location 'http://0.0.0.0:8080/get_tasks' \
--header 'Authorization: <API_KEY>' \
--header 'Content-Type: application/json' \
--data '{"build": "front_arm"}'
```
**Пример ответа**:
```
["build_lime_golems", "map_gray_goblins", "design_olive_goblins", "build_teal_goblins", "build_silver_goblins", "create_lime_goblins", "write_teal_witches", "enable_white_golems", "coloring_silver_golems", "train_maroon_golems", "upgrade_aqua_centaurs", "map_fuchsia_centaurs", "read_lime_centaurs", "create_blue_centaurs", "bring_purple_humans", "write_yellow_humans", "read_maroon_humans", "design_blue_humans", "write_gray_humans", "train_fuchsia_orcs", "design_maroon_golems", "write_navy_golems", "design_yellow_golems", "read_white_leprechauns", "coloring_fuchsia_leprechauns", "write_maroon_humans", "upgrade_black_humans", "create_green_humans", "upgrade_silver_humans", "map_yellow_humans", "coloring_black_goblins", "design_maroon_witches", "design_teal_golems", "design_yellow_centaurs", "map_purple_humans", "read_aqua_orcs", "read_gray_golems", "train_white_leprechauns", "upgrade_gray_humans"]
```
*Примечание: API_KEY находится в файле .env (пример расположен в репозитории в файле .env.example)*

**Примечание2: сортировка тасок реализована вручную, но вообще можно воспользоваться библиотекой graphlib (создать объект класса graphlib.TopologicalSorter(graph) и вызвать метод static_order())***

### Тестирование:
Тесты расположены в директории "tests".    
Тесты реализованы на классы TaskManager и TopologicalSorting, которые отвечают за работу с билдами и тасками и реализацию сортировки.

#### Запуск тестов:
Для запуска тестов из рабочей директории проекта необходимо в терминале ввести следующую команду:
```
python -m unittest tests/test_task_sorting.py
```
#### Тестирование стиля кода:
Для тестирования кода на стилистические ошибки и нарушения различных стандартов необходимо из рабочей директории проекта в терминале ввести следующую команду:
```
flake8 .
```

### Cтек технологий проекта:
- python 3.10.7
- fastapi
- pyyaml
- docker
- flake8
- pipenv
  










