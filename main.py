# import requests
# from fastapi import FastAPI, Query
# from typing import List
# def getEmail(docId):
#   headers = {
#       'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36',
#       'Accept': '*/*',
#       'Accept-Language': 'en-US,en;q=0.5',
#       # 'Accept-Encoding': 'gzip, deflate, br',
#       'Referer': 'https://www.justdial.com/jdmart/Delhi/Vardhman-Automobiles-Pvt-Ltd-Old-Dlf-Colony/011PXX11-XX11-190529153926-G3S9_BZDET/catalogue?ref=auto&searchfrom=auto|home',
#       'content-type': 'application/json',
#     #   'wert': 'MDExUFhYMTFYWDExMTkwNTI5MTUzOTI2RzNTOURlbGhpVmFyZGhtYW5BdXRvbW9iaWxlc1B2dEx0ZE9sZERsZkNvbG9ueQ==',
#       'Sec-Fetch-Dest': 'empty',
#       'Sec-Fetch-Mode': 'cors',
#       'Sec-Fetch-Site': 'same-origin',
#       'Connection': 'keep-alive',
#   }
  
#   params = {
#       # 'search': 'Vardhman-Automobiles-Pvt-Ltd-Old-Dlf-Colony',
#       'docid': docId,
#       'prevdocid': '',
#       'case': 'detail',
#       'city': 'Delhi',
#       'area': 'Ramesh Nagar',
#       'usercity': '',
#       'slong': '',
#       'slat': '',
#       'wap': '2',
#       'login_mobile': '',
#       'mvbksrc': 'ft,pvr,cinemax,fc',
#       'search_bdcatid': '',
#       'bd_msgtype': '',
#       'bd_captiontype': '',
#       'bd_text': '',
#       'vpfs': '8-100',
#       'jdlite': '0',
#       'keyword': '',
#       'debugmode': '1',
#       'dummy': '0',
#       'querySieve': [
#           'search',
#           '',
#       ],
#       'owner': '0',
#       'freelist': '',
#       'jde': '',
#       'new': '1',
#       'type': '',
#       'mp': '0',
#       'b2b': '1',
#       'national_catid': '',
#       'catname': '',
#       'bc': '',
#       'design': '1',
#       'sieve': '{"name":"detailModel","selector":"detail","runInit":false}',
#       'trk': '0',
#       'selectedImage': '',
#       'source': '2',
#       'version': '4.1',
#       'searchReferrer': 'gen',
#       'utmCampaign': '',
#       'utm_campaign': '',
#       'referer': 'https://www.justdial.com/',
#       'utm_source': '',
#       'utm_medium': '',
#       'lat': '28.651',
#       'long': '77.131',
#       'enc': '1',
#       'env': 'p',
#   }
  
#   response = requests.get(
#       'https://www.justdial.com/api/india_api_write/20march2020/searchziva.php',
#       params=params,
#       headers=headers,
#   )
#   return response.json()["main"]["maintab"]["email"]


