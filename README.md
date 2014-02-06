NewDjango
=========
my app on heroku
now added on another machine
auto store

=======================================
importand links to usefull to stat up
=======================================
1: Django heroku setup: https://devcenter.heroku.com/articles/getting-started-with-django

2: Django full set up : http://www.deploydjango.com/heroku/index.html

3: startup Django : https://docs.djangoproject.com/en/1.6/intro/tutorial01/ 

4: Eclicps setup : http://techs.studyhorror.com/how-develop-django-project-pydev-eclipse-i-12

5: Mysql and other setup :http://www.realpython.com/blog/python/migrating-your-django-project-to-heroku/#.UvN4Xd_FtTM

========================================
important command 
========================================
1:for point virtual enviroment : $source venv/bin/activate

2:For satisfy system requiremnt: : $pip install -r requirements.txt

3:run djangocode : $python manage.py runserver (optional)ip:port

4:git command required : ---
 			
                         i) $git status # view changes

                        ii) $git add path/to/file # add the file changes done

                       iii) $git commit -m "message" # add comit messge and now ready

                        iv) $git push origin master # push on to the git hub repo    

5: push on heroku : $git push heroku master

6: oprn it on default browser : $heroku open 

============================================
git password store method
============================================

1: git config --global credential.helper store # it store password ask onlr once for first commit

2: git config --global credential.helper cache #for some period of time 15 min

3: git config --global credential.helper 'cache --timeout=600' # for time interval for seconds 600=10 mins

4: t config remote.origin.url https://username:password@github.com/gtrdotmcs/NewDjango.git
