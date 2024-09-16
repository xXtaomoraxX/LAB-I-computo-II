#importamos las librerias
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
#importamos los widgets 
from PyQt5.QtCore import Qt  # Asegúrate de importar Qt #este solucionara un error anterior al momento de 
#definir la variable Qt, esta no aparecia y de paso ahorrara el espacio de crearla desde cero
#Creamos la clase ventana, en ella se mostraran los datos
class Ventana(QWidget):
    def __init__(self):#inicializamos la clase con sus atributos
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Datos Personales')
        self.setGeometry(100, 100, 400, 200)#creamos las dimensiones del mensaje 

        layout = QVBoxLayout()

        self.nombre_label = QLabel('Nombre Completo:', self)
        self.nombre_input = QLineEdit(self)#aqui introduciremos el nombre

        self.edad_label = QLabel('Edad:', self)
        self.edad_input = QLineEdit(self)#aqui introduciremos la edad

        self.boton = QPushButton('Mostrar', self)#creamos el boton
        self.boton.clicked.connect(self.mostrar_datos)

        self.resultado = QLabel('', self)
        #gestionaremos aqui las dimensiones de la ventana
        layout.addWidget(self.nombre_label) 
        layout.addWidget(self.nombre_input)
        layout.addWidget(self.edad_label)
        layout.addWidget(self.edad_input)
        layout.addWidget(self.boton)
        layout.addWidget(self.resultado)

        self.setLayout(layout)

    def mostrar_datos(self):
        nombre = self.nombre_input.text()
        edad = self.edad_input.text()
        self.resultado.setText(f'Nombre: {nombre}\nEdad: {edad}')#nos aeguramos que imprima en pantalla
        #los datos introducidos por el usuario y se cumplan las condiciones del tipo de caracter
        self.resultado.setAlignment(Qt.AlignCenter)  # Asegúrate de que Qt esté definido
        #recordar que el objetivo que es aparezcan centrados los datos en la ventana 
#este if mantendra abierta la ventana hasta que el usuario decida cerrarla 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