# def getData(page, city, area, qurry):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36',
#         'Accept': '*/*',
#         'Accept-Language': 'en-US,en;q=0.5',
#         'Referer': 'https://www.justdial.com/Delhi/Tyre-Dealers-in-Ramesh-Nagar/nct-10505416?ismap=undefined&srcterm=Tyre%20Dealers',
#         'content-type': 'application/json',
#         'Sec-Fetch-Dest': 'empty',
#         'Sec-Fetch-Mode': 'cors',
#         'Sec-Fetch-Site': 'same-origin',
#         'Connection': 'keep-alive',
#     }
#     params = {
#         'city': city,
#         'usercity': '',
#         'area': area,
#         'lat': '28.651',
#         'long': '77.131',
#         'darea_flg': '0',
#         'case': 'spcall',
#         'stype': 'category_list',
#         'search': qurry,
#         # 'national_catid': '10505416',
#         # 'national_catid': '10110698',
#         # 'nextdocid': '011PXX11.XX11.190526104526.B6T9,011PXX11.XX11.211124110019.L3M2,011PXX11.XX11.190118154902.N1T3,011PXX11.XX11.101124180946.F2X3,011PXX11.XX11.221014135025.J2Y1,011PXX11.XX11.170213145825.H1J6,011PXX11.XX11.091223074016.I2R9,011PXX11.XX11.171222180913.K6T1,011PXX11.XX11.190712231509.R8S8,011PXX11.XX11.100730182726.F2D1',
#         'attribute_values': '[[]]',
#         'sffilter': '',
#         'basedon': '',
#         'sortby': '',
#         'nearme': '0',
#         'rnd1': '0.74521',
#         'rnd2': '0.48429',
#         'rnd3': '0.21668',
#         'max': '100',
#         'pg_no': str(page),
#         'wap': '2',
#         'debugmode': '1',
#         'pecounter': '0',
#         'median_latitude': '28.65109',
#         'median_longitude': '77.13123',
#         'bd_text': 'Best Deal',
#         'login_mobile': '',
#         'search_option': '0',
#         'sort_order': '0',
#         'pricedesc': '0',
#         'priceasc': '0',
#         'checkin': '',
#         'checkout': '',
#         'attr_search': 'Car',
#         'opt': '',
#         'dummy': '0',
#         'querySieve': [
#             'search',
#             'checkout',
#             'checkin',
#         ],
#         'adword_pos': '{"3":"verticalslider-3","15":"skipprod-10"}',
#         'locflg': '0',
#         'view_flag': '0',
#         'sieve': '{"name":"resultModel","selector":"result","runInit":true}',
#         'seopage': '',
#         # 'sHash': 'AhqN9IVUkHmAaulhnFdnZ',
#         # 'dHash': 'HyKljKRLBnGdRnaQF-fhQ',
#         'bdtextdata': 'Get Best Deal',
#         'bdtextdatali': 'Get Best Deal',
#         'isgroup': '',
#         'new': '1',
#         'smprod': '0',
#         'asflg': '',
#         'enid': '',
#         'enflg': '',
#         'ncatid': '',
#         'trk': '0',
#         'ismap': '0',
#         'jdmart': '0',
#         'supplier': '',
#         'pgtypSieve': '',
#         'source': '2',
#         'version': '4.1',
#         'searchReferrer': 'gen|back|dtlpg',
#         'utmCampaign': '',
#         'utm_campaign': '',
#         'utm_source': '',
#         'utm_medium': '',
#         'enc': '1',
#         'env': 'p',
#     }

#     base_url = 'https://www.justdial.com/api/india_api_write/20march2020-live/searchziva.php'
#     # base_url = 'https://www.justdial.com/api/india_api_write/20march2020/searchziva.php'
#     response = requests.get(base_url, params=params, headers=headers)
#     return response.json()



# # Your existing code for data extraction
# def extract_data(qurry: str, searcharea: str, searchCity: str):
#     qurry = qurry.replace(" ", "-")
#     current_page = 1
#     total_pages = 25
#     all_data = []  # List to store data from all pages
#     while current_page <= total_pages:
#         data = getData(str(current_page), searchCity, searcharea, qurry)
#         if len(data['main']['data']) < 1:
#             break
#         for i in range(0, len(data['main']['data'])):
#             DOcIdKey=str(data['main']['columns']['docid'])
#             NameKey = str(data['main']['columns']['name'])
#             AddrKey = str(data['main']['columns']['NewAddress'])
#             FUllADkey = str(data['main']['columns']['area'])
#             UserType = str(data['main']['columns']['type'])
#             latKey = str(data['main']['columns']['lat'])
#             longKey = str(data['main']['columns']['lon'])
#             PhoneKey = str(data['main']['columns']['VNumber'])
#             attr_key = str(data['main']['columns']['attr_data'])
#             EventDataKey = str(data['main']['columns']['event_data'])
#             EventData = data['main']['data'][i][EventDataKey]

