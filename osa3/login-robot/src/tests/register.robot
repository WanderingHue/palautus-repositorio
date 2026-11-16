*** Settings ***
Resource  resource.robot
Test Setup  User Creation Query

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kissa  katti123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kissa  katti123
    Output Should Contain  User with username kissa already exists

Register With Too Short Username And Valid Password
# ...

Register With Enough Long But Invalid Username And Valid Password
# ...

Register With Valid Username And Too Short Password
# ...

Register With Valid Username And Long Enough Password Containing Only Letters
# ...

*** Keywords ***
User Creation Query
    Input New Command
