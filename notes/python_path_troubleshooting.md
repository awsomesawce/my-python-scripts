# Python Path Troubleshooting

**Python** scripts can be run in many different ways.  The most simple way is to just run `python script_name.py` (or `python3 script_name.py` in Debian-based distros.).

On Windows, python3 can be installed in many different ways, and this affects how things work on the system.

An answer to this is to just use virtual environments for everything, but this can be cumbersome and confusing.

In general, virtual envs will modify PATH so that the project's python interpreter shows up first.

## Virtual Environment Implementations

Multiple tools exist for working with Python virtual environments.  These include:

- [pipx]
- [pipenv](): This tool uses Pipfile and Pipfile.lock to manage dependencies.
- [virtualenv]
- [virtualenvwrapper]
- [tox]

You can also use the tool included with the Python standard library called `venv`.  This is administered by typing `python3 -m venv`.

## Virtual Env Configuration

There exist many different configuration file types for virtual environment config.

A few examples:

- _pyproject.toml_
- _pyvenv.cfg_
- _requirements.txt_: The oldest type.
- _Pipfile_ and _Pipfile.lock_

For more information, check out the standard library venv [here](https://docs.python.org/3/library/venv.html) and [here](https://docs.python.org/3/tutorial/venv.html)
or the [pipenv docs](https://pipenv.pypa.io/en/latest/).
