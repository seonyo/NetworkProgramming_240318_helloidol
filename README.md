# helloidol

---

1. startproject helloidol
   1. python -m pip install django~=4.2 (4.2의 최신 버전 설치)
   2. django-admin startproject _helloidol_ .
   3. [python mange.py migrate]
   4. python manage.py runserver
   

2. startapp _playground_
   1. Terminal
      1. python manege.py startapp _playground_
   2. helloidol/settings.py
      1. 'playgound', in INSTALLED_APPS
   

3. playground/
   - 정보 전달: urls -> views -> (models ->) templates
   - 코드 작성: (models ->)views -> templates -> urls
   1. views
      1. say_ _hello()_
      2. say_ _hello_html()_
   2. urls
      1. _playground/hello/_ -> _say_hello_
      2. _playground/hello_html/_ -> _say_hello_html()_
   3. templates/playground/
      1. hello.html
   4. helloiols/
      1. urls, playgrounds/urls
         1. _playground/_ -> _hello/_ -> _say_hello()_
         2. _playground/_ -> _hello_html/_ -> _say_hello_html()_
         3. 