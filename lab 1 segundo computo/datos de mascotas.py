#importamos las librerias de pyQT
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout
#importamos los widgets 
#creamos la clase con sus atributos
class Ventana(QWidget):
    def __init__(self):#incializamos la clase junto a sus atributos
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Datos de Mascotas')#mensaje impreso en pantalla de la ventana de estado
        self.setGeometry(100, 100, 400, 400)#definimos sus dimensiones de tamaño

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.mascotas = []#creamos el metodo para los datos de las mascotas
        for i in range(3):#recordemos que son 3 mascotas 
            #usaremos un bucle for para ejecutar el siguiente bloque de comados
            # en el cual iran los datos de las tres mascotas
            nombre_label = QLabel(f'Nombre Mascota {i+1}:', self)#pediremos el nombre de la mascota
            nombre_input = QLineEdit(self)#introducir el nombre
            tipo_label = QLabel(f'Tipo Mascota {i+1}:', self)#pediremos el tipo de mascota
            tipo_input = QLineEdit(self)#introducir el tipo de mascota
            edad_label = QLabel(f'Edad Mascota {i+1}:', self)#pediremos la edad de la mascota
            edad_input = QLineEdit(self)#introducimos la edad de la mascota 

            self.form_layout.addRow(nombre_label, nombre_input)
            self.form_layout.addRow(tipo_label, tipo_input)
            self.form_layout.addRow(edad_label, edad_input)

            self.mascotas.append((nombre_input, tipo_input, edad_input))

        self.boton = QPushButton('Mostrar Datos', self)#crearemos el boton
        self.boton.clicked.connect(self.mostrar_datos)#metodo para conectar el botom

        self.resultado = QLabel('', self)
        #definiremos las dimensiones del boton y las acciones 
        layout.addLayout(self.form_layout)
        layout.addWidget(self.boton)
        layout.addWidget(self.resultado)

        self.setLayout(layout)

    def mostrar_datos(self):#crearemos el metodo para mostrar los datos
        datos = []
        #crearemos el siguiente ciclo para enumerar el orden de las tres mascotas
        for i, (nombre_input, tipo_input, edad_input) in enumerate(self.mascotas):
            nombre = nombre_input.text()
            tipo = tipo_input.text()
            edad = edad_input.text()
            datos.append(f'Mascota {i+1} - Nombre: {nombre}, Tipo: {tipo}, Edad: {edad}')
            #verificara que las condiciones del tipo de valor de los datos sea correcta

        self.resultado.setText('\n'.join(datos))
#el siguiente if nos mantendra abierta la ventana hasta que el usario decida cerrar 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
