#importamos las librerias
import sys
#importamos los widgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
#definimos la clase
class Ventana(QWidget):
    def __init__(self):#inicializamos la clase con sus atributos 
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Clave Secreta')#mensaje mostrado en pantalla, o titulo
        self.setGeometry(100, 100, 400, 200)#definimos las dimensiones de la ventana

        layout = QVBoxLayout()

        self.clave_label = QLabel('Introduce tu clave secreta:', self)#mensaje que indique al usuario que 
        #introduzca su clave
        self.clave_input = QLineEdit(self) #introducimos la clave
        self.clave_input.setEchoMode(QLineEdit.Password)  # Oculta los caracteres
        #recordemos que el objetivo es que no se muestre la contraseña al introducirla 
        self.boton = QPushButton('Mostrar Clave', self) #creamos el boton
        self.boton.clicked.connect(self.mostrar_clave)

        self.resultado = QLabel('', self)
        #gestion de la dimension de la ventana 
        layout.addWidget(self.clave_label)
        layout.addWidget(self.clave_input)
        layout.addWidget(self.boton)
        layout.addWidget(self.resultado)

        self.setLayout(layout)

    def mostrar_clave(self):#crearemos el metodo para mostrar la clave en pantalla al tocar el voton
        clave = self.clave_input.text()
        self.resultado.setText(f'Clave: {clave}')
#este if nos mantendra abierta la ventana hasta que la decida cerrar el usuario 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
