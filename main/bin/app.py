import web
import mobius_transformations as mbt
import numpy as np
import time


urls = (
  '/','Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        return render.index()


    def POST(self):
        
        form = web.input(nameradio="1")
        
        print(form.nameradio)
        

        return  render.respuesta(amigo=form.nameradio)
     

if __name__ == "__main__":
    app.run()