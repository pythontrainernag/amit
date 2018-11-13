*** Settings ***
Variables         input.yaml
Library           sa.py

*** Test Cases ***
connect_sample
    : FOR    ${server}    IN    @{servers}
    \    Connect    ${server}
    \    Create Alias    ${server}
    \    Verify Alias    ${server}
