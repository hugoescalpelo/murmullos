# Configuración de Python

El siguiente código corre sobre una Raspberry Pi 3B+

## Comprobar Python

Para comprobar que python se encuentra instalado, corre el siguiente comando en una terminal.

```
python --version
```
 En este caso el resultado fue el siguiente:

```
Python 3.9.2
```
En caso de no tener python instalado, corre el siguiente programa. Este comando requiere conexión a Internet.
```
sudo apt-get update
sudo apt-get install python3
```

## Caso murmullosGooglePublicAPI.py
### Instalacion de bibliotecas

Instala las bibliotecas necesarias:
```
pip install SpeechRecognition
pip install pyaudio
pip install RPi.GPIO
```
Estos comandos requieren conexión a Internet.
### Codigo via GIT

Para pasar el código a la Raspberry Pi se usará Git y Github.

1. Comprueba que tienes GIT instalado con el siguiente comando
    ```
    git --version
    ```

    En mi caso, el resultado fue el siguiente.
    ```
    git version 2.30.2
    ```
    En caso de que no tengas instalado GIT, ejecuta los siguientes comandos.
    ```
    sudo apt-get update # Actualiza el sistema
    sudo apt-get install git    # Instala GIT
    ```
2. Clona este repositorio.
    
    Se recomienda crear una carpeta llamada GitHub en Documents. Puedes hacerlo con el siguiente comando.
    
    ```
    cd ~/Documents  # Cambia al directorio "Documents" (si no estás allí ya)
    mkdir GitHub     # Crea la carpeta llamada "GitHub"
    ```
    Entra al directorio GitHub

    ```
    cd GitHub
    ```

    Para clonar el repositorio, ejecuta el siguiente comando


Estos comandos requieren conexión a Internet.
### Determinar el Index del micrófono
Conecta el microfono y corre el programa llamado detectarmicrofono.py
