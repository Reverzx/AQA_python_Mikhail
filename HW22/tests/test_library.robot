*** Settings ***
Library    ../source/Library.py

*** Variables ***
${BOOK_NAME}    The Hobbit
${AUTHOR}       Books by J.R.R. Tolkien
${PAGES}        400
${ISBN}         0006754023
${VASYA}        Vasya
${PETYA}        Petya

*** Test Cases ***

Reserve Book
    ${book}=      Create Book        ${BOOK_NAME}    ${AUTHOR}    ${PAGES}    ${ISBN}
    ${user}=     Create Reader      ${VASYA}
    Reserve Book  ${user}           ${book}
    ${reserved}=  Get Reserved By    ${book}
    Should Be Equal    ${reserved}    ${VASYA}

Reserve Book Blocked
    ${book}=      Create Book        ${BOOK_NAME}    ${AUTHOR}    ${PAGES}    ${ISBN}
    ${user_1}=     Create Reader      ${VASYA}
    ${user_2}=     Create Reader      ${PETYA}
    Reserve Book  ${user_1}           ${book}
    Reserve Book  ${user_2}           ${book}
    ${reserved}=  Get Reserved By    ${book}
    Should Not Be Equal    ${reserved}    ${PETYA}

Cancel Reserve
    ${book}=      Create Book        ${BOOK_NAME}    ${AUTHOR}    ${PAGES}    ${ISBN}
    ${user}=     Create Reader      ${VASYA}
    Reserve Book  ${user}           ${book}
    Cancel Reserve  ${user}         ${book}
    ${reserved}=  Get Reserved By    ${book}
    Should Be Equal As Strings    ${reserved}    None

Cancel Reserve By Wrong Reader
    ${book}=      Create Book        ${BOOK_NAME}    ${AUTHOR}    ${PAGES}    ${ISBN}
    ${user_1}=     Create Reader      ${VASYA}
    ${user_2}=     Create Reader      ${PETYA}
    Reserve Book  ${user_1}           ${book}
    Cancel Reserve  ${user_2}         ${book}
    ${reserved}=  Get Reserved By    ${book}
    Should Be Equal    ${reserved}    ${VASYA}

Get Book After Reserve
    ${book}=      Create Book        ${BOOK_NAME}    ${AUTHOR}    ${PAGES}    ${ISBN}
    ${user}=     Create Reader      ${VASYA}
    Reserve Book  ${user}           ${book}
    Get Book      ${user}           ${book}
    ${received}=  Get Received By    ${book}
    Should Be Equal    ${received}    ${VASYA}

Get Book Without Reserve
    ${book}=      Create Book        ${BOOK_NAME}    ${AUTHOR}    ${PAGES}    ${ISBN}
    ${user}=     Create Reader      ${VASYA}
    Get Book      ${user}           ${book}
    ${received}=  Get Received By    ${book}
    Should Be Equal    ${received}    ${VASYA}

Get Book With Wrong User
    ${book}=      Create Book        ${BOOK_NAME}    ${AUTHOR}    ${PAGES}    ${ISBN}
    ${user_1}=     Create Reader      ${VASYA}
    ${user_2}=     Create Reader      ${PETYA}
    Reserve Book  ${user_2}           ${book}
    Get Book      ${user_1}           ${book}
    ${received}=  Get Received By    ${book}
    Should Not Be Equal    ${received}    ${VASYA}

Return Book
    ${book}=      Create Book        ${BOOK_NAME}    ${AUTHOR}    ${PAGES}    ${ISBN}
    ${user}=     Create Reader      ${VASYA}
    Reserve Book  ${user}           ${book}
    Get Book      ${user}           ${book}
    Return Book   ${user}           ${book}
    ${received}=  Get Received By    ${book}
    Should Be Equal As Strings    ${received}    None

Return Book With Wrong User
    ${book}=      Create Book        ${BOOK_NAME}    ${AUTHOR}    ${PAGES}    ${ISBN}
    ${user_1}=     Create Reader      ${VASYA}
    ${user_2}=     Create Reader      ${PETYA}
    Reserve Book  ${user_1}           ${book}
    Get Book      ${user_1}           ${book}
    Return Book   ${user_2}           ${book}
    ${received}=  Get Received By    ${book}
    Should Be Equal    ${received}    ${VASYA}


