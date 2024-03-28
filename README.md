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
      3. say_ _bye_html()_
      4. -> templates에 context 전달
   2. urls
      1. _playground/hello/_ -> _say_hello_
      2. _playground/hello_html/_ -> _say_hello_html()_
   3. templates/playground/
      1. hello.html
      2. bye.html
4. helloiols/
   1. urls, playgrounds/urls
      1. _playground/_ -> _hello/_ -> _say_hello()_
      2. _playground/_ -> _hello_html/_ -> _say_hello_html()_
      3. _playground/_ -> _byt_html/_ -> _say_bye_html()_
      
--- 

5. startapp 두산베어스
   1. Terminal
      1. python manage.py startapp 두산베어스
   2. helloidol/settings.py
      1. '두산베어스', in INSTALLED_APPS
6. 두산베어스/
   1. views
      1. show_철원()
      2. show_의지()
      3. show_수빈()
   2. templates/두산베어스/
      1. 철원.html
         1. title: 두산베어스 - 철원
         2. h1 : 두산베어스
         3. h2 : 정철원
         4. img : 정철원 프로필 사진
            1. border-radius: 50%;
      2. 의지.html
      3. 수빈.html
   3. urls
      1. 두산베어스/ -> 철원/ -> show_철원()
      2. 두산베어스/ -> 의지/ -> show_의지()
      3. 두산베어스/ -> 수빈/ -> show_수빈()