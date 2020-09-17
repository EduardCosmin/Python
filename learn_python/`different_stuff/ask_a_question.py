def main(question):
    #import libraries
    from selenium import webdriver
    from selenium.webdriver.common.keys import keys
    from selenium.webdriver.chrome.options import Options
    
    #configure some options
    options=Options()   #get the selenium.webdriver.chrome.options Options() function.
    options.add_experimental_option("excludeSwitches",['enable-automation'])
    
    #get the browser
    browser=webdriver.chrome(options=options)
    browser.get("https://www.google.com/")
    
    #find the search bar and send over the search query
    elem = browser.find_element_by_name("q")
    elem.clear()
    elem.send_keys(question)
    elem.send_keys(keys.RETURN)

if __name__=="__main__":
    main(input("Enter your question here: "))