#             UserName = data['main']['data'][i][NameKey]
#             UserAdress = data['main']['data'][i][AddrKey]
#             fulladdres = data['main']['data'][i][FUllADkey]
#             UserType = data['main']['data'][i][UserType]
#             DocId=data['main']['data'][i][DOcIdKey]
#             PhoneNumber = str(data['main']['data'][i][PhoneKey]['vnumber'])
#             gmail=getEmail(str(DocId))
#             # if len(gmail)<2:
#                 # print(f"Name {UserName}  docId :  {DocId} \n")
#             # PhoneNumber = str(data['main']['data'][i][PhoneKey])
#             PhoneNumber = PhoneNumber.replace('_vn', '').replace(
#                 '(', '').replace(')', '').replace('-', '')
#             EstablishedData = data['main']['data'][i][attr_key]['node2']

#             lattitude = data['main']['data'][i][latKey]
#             longitude = data['main']['data'][i][longKey]

#             try:
#                 rating = EventData['rating']
#                 ratingCount = EventData['rating_cnt']

#                 city = EventData['city']
#                 Dcity = EventData['dcity']
#                 area = EventData['area']
#                 pincode = EventData['pin']
#             except:
#                 continue
#             all_data.append({
#                 "Name": UserName,
#                 "Type": UserType,
#                 "email":gmail,
#                 "PhoneNumber": PhoneNumber,
#                 "rating": rating,
#                 "ratingCount": ratingCount,
#                 "Established": EstablishedData,
#                 "Area":area,
#                 "city": city,
#                 "Dcity": Dcity,
#                 "pincode": pincode,
#                 "lattitude": lattitude,
#                 "longitude": longitude,
#                 "FullAddress": UserAdress+" "+fulladdres
#             })
#         current_page += 1
#     return all_data

# # Create a FastAPI app
# app = FastAPI()

# # Define a route to return all data as JSON
# #http://localhost:8000/get_all_data?qurry=<your_query_here>&searcharea=<your_search_area_here>&searchCity=<your_search_city_here>
# @app.get("/get_all_data")
# def get_all_data(qurry: str = Query(...), searcharea: str = Query(...), searchCity: str = Query(...)):
#     # print(qurry, searcharea, searchCity)
#     all_data = extract_data(qurry, searcharea, searchCity)  # Call your existing function to get all data
#     return {"data": all_data}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)


import requests, uvicorn
from fastapi import FastAPI, Query
from typing import List
def getEmail(docId):
  headers = {
      'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36',
      'Accept': '*/*',
      'Accept-Language': 'en-US,en;q=0.5',
      # 'Accept-Encoding': 'gzip, deflate, br',
      'Referer': 'https://www.justdial.com/jdmart/Delhi/Vardhman-Automobiles-Pvt-Ltd-Old-Dlf-Colony/011PXX11-XX11-190529153926-G3S9_BZDET/catalogue?ref=auto&searchfrom=auto|home',
      'content-type': 'application/json',
    #   'wert': 'MDExUFhYMTFYWDExMTkwNTI5MTUzOTI2RzNTOURlbGhpVmFyZGhtYW5BdXRvbW9iaWxlc1B2dEx0ZE9sZERsZkNvbG9ueQ==',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-origin',
      'Connection': 'keep-alive',
  }
  
  params = {
      # 'search': 'Vardhman-Automobiles-Pvt-Ltd-Old-Dlf-Colony',
      'docid': docId,
      'prevdocid': '',
      'case': 'detail',
      'city': 'Delhi',
      'area': 'Ramesh Nagar',
      'usercity': '',
      'slong': '',
      'slat': '',
      'wap': '2',
      'login_mobile': '',
      'mvbksrc': 'ft,pvr,cinemax,fc',
      'search_bdcatid': '',
      'bd_msgtype': '',
      'bd_captiontype': '',
      'bd_text': '',
      'vpfs': '8-100',
      'jdlite': '0',
      'keyword': '',
      'debugmode': '1',
      'dummy': '0',
      'querySieve': [
          'search',
          '',
      ],
      'owner': '0',
      'freelist': '',
      'jde': '',
      'new': '1',
      'type': '',
      'mp': '0',
      'b2b': '1',
      'national_catid': '',
      'catname': '',
      'bc': '',
      'design': '1',
      'sieve': '{"name":"detailModel","selector":"detail","runInit":false}',
      'trk': '0',
      'selectedImage': '',
      'source': '2',
      'version': '4.1',
      'searchReferrer': 'gen',
      'utmCampaign': '',
      'utm_campaign': '',
      'referer': 'https://www.justdial.com/',
      'utm_source': '',
      'utm_medium': '',
      'lat': '28.651',
      'long': '77.131',
      'enc': '1',
      'env': 'p',
  }
  
  response = requests.get(
      'https://www.justdial.com/api/india_api_write/20march2020/searchziva.php',
      params=params,
      headers=headers,
  )
  return response.json()["main"]["maintab"]["email"]


