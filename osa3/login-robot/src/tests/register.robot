*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kissa  katti123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  vesi1234
    Output Should Contain  User with username kalle already exists

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command

