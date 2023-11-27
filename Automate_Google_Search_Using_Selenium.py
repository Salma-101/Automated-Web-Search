# AUTOMATE GOOGLE SEARCH USING SELENIUM

from selenium import webdriver

# taking input from user
search_string = input("Input the URL or string you want to search for: ")

# this id done to structure the string into search URL
# (can be ignored)
search_string = search_string.replace(' ', '+')

# geckodriver for Mozilla Firefox
browser = webdriver.Chrome()

for i in range(1):
    matched_elements = browser.get("https://www.google.com/search?q=" + search_string + "&start" + str(i))
