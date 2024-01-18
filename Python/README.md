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
pip install pip install google-cloud-speech
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
    Estos comandos requieren conexión a Internet.
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

    ```
    git clone https://github.com/hugoescalpelo/murmullos.git
    ```
    Este comando requiere conexión a Internet.

### Determinar el Index del micrófono
Conecta el microfono y corre el programa llamado detectarmicrofono.py

Puedes hacerlo con el siguiente comando.
```
python ~/Documents/GitHub/murmullos/Python/detectarmicrofono.py
```
En mi caso aparece lo siguiente
```
Microfono 0: bcm2835 Headphones: - (hw:0,0)
Microfono 1: UM10: USB Audio (hw:2,0)
Microfono 2: sysdefault
Microfono 3: lavrate
Microfono 4: samplerate
Microfono 5: speexrate
Microfono 6: pulse
Microfono 7: upmix
Microfono 8: vdownmix
Microfono 9: dmix
Microfono 10: default
```
Mi modelo de microfono es UM10, por lo que usaré el Index 1 en el siguiente programa.

Este comando requiere conexión a Internet.

## Ejecutar programa

Antes de ejecutar el programa, abre el archivo llamado murmulllosGooglePublicAPI.py en la carpeta Python de este repositorio haciendo doble clic sobre el. Se abrirá un editor de codigo, busca la linea 15 coloca el valor adecuado a la variable `device_index`. En mi caso, toda la linea de código  queda de la siguiente forma ```with sr.Microphone(device_index=1) as source:```.

Guarda los cambios y cierra el editor.

En la terminal de comandos ejecuta el siguiente comando para ejecutar el programa.

```
python ~/Documents/GitHub/murmullos/Python/murmullosGooglePublicAPI.py
```