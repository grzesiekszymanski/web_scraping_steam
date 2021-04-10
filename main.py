from selenium import webdriver
from functions import *


def main():
    start = input("Enter name of the game:\n")
    number_of_items = input("Number of items to search:\n")
    try:
        int(number_of_items)
    except:
        print("Please enter a number!")
        exit()
    str(number_of_items)
    PATH = "C:\Program Files\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.maximize_window()
    driver.get("https://store.steampowered.com")

    enter_data(driver, start)
    names_of_items(driver, number_of_items)


main()
