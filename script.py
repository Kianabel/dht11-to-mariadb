#!/usr/bin/python3

import adafruit_dht
import board
import time
import mysql.connector
from mysql.connector import Error

dht = adafruit_dht.DHT22(board.D14, use_pulseio=False) # D14 am besten so lassen, kann aber angepasst werden

# Funktion, um die Temperatur in die DB zu schreiben (wird im Hauptprozess aufgerufen)
def insert_temperature(temp):
    try:
        # Verbindung zur DB aufbauen
        connection = mysql.connector.connect(
            host='localhost',  # IP der DB (localhost, wenn auf demselben Gerät)
            database='tempdb',  # Tabellenname
            user='temp_user',  # Benutzername (root wird vermutlich nicht funktionieren)
            password='temp_password'  # Passwort des Benutzers
        )

        # Überprüfen, ob die Verbindung zur DB steht
        if connection.is_connected():
            cursor = connection.cursor()
            query = "INSERT INTO temp (record_time, temperature) VALUES (NOW(), %s)"  # SQL-Query definieren, %s signalisiert die Temperaturvariable
            cursor.execute(query, (temp,))  # Cursor-Objekt, um die Query auszuführen
            connection.commit()  # Mitteilung an die DB, dass die Änderungen gespeichert werden sollen
            cursor.close()  # Cursor wird geschlossen
            connection.close()  # Verbindung wird geschlossen
            print("Hat brutalst funktioniert")  # Log, falls es funktioniert hat
    except Error as e:
        print("Fehler: {}".format(e))  # Log, falls ein Fehler auftritt

# Hauptprozess
while True:
    try:
        # Temperatur und Feuchtigkeit werden mithilfe der adafruit_dht-Bibliothek ermittelt
        temp = dht.temperature  # Wird verwendet
        hum = dht.humidity  # Wird nicht verwendet, weil 'can't be asked'

        # console.log
        print(temp)
        print(hum)

        # Funktion wird aufgerufen, um die Temperatur zu speichern, sofern der Inhalt nicht null ist
        if temp is not None:
            insert_temperature(temp)

    except RuntimeError as error:
        # Fehlerbehandlung, wenn der Sensor Probleme macht
        print(error.args[0])
        time.sleep(2.0)  # 2 Sekunden Verzögerung, bis es erneut versucht wird
        continue

    # Intervall in Sekunden, nach dem die nächste Temperatur ausgelesen und gespeichert wird (hier 10 Sekunden)
    time.sleep(10.0)
