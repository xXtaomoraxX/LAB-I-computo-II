#importamos las librerias
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout
#importamos los widgets 
#Creamos la clase junto a sus atributos
class Ventana(QWidget):
    def __init__(self):#inicializamos la clase
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Datos Personales')#mensaje que se mostrara en la ventana de estado
        self.setGeometry(100, 100, 400, 600)#definir las dimension del tamaño de la ventana

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.datos_persona = []#crearemos el metodo para almacenar todos los datos de la persona
        etiquetas = [#recordar que son 10 datos personales de una persona 
            'Nombre Completo', 'Edad', 'Género', 'Dirección', 'Teléfono',
            'Correo Electrónico', 'Ocupación', 'Nacionalidad', 'Estado Civil', 'Hobbies'
        ]
        #con un ciclo for ejecutaremos el siguiente bloque de comandos
        for etiqueta in etiquetas:
            label = QLabel(f'{etiqueta}:', self)
            input_field = QLineEdit(self)
            self.form_layout.addRow(label, input_field)
            self.datos_persona.append(input_field)

        self.boton = QPushButton('Mostrar Datos', self)#crearemos el boton
        self.boton.clicked.connect(self.mostrar_datos)#metodo para conectar el boton

        self.resultado = QLabel('', self)
        #gestionaremos las dimensiones de la ventana 
        layout.addLayout(self.form_layout)
        layout.addWidget(self.boton)
        layout.addWidget(self.resultado)

        self.setLayout(layout)

    def mostrar_datos(self):#metodo para mostrar los datos en pantalla
        datos = []#con el siguiente ciclo for iremos ejecutando en orden cada dato hasta completar los campos
        for i, input_field in enumerate(self.datos_persona):
            datos.append(f'{self.form_layout.itemAt(i*2).widget().text()}: {input_field.text()}')
        #verificara el resultado de que los campos sean llenados con el respectivo tipo de valor que
        #deben tener
        self.resultado.setText('\n'.join(datos))
#con el siguiente if mantendremos abierta la ventana hasta que el usuario decida cerrarla 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
