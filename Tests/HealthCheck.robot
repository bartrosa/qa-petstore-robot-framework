*** Settings ***
Library           libraries.PortalAPIAuth
Library           resources.keywords.custom_keywords
Variables         resources.variables.common_variables

*** Variables ***
${BASE_URL}       ${env.get_env_variable('BASE_URL')}
${CLIENT_ID}      ${env.get_env_variable('CLIENT_ID')}
${CLIENT_SECRET}  ${env.get_env_variable('CLIENT_SECRET')}

*** Test Cases ***
Health Check
    [Documentation]  Verify that the API is healthy
    ${token}=  Get Token
    Check API Health  ${BASE_URL}  ${token}

