# This is a backend website for feel free

Installation guide for MAC user
-----------------------------------------

1. Pull down the source code
git clone https://github.com/cchuang6/feel_free_site.git

2. Install Anaconda
http://continuum.io/downloads

3. Create a virtual env
$ conda create -n feel_free django

4. Activate the virtualenv
$ source activate feel_free

5. Install depdendencies for your virtual env
pip install -r requirement.txt

6. Create a database
python manage.py createdb

6. Run it
python manage.py runserver

