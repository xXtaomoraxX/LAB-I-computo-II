#importamos las clases
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
#importamos los widgets 
#definimos la clase
class Ventana(QWidget):
    def __init__(self):#inicializamos la clase junto a sus atributos
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Datos Personales')#mensaje mostrado en la ventana
        self.setGeometry(100, 100, 400, 200)#definimos las dimensiones del tamaño de la ventana 

        layout = QVBoxLayout()

        self.cedula_label = QLabel('Número de Cédula:', self)#mensaje que pedira el numero de cedula
        self.cedula_input = QLineEdit(self)#introducimos el numero de cedula(dui)

        self.nombre_label = QLabel('Nombre Completo:', self)#mensaje que pedira el nombre del usuario
        self.nombre_input = QLineEdit(self)#introducimos el nombre 

        self.boton = QPushButton('Mostrar Datos', self)#creamos el boton
        self.boton.clicked.connect(self.mostrar_datos)

        self.resultado = QLabel('', self)
        #gestionamos las dimensiones del tabaño de la ventana
        layout.addWidget(self.cedula_label)
        layout.addWidget(self.cedula_input)
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_input)
        layout.addWidget(self.boton)
        layout.addWidget(self.resultado)

        self.setLayout(layout)

    def mostrar_datos(self):#definimos el metodo para mostrar los datos
        cedula = self.cedula_input.text()
        nombre = self.nombre_input.text()
        self.resultado.setText(f'Número de Cédula: {cedula}\nNombre: {nombre}')
        #comprobara que las condiciones se cumplan en los valores introducidos
        #(que sean de tipo caracter y valor)
        
#el siguiente if mantendra nuestra ventana abierta hasta que el usuario la cierre 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
