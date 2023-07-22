import curlify
import requests
import random


class BackendRequests:
    get_books_url = "https://demoqa.com/BookStore/v1/Books"
    authorization_token_url = "https://demoqa.com/Account/v1/GenerateToken"
    authorize_account_url = "https://demoqa.com/Account/v1/Authorized"
    post_book_url = "https://demoqa.com/BookStore/v1/Books"
    userID = "b5d1f0f7-6bac-4f5c-9be6-4437f506f8e2"
    name = "razvan"
    password = "123Abcdefg@"
    token = ""
    authorize_body = {
        "userName": name,
        "password": password
    }
    collectionOfIsbns = []
    book_list_id = []

    def generate_books(self):
        books_get = requests.get(self.get_books_url)
        for i in range(len(books_get.json()["books"])):
            self.book_list_id.append(books_get.json()["books"][i]['isbn'])
        number_of_books = random.randint(1, 8)

        for i in range(number_of_books):
            random.shuffle(self.book_list_id)
            self.collectionOfIsbns.append(self.book_list_id.pop())
        print(self.collectionOfIsbns)
        return self.collectionOfIsbns

    def authorize_account(self):
        post_authorize_account = requests.post(self.authorize_account_url, self.authorize_body)
        return post_authorize_account

    def generate_token(self):
        post_token = requests.post(self.authorization_token_url, self.authorize_body)
        self.token = post_token.json()["token"]
        print(self.token)

    def post_books(self):
        post_book_body = {
            "userId": self.userID,
            "collectionOfIsbns": [
                {
                    "isbn": self.generate_books()
                }
            ]
        }
        headers = {"Authorization": "Bearer " + self.token,
                   # "Content-Type": "application/json",
                   "User-Agent": "foo",
                   "accept": "application/json"}
        post_book_request = requests.post(self.post_book_url, post_book_body, headers=headers, stream=True, timeout=30)
        return post_book_request


backend_requests = BackendRequests()
backend_requests.authorize_account()
backend_requests.generate_token()
print(curlify.to_curl(backend_requests.authorize_account().request))
backend_requests.post_books()
