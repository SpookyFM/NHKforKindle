# NHKforKindle

This is a fork of the original script for downloading easy Japanese news from NHK and packaging them from Kindle by vebaev https://github.com/vebaev/NHKforKindle

This version will save which news item was the latest it downloaded. The next time it is run, it downloads all news items until the last synced. If non are found, it will download the last 5 news items. Additionally, a second script will send the resulting file as a mail automatically.

To set up the mail, please edit sendmail.py before running with your SMTP login details.