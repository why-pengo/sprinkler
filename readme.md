# Raspberry Pi Sprinkler ][

## Testing
pytest --cov=.

# TODOs
## The Shoulders I Stood On. 
Would have been much harder and taken a lot longer without these resources.

* [Web Controlled 8 Channel Powerstrip](http://www.instructables.com/id/Web-Controlled-8-Channel-Powerstrip/)
* [Simple and intuitive web interface for your Raspberry Pi](http://www.instructables.com/id/Simple-and-intuitive-web-interface-for-your-Raspbe/)
* [pi sprinkler timer](https://github.com/aaronnewcomb/pi-sprinkler-timer)
* [KnowHow episode 254](https://twit.tv/shows/know-how/episodes/254)
    
## GPIO to Relay pins

Wire color | phy | GPIO   | Relay 
-----------|-----|--------|-------
 white     |  1  | 3.3V   | 10 VCC
 brown     |  2  | 5V     | JD-VCC
 black     |  6  | GND    |  1 GND
 grey      |  7  | GPIO7  |  9 IN8
 purple    | 11  | GPIO17 |  2 IN1 
 blue      | 12  | GPIO18 |  3 IN2
 green     | 13  | GPIO27 |  4 IN3
 yellow    | 15  | GPIO22 |  5 IN4
 orange    | 16  | GPIO23 |  6 IN5
 red       | 18  | GPIO24 |  7 IN6
 brown     | 22  | GPIO25 |  8 IN7
 
## GPIO readall ouput

```bash
$ gpio readall
+-----+-----+---------+------+---+---Pi 3---+---+------+---------+-----+-----+
| BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
+-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
|     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
|   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
|   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
|   4 |   7 | GPIO. 7 |  OUT | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
|     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
|  17 |   0 | GPIO. 0 |  OUT | 1 | 11 || 12 | 1 | OUT  | GPIO. 1 | 1   | 18  |
|  27 |   2 | GPIO. 2 |  OUT | 1 | 13 || 14 |   |      | 0v      |     |     |
|  22 |   3 | GPIO. 3 |  OUT | 1 | 15 || 16 | 1 | OUT  | GPIO. 4 | 4   | 23  |
|     |     |    3.3v |      |   | 17 || 18 | 1 | OUT  | GPIO. 5 | 5   | 24  |
|  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
|   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 1 | OUT  | GPIO. 6 | 6   | 25  |
|  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
|     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
|   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
|   5 |  21 | GPIO.21 |   IN | 1 | 29 || 30 |   |      | 0v      |     |     |
|   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | IN   | GPIO.26 | 26  | 12  |
|  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
|  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
|  26 |  25 | GPIO.25 |   IN | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
|     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
+-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
| BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
+-----+-----+---------+------+---+---Pi 3---+---+------+---------+-----+-----+
```

## pipenv

*   [pipenv info](https://github.com/pypa/pipenv)
*   pip install pipenv # if not installed
*   export LANG=en_US.utf-8 # if you get a warning about ASCII encoding
*   pipenv install # to setup virutalenv with requirements set in Pipfile
*   pipenv shell # to start working on project
*   exit # when you are done


TODO:
Use a production WSGI server instead.
Add login/password/sessions
Add weekly scheduler

## Self-Signed Certificate
If you want to encrypt traffic to your sprinkler controller you can use a self-signed cert, which
is considered very bad practice. It requires managing the cert on your server and any clients.

* [Detailed Info](https://www.sslshopper.com/article-how-to-create-and-install-an-apache-self-signed-certificate.html)

# create cert
```shell
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout mysitename.key -out mysitename.crt
```
