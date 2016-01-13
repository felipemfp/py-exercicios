# Implementar uma aplicação Web com uma saudação dependente do horário
# (exemplos: “Bom dia, são 09:00.”, “Boa tarde, são 13:00.” e “Boa noite, são 23:00.”)

import  time
import cherrypy

class Root(object):
    @cherrypy.expose
    def index(self):
        hours = "{:02}:{:02}".format(time.localtime().tm_hour, time.localtime().tm_min)
        if "06:00" < hours <= "12:00":
            return "Bom dia! São {}.".format(hours)
        elif "12:00" < hours <= "18:00":
            return "Boa tarde! São {}.".format(hours)
        else:
            return "Boa noite! São {}.".format(hours)

cherrypy.quickstart(Root())