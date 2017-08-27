# waheey-bot

Simple Twitterbot, that writes "WAHEEY" every hour.

# Installation

Use `git clone https://github.com/ExNG/waheey-bot.git` to download the project and install [python-twitter](https://github.com/bear/python-twitter) using `pip install python-twitter`

The hourly part is being managed by he Linux native Cron.hourly.
For that go into the folder with `main.py` and use use: `mv main.py /etc/cron.hourly/ && cd /etc/cron.hourly && touch waheey-bot.sh && echo "python main.py" > waheey-bot.sh`
