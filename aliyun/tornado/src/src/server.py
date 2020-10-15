import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        rid = self.request.headers.get('x-fc-request-id',None)
        print("FC Invoke Start RequestId: " + str(rid));

        # your logic
        self.write("GET: Hello world")

        print("FC Invoke End RequestId: " + str(rid));

    def post(self):
        rid = self.request.headers.get('x-fc-request-id',None)
        print("FC Invoke Start RequestId: " + str(rid));

        # your logic
        self.write("GET: Hello world")

        print("FC Invoke End RequestId: " + str(rid));

def make_app():
    return tornado.web.Application([
        (r"/.*", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    port = os.environ.get("FC_SERVER_PORT", "9000")
    app.listen(int(port))
    tornado.ioloop.IOLoop.current().start()