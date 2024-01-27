# Поиск в интернете:
# Создайте программу, которая позволяет пользователю вводить запрос, а затем отображает результаты поиска из
#  поисковой системы, используя API.

# import requests


# from pppp import API_TOKEN


# def search(query, api_key, cx):
#     base_url = "https://www.googleapis.com/customsearch/v1"
#     params = {
#         'q': query,
#         'key': api_key,
#         'cx': cx
#     }


#     try:
#         response = requests.get(base_url, params=params)
#         data = response.json()
#         print(data)
#         if 'items' in data:
#             for index, item in enumerate(data['items'], 1):
#                 print(f"{index}. {item['title']}")
#                 print(f"{item['link']}")
#         else:
#             print("Not found")
#     except Exception as e:
#         print(f"Error {e}")


# if __name__ == "__main__":
#     user_query = input("Введите запрос: ")
#     api_key = "62345a17f70ced95619a91ddf23c5e90" 
#     cx = "62345a17f70ced95619a91ddf23c5e90"  
#     search(user_query, api_key, cx)






# import requests

# # get the API KEY here: https://developers.google.com/custom-search/v1/overview
# API_KEY = "AIzaSyCZTbIYCXCM3PG_-l4akOQQNYYAeEE1RGc"
# # get your Search Engine ID on your CSE control panel
# SEARCH_ENGINE_ID = "<INSERT_YOUR_SEARCH_ENGINE_ID_HERE>"

# # the search query you want
# query = "python"
# # using the first page
# page = 1
# # constructing the URL
# # doc: https://developers.google.com/custom-search/v1/using_rest
# # calculating start, (page=2) => (start=11), (page=3) => (start=21)
# start = (page - 1) * 10 + 1
# url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
# data = requests.get(url).json()
# # get the result items
# search_items = data.get("items")
# # iterate over 10 results found
# for i, search_item in enumerate(search_items, start=1):
#     try:
#         long_description = search_item["pagemap"]["metatags"][0]["og:description"]
#     except KeyError:
#         long_description = "N/A"
#     # get the page title
#     title = search_item.get("title")
#     # page snippet
#     snippet = search_item.get("snippet")
#     # alternatively, you can get the HTML snippet (bolded keywords)
#     html_snippet = search_item.get("htmlSnippet")
#     # extract the page url
#     link = search_item.get("link")
#     # print the results
#     print("="*10, f"Result #{i+start-1}", "="*10)
#     print("Title:", title)
#     print("Description:", snippet)
#     print("Long description:", long_description)
#     print("URL:", link, "\n")

















































import requests

def google_search(query, api_key, cx):
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'cx': cx,
        'q': query
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if 'items' in data:
            for item in data['items']:
                print(f"Title: {item['title']}")
                print(f"Link: {item['link']}")
                print("\n")
        else:
            print("Нет результатов поиска.")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")

if __name__ == "__main__":
    user_query = input("Введите запрос для поиска: ")
    api_key = "AIzaSyCZTbIYCXCM3PG_-l4akOQQNYYAeEE1RGc" 
    cx = "8737dff7f91bf4346"  

    google_search(user_query, api_key, cx)
