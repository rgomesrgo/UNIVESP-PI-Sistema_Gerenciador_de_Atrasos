#!/bin/bash

echo "Aplicando migrações..."
python manage.py migrate

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "Criando superusuário lucas_admin..."
echo "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='lucas_admin').exists():
    User.objects.create_superuser('lucas_admin', '23213289@aluno.univesp.br', 'Univesp2025')
" | python manage.py shell
