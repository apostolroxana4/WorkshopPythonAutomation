import requests
import random
import pprint


class BackendRequests:
    get_books_url = "https://demoqa.com/BookStore/v1/Books"
    authorization_token_url = "https://demoqa.com/Account/v1/GenerateToken"
    authorize_account_url = "https://demoqa.com/Account/v1/Authorized"
    post_book_url = "https://demoqa.com/BookStore/v1/Books"
    userID = "b5d1f0f7-6bac-4f5c-9be6-4437f506f8e2"
    get_user_details_url = "https://demoqa.com/Account/v1/User/"+userID
    delete_books_url = "https://demoqa.com/BookStore/v1/Books?UserId="+userID
    name = "razvan"
    password = "123Abcdefg@"
    token = ""
    authorize_body = {
        "userName": name,
        "password": password
    }

    book_list_id = []

    def generate_books(self):
        collectionOfIsbns = []
        books_get = requests.get(self.get_books_url)
        for i in range(len(books_get.json()["books"])):
            self.book_list_id.append(books_get.json()["books"][i]['isbn'])


        random.shuffle(self.book_list_id)
        collectionOfIsbns.append(self.book_list_id.pop())
        return collectionOfIsbns

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
        headers = {"Authorization": "Bearer " + self.token}
        requests.post(self.post_book_url, json=post_book_body, headers=headers, timeout=30)

    def get_user_details(self):
        headers = {"Authorization": "Bearer " + self.token}
        get_user_info = requests.get(self.get_user_details_url, headers=headers)
        pprint.pprint(get_user_info.json()["books"])

    def delete_books(self):
        headers = {"Authorization": "Bearer " + self.token}
        requests.delete(self.delete_books_url, headers=headers)

backend_requests = BackendRequests()
backend_requests.authorize_account()
backend_requests.generate_token()
backend_requests.post_books()
backend_requests.post_books()

backend_requests.get_user_details()
backend_requests.delete_books()
backend_requests.get_user_details()
