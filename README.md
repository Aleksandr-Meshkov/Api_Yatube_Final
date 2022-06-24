# Как запустить проект
Клонировать репозиторий и перейти в него в командной строке:

git@github.com:Aleksandr-Meshkov/api_final_yatube.git

cd api_final_yatube

Cоздать и активировать виртуальное окружение:

python -m venv env

source venv/Scripts/activate

Установить зависимости из файла requirements.txt:

pip install -r requirements.txt

Выполнить миграции:

python manage.py migrate

Запустить проект:

python3 manage.py runserver