def getData(page, city, area, qurry):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.justdial.com/Delhi/Tyre-Dealers-in-Ramesh-Nagar/nct-10505416?ismap=undefined&srcterm=Tyre%20Dealers',
        'content-type': 'application/json',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Connection': 'keep-alive',
    }
    params = {
        'city': city,
        'usercity': '',
        'area': area,
        'lat': '28.651',
        'long': '77.131',
        'darea_flg': '0',
        'case': 'spcall',
        'stype': 'category_list',
        'search': qurry,
        # 'national_catid': '10505416',
        # 'national_catid': '10110698',
        # 'nextdocid': '011PXX11.XX11.190526104526.B6T9,011PXX11.XX11.211124110019.L3M2,011PXX11.XX11.190118154902.N1T3,011PXX11.XX11.101124180946.F2X3,011PXX11.XX11.221014135025.J2Y1,011PXX11.XX11.170213145825.H1J6,011PXX11.XX11.091223074016.I2R9,011PXX11.XX11.171222180913.K6T1,011PXX11.XX11.190712231509.R8S8,011PXX11.XX11.100730182726.F2D1',
        'attribute_values': '[[]]',
        'sffilter': '',
        'basedon': '',
        'sortby': '',
        'nearme': '0',
        'rnd1': '0.74521',
        'rnd2': '0.48429',
        'rnd3': '0.21668',
        'max': '100',
        'pg_no': str(page),
        'wap': '2',
        'debugmode': '1',
        'pecounter': '0',
        'median_latitude': '28.65109',
        'median_longitude': '77.13123',
        'bd_text': 'Best Deal',
        'login_mobile': '',
        'search_option': '0',
        'sort_order': '0',
        'pricedesc': '0',
        'priceasc': '0',
        'checkin': '',
        'checkout': '',
        'attr_search': 'Car',
        'opt': '',
        'dummy': '0',
        'querySieve': [
            'search',
            'checkout',
            'checkin',
        ],
        'adword_pos': '{"3":"verticalslider-3","15":"skipprod-10"}',
        'locflg': '0',
        'view_flag': '0',
        'sieve': '{"name":"resultModel","selector":"result","runInit":true}',
        'seopage': '',
        # 'sHash': 'AhqN9IVUkHmAaulhnFdnZ',
        # 'dHash': 'HyKljKRLBnGdRnaQF-fhQ',
        'bdtextdata': 'Get Best Deal',
        'bdtextdatali': 'Get Best Deal',
        'isgroup': '',
        'new': '1',
        'smprod': '0',
        'asflg': '',
        'enid': '',
        'enflg': '',
        'ncatid': '',
        'trk': '0',
        'ismap': '0',
        'jdmart': '0',
        'supplier': '',
        'pgtypSieve': '',
        'source': '2',
        'version': '4.1',
        'searchReferrer': 'gen|back|dtlpg',
        'utmCampaign': '',
        'utm_campaign': '',
        'utm_source': '',
        'utm_medium': '',
        'enc': '1',
        'env': 'p',
    }

    base_url = 'https://www.justdial.com/api/india_api_write/20march2020-live/searchziva.php'
    # base_url = 'https://www.justdial.com/api/india_api_write/20march2020/searchziva.php'
    response = requests.get(base_url, params=params, headers=headers)
    return response.json()



