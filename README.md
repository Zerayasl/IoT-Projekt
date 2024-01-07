# IoT-Projekt
Von Gruppe 09: Asli Zeray, Salim Doumbia, Roman Leu

## Einleitung
Dieses Raspberry Pi-Projekt als Smart-Mirror kombiniert Bilderkennung und Wetterdaten, um sicherzustellen, dass man stets angemessen für das Wetter gekleidet ist. Dies vereinfacht Morgenroutine, indem er einen schnellen Rat gibt, ohne dass man selbst das Wetter prüfen muss. Die Anwendung verwendet eine Kamera, ein Image-Classification-Modell und ein Node-RED-Dashboard, um die erkannte Kleidung sowie aktuelle Wetterinformationen anzuzeigen. In seiner Einfachheit zeigt er, wie IoT-Geräte spezifische, alltägliche Probleme mit einer smarten Lösung adressieren können.

## Funktionen
- Kleidererkennung: Die Kamera erfasst Bilder der getragenen Kleidung, und ein Image-Classification-Modell analysiert die Bilder, um die Art der Kleidung zu identifizieren.

- Wetterdaten: Die Anwendung verwendet aktuelle Wetterdaten, um zu bestimmen, welcher Kleidungsstil für die aktuellen Wetterbedingungen angemessen ist.

- Node-RED-Dashboard: Die Wetterinformationen werden in einem übersichtlichen Node-RED-Dashboard dargestellt.

## Installation
1. Raspberry Pi Setup: Bitte Raspberry Pi ordnungsgemäß eingerichten und die Kamera anschliessen.

2. Virtual environment einrichten:
   - $ sudo pip install virtualenv
   - $ virtualenv [nameofvenv]
   - $ cd [nameofvenv]
   - $ source bin/activate

4. Abhängigkeiten installieren: Führe das Skript zur Installation der erforderlichen Abhängigkeiten aus. Dies kann beispielsweise OpenCV, TensorFlow und andere Python-Bibliotheken umfassen.
   - $ pip install -r requirements.txt

6. Node-RED einrichten: Konfiguriere Node-RED auf deinem Raspberry Pi und importiere das bereitgestellte Flow-Skript für das Dashboard.
   - Node-RED: v3.1.3
   - Node.js: v20.10.0
   - npm: 10.2.3
   - $ npm install -g --unsafe-perm node-red

8. LTS Version, Node.js und npm installieren
   - $ bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)

## Running
1. Node-Red starten: Nach der Installation können Sie den Befehl node-red verwenden, um Node-RED in Ihrem Terminal zu starten.
   - $ node-red

3. Anwendung starten: Öffnen Sie einen weiteren Terminal und aktivieren Sie die erstellte virtuelle Umgebung. Dann können Sie diesen folgenden Pfad öffnen und den Python-File starten.
   - $ cd ~/examples/lite/examples/image_classification/raspberry_pi/ $ sh setup.sh $ python3 classify.py

## Autostart on boot
- $ sudo systemctl enable nodered.service
- To Disable the Service: $ sudo systemctl disable nodered.service
