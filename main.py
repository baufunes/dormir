from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class SueñoApp(App):
    def build(self):
        # Contenedor principal
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Título
        title = Label(text='Horas de sueño', size_hint_y=0.15, bold=True, font_size='24sp')
        main_layout.add_widget(title)
        
        # Pregunta 1
        label1 = Label(text='¿Ya te acostás? (sí/no):', size_hint_y=0.1)
        input1 = TextInput(text='', multiline=False, size_hint_y=0.1)
        main_layout.add_widget(label1)
        main_layout.add_widget(input1)
        
        # Pregunta 2
        label2 = Label(text='¿Qué hora es? (24h):', size_hint_y=0.1)
        input2 = TextInput(text='', multiline=False, size_hint_y=0.1, input_filter='int')
        main_layout.add_widget(label2)
        main_layout.add_widget(input2)
        
        # Resultado
        result_label = Label(text='', size_hint_y=0.2, markup=True)
        main_layout.add_widget(result_label)
        
        # Botón
        button = Button(text='Calcular', size_hint_y=0.15)
        button.bind(on_press=lambda x: self.calcular(input1.text, input2.text, result_label))
        main_layout.add_widget(button)
        
        return main_layout
    
    def calcular(self, dormir, hora, result_label):
        if dormir.lower() == "sí" or dormir.lower() == "si":
            try:
                hr_dormir = int(hora)
                hr_despertar = hr_dormir + 8
                
                # Validar que no pase de 24 horas
                if hr_despertar > 24:
                    hr_despertar = hr_despertar - 24
                
                result_label.text = f'[b]Te tenés que despertar a las {hr_despertar}:00[/b]'
            except ValueError:
                result_label.text = '[color=ff0000]Ingresa una hora válida[/color]'
        else:
            result_label.text = '[color=ff6600]¿Y entonces para qué abrís la app?[/color]'

if __name__ == '__main__':
    SueñoApp().run()