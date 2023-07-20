import requests
import random

create_user_url = "https://demoqa.com/Account/v1/User"
get_books_url = "https://demoqa.com/BookStore/v1/Books"

userID = "b5d1f0f7-6bac-4f5c-9be6-4437f506f8e2"
name = "razvan"
password = "123Abcdefg@"

books_get = requests.get(get_books_url)
book_list_id = []
for i in range(len(books_get.json()["books"])):
    book_list_id.append(books_get.json()["books"][i]['isbn'])

number_of_books = random.randint(1, 8)
collectionOfIsbns = []

for i in range(number_of_books):
    random.shuffle(book_list_id)
    collectionOfIsbns.append(book_list_id.pop())
# print(collectionOfIsbns)



##########################################
authorize_token_url = "https://demoqa.com/Account/v1/GenerateToken"
authorized_url = "https://demoqa.com/Account/v1/Authorized"

authorize_body = {
  "userName": name,
  "password": "123Abcdefg@"
}

post_authorized = requests.post(authorized_url, authorize_body)
post_authorize = requests.post(authorize_token_url, authorize_body)
print(post_authorize.json()["token"])
token = post_authorize.json()["token"]

post_book_url = "https://demoqa.com/BookStore/v1/Books"

post_book_body = {
  "userId" : userID,
  "collectionOfIsbns":[
    {
      "isbn" : collectionOfIsbns
    }
  ]
}

headers = {"Authorization" : "Bearer " + token}
post_book_request = requests.post(post_book_url, post_book_body, headers= headers)
print(post_book_request.json())