# # import requests
# # import json
# #
# # headers = {
# #     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
# #     "Accept": "application/json, text/plain, */*",
# #     "device": "pc"
# # }
# #
# # url = 'https://lalafo.kg'
# #
# # response = requests.get(url)
# #
# # r = requests.get(url, headers=headers)
# # data = r.json()
# # print(data)
# # #
# # with open('Продажа авто.json', 'w', encoding='UTF-8') as file:
# #     json.dump(data, file, indent=2, ensure_ascii=False)
# #     print(f'Данные сохранены в lalafo_data.json')



# #
# import httpx
# import json
# import asyncio
# import time

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
#     "Accept": "application/json, text/plain, */*",
#     "device": "pc",
# }
# # url = "https://lalafo.kg/bishkek/q-%D0%9F%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0-%D0%B0%D0%B2%D1%82%D0%BE"
# # url = "https://lalafo.kg/kyrgyzstan/transport"
# url = "https://pagead2.googlesyndication.com/getconfig/sodar?sv=200&tid=gpt&tv=m202311150101&st=env"




# async def fetch_data(url):
#     async with httpx.AsyncClient() as client:
#         try:
#             response = await client.get(url, headers=headers)
#             response.raise_for_status()
#             return response.json()
#         except httpx.HTTPError as exc:
#             print(f"HTTP error occurred: {exc}")
#             return None
#         except json.JSONDecodeError:
#             print("Error decoding JSON response")
#             print(response.text)
#             return None

# async def save_data_to_file(data, filename):
#     with open(filename, "a", encoding="UTF-8") as file:
#         json.dump(data, file, indent=2, ensure_ascii=False)
#         print(f"Data saved to {filename}")

# async def main():
#     data = await fetch_data(url)

#     if data:
#         # await save_data_to_file(data, "Продажа квартир2.json")
#         await save_data_to_file(data, "Продажа авто2.json")
#         # await save_data_to_file(data, "Аренда квартир2.json")

#     await asyncio.sleep(3)

# if __name__ == "__main__":
#     start_time = time.time()
#     asyncio.run(main())
#     end_time = time.time()
#     print(f"Data saved. Execution time: {end_time - start_time} seconds.")





# import httpx
# import json
# import asyncio
# import time

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
#     "Accept": "application/json, text/plain, */*",
#     "device": "pc",
# }

# url = "https://lalafo.kg/kyrgyzstan/uslugi/q-%D0%B0%D0%B2%D1%82%D0%BE"
# # url = "https://pagead2.googlesyndication.com/getconfig/sodar?sv=200&tid=gpt&tv=m202311150101&st=env"


# async def fetch_data(url):
#     async with httpx.AsyncClient() as client:
#         try:
#             response = await client.get(url, headers=headers)
#             response.raise_for_status()
#             return response.json()
#         except httpx.HTTPError as exc:
#             print(f"HTTP error occurred: {exc}")
#             return None
#         except json.JSONDecodeError:
#             print("Error decoding JSON response")
#             print(response.text)
#             return None


# async def save_data_to_file(data, filename):
#     # Using 'w' mode to overwrite the file each time
#     with open(filename, "w", encoding="UTF-8") as file:
#         json.dump(data, file, indent=2, ensure_ascii=False)
#         print(f"Data saved to {filename}")


# async def main():
#     data = await fetch_data(url)

#     if data:
#         await save_data_to_file(data, "Продажа авто2.json")

#     # No specific reason for the sleep, you can remove it if not needed
#     await asyncio.sleep(3)

# if __name__ == "__main__":
#     start_time = time.time()
#     asyncio.run(main())
#     end_time = time.time()
#     print(f"Data saved. Execution time: {end_time - start_time} seconds.")




# import httpx
# import json
# import asyncio
# import time

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
#     "Accept": "application/json, text/plain, */*",
#     "device": "pc",
# }

# url = "https://lalafo.kg/kyrgyzstan/uslugi/q-%D0%B0%D0%B2%D1%82%D0%BE"

# async def fetch_data(url):
#     async with httpx.AsyncClient() as client:
#         try:
#             response = await client.get(url, headers=headers)
#             response.raise_for_status()
#             return response.json()
#         except httpx.HTTPError as exc:
#             print(f"HTTP error occurred. Status code: {exc.response.status_code}, Text: {exc.response.text}")
#             return None
#         except json.JSONDecodeError:
#             print("Error decoding JSON response")
#             print(response.text)
#             return None
#         except Exception as e:
#             print(f"An unexpected error occurred: {e}")
#             return None

# async def save_data_to_file(data, filename):
#     with open(filename, "w", encoding="UTF-8") as file:
#         json.dump(data, file, indent=2, ensure_ascii=False)
#         print(f"Data saved to {filename}")

# async def main():
#     data = await fetch_data(url)

#     if data:
#         await save_data_to_file(data, "Продажа авто2.json")

# if __name__ == "__main__":
#     start_time = time.time()
#     asyncio.run(main())
#     end_time = time.time()
#     print(f"Data saved. Execution time: {end_time - start_time} seconds.")



# import httpx
# import json
# import asyncio
# import time

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
#     "Accept": "application/json, text/plain, */*",
#     "device": "pc",
# }

# url = "https://lalafo.kg/kyrgyzstan/uslugi/q-%D0%B0%D0%B2%D1%82%D0%BE"
# url = "https://pagead2.googlesyndication.com/getconfig/sodar?sv=200&tid=gpt&tv=m202311150101&st=env"
# url = "https://pagead2.googlesyndication.com/getconfig/sodar?sv=200&tid=gpt&tv=m202311150101&st=env"




# async def fetch_data(url):
#     async with httpx.AsyncClient() as client:
#         try:
#             response = await client.get(url, headers=headers)
#             response.raise_for_status()
#             return response.json()
#         except httpx.HTTPError as exc:
#             print(f"HTTP error occurred. Status code: {exc.response.status_code}, Text: {exc.response.text}")
#             return None
#         except json.JSONDecodeError:
#             print("Error decoding JSON response")
#             print(response.text)
#             return None
#         except Exception as e:
#             print(f"An unexpected error occurred: {e}")
#             return None

# async def save_data_to_file(data, filename):
#     with open(filename, "w", encoding="UTF-8") as file:
#         json.dump(data, file, indent=2, ensure_ascii=False)
#         print(f"Data saved to {filename}")

# async def main():
#     while True:
#         data = await fetch_data(url)

#         if data:
#             await save_data_to_file(data, "Продажа авто2.json")

#         # Adjust the sleep duration based on your needs
#         await asyncio.sleep(60)  # Sleep for 60 seconds

# if __name__ == "__main__":
#     try:
#         asyncio.run(main())
#     except KeyboardInterrupt:
#         print("Script terminated by user.")



import aiohttp
import asyncio
import json
import time


start = time.time()


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "device": "pc"
}

lalafo_url = 'https://lalafo.kg/api/search/v3/feed/details/57367396?expand=url'

async def fetch_lalafo_data(session, url):
    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            data = await response.json()
            return data
        else:
            print(f"Error fetching data: {response.status}")
    return None

async def main():
    async with aiohttp.ClientSession() as session:
        lalafo_data = await fetch_lalafo_data(session, lalafo_url)
        if lalafo_data:
            with open('Продажа авто.json', 'a', encoding='UTF-8') as file:
                json.dump(lalafo_data, file, indent=2, ensure_ascii=False)
                print(f'Данные сохранены в Продажа авто.json')

if __name__ == '__main__':
    asyncio.run(main())
    
    



end_time = time.time()


res = end_time - start



