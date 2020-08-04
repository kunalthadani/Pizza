from django.urls import path

from . import views

urlpatterns = [
	path("confirm",views.confirm,name = "confirm"),
	path("previous",views.previous_orders,name = "previous"),
	path("orders",views.orders,name = "orders"),
	path("place",views.place,name = "place"),
	path("cart",views.added_cart,name = "cart"),
	path("page/<int:page_id>",views.page,name = "page"),
	path("logout/",views.logout_view,name = "logout"),
	path("login/",views.login_view,name = "login"),
	path("registered/",views.registered,name="registered"),
	path("register/", views.register, name = "register"),
    path("", views.index, name="index")
]