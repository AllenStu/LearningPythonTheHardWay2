import web

# urls = ('/','Index')
urls = ('/hello', 'Index')

app = web.application(urls,globals())
render = web.template.render('templates/', base="layout")

class Index(object):

    def __init__(self):
        self.var1 = ""

    def GET(self):

        # Solution 1
        """
            Simply displays "Hello World" in the screen
            run python bin/app.py in the terminal (root dir)
            type in the URL: http://localhost:8080/
        """
        # greeting = "Hello World"
        # # return greeting
        # return render.index(greeting=greeting)

        # Solution 2
        """
            Displays Hello + name coming from URL
            type in the URL:
            http://localhost:8080/hello?name=Frank&greet=Hola
        """
        # form = web.input(name="Nobody")
        # # greeting = "Hello, %s" % form.name
        # greeting = "%s, %s" % (form.greet, form.name)
        # return render.index(greeting=greeting)

        # Solution 3
        """
            Displays greet + name coming from URL
            type in the URL :
            http://localhost:8080/hello?name=Frank
            Description: (1) Displays Error message (2)
        """
        # form = web.input(name="Nobody", greet=None)
        # if form.greet:
        #     greeting = "%s, %s" %(form.greet, form.name)
        #     return render.index(greeting=greeting)
        # else:
        #     return "ERROR: greet is required."

        # Solution 4
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody",greet="Hello")
        greeting = "%s , %s" % (form.greet, form.name)
        return render.index(greeting=greeting)


if __name__ == "__main__":
    app.run()


# at the root, run python bin/app.py