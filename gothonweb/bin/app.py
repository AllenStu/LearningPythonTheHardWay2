import web

urls = ('/','Index')
app = web.application(urls,globals())
render = web.template.render('templates/')

class Index(object):

    def __init__(self):
        self.var1 = ""

    def GET(self):
        greeting = "Hello World"
        # return greeting
        return render.index(greeting=greeting)

    # def POST(self):
    #     sampleWord = "Hi there sam!"
    #     return sampleWord

if __name__ == "__main__":
    app.run()


# at the root, run python bin/app.py