from flask import Blueprint, send_from_directory
from os import getcwd
from Helpers.helper import generarPdf
from responses.response_json import response_json

content = {
    "nombreEstudiante": "Cristobal",
    "cedulaEstudiante": "19762932",
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

routes_files = Blueprint("routes_files",__name__)

PATH_FILE_OUTPUT = getcwd() + "/Outputs"


@routes_files.get(f"/download/<string:{generarPdf(content)}>")
def download_file(name_file):
    return send_from_directory(PATH_FILE_OUTPUT,path=name_file, as_attachment=True)