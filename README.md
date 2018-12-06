# KAIST-albabot
Ara에 새로운 알바 소식이 올라오면 텔레그램으로 알려줍니다  

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

KAIST-albabot needs telegram bot API, and telegram @BotFather will provide it.   
Refer [here](https://core.telegram.org/bots/api).

<br>

# Getting started
 
`kaist-albabot.py` needs bot API number. fill it up manually. 
After that, add kaist-albabot.py to crontab.  

    $ crontab -e
    */10 * * * * python3 your-directory-path/kaist_albabot/kaist_albabot.py
    
  
