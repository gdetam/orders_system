# orders system
***

## Settings

### For Google Sheets <br>

Add file creds.json from Google Sheets to the project<br>
#### Add in .env file:<br>
Add id of the table from which the data is read
```commandline
SPREADSHEET_ID = <YOUR SPREADSHEET ID>
```
### For Telegram bot <br>
#### Add in .env file:<br>
Add your bot token
```commandline
BOT_TOKEN = <YOUR BOT TOKEN>
```
Add chat id to send expired orders
```commandline
CHAT_ID = <YOUR CHAT ID>
```
---
## Start and Run

Start local server postgres 127.0.0.1:5432.<br>

```commandline
$ python -m venv venv
```
```commandline
$ source venv/bin/activate
```
```commandline
$ pip install -r requirements.txt
```
```commandline
python main.py
```
#### Docker
```commandline
$ docker-compose up 
```
---

## Authors 👨‍💻

Contributors names and contact info

ex. gdetam  
ex. [@gdetam](https://t.me/onlygdetam)

### License

This project is licensed under the [MIT License](LICENSE.txt)