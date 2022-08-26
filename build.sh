#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
echo "from django.contrib.auth import get_user_model;
from lawapp.users.models import Profile;
from lawapp.levels.models import Level;
level = Level(description='Administrador');
level.save();
User = get_user_model(); 
user = User.objects.create_superuser('tech', 'fhersa@gmail.com', 'pepito911');
user.save();
profile = Profile(user=user, description='Admin', level=level);
profile.save();
" | python manage.py shell
