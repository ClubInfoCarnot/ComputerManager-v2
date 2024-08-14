import sanic
import sanic.response
import dotenv
from pages.index import RoutesIndex
#from sanic_dispatcher import SanicDispatcherMiddlewareController

dotenv.load_dotenv(".env")

app = sanic.Sanic(name="ComputerManager-v2")

@app.route('/')
async def index(request) -> sanic.HTTPResponse:
    index = RoutesIndex()
    return sanic.response.html(index.render())

# Base route for CSS files delivery
@app.route(name='/styles/<filename>', uri='/styles/<filename>')
async def styles(request, filename) -> sanic.HTTPResponse:
    return await sanic.response.file(f'styles/{filename}')

# Base route for JS files delivery
@app.route(name='/js/<filename>', uri='/js/<filename>')
async def js(request, filename) -> sanic.HTTPResponse:
    return await sanic.response.file(f'js/{filename}')

# Base route for image files delivery
@app.route(name='/img/<filename>', uri='/img/<filename>')
async def img(request, filename) -> sanic.HTTPResponse:
    return await sanic.response.file(f'img/{filename}')

# Base route for content files delivery (like PDF files, custom created img, etc.)
@app.route(name='/content/<filename>', uri='/content/<filename>')
async def content(request, filename) -> sanic.HTTPResponse:
    return await sanic.response.file(f'content/{filename}')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, workers=4, access_log=True)