from fabric.api import run

def install_app():
	run('sudo git clone https://github.com/josejapch/proyectoIV1617.git')
	run('cd proyectoIV1617 && sudo pip install -r requirements.txt')
	run('sudo python proyectoIV1617/manage.py makemigrations')
	run('sudo python proyectoIV1617/manage.py migrate')

def app_up():
	run('sudo python proyectoIV1617/manage.py runserver 0.0.0.0:80')

def test_app():
	run('python proyectoIV1617/manage.py test')

def app_down():
	run('sudo pkill python')

def delete_app():
	run('sudo rm -Rf proyectoIV1617')
