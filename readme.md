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
 
## poetry

*   sudo apt install build-essential libssl-dev libffi-dev python3-dev cargo
*   pip install --user poetry
*   poetry install # to setup virutalenv with requirements set in Pipfile
*   poetry shell # to start working on project
*   exit # when you are done


TODO:
Use a production WSGI server instead.
Add login/password/sessions
