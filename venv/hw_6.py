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
    book_id = book["id"]
    print(book)

    # Создаём книгу POST /role/, вы запоминаете его id.
    role_param = {'name': "T.Red",
                  'type': "Test data",
                  'level': 50,
                  'book': book_id}
    post = requests.post(url=url_role, data=role_param)
    role = post.json()
    role_id = role['id']
    print(role)

    # Проверяете, что она создалась и доступна по ссылке GET/role/[id]
    get_id = requests.get(url_role + str(role_id))
    print(get_id.json())

    # Проверяете, что она есть в списке книг по запросу GET /role/
    get = requests.get(url=url_role)
    get_j = get.json()
    for i in get_j:
        new_id = i["id"]
        if new_id == role_id:
            print("Book data: ", i)

    # Изменяете данные этой книги методом PUT /role/[id]/
    new_role_param = {'name': "T.Red",
                      'type': "New data",
                      'level': 90,
                      'book': book_id}
    put = requests.put(url=url_role + str(role_id) + '/', data=new_role_param)
    put_resp = put.json()

    # Проверяете, что она изменилась и доступна по ссылке /role/[id]
    get_id_put = requests.get(url_role + str(role_id))
    print(get_id_put.json())

    # Проверяете, что она есть в списке книг по GET /books/ с новыми данными.
    get_list = requests.get(url_role)
    get_resp = get_list.json()
    for i in get_resp:
        new_role_id = i["id"]
        if new_role_id == role_id:
            print("Book new data: ", i)

    # Удаляете эту книгу методом DELETE /books/[id].
    get_for_delete = requests.get(url_role)
    get_resp_delete = get_for_delete.json()
    for i in get_resp_delete:
        name = i["name"]
        role_id = i["id"]
        if name == "T.Red":
            delete = requests.delete(url=url_role + str(role_id))

    get_delete = requests.get(url_role)
    resp_delete = get_delete.json()
    for i in resp_delete:
        test_id = i["id"]
        if test_id == role_id:
            print("Book for delete: ", i)

    book_get_for_delete = requests.get(url)
    get_resp_delete = book_get_for_delete.json()
    for i in get_resp_delete:
        author = i["author"]
        book_id = i["id"]
        if author == "T.Red":
            delete = requests.delete(url=url + str(book_id))


