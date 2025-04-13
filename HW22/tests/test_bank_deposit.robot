*** Settings ***
Library    ../source/Bankdeposit.py
Library    Collections

*** Test Cases ***

Register Client
    ${id}=    Register Test Client
    ${data}=  Get Client Data
    Dictionary Should Contain Value    ${data}    Test
    Dictionary Should Contain Item     ${data}    start_balance    ${None}
    Dictionary Should Contain Item     ${data}    years            ${None}

Open Deposit Account
    Register Test Client
    Open Deposit    1000    1
    ${data}=  Get Client Data
    Should Be Equal As Numbers    ${data['start_balance']}    1000
    Should Be Equal As Numbers    ${data['years']}            1

Open Deposit Account
    ${result}=    Open Deposit For Invalid Client
    Should Be Equal    ${result}    Такого клиента не существует!

Calculate Deposit Interest
    Register Test Client
    Open Deposit    1000    1
    ${interest}=    Calculate Interest
    Should Be True    ${interest} >= 1104.61 and ${interest} <= 1104.81

Convert Deposit To USD
    Register Test Client
    Open Deposit    1000    1
    ${amount_and_currency}=    Convert To Currency    USD
    ${amount}=    Set Variable    ${amount_and_currency[0]}
    ${currency}=  Set Variable    ${amount_and_currency[1]}
    Should Be True    ${amount} >= 340.86 and ${amount} <= 341.06
    Should Be Equal    ${currency}    USD

Close Deposit
    Register Test Client
    Open Deposit    1000    1
    Close Deposit
    ${data}=  Get Client Data
    Should Be Equal    ${data['start_balance']}    ${None}
    Should Be Equal    ${data['years']}            ${None}

Close Deposit Without Opening
    Register Test Client
    ${result}=    Close Deposit
    Should Be Equal    ${result}    Клиент сначала должен открыть депозит