# Your existing code for data extraction
def extract_data(qurry: str, searcharea: str, searchCity: str, current_page:str):
    qurry = qurry.replace(" ", "-")
    # current_page = 1
    # total_pages = 25
    all_data = []  # List to store data from all pages
    # while current_page <= total_pages:
    data = getData(str(current_page), searchCity, searcharea, qurry)
    # if len(data['main']['data']) < 1:
    #     break
    for i in range(0, len(data['main']['data'])):
        DOcIdKey=str(data['main']['columns']['docid'])
        NameKey = str(data['main']['columns']['name'])
        AddrKey = str(data['main']['columns']['NewAddress'])
        FUllADkey = str(data['main']['columns']['area'])
        UserType = str(data['main']['columns']['type'])
        latKey = str(data['main']['columns']['lat'])
        longKey = str(data['main']['columns']['lon'])
        PhoneKey = str(data['main']['columns']['VNumber'])
        attr_key = str(data['main']['columns']['attr_data'])
        EventDataKey = str(data['main']['columns']['event_data'])
        EventData = data['main']['data'][i][EventDataKey]

        UserName = data['main']['data'][i][NameKey]
        UserAdress = data['main']['data'][i][AddrKey]
        fulladdres = data['main']['data'][i][FUllADkey]
        UserType = data['main']['data'][i][UserType]
        DocId=data['main']['data'][i][DOcIdKey]
        PhoneNumber = str(data['main']['data'][i][PhoneKey]['vnumber'])
        gmail=getEmail(str(DocId))
        # if len(gmail)<2:
            # print(f"Name {UserName}  docId :  {DocId} \n")
        # PhoneNumber = str(data['main']['data'][i][PhoneKey])
        PhoneNumber = PhoneNumber.replace('_vn', '').replace(
            '(', '').replace(')', '').replace('-', '')
        EstablishedData = data['main']['data'][i][attr_key]['node2']

        lattitude = data['main']['data'][i][latKey]
        longitude = data['main']['data'][i][longKey]

        try:
            rating = EventData['rating']
            ratingCount = EventData['rating_cnt']

            city = EventData['city']
            Dcity = EventData['dcity']
            area = EventData['area']
            pincode = EventData['pin']
        except:
            continue
        all_data.append({
            "Name": UserName,
            "Type": UserType,
            "email":gmail,
            "PhoneNumber": PhoneNumber,
            "rating": rating,
            "ratingCount": ratingCount,
            "Established": EstablishedData,
            "Area":area,
            "city": city,
            "Dcity": Dcity,
            "pincode": pincode,
            "lattitude": lattitude,
            "longitude": longitude,
            "FullAddress": UserAdress+" "+fulladdres
        })
        # current_page += 1
    return all_data

# Create a FastAPI app
app = FastAPI()

# Define a route to return all data as JSON
#http://localhost:8000/get_all_data?qurry=<your_query_here>&searcharea=<your_search_area_here>&searchCity=<your_search_city_here>@current_page=1
# http://localhost:8000/get_all_data?qurry=Computers&searcharea=Delhi&searchCity=Delhi&current_page=2
@app.get("/get_all_data")
def get_all_data(q: str = Query(...), searcharea: str = Query(...), searchCity: str = Query(...), current_page: str = Query(...)):
    # print(qurry, searcharea, searchCity)
    all_data = extract_data(q, searcharea, searchCity,current_page)  # Call your existing function to get all data
    return {"data": all_data}

if __name__ == "__main__":
    
      uvicorn.run(app, host="0.0.0.0", port=3000)


        





        
