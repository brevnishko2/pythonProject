*** Settings ***
Library  SeleniumLibrary


*** Keywords ***
start test
    open browser  https://www.ebay.com  chrome
    maximize browser window

end test
    close browser