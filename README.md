# KAIST-albabot
Ara에 새로운 알바 소식이 올라오면 텔레그램으로 알려주는 서비스입니다.   
This is a telegram service that notifies you when news of a new part-time job is posted in Ara.  

<br>

# Environment
Download KAIST-albabot  

    $ git clone https://github.com/eternalklaus/KAIST-albabot.git

<br>

Install python dependency libraries. `KAIST-albabot` is compatible with Python 3.  

    $ apt-get install python3
    $ pip3 install beautifulsoup4
    $ pip3 install requests
    $ pip3 install python-telegram-bot

<br>

`KAIST-albabot` needs telegram bot API, and telegram `@BotFather` will provide it.   
If you're not familiar with telegram bot, see [here](https://core.telegram.org/bots/api).

<br>

# Getting started
 
As I mentioned above, `kaist-albabot.py` needs bot API number.   
Fill it to the blank space of *line 86 in kaist_albabot.py* manually.  
After that, add kaist-albabot.py to crontab.  

    $ crontab -e
    */10 * * * * python3 your-directory-path/kaist_albabot/kaist_albabot.py
    
  
