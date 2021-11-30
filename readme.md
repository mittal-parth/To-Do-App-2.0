# WEC NITK GDSC Task ID: Progressive Web Application with OAuth

A To-Do App with OAuth that can be installed as a PWA. It supports media and Speech to text input features as well.

https://user-images.githubusercontent.com/76661350/143526700-4fbf524e-33d1-4e70-b3ec-fd64835dc9c5.mp4


<br>
<h2>Installation Guide</h2>
<h3>Virtual Enironment</h3>

`pip install virtualenvwrapper-win`<br>
`mkvirtualenv test` &nbsp; _test = name of virtual env_

<br>
<h3>Install required packages:</h3>

`pip install -r requirements.txt`<br>
_After ensuring that we are in a virtual environment (If not, use `workon test`)_

<h3>To run project:</h3>

`python manage.py makemigrations` <br>
`python manage.py migrate` <br>
`python manage.py runserver`<br>
<p>Visit development server at http://127.0.0.1:8000 </p>
<br>
<h3>Create Super user:</h3>

`python manage.py createsuperuser`
<p>Enter desired credentials</p>
<br>

<h3>To use emailing features (optional)</h3>
<p>Note: It currently uses Gmail's smtp <br>
Head to <a href="https://github.com/mittal-parth/To-Do-App-2.0/blob/main/todo_class_based/settings.py#L170-L171">settings.py </a> <br>
Enter the details at EMAIL_HOST_USER and EMAIL_HOST_PASSWORD <br>
Follow <a href="https://devanswers.co/allow-less-secure-apps-access-gmail-account/">this</a> to enable sending mails via gmail</p>
<br>

<h3>Admin Site:</h3>

http://127.0.0.1:8000/admin

<br>
<h2>Tech Stack</h2>
<code><img height="40" width="40" src="https://img.icons8.com/color/48/000000/python--v1.png" alt="Python"></code>
<code><img height="40" width="40" src="https://user-images.githubusercontent.com/76661350/143919769-d61dd74a-ef98-49db-b1d0-781cb2df501c.png"></code>
<code><img height="45" width="40" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/html/html.png" alt="HTML"></code>
<code><img height="36" width="40" src="https://cdn.iconscout.com/icon/free/png-256/css-131-722685.png" alt="CSS"></code>
<code><img height="36" width="40" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/javascript/javascript.png" alt="Javascript"></code>
<br>
<br>

<h2>Implemented Features</h2>
<ul>
    <li>User Authentication with OAuth</li>
    <li>Progressive Web Application functionality</li>
    <li>Speech to Text Input</li>
    <li>Image upload using both file system and camera</li>
    <li>Create, Read, Update and Delete Tasks</li>
    <li>Search for Tasks</li>
</ul>

<br>
<br>
<h2>References:</h2>
<a href="https://github.com/silviolleite/django-pwa">Django PWA</a><br>
<a href="https://django-allauth.readthedocs.io/en/latest/">Django All Auth Documentation</a><br>
<a href="https://stiltsoft.com/blog/2013/05/google-chrome-how-to-use-the-web-speech-api/">Using the Web Speech API</a><br>
<a href="https://www.youtube.com/watch?v=llbtoQTt4qw">Django Class Based Views ToDo</a>



