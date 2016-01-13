# Implementar uma aplicação Web com um formulário que receba
# expressões Python e retorne a expressão com seu resultado.

import traceback
import cherrypy

class Root(object):

    TEMPLATE = """
<html>
    <body>
        <form action="/">
            <input type="text" name="expression" value="{}" placeholder="Expressão" />
            <input type="submit" value="Enviar">
        </form>
        <pre>{}</pre>
    </body>
</html>
    """

    @cherrypy.expose
    def index(self, expression = ""):
        out = ""
        if expression:
            try:
                out = eval(expression)
            except:
                out = traceback.format_exc()

        return self.TEMPLATE.format(expression, out)

cherrypy.quickstart(Root())