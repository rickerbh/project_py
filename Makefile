setup:
	pip3 install nose nosy

test:
	python3 setup.py test

watch:
	nosy
