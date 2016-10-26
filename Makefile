install:
	apt-get update
	apt-get install -y python-dev
	apt-get install -y python-pip

install-requirements:
	pip install -r requirements.txt

test:
	python manage.py test

