import web
import user_handler as uh
import time


urls = (
  '/','Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        return render.index(mensaje = '')


    def POST(self):
        
        form = web.input(nameradio="Temp", pwd = 'Temp')
        
        if(not uh.check_user(form.nameradio, form.pwd)):
            return render.index(mensaje = '(La contrasena es incorrecta)')
        else:    
            return  render.respuesta(amigo=uh.give_secret_santa(form.nameradio))

        
     

if __name__ == "__main__":
    app.run()