import requests
import json

# response = urllib.request.urlopen('http://pulse-rest-testing.herokuapp.com/')
# print(response.read())

# class FirstScript():
#     url = 'http://pulse-rest-testing.herokuapp.com/books/'
#     # Создаём книгу POST /books/, вы запоминаете его id.
#     params = {'title': 'Second Book', 'author': 'T.Red'}
#     post = requests.post(url, data=params)
#     d = post.json()
#     d_id = d["id"]
#     print(d_id)
#
#     # Проверяете, что она создалась и доступна по ссылке GET/books/[id]
#     get_id = requests.get(url + str(d_id))
#     print(get_id.json())
#
#     # Проверяете, что она есть в списке книг по запросу GET /books/
#     get = requests.get(url=url)
#     get_j = get.json()
#     for i in get_j:
#         book_id = i["id"]
#         if book_id == d_id:
#             print("Book data: ", i)
#
#     # Изменяете данные этой книги методом PUT /books/[id]/
#     new_params = {'title': '2 Book', 'author': 'T.Red'}
#     put = requests.put(url=url + str(d_id) + '/', data=new_params)
#     put_resp = put.json()
#
#     # Проверяете, что она изменилась и доступна по ссылке /books/[id]
#     get_id_put = requests.get(url + str(d_id))
#     print(get_id_put.json())
#
#     # Проверяете, что она есть в списке книг по GET /books/ с новыми данными.
#     get_list = requests.get(url)
#     get_resp = get_list.json()
#     for i in get_resp:
#         book_id = i["id"]
#         if book_id == d_id:
#             print("Book new data: ", i)
#
#     # Удаляете эту книгу методом DELETE /books/[id].
#     get_for_delete = requests.get(url)
#     get_resp_delete = get_for_delete.json()
#     for i in get_resp_delete:
#         author = i["author"]
#         book_id = i["id"]
#         if author == "T.Red":
#             delete = requests.delete(url=url + str(book_id))
#
#     get_delete = requests.get(url)
#     resp_delete = get_delete.json()
#     for i in resp_delete:
#         book_id = i["id"]
#         if book_id == d_id:
#             print("Book for delete: ", i)


class SecondScript():
    url_role = 'http://pulse-rest-testing.herokuapp.com/roles/'
    url = 'http://pulse-rest-testing.herokuapp.com/books/'
    # Создаём тестовую книгу
    params = {'title': 'Test data', 'author': 'T.Red'}
    post = requests.post(url, data=params)
    book = post.json()
    d_id = book["id"]
    print(book)

    # Создаём книгу POST /books/, вы запоминаете его id.
    role_param = {'name': "T.Red",
                  'type': "Test data",
                  'level': 50}
    post = requests.post(url=url_role, data=role_param)
    d = post.json()
    d_id = d["id"]
    print(d_id)

