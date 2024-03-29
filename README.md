# IoT-Projekt
von Gruppe 09: Asli Zeray, Salim Doumbia, Roman Leu

## Einleitung
Dieses Raspberry Pi-Projekt als Smart-Mirror kombiniert Bilderkennung und Wetterdaten, um sicherzustellen, dass man stets angemessen für das Wetter gekleidet ist. Dies vereinfacht Morgenroutine, indem er einen schnellen Rat gibt, ohne dass man selbst das Wetter prüfen muss. Die Anwendung verwendet eine Kamera, ein Image-Classification-Modell und ein Node-RED-Dashboard, um die erkannte Kleidung sowie aktuelle Wetterinformationen anzuzeigen. In seiner Einfachheit zeigt er, wie IoT-Geräte spezifische, alltägliche Probleme mit einer smarten Lösung adressieren können.

## !! WICHTIGE Anpassungen !!
1. Node-RED starten: Nach der Installation des Node-RED können Sie den Befehl node-red verwenden, um Node-RED in Ihrem Terminal zu starten. Nicht note-red-start !
   - $ node-red

2. Bitte den HttpStatic-Pfad im File *Settings.js* des *.node-red* Ordners anpassen:<br>
- Zur Info: Bei uns ist *.node-red* hier abgelegt: /home/pi/.node-red<br>
> httpStatic: '/home/pi/.node-red/image/',

3. Die Iconpfade im Classify.py Code anpassen! So sieht der Pfad ab der Zeile 126 im Classify.py aus:<br>

> *Iconpfad*<br>
> *sun_icon_path = '/home/pi/examples/lite/examples/image_classification/raspberry_pi/iconsonne.jpg'*<br>
> *cloud_icon_path = '/home/pi/examples/lite/examples/image_classification/raspberry_pi/iconwolke.jpg'*<br>
> *snow_icon_path = '/home/pi/examples/lite/examples/image_classification/raspberry_pi/iconschnee.jpg'*

4. Anwendung starten: Öffnen Sie einen weiteren Terminal und aktivieren Sie die erstellte virtuelle Umgebung. Dann können Sie auf den folgenden Pfad und den Classify.py starten.
   - $ cd ~/examples/lite/examples/image_classification/raspberry_pi/
   - $ sh setup.sh
   - $ python3 classify.py

## Ergänzende Info über die Dateien/Dokumente
- Im Node-RED-Dateien befinden sich die Flows.
- Im Video-Datei befindet sich das Projektvideo.
- Im Image-Datei befindet sich der Snapshot in JPG-Format.
- Die restlichen Dateien gehören zum Code Classify.py.

  
## Allg. Info über die Funktionen
- Kleidererkennung: Die Kamera erfasst Bilder der getragenen Kleidung, und ein Image-Classification-Modell analysiert die Bilder, um die Art der Kleidung zu identifizieren.

- Wetterdaten: Die Anwendung verwendet aktuelle Wetterdaten, um zu bestimmen, welcher Kleidungsstil für die aktuellen Wetterbedingungen angemessen ist.

- Node-RED-Dashboard: Die Wetterinformationen werden in einem übersichtlichen Node-RED-Dashboard dargestellt.

## Allg. Anleitung für den Setup
1. Raspberry Pi Setup: Bitte Raspberry Pi ordnungsgemäß eingerichten und die Kamera anschliessen.

2. Virtual environment einrichten:
   - $ sudo pip install virtualenv
   - $ virtualenv [nameofvenv]
   - $ cd [nameofvenv]
   - $ source bin/activate

3. Abhängigkeiten installieren: Führe das Skript zur Installation der erforderlichen Abhängigkeiten aus. Dies kann beispielsweise OpenCV, TensorFlow und andere Python-Bibliotheken umfassen.
   - $ pip install -r requirements.txt

4. Node-RED einrichten: Konfiguriere Node-RED auf deinem Raspberry Pi und importiere das bereitgestellte Flow-Skript für das Dashboard.<br>

> Node-RED: v3.1.3<br>
> Node.js: v20.10.0<br>
> npm: 10.2.3<br>
   
   - $ npm install -g --unsafe-perm node-red

6. LTS Version, Node.js und npm installieren
   - $ bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)<br>
> Autostart on boot: $ sudo systemctl enable nodered.service  
> To Disable the Service: $ sudo systemctl disable nodered.service<br>

## Weitere allg. Infos 
- Wenn die API Keys nicht funktionieren, kann man diese unter folgenden Seiten erstellen:
   - Wettersanzeige im Classify.py: *https://open-meteo.com*
   - Wetteranzeige im Node-RED: *https://home.openweathermap.org*
