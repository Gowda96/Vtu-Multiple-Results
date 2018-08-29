from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
def getRes():
    global driver
    url="http://results.vtu.ac.in/vitaviresultnoncbcs18/index.php"
    driver=webdriver.Chrome("#PATH TO CHROME DRIVER");
    first=driver.get("https://www.google.com")
    
    startUsn=input("Enter Starting Usn")
    endUsn=input("Enter Last Usn")
    intStartLastDigits=int(startUsn[7:10])
    intEndLastDigits=int(endUsn[7:10])    
    

    for i in range(intStartLastDigits,intEndLastDigits):
        if(i<100):
            requsn=startUsn[0:7]+str(0)+str(i)
            pass
        else:
            requsn=startUsn[0:7]+str(i)
            pass
        print(requsn)
        
        #OPENING NEW TAB FOR EVERY RESULT
        try:
            driver.execute_script("window.open('http://results.vtu.ac.in/vitaviresultnoncbcs18/index.php');")
            driver.switch_to.window(driver.window_handles[-1])
                    
            usn_field=driver.find_element_by_xpath('//input[@name="lns"]').send_keys(requsn) #Fill URL
            submit=driver.find_element_by_xpath('//input[@id="submit"]').click()
            driver.switch_to_window(driver.window_handles[0])
        except NoAlertPresentException:
            pass
            
        pass
    driver.switch_to_window(driver.window_handles[-1])
        
        
        
        
getRes()
        
        
    
    
    
