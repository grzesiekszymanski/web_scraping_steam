from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def enter_data(driver, start):
    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable((By.ID, 'acceptAllButton'))).click()

    start_box = wait.until(EC.element_to_be_clickable((By.ID, 'store_nav_search_term')))
    start_box.send_keys(start)
    start_box.send_keys(Keys.ENTER)

    wait.until(EC.element_to_be_clickable((By.ID, 'acceptAllButton'))).click()


def names_of_items(driver, number_of_items):
    open('items.csv', 'w').close()
    i = 1
    while i <= int(number_of_items):
        nums = ['{}'.format(str(i))]
        try:
            for num in nums:

                items = driver.find_element_by_xpath \
                    ('//*[@id="search_resultsRows"]/a[{}]/div[2]/div[1]/span'
                    .format(str(num))).get_attribute('innerHTML')

                items2 = driver.find_element_by_xpath \
                    ('//*[@id="search_resultsRows"]/a[{}]/div[2]/div[4]/div[2]'
                    .format(str(num))).get_attribute('innerHTML')
                filename = 'items.csv'

                with open(filename, 'a+') as my_table:

                    if items2.strip() == "":
                        items2 = "FOR FREE"

                    my_table.write(items + "\n" + items2.strip()[-8:] + "\n")
        except:
            print(number_of_items + ' items not found!\nAll found items were saved in a file "items.csv"')
            break
        i += 1