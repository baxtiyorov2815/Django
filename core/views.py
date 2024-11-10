from django.shortcuts import HttpResponse # type: ignore


def user_info(request, user_id, username):
    text = f"<b>User ID: {user_id}</br>Username: {username}</b>"
    return HttpResponse(text)


def product_info(request, product_id=1, product_name="Nomalum"):
    text = f"<b>Product ID: {product_id}</br> Productname: {product_name}</b>"
    return HttpResponse(text)
