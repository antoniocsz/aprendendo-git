# Como usar o Flask Action

Primeiro é necessário fazer a instalação do vitualenv para criar um ambiente:

``` sh
$ sudo pip install virtualenv
```

Após a instalação virtualenv, crie o ambiente e ative-o:

``` sh
$ virtualenv nome_do_seu_ambiente
$ source nome_do_seu_ambiente/bin/activate
```
Caso queria desativar o ambiente de desenvolvimento:

``` sh
$ deactivate
```

Depois de ativar o ambiente instale o Flask e o Flask Action:

``` sh
$ pip install Flask
$ pip install Flask-Actions
```

Para criar um projeto com Flask Action faça:
``` sh
$ flask_admin.py startproject nome_do_projeto
```

Seu projeto será criado com o seguinte formato:
``` sh
nome_do_projeto/
    nome_do_projeto
        __init__.py
        static
            style.css
        template
            layout.html
        views
            frontend.py
            frontend.pyc
            __init__.py
            __init__.pyc
    manage.py
    settings.py
```
Para executar:
``` sh
$ python manage.py runserver
```
