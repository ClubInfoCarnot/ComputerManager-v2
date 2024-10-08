# ComputerManager-v2
## Comment fonctionne le projet
- Dans le fichier `constants.py`:
    - ```py
        ENV = Environment(loader=FileSystemLoader("html"))
        ```
        Cette ligne permet de charger le dossier html
- Dans le fichier `main.py`:
    - ```py
        @app.route(name='/styles/<filename>', uri='/styles/<filename>')
        async def styles(request, filename) -> sanic.HTTPResponse:
            return await sanic.response.file(f'styles/{filename}')
        ```
        Le décorateur @app.route permet de paramétrer d'associer la route au chemin des ressources.
    - ```py
        @app.route('/')
        async def index(request) -> sanic.HTTPResponse:
            index = RoutesIndex()
            return sanic.response.html(index.render())
        ```
        On crée une association entre la route '/' et le fichier `index.py` qui renvoit un code html.
    - ```py
        app.run(host='0.0.0.0', port=8000, workers=4, access_log=True)
        ```
        Ici, on lance le serveur avec le port 8000.
- Dans le fichier `index.py`:
    - ```py
        class RoutesIndex():
            def __init__(self) -> None:
                pass

            def render(self):
                template = ENV.get_template("home.html")
                data: dict = \
                    {
                        "title": "Accueil",
                    }
                content = template.render(data)
                
                return content
        ```
        - On crée une classe Routes\<FileName\>
        - On crée ensuite une méthode `render()`.
        Dans cette méthode. On récupère le fichier html que l'on veut associer au fichié .py, ici `home.html`.\
        Le dictionnaire `data` contient l'ensemble des variables déclarés dans le fichier .html. \
        La variable `content` contient le code html modifié avec les bonnes valeurs. \
        Et enfin, on renvoit le code html modifié.

## Comment déclarer des variables dans le fibhier .html ?
Pour créer des "variables" dans le fichier html. Il faut entourer de deux paires de crochets le nom de sa variable de la sorte : `{{ nom_de_ma_variable }}`. \
Exemple avec un fichier .html et le contenu du dictionnaire `data` dans le fichier .py:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body>
    <p>{{ text }}</p>
</body>
</html>
```
Fichier .html
```py
data: dict = \
    {
        "title": "Titre de ma page",
        "text": "Voici le texte que je souhaite afficher sur ma page"
    }
```
Fichier .py \
\
Résultat: \
![Résultat](./img/result.png)
## Créer du contenu pour le site
Pour créer du contenu à ajouter sur le site, il vous suffit juste de créer les fichiers .html dans le dossier `html`. \
Les fichiers .css dans le dossier `styles`. \
Les fichiers .js dans le dossier `js`. \
Les images dans le dossier `img`.\
Et enfin, les fichiers .py qui relient les pages html aux routes dans le dossier `pages`.