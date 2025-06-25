## Installation
Currently in Alpha, you must clone and install dependencies (in project.toml) from package manager of choice 
#### Getting the Repository

1. Clone the Project:
	- get command from green Code button above repository
	- or `git clone https://github.com/Welxi/HePYaestus.git`

2. Move to Folder Created

3. create a [virtual environment](https://docs.python.org/3/library/venv.html) and set your console to use it. This will depend on Operating System and Python installation

4. point package manager to the pyproject.toml
    - `uv sync`
    - `pip install pyproject.toml --extra dev` 

You should be able to run `pytest` to run tests and explore the project. If you run into any probelms please open an Issue on the GitHub