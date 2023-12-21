## build-system
### Description:
Build system based on sorting binding tasks according to their dependencies.

### Service installation and launching:
Preconditions:
- Python must be installed
- Docker daemon must be running
1) Clone the repository: git clone https://github.com/valeriyaduran/build-system.git
2) Launch the service: from the project working directory enter the following command in the terminal: 'docker compose up' or 'sudo docker compose up' (depending on permissions)


### Working with the service:
Builds and tasks are stored in "builds" directory.

To get a list of tasks by build name, sorted based on their dependencies, you need to send a POST request containing the build name.

**Request example**:
```
curl --location 'http://0.0.0.0:8080/get_tasks' \
--header 'API-Key: <API_KEY>' \
--header 'Content-Type: application/json' \
--data '{"build": "front_arm"}'
```
**Response example**:
```
["build_lime_golems", "map_gray_goblins", "design_olive_goblins", "build_teal_goblins", "build_silver_goblins", "create_lime_goblins", "write_teal_witches", "enable_white_golems", "coloring_silver_golems", "train_maroon_golems", "upgrade_aqua_centaurs", "map_fuchsia_centaurs", "read_lime_centaurs", "create_blue_centaurs", "bring_purple_humans", "write_yellow_humans", "read_maroon_humans", "design_blue_humans", "write_gray_humans", "train_fuchsia_orcs", "design_maroon_golems", "write_navy_golems", "design_yellow_golems", "read_white_leprechauns", "coloring_fuchsia_leprechauns", "write_maroon_humans", "upgrade_black_humans", "create_green_humans", "upgrade_silver_humans", "map_yellow_humans", "coloring_black_goblins", "design_maroon_witches", "design_teal_golems", "design_yellow_centaurs", "map_purple_humans", "read_aqua_orcs", "read_gray_golems", "train_white_leprechauns", "upgrade_gray_humans"]
```
*Note: API_KEY stored in .env (you can check .env.example)*

### Testing:
Tests are stored in "tests" directory.    
Tests are implemented for TaskManager and TaskSorting classes as well as on the app API.

#### Tests launching:
To run tests enter the following command in the terminal of 'build-system-fastapi' container:
```
export PYTHONPATH=. && pytest
```
To check test coverage enter the following command in the terminal of 'build-system-fastapi' container:
```
coverage run -m pytest
```
and to see the report:
```
coverage report -m
```
#### Test coverage report
![](/Users/valeriaduran/Desktop/Screenshot 2023-12-21 at 10.34.22.png)

#### Code style testing:
To check the code for stylistic errors and standards violations enter the following command from the project’s working directory in the terminal:
```
flake8 .
```

### Project tech stack:
- python 3.10.7
- fastapi
- pyyaml
- docker
- pytest
- coverage
- flake8
- pipenv
  











