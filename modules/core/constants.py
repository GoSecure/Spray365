# Source for endpoint_ids and client_ids: https://github.com/Gerenios/AADInternals/blob/master/AccessToken_utils.ps1

endpoint_ids = {
    "aad_graph_api": "https://graph.windows.net",
    "azure_mgmt_api": "https://management.azure.com",
    "cloudwebappproxy": "https://proxy.cloudwebappproxy.net/registerapp",
    "ms_graph_api": "https://graph.microsoft.com",
    "msmamservice": "https://msmamservice.api.application",
    "office_mgmt": "https://manage.office.com",
    "officeapps": "https://officeapps.live.com",
    "outlook": "https://outlook.office365.com",
    "sara": "https://api.diagnostics.office.com",
    "spacesapi": "https://api.spaces.skype.com",
    "webshellsuite": "https://webshell.suite.office.com",
    "windows_net_mgmt_api": "https://management.core.windows.net",
}

client_ids = {
    "aad_account": "0000000c-0000-0000-c000-000000000000",
    "aad_brokerplugin": "6f7e0f60-9401-4f5b-98e2-cf15bd5fd5e3",
    "aad_cloudap": "38aa3b87-a06d-4817-b275–7a316988d93b",
    "aad_join": "b90d5b8f-5503-4153-b545-b31cecfaece2",
    "aad_pinredemption": "06c6433f-4fb8-4670-b2cd-408938296b8e",
    "aadconnectv2": "6eb59a73-39b2-4c23-a70f-e2e3ce8965b1",
    "aadrm": "90f610bf-206d-4950-b61d-37fa6fd1b224",
    "aadsync": "cb1056e2-e479-49de-ae31-7812af012ed8",
    "adibizaux": "74658136-14ec-4630-ad9b-26e160ff0fc6",
    "apple_internetaccounts": "f8d98a96-0999-43f5-8af3-69971c7bb423",
    "az": "1950a258-227b-4e31-a9cf-717495945fc2",
    "azure_mgmt": "84070985-06ea-473d-82fe-eb82b4011c9d",
    "azure_mobileapp_android": "0c1307d4-29d6-4389-a11c-5cbe7f65d7fa",
    "azureadmin": "c44b4083-3bb0-49c1-b47d-974e53cbdf3c",
    "azuregraphclientint": "7492bca1-9461-4d94-8eb8-c17896c61205",
    "azuremdm": "29d9ed98-a469-4536-ade2-f981bc1d605e",
    "dynamicscrm": "00000007-0000-0000-c000-000000000000",
    "exo": "a0c73c16-a7e3-4564-9a95-2bdf47383716",
    "graph_api": "1b730954-1685-4b74-9bfd-dac224a7b894",
    "intune_mam": "6c7e8096-f593-4d72-807f-a5f86dcc9c77",
    "ms_authenticator": "4813382a-8fa7-425e-ab75-3b753aab3abb",
    "ms_myaccess": "19db86c3-b2b9-44cc-b339-36da233a3be2",
    "msdocs_tryit": "7f59a773-2eaf-429c-a059-50fc5bb28b44",
    "msmamservice": "27922004-5251-4030-b22d-91ecd9a37ea4",
    "o365exo": "00000002-0000-0ff1-ce00-000000000000",
    "o365spo": "00000003-0000-0ff1-ce00-000000000000",
    "o365suiteux": "4345a7b9-9a63-4910-a426-35363201d503",
    "office": "d3590ed6-52b3-4102-aeff-aad2292ab01c",
    "office_mgmt": "389b1b32-b5d5-43b2-bddc-84ce938d6737",
    "office_mgmt_mobile": "00b41c95-dab0-4487-9791-b9d2c32c80f2",
    "office_online": "bc59ab01-8403-45c6-8796-ac3ef710b3e3",
    "office_online2": "57fb890c-0dab-4253-a5e0-7188c88b2bb4",
    "onedrive": "ab9b8c07-8f02-4f72-87fa-80105867a763",
    "patnerdashboard": "4990cffe-04e8-4e8b-808a-1175604b879",
    "powerbi_contentpack": "2a0c3efa-ba54-4e55-bdc0-770f9e39e9ee",
    "pta": "cb1056e2-e479-49de-ae31-7812af012ed8",
    "sara": "d3590ed6-52b3-4102-aeff-aad2292ab01c",
    "skype": "d924a533-3729-4708-b3e8-1d2445af35e3",
    "sp_mgmt": "9bc3ab49-b65d-410a-85ad-de819febfddc",
    "synccli": "1651564e-7ce4-4d99-88be-0a65050d8dc3",
    "teams": "1fec8e78-bce4-4aaf-ab1b-5451cc387264",
    "teams_client": "1fec8e78-bce4-4aaf-ab1b-5451cc387264",
    "teamswebclient": "5e3ce6c0-2b1f-4285-8d4b-75ee78787346",
    "webshellsuite": "89bee1f7-5e6e-4d8a-9f3d-ecd601259da7",
    "windows_configdesigner": "de0853a1-ab20-47bd-990b-71ad5077ac7b",
    "www": "00000006-0000-0ff1-ce00-000000000000",
}

user_agents = {
    "android": "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Mobile Safari/537.36",
    "apple_iphone_safari": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "apple_mac_firefox": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0",
    "linux_firefox": "Mozilla/5.0 (X11; Linux i686; rv:94.0) Gecko/20100101 Firefox/94.0",
    "win_chrome_win10": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "win_ie11_win7": "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
    "win_ie11_win8": "Mozilla/5.0 (Windows NT 6.2; Trident/7.0; rv:11.0) like Gecko",
    "win_ie11_win8.1": "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko",
    "win_ie11_win10": "Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko",
    "win_edge_win10": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44",
}

# Error codes that indicated a failure; see https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes
auth_error_codes = {
    50034: "User not found",
    50126: "Invalid credentials",
}

# Error codes that also indicate a successful login; see https://github.com/AzureAD/microsoft-authentication-library-for-dotnet/wiki/Client-Applications#common-invalid-client-errors
auth_complete_success_error_codes = [7000218, 65001]

# Error codes that indicated a partial success (valid creds); see https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes
auth_partial_success_error_codes = {
    530031: "Conditional Access blocked the access token issuance",
    50053: "Account locked or sign-in blocked because it came from a malicious IP",
    50055: "Account password expired",
    50057: "Account disabled",
    50158: "External validation failed (is there a conditional access policy?)",
    50076: "Multi-Factor Authentication Required",
    53003: "Conditional access policy prevented access",
    700016: "Application was not found in the directory",
}
