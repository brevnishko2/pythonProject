*** Settings ***
Documentation  First test case
Resource  ../../resource/ebay.robot
Resource  ../../resource/ebaybasicfunc.robot
Test Setup  start test
Test Teardown  end test

*** Variables ***


*** Test Cases ***
Verify basic search funtionality for ebay search
    [Documentation]  This test case verifies the basic search
    [Tags]  Functional

    verify basic functionality
