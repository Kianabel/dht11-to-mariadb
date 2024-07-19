# dht11-to-mariadb

## Beschreibung

Python-Skript für die Realtime-Verbindung eines DHT11/22-Sensors mit einer MariaDB auf dem Raspberry Pi 4.

## Vorrausetzungen
- Python 3.x
- GitHub CLI
- maybe pip3

## Installation

### 1. MariaDB Server
Installation des MariaDB-Servers auf Debian-Geräten:

```bash
sudo apt update
sudo apt install mariadb-server
```

### 2. Python-Bibliotheken

Installation von pip3:

```bash
sudo apt install python3-pip
```

Installation der Bibliotheken mit pip:

```bash
pip3 install adafruit-circuitpython-dht
pip3 install mysql-connector-python
```
### 3. Repo klonen

```bash
cd
git clone https://github.com/Kianabel/dht11-to-mariadb
```

### 4. Hardware Setup

Sensor anschließen. In script.py ist D14 ausgewählt, also am besten direkt an PIN 14 anschließen:

### 5. Datenbank-Konfiguration

tempdb ist der Datenbankname, kann abgeändert werden, sollte dann aber auch im Skript angepasst werden.

```bash
sudo mysql -u root -p
```

```sql
CREATE DATABASE tempdb;
USE tempdb;
CREATE TABLE temp (
    id INT AUTO_INCREMENT PRIMARY KEY,
    record_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    temperature DECIMAL(5,2)
);
```

```sql
CREATE USER 'temp_user'@'localhost' IDENTIFIED BY 'temp_password';
GRANT ALL PRIVILEGES ON tempdb.* TO 'temp_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

Username u. Passwort können und sollten vermutlich geändert werden. Aber sollte so auch funktionieren.

### Run

als letztes beten das es funktioniert und abfahrt:

```bash
python3 script.py
```


### Anmerkungen

Sehr wahrscheinlich wird iwas nicht funktionieren, also viel Spaß