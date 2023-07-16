# Raspberry Pi Sprinkler ][

[See the documentation on building the hardware](https://why-pengo.github.io/sprinkler/)

## Details

* OS: Raspbian GNU/Linux 11 (bullseye) armv7l
* Host: Raspberry Pi 3 Model B Rev 1.2
* CPU: BCM2835 (4) @ 1.200GHz
* Memory: 1Gb

## Testing
pytest --cov=.

## The Shoulders I Stood On. 
Would have been much harder and taken a lot longer without these resources.

* [Web Controlled 8 Channel Powerstrip](http://www.instructables.com/id/Web-Controlled-8-Channel-Powerstrip/)
* [Simple and intuitive web interface for your Raspberry Pi](http://www.instructables.com/id/Simple-and-intuitive-web-interface-for-your-Raspbe/)
* [pi sprinkler timer](https://github.com/aaronnewcomb/pi-sprinkler-timer)
* [KnowHow episode 254](https://twit.tv/shows/know-how/episodes/254)
    
## GPIO to Relay pins

| Wire color | phy | GPIO   | Relay  |
|------------|-----|--------|--------|
| white      |  1  | 3.3V   | 10 VCC |
| brown      |  2  | 5V     | JD-VCC |
| black      |  6  | GND    | 1 GND  |
| grey       |  7  | GPIO7  | 9 IN8  |
| purple     | 11  | GPIO17 | 2 IN1  |
| blue       | 12  | GPIO18 | 3 IN2  |
| green      | 13  | GPIO27 | 4 IN3  |
| yellow     | 15  | GPIO22 | 5 IN4  |
| orange     | 16  | GPIO23 | 6 IN5  |
| red        | 18  | GPIO24 | 7 IN6  |
| brown      | 22  | GPIO25 | 8 IN7  |
 
## poetry

* sudo apt install build-essential libssl-dev libffi-dev python3-dev cargo
* pip install --user poetry
* poetry install # to setup virutalenv with requirements set in Pipfile
* poetry shell # to start working on project
* exit # when you are done


## Warning about PinFactoryFallback
https://gpiozero.readthedocs.io/en/stable/faq.html#why-do-i-get-pinfactoryfallback-warnings-when-i-import-gpiozero

## Nginx 

### Generate a self-signed certificate

As I am using this only on my local private network, I'll use a self-signed cert. 
I followed this Digital Ocean [guide](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-nginx-on-debian-10)

### Docker compose for nginx

```bash
cd nginx
docker-compose up
```

### Django startup

```bash
poetry shell
python manage.py collectstatic
gunicorn --bind 0.0.0.0:8000 controller.wsgi:application
```