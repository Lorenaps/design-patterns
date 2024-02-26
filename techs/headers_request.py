import requests

url = 'https://httpbin.org/headers'
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.8,pt-BR;q=0.5,pt;q=0.3",
        "Content-Type": "application/json",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Referer": "https://www4.planalto.gov.br/",
        "Cookie": "SERVERID=pzp8142; TS01ab383d=0150f80db13953ceda435a2b00e5f79aafe6c8ea3d71e9dc3754ffbeb65cb4c981f652c13f6465a0c237754b552525f89f26a5ccbce05ad83b1e658e4ca4b45145bf58456f94dcedeab783433f518e0d6cf9ce5271e2c2a1e7cd990c931053d394acc2cd17; TSPD_101=086567d05fab2800aa2f935cf5f2a5bc77332c875703d624f2623f48ad9dbd4ca7eda746e0197d555b0cf52462c55d9908fbe218fc051800a6aed64f008c59c6304602e69b56a39104eeedb0a518443c; TS8fc0b045027=086567d05fab20000f02bd3ea413d82a9f5db443169d4991f1b6714dfe5b3a8a2725915250ea33880829d97086113000322534ba00fe4500f45685d6f661d2dc777da1cc4470a58b719768257f79302b47ebbbbe60c84b03d64695899c730856; TS06ca52b0077=086567d05fab28007aecde328b51a55eb00d6704634577d8c822912b04047c47f0ab4b3a1cea022a95ced1fa14dc08740892b90579172000a7bd09bac221c0eb0a80ac328bbd1fa08ef75341472a72e9315ef73ffdfa9e09"
        }

page = requests.get(url)
#print(page.content)


# Saída:
# {
#     "headers": {
#         "Accept": "*/*",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Host": "httpbin.org",
#         "User-Agent": "python-requests/2.31.0",
#         "X-Amzn-Trace-Id": "Root=1-65dcede1-1cd53be90a49835324d8c7cc"
#     }
# }

page = requests.get(url, headers=headers)
print(page.content)

# Saída:
# {
#     "headers": {    
#         "Accept": "application/json, text/plain, */*",     
#         "Accept-Encoding": "gzip, deflate, br",     
#         "Accept-Language": "en-US,en;q=0.8,pt-BR;q=0.5,pt;q=0.3",     
#         "Content-Type": "application/json",     
#         "Cookie": "SERVERID=pzp8142; TS01ab383d=0150f80db13953ceda435a2b00e5f79aafe6c8ea3d71e9dc3754ffbeb65cb4c981f652c13f6465a0c237754b552525f89f26a5ccbce05ad83b1e658e4ca4b45145bf58456f94dcedeab783433f518e0d6cf9ce5271e2c2a1e7cd990c931053d394acc2cd17; TSPD_101=086567d05fab2800aa2f935cf5f2a5bc77332c875703d624f2623f48ad9dbd4ca7eda746e0197d555b0cf52462c55d9908fbe218fc051800a6aed64f008c59c6304602e69b56a39104eeedb0a518443c; TS8fc0b045027=086567d05fab20000f02bd3ea413d82a9f5db443169d4991f1b6714dfe5b3a8a2725915250ea33880829d97086113000322534ba00fe4500f45685d6f661d2dc777da1cc4470a58b719768257f79302b47ebbbbe60c84b03d64695899c730856; TS06ca52b0077=086567d05fab28007aecde328b51a55eb00d6704634577d8c822912b04047c47f0ab4b3a1cea022a95ced1fa14dc08740892b90579172000a7bd09bac221c0eb0a80ac328bbd1fa08ef75341472a72e9315ef73ffdfa9e09",     
#         "Host": "httpbin.org",     
#         "Referer": "https://www4.planalto.gov.br/",     
#         "Sec-Fetch-Dest": "empty",     
#         "Sec-Fetch-Mode": "cors",     
#         "Sec-Fetch-Site": "same-origin",     
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",     
#         "X-Amzn-Trace-Id": "Root=1-65dceeed-2562380e36e6108a76592c60"  
#     }
# }
