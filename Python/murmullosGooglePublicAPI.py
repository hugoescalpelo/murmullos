import RPi.GPIO as GPIO
import speech_recognition as sr
import time

LED_PIN = 17  # Ajusta el número del pin GPIO según tu configuración

def configurar_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.LOW)

def escuchar_microfono():
    recognizer = sr.Recognizer()

    with sr.Microphone(device_index=2) as source:
        print("Escuchando...")

        while True:
            try:
                audio = recognizer.listen(source, timeout=5)
                texto = recognizer.recognize_google(audio, language="es-ES")

                if texto:
                    print(f"Texto detectado: {texto}")
                    encender_led()
                    time.sleep(5)  # Espera 5 segundos antes de volver a escuchar
                    apagar_led()
            except sr.UnknownValueError:
                apagar_led()
            except sr.RequestError as e:
                print(f"Error en la solicitud a Google API: {e}")
                apagar_led()

def encender_led():
    GPIO.output(LED_PIN, GPIO.HIGH)
    print("LED Encendido")

def apagar_led():
    GPIO.output(LED_PIN, GPIO.LOW)
    print("LED Apagado")

if __name__ == "__main__":
    configurar_gpio()
    escuchar_microfono()
