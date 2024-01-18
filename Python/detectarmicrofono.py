import speech_recognition as sr

def listar_dispositivos():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"Microfono {index}: {name}")

if __name__ == "__main__":
    listar_dispositivos()