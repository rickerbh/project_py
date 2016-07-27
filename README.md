# Base Python Project

Here's a base setup for a python project. 

- Get the source: `git clone https://github.com/rickerbh/project_py.git`
- Edit `setup.py` and change the name/packages fields for your project. 
- Rename `MY_PROJECT` to the name of your project
- Tests go in `tests`
- Code goes in your renamed `MY_PROJECT`

The makefile has 3 targets.

- `make setup` will install dependencies with `pip3`
- `make test` will run nose and execute the tests
- `make watch` will run nosy and watch for tests/source changes, and rerun tests automatically
