from constants import ENV

class RoutesLogin():
    def __init__(self) -> None:
        pass

    def render(self):
        template = ENV.get_template("login.html")
        data: dict = \
            {
                "title": "Connexion",
            }
        content = template.render(data)
        
        return content