# Waheey Twitter Bot

Simple Twitterbot, that writes "WAHEEY" every hour.

# Installation

Use `git clone https://github.com/ExNG/waheey-bot.git` to download the project and install [python-twitter](https://github.com/bear/python-twitter) using `pip install python-twitter`

# Auto Tweet

For the timing i use cron.
`crontab -e` and append `0,30 * * * * python *path to .py file* >/dev/null` this will trigger every 30
