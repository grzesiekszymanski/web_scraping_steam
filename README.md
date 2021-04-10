# Web scraping

web_scraping_steam is a program written with the Selenium module. It works for the Chrome browser.

Description how the program works - the user enters the following data: name of the game and the number of items he wants to find. 
After confirming the data, a browser opens the webpage "https://store.steampowered.com". Then, the expected items are searched and
saved with the price in the file "items.csv". If the user provides incorrect data or the expected items are not found, the user will 
be informed.
