#EL siguiente codigo tiene como objetivo comprobar choques de horario entre las horas de clases y entrenos
#de los clubes, si hay una clase que sea a la misma hora del entreno el programa le avisara,
#que existe un choque de horarios
#importamos las librerias
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QSpinBox, QPushButton, QHBoxLayout
#recorda que en los widgets hemos usado Qcombobox, y Qspinbox como obligacion para este programa
class Ventana(QWidget):#creamos la clase para la ventana
    def __init__(self):#inicializamos la clase junto a sus atributos
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Verificación de Choques de Horarios')#mensaje que aparecera en la ventana
        self.setGeometry(100, 100, 400, 400)#dimensiones del tamaño definidas de la ventana

        layout = QVBoxLayout()

        # Horario de clases
        self.clases_label = QLabel('Horario de Clases:', self)#mensaje que aparecera en el horario clases
        self.clases_inicio_label = QLabel('Inicio:', self)#aqui nos indicara que sera la hora de inicio
        self.clases_inicio_hora = QSpinBox(self)
        self.clases_inicio_hora.setRange(0, 23)#definimos el rango de horas en 23
        self.clases_inicio_minuto = QSpinBox(self)
        self.clases_inicio_minuto.setRange(0, 59)#definimos el rango de los minutos en 59
        self.clases_fin_label = QLabel('Fin:', self)#aqui indica que sera el fin en que termina la clase
        self.clases_fin_hora = QSpinBox(self)
        self.clases_fin_hora.setRange(0, 23)
        self.clases_fin_minuto = QSpinBox(self)
        self.clases_fin_minuto.setRange(0, 59)

        self.materia_label = QLabel('Materia:', self)#aqui nos indicara a que materia pertenece
        self.materia_combo = QComboBox(self)
        self.materia_combo.addItems(['Matemáticas', 'Ciencias', 'Historia', 'Lenguaje', 'Arte'])
        #seleccionaremos a cual materia pertenece

        clases_layout = QHBoxLayout()
        clases_layout.addWidget(self.clases_inicio_label)
        clases_layout.addWidget(self.clases_inicio_hora)
        clases_layout.addWidget(self.clases_inicio_minuto)
        clases_layout.addWidget(self.clases_fin_label)
        clases_layout.addWidget(self.clases_fin_hora)
        clases_layout.addWidget(self.clases_fin_minuto)

        # Horario de entrenamiento
        self.entrenamiento_label = QLabel('Horario de Entrenamiento:', self)#aqui empezara el horario de entrenos
        self.entrenamiento_inicio_label = QLabel('Inicio:', self)#inicio de los entrenos
        self.entrenamiento_inicio_hora = QSpinBox(self)
        self.entrenamiento_inicio_hora.setRange(0, 23)#recorda que el rango de horas es el formato de 24
        self.entrenamiento_inicio_minuto = QSpinBox(self)
        self.entrenamiento_inicio_minuto.setRange(0, 59)#el rango en minutos sera en 59 
        self.entrenamiento_fin_label = QLabel('Fin:', self)#fin de los entrenos
        self.entrenamiento_fin_hora = QSpinBox(self)
        self.entrenamiento_fin_hora.setRange(0, 23)
        self.entrenamiento_fin_minuto = QSpinBox(self)
        self.entrenamiento_fin_minuto.setRange(0, 59)

        self.club_label = QLabel('Club:', self)#indica a que club pertenece
        self.club_combo = QComboBox(self)
        self.club_combo.addItems(['Fútbol', 'Baloncesto', 'Natación', 'Teatro', 'Música'])
        #seleccionaremos un club

        entrenamiento_layout = QHBoxLayout()
        entrenamiento_layout.addWidget(self.entrenamiento_inicio_label)
        entrenamiento_layout.addWidget(self.entrenamiento_inicio_hora)
        entrenamiento_layout.addWidget(self.entrenamiento_inicio_minuto)
        entrenamiento_layout.addWidget(self.entrenamiento_fin_label)
        entrenamiento_layout.addWidget(self.entrenamiento_fin_hora)
        entrenamiento_layout.addWidget(self.entrenamiento_fin_minuto)

        # Botón para verificar choques
        self.boton = QPushButton('Verificar Choques', self)#crearemos el boton
        self.boton.clicked.connect(self.verificar_choques)#conectamos el boton

        self.resultado = QLabel('', self)#almacena el resultado
        
        layout.addWidget(self.clases_label)
        layout.addLayout(clases_layout)
        layout.addWidget(self.materia_label)
        layout.addWidget(self.materia_combo)
        layout.addWidget(self.entrenamiento_label)
        layout.addLayout(entrenamiento_layout)
        layout.addWidget(self.club_label)
        layout.addWidget(self.club_combo)
        layout.addWidget(self.boton)
        layout.addWidget(self.resultado)

        self.setLayout(layout)

    def verificar_choques(self):#creamos el metodo para verificar si hay choques
        clases_inicio = self.clases_inicio_hora.value() * 60 + self.clases_inicio_minuto.value()
        clases_fin = self.clases_fin_hora.value() * 60 + self.clases_fin_minuto.value()
        entrenamiento_inicio = self.entrenamiento_inicio_hora.value() * 60 + self.entrenamiento_inicio_minuto.value()
        entrenamiento_fin = self.entrenamiento_fin_hora.value() * 60 + self.entrenamiento_fin_minuto.value()
        #tendremos como condicion si se dan a las mismas horas entonces habra un choque
        #y el programa nos dira que hay un choque de horarios
        if (clases_inicio < entrenamiento_fin and clases_fin > entrenamiento_inicio):
            self.resultado.setText('¡Hay un choque de horarios!')
            #caso contrario dira que no hay choques de horario
        else:
            self.resultado.setText('No hay choques de horarios.')
#el siguiente if mantendra la ventana abierta hasta que el usuario decida cerrar
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
