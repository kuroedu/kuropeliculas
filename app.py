import web
from web import form
import datos


data = datos.Data_file()
data.data_readCliente()
data.data_readPelicula()

render = web.template.render('templates/', base = 'base')
db = web.database(dbn='mysql', db='rentas', user='root', pw='kuro')



urls = ('/','index')

data_form = form.Form(
    form.Dropdown('Cliente',data.data_campoCliente('Cliente')),
    form.Dropdown('Pelicula', data.data_campoPelicula('Pelicula')),
    form.Dropdown('Formato', ['Formato','Blueray','DVD']),
    form.Textbox("Tiempo")
      
)

class index:        
    def GET(self):
        erL = data_form 
        return render.index(erL,None,None,None,None)

    def POST(self):
        erL = data_form
        if not erL.validates():
            return render.index(erL,None,None,None,None)
        else:
            print erL.d.Cliente , erL.d.Pelicula, erL['Formato'].value, erL.d.Tiempo
            if  erL['Formato'].value == 'Blueray':         
                result=db.insert('renta', pelicula = erL['Pelicula'].value, total = int(erL.d.Tiempo) * 20 , formato= erL['Formato'].value ,tiempo=erL.d.Tiempo)
                return render.index(erL,int(erL.d.Tiempo) * 20 ,erL['Pelicula'].value, erL['Formato'].value ,erL.d.Tiempo)
            else:
                result=db.insert('renta', pelicula = erL['Pelicula'].value, total = int(erL.d.Tiempo) * 20 , formato= erL['Formato'].value ,tiempo=erL.d.Tiempo)
                return render.index(erL,int(erL.d.Tiempo) * 10 ,erL['Pelicula'].value,erL['Formato'].value ,erL.d.Tiempo)
                 


if __name__ == "__main__":
    app = web.application(urls, globals())
    web.internalerror = web.debugerror
    app.run()