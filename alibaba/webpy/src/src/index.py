import web
 
urls = (
    '/(.*)', 'hello'
)
 
app = web.application(urls, globals())
 
class hello:
    def GET(self, name):
        return 'Hello, ' + name if name else 'world'+ '!'
 
if __name__ == "__main__":
    app.run()