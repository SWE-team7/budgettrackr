from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def Amazon(input):
    # Initiate the browser
    browser  = webdriver.Chrome(ChromeDriverManager().install())

    # Open the Website
    browser.get("https://amazon.com")
    
    inputBox = browser.find_element("id", "twotabsearchtextbox")
        
    inputBox.send_keys(input , Keys.ENTER)
    
    href = browser.find_element(By.CLASS_NAME, "s-image")
    
    href.click()
        
    print("\nProduct name:\n", browser.find_element("id", "productTitle").text)
    print("\n")
    print("Price: ", browser.find_element(By.CLASS_NAME, "a-price-symbol").text, browser.find_element(By.CLASS_NAME, "a-price-whole").text,".", browser.find_element(By.CLASS_NAME, "a-price-fraction").text ) 
    print("\n")
    print("Product Info:\n", browser.find_element("id", "productDetails_detailBullets_sections1").text)
    print("\n")
    
# def bestBuy(input):    
#     # Initiate the browser
#     browser  = webdriver.Chrome(ChromeDriverManager().install())

#     # Open the Website
#     browser.get("https://bestbuy.com")
    
#     inputBox = browser.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/header/div[1]/div/div[1]/div/form/input[1]")
        
#     inputBox.send_keys(input , Keys.ENTER)
    
#     href = browser.find_element(By.CLASS_NAME, "product-image ")
    
#     href.click()
        
#     print("\nProduct name:\n", browser.find_element(By.CLASS_NAME, "sku-title").text)
#     print("\n")
#     print("Price: ", browser.find_element(By.XPATH, "/html/body/div[4]/main/div[3]/div/div[1]/div[3]/div[2]/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/div/span[1]").text)
#     print("\n")
#     print("Product Info:\n", browser.find_element(By.XPATH, "/html/body/div[4]/main/div[3]/div/div[1]/div[3]/div[1]/div[2]/div/div/ul/li[1]/span/a/div").text)
#     print("\n")
       
# def newegg(input):
#     # Initiate the browser
#     browser  = webdriver.Chrome(ChromeDriverManager().install())

#     # Open the Website
#     browser.get('https://newegg.com')
    
#     searchBar = browser.find_element(By.CLASS_NAME, "header2021-search-button")
#     searchBar.click()
    
#     inputBox = browser.find_element(By.XPATH, "/html/body/div[17]/header/div[1]/div[1]/div[1]/div[5]/form/div/div[1]/input")
        
#     inputBox.send_keys(input , Keys.ENTER)
    
#     href = browser.find_element(By.XPATH, "/html/body/div[14]/div[3]/section/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div[3]/div[3]/div[1]/div/a/img")
    
#     href.click()
    
        
    # print("\nProduct name:\n", browser.find_element(By.CLASS_NAME, "product-title").text)
    # print("\n")
    # print("Price: ", browser.find_element(By.CLASS_NAME, "price-current").text)
    # print("\n")
    # print("Product Info:\n", browser.find_element(By.CLASS_NAME, "product-seller-rating").text)
    # print("\n")
                
def main():
    
    search = input("Please enter a Product: ")
    
    print("Amazon: ")
    Amazon(search)
    
    #print("BestBuy: ")
    #bestBuy(search)
    
    # print("newegg: ")
    # newegg(search)
    
if __name__=="__main__":
    main()