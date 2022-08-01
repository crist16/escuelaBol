
from flask import Flask, send_from_directory,request
from Helpers.helper import generarPdf
from os import getcwd
from datetime import datetime
import time
from routes.files import routes_files
from docx2pdf import convert

mesesDic = {
    "01":'Enero',
    "02":'Febrero',
    "03":'Marzo',
    "04":'Abril',
    "05":'Mayo',
    "06":'Junio',
    "07":'Julio',
    "08":'Agosto',
    "09":'Septiembre',
    "10":'Octubre',
    "11":'Noviembre',
    "12":'Diciembre'
}

def obtenerFechaActual():
    fecha = datetime.now()
    diaHoy = fecha.strftime("%d")
    mesHoy = fecha.strftime("%m")
    yearHoy = fecha.strftime("%Y")
    fechaCompletaDeHoy = {
        "dia" : diaHoy,
        "year" : yearHoy
    }
    for mes in  mesesDic:
        if mes == mesHoy:
            fechaCompletaDeHoy["mes"] = mesesDic[mes]
    return fechaCompletaDeHoy

app = Flask(__name__)
PATH_FILE_OUTPUT = getcwd() + "/Outputs"
content = {
    "nombreEstudiante": "Cristobal",
    "cedulaEstudiante": "19762932",
    "apellidoEstudiante" : "Castro",
    "ciudadNacimiento": "Cumana",
    "diaNacimiento": "05-05-1991",
    "mesNacimiento": "Mayo",
    "gradoCurso": "Tercer",
    "literal": "A",
    "periodoEscolar": "2022-2023",
    "gradoPromovido": "Cuarto",
    "nivelPromovido": "Basica",
    "diaExpedicion": "13",
    "mesExpedicion": "Julio",
    "yearExpedicion": "2022"

}



#app.register_blueprint(routes_files)



@app.route('/')
def hello_world():  # put application's code here

    return  "Hello world"

@app.post(f"/constancia/prosecucion")
def exportarProsecicion():
    fechaActual = obtenerFechaActual()
   # print(fechaActual)
    valores = request.get_json()
    valores["diaExpedicion"] = fechaActual["dia"]
    valores["mesExpedicion"] = fechaActual["mes"]
    valores["yearExpedicion"] = fechaActual["year"]
    name_file = generarPdf(valores)
    print(name_file)
    return send_from_directory(PATH_FILE_OUTPUT,path=name_file, as_attachment=True)





if __name__ == '__main__':
    app.run(debug=True,port=4000)
