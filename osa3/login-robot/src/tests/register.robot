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

Register With Too Short Username And Valid Password
    Input Credentials  ki  katti123
    Output Should Contain  Username must be at least three characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kissa123  katti123
    Output Should Contain  Username must only contain uncapitalized letters from a-z


*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command

