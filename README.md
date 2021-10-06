Django starter template
=====================

My Django starter template. Going to change a little from time to time. But even now it saves a lot of time!

**Install**
```
mkdir new_project
cd new_project
python3 -m venv venv
source venv/bin/activate
mkdir src
cd src
git clone https://github.com/defenitionofreal/django-starter-template.git
pip install -r requirements.txt
```

Generate random secret key - https://djecrety.ir/

Or do something like this:
```
from django.core.management.utils import get_random_secret_key  
get_random_secret_key()
```

**In .gitingore dont forget to uncomment .env, local.py and media !!!**
