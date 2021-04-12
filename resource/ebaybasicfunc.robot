*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${search_text}  огурцы
*** Keywords ***
Verify basic functionality
    input text  //*[@id="gh-ac"]  ${search_text}
    press keys  //*[@id="gh-btn"]  [Return]
    page should contain  результат. для ${search_text}

