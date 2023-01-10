import pytest
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", MainHandler),
])

@pytest.fixture
def app():
    return application

# Works
@pytest.mark.gen_test
def test_hello_world(http_client, base_url):
    response = yield http_client.fetch(base_url)
    assert response.code == 200

# Does not work
@pytest.mark.gen_test
async def test_tornado(http_client):
    response = await http_client.fetch('http://www.tornadoweb.org/')
    assert response.code == 200