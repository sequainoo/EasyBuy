source ./venv/bin/activate
export EASYBUY_MYSQL_USER=easybuy_dev EASYBUY_MYSQL_PWD=easybuy_pwd MYSQL_HOST=localhost EASYBUY_MYSQL_DB=easybuy_test_db sudo
/home/sequainoo/projects/EasyBuy/venv/bin/gunicorn --bind 0.0.0.0:5000 web_app.app:app
