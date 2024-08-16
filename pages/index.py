from constants import ENV

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