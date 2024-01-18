import RPi.GPIO as GPIO
import speech_recognition as sr
from google.oauth2 import service_account
from google.cloud import speech_v1p1beta1 as speech

LED_PIN = 17

def configure_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.LOW)

def listen_microphone():
    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone(device_index=1) as source:
                print("Escuchando...")
                audio = recognizer.listen(source, timeout=5)

            print("Procesando audio...")
            texto = recognize_google_cloud(audio)
            if texto:
                print(f"Texto detectado: {texto}")
                turn_on_led()
                time.sleep(5)
                turn_off_led()
        except sr.UnknownValueError:
            turn_off_led()
        except sr.RequestError as e:
            print(f"Error en la solicitud a Google API: {e}")
            turn_off_led()

def recognize_google_cloud(audio):
    credentials = service_account.Credentials.from_service_account_file(
        'ruta/a/tu/archivo-de-credenciales.json')  # Reemplaza con la ruta de tus credenciales
    client = speech.SpeechClient(credentials=credentials)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="es-ES",
    )

    audio_content = audio.frame_data

    response = client.recognize(config=config, audio={"content": audio_content})
    for result in response.results:
        return result.alternatives[0].transcript

def turn_on_led():
    GPIO.output(LED_PIN, GPIO.HIGH)
    print("LED Encendido")

def turn_off_led():
    GPIO.output(LED_PIN, GPIO.LOW)
    print("LED Apagado")

if __name__ == "__main__":
    configure_gpio()
    listen_microphone()
