from flask import Flask
#from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/<nombre>")
def hola(nombre="Invitado"):
 #   nombre= request.args.get('nombre',nombre)
    context={'nombre': nombre}
    return render_template("index.html", **context)

@app.route("/imagenes")
def imagenes():
    return "Estas son las imagenes"

@app.route("/suma/<int:a>/<int:b>")
@app.route("/suma/<float:a>/<float:b>")
def sumar(a=0, b=0):
  #   return """
  #   <!doctype html>
  #   <html>
  #       <head>
  #           <title> Suma  </title>
  #           <body>
  #           <h1> {} + {} = {} </h1>
  #           </body>
  #       </head>
  #   </html>
  #   """.format(a,b,a+b)
  # #  return "{} más {} es : {}".format(a,b,a+b)

  #return render_template("suma.html",a=a,b=b)
  context={'a':a,'b':b}
  return render_template("suma.html",**context)

if __name__ == "__main__":
    app.run(debug=True)