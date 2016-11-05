install:
	apt-get update
	apt-get install -y python-dev
	apt-get install -y python-pip

install-requirements:
	pip install -r requirements.txt

install-bd:
	python manage.py makemigrations
	python manage.py migrate

test:
	python manage.py test

