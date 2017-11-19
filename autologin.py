from selenium import webdriver                      #can be executed via command line easily
from time import sleep  #import the packages
 
usr=input("Enter email id:") #take inputs
pwd=input("Enter Password:")
 
driver=webdriver.Chrome()          #initialize to operate on chrome
driver.get('https://twitter.com/login')  #open url
print("Twitter Opened")    #show the progress
sleep(2)  #delay
 
a = driver.find_element_by_class_name("js-username-field") #search for the username field on https://twitter.com/login 
a.send_keys(usr)    #send the entered values to the username field
print("Id Entered") #show progress
sleep(1) #delay
 
b = driver.find_element_by_class_name("js-password-field")  #search for the password field on https://twitter.com/login 
b.send_keys(pwd)  #send the entered values to the password field
print("Password Entered")  #show progress
 
c=driver.find_element_by_css_selector("button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium") #automatically submit the files
c.click()  #automatically click the "enter" button
 
print("Twitter Logged ") #show progress
sleep(60)  #delay
driver.quit() #exit
