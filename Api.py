import uvicorn
import random
import uuid

from pydantic import BaseModel, Field
from typing import Annotated , List

from fastapi.responses import FileResponse , JSONResponse ,HTMLResponse 
from fastapi import FastAPI , HTTPException , Request , Form , Depends , APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import UploadFile, File, Form, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from fastapi.responses import RedirectResponse



from main import *
from BaseModel import *
from Account import *
from Product import *
from Promotion import *
from Order import *
from Customer import *
from Payment import *
from Apple import *
from Apple import *
from Cart import *
from Category import *
from Help import *
from Address import *


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# เพิ่ม session middleware เข้าไปใน FastAPI
app.add_middleware(SessionMiddleware, secret_key="siasasasas")


# main
@app.get("/", tags=['root'], response_class=HTMLResponse)
async def root(request: Request):
    product_list = apple.get_product_list()
    product_list_3item = product_list[:3]  # Slicing the list in Python
    return templates.TemplateResponse(
        request=request, name="index.html" , context={"product_list_3item":product_list_3item}
    )


# ------- category----------

# see category
@app.get("/category", tags=["category"] , response_class=HTMLResponse)
async def see_category(request: Request):
    category_list = apple.get_category_list()
    return templates.TemplateResponse(
        request=request, name="categories.html", context={"category_list": category_list}
    )

# see category detail
@app.get("/category/{category_name}", tags=["category"] , response_class=HTMLResponse)
async def see_category_detail(request: Request , category_name:str):
    category = apple.search_category_from_name(category_name)
    product_list = apple.get_product_list_from_category(category)
    if category is None: 
        return HTMLResponse("<script>window.location.href = '/category'</script>")
    return templates.TemplateResponse(
        request=request, name="categories_detail.html", context={"category": category , "product_list": product_list }
    )
  

# ------- product ----------

# see product 
@app.get("/product", tags=["product"],response_class=HTMLResponse)
async def see_all_product(request: Request):
    product_list = apple.get_product_list()
    return templates.TemplateResponse(
        request=request, name="product_all.html", context={"product_list": product_list}
    )
    
# see details product
@app.get("/product/{product_name}" ,tags=["product_detail"],response_class=HTMLResponse)
async def see_product_detail(request: Request , product_name:str ):
    user_email = apple.check_session(request)
    product = apple.search_product_from_name(product_name)
    customer_id = None
    if  user_email is not None :
        customer_id = apple.search_customer_from_email(user_email).get_customer_id()
    if product is not None :
        return templates.TemplateResponse(
            request=request, name="product_detail.html" , context={"product": product ,"user_email": user_email ,"customer_id" : customer_id}
        )
    return HTMLResponse("<script>window.location.href = '/product'</script>")
    

#add product to cart
@app.post("/product" ,tags=["product_to_cart"] ,response_class=HTMLResponse)
async def product_to_cart(request: Request , product_id: Annotated[int, Form()]):
    user_email = apple.check_session(request)
    if user_email is None :
        return HTMLResponse("<script>window.location.href = '/login'</script>")
    customer = apple.search_customer_from_email(user_email)
    customer_id = customer.get_customer_id()
    if apple.add_product_to_cart(product_id , customer_id):
        return HTMLResponse("<script>window.location.href = '/cart'</script>")
    else:
        raise Exception("eror product to cart")


# -----------Account---------------
# Account
@app.get("/account" ,tags=["Account"],response_class=HTMLResponse)
async def see_account(request: Request  ):
    user_email = apple.check_session(request)
    customer_id = None
    if apple.search_customer_from_email(user_email) is not None :
        customer_id = apple.search_customer_from_email(user_email).get_customer_id()
        customer = apple.search_customer_from_id(customer_id)
        return templates.TemplateResponse(
            request=request, name="account.html" , context={ "user_email": user_email ,"customer" : customer}
        )
    return HTMLResponse("<script>window.location.href = '/login'</script>")


# --------cart ----------------

# see cart 
@app.get("/cart" ,tags=["cart"] ,response_class=HTMLResponse)
async def see_cart(request: Request):
    user_email = apple.check_session(request)
    if user_email is None :
        return HTMLResponse("<script>window.location.href = '/login'</script>")
    customer = None
    total_items = 0
    if apple.search_customer_from_email(user_email) is not None :
        customer = apple.search_customer_from_email(user_email)
        total_items = len(customer.search_cart_from_status().get_product_list())
        customer.search_cart_from_status().calculates_amount()
        cart = customer.search_cart_from_status()
        total_amount = customer.search_cart_from_status().get_amount()
    return templates.TemplateResponse(
        request=request, name="cart.html" , context={"customer": customer  , "cart":cart , "total_items": total_items ,"total_amount" : total_amount}
    )

# delete product in cart
@app.post('/cart/delete/',tags=["cart"], response_class=HTMLResponse)
async def delete_product_in_cart(request: Request, product_no : Annotated[int, Form()]):
    user_email = apple.check_session(request)
    if apple.search_customer_from_email(user_email) is not None:
        customer = apple.search_customer_from_email(user_email)
        cart_product_list = customer.search_cart_from_status().get_product_list()
        print(product_no)
        product_no = product_no - 1
        if 0 <= product_no < len(cart_product_list):
            del cart_product_list[product_no]
            return HTMLResponse("<script>window.location.href = '/cart'</script>")
    return 'error'
        
# fill details before make order 
@app.get("/cartdetail", tags=["cart"] ,response_class=HTMLResponse)
async def fill_details_before_make_order(request: Request):
    user_email = apple.check_session(request)
    if user_email is not None:
        if apple.search_customer_from_email(user_email) is not None:
            customer = apple.search_customer_from_email(user_email)
            cart = customer.search_cart_from_status()
            total_items = len(customer.search_cart_from_status().get_product_list())
            customer.search_cart_from_status().calculates_amount()
            total_amount = customer.search_cart_from_status().get_amount()
        return templates.TemplateResponse(
            request=request, name="cart_detail.html", context={"customer":customer , "cart":cart , "total_amount": total_amount , "total_items": total_items}
        )
    return HTMLResponse("<script>window.location.href = '/login'</script>")

# -------  promotion ----------
# see promotion (class)
@app.get("/promotion", tags=["promotion"] ,response_class=HTMLResponse)
async def see_all_promotion(request: Request):
    return templates.TemplateResponse(
        request=request, name="promotion_all.html", context={"promotion_list": apple.get_promotion_list()}
    )

# use promo code
@app.post("/codepormo", tags=["promotion"] ,response_class=HTMLResponse)
async def use_promo_code(request: Request ,customer_id: Annotated[int, Form()],code: Annotated[str, Form()]):
    success = apple.use_promotion_code(customer_id,code)
    if success:
        return HTMLResponse("<script>window.location.href = '/cart?act=codesucces'</script>")
    else:
        return HTMLResponse("<script>window.location.href = '/cart?act=Nocode'</script>")

# delete promotion in cart
@app.post('/codepormo/delete/',tags=["promotion"], response_class=HTMLResponse)
async def delete_promotion_in_cart(request: Request, promotion_no : Annotated[int, Form()]):
    user_email = apple.check_session(request)
    if apple.search_customer_from_email(user_email) is not None:
        customer = apple.search_customer_from_email(user_email)
        cart_promotion_list = customer.search_cart_from_status().get_promotion_list()
        print(promotion_no)
        promotion_no = promotion_no - 1
        if 0 <= promotion_no < len(cart_promotion_list):
            del cart_promotion_list[promotion_no]
            return HTMLResponse("<script>window.location.href = '/cart'</script>")
    return 'error'
        
# -------- address ------------

# add address form
@app.get("/address", tags=["address"] ,response_class=HTMLResponse)
async def see_all_promotion(request: Request , page:str ):
    user_email = apple.check_session(request)
    if apple.search_customer_from_email(user_email) is not None:
        customer = apple.search_customer_from_email(user_email)
        if customer is not None:
             return templates.TemplateResponse (
                        request=request, name="address_crete.html" , context={"customer":customer , "page" : page}
                    )
    return 'error'

# add address 
@app.post('/address',tags=["address"], response_class=HTMLResponse)
async def see_all_promotion(
        request: Request,
        name_first  : Annotated[str, Form()] ,
        name_last  : Annotated[str, Form()] ,
        phone  : Annotated[str, Form()] ,
        homeid_detail  : Annotated[str, Form()] ,
        district : Annotated[str, Form()] ,
        amphoe  : Annotated[str, Form()] ,
        province : Annotated[str, Form()] ,
        zipcode  : Annotated[str, Form()] ,
        page : Annotated[str, Form()]
    ):
    user_email = apple.check_session(request)
    if apple.search_customer_from_email(user_email) is not None:
        customer = apple.search_customer_from_email(user_email)
        if customer is not None:
            address_id = int(uuid.uuid4())
            name = name_first + " " + name_last
            customer.add_address(Address(address_id, name ,phone, homeid_detail ,district , amphoe  ,province , zipcode))
            if page == "account" :
                return HTMLResponse("<script>window.location.href = '/account'</script>")
            else :
                return HTMLResponse("<script>window.location.href = '/cartdetail'</script>")
    return 'error'

    
# delelt address 
@app.post('/address/delete',tags=["address"], response_class=HTMLResponse)
async def delete_address(request: Request, address_id : Annotated[int, Form()] , page : Annotated[str, Form()]):
    user_email = apple.check_session(request)
    if apple.search_customer_from_email(user_email) is not None:
        customer = apple.search_customer_from_email(user_email)
        print(address_id)
        if customer.delete_address_from_id(address_id):
            if page == "account" :
                return HTMLResponse("<script>window.location.href = '/account'</script>")
            else :
                return HTMLResponse("<script>window.location.href = '/cartdetail'</script>")
    return 'error'


# -------- order ----------


# submit to make Order   
@app.post("/MakeOrder", tags=["Order"])
async def submit_to_make_order(customer_id : Annotated[int, Form()] , name : Annotated[str, Form()], phone : Annotated[str, Form()], address : Annotated[str, Form()]):
    order_id = apple.submit_to_make_order(customer_id , name, phone, address)
    order = apple.search_order_from_id(str(order_id))
    if order is not None:
        url = "<script>window.location.href = '/order/" + order_id +"'</script>"
        return HTMLResponse(url)
    else:
        return HTMLResponse("<script>window.location.href = '/cart?act=Makeordererror'</script>")
    
# see order all
@app.get("/order", tags=["Order"] ,response_class=HTMLResponse)
async def see_all_order(request: Request ):
    user_email = apple.check_session(request)
    if user_email is not None:
        if apple.search_customer_from_email(user_email) is not None:
            customer = apple.search_customer_from_email(user_email)
        return templates.TemplateResponse(
            request=request, name="order_all.html", context={"customer":customer}
        )
    return HTMLResponse("<script>window.location.href = '/login'</script>")

# see order detail
@app.get("/order/{order_id}", tags=["Order"], response_class=HTMLResponse)
async def see_order_detail(request: Request, order_id: str):
    user_email = apple.check_session(request)
    if user_email is None:
        return HTMLResponse("<script>window.location.href = '/login'</script>")
    customer = apple.search_customer_from_email(user_email)
    if customer is None:
        return HTMLResponse("<script>window.location.href = '/login'</script>")
    order = customer.search_order_from_id(str(order_id))
    if order is None:
        return HTMLResponse("<script>window.location.href = '/cart?act=Makeordererror&order'</script>")
    cart = order.get_cart()
    if cart is None:
        return HTMLResponse("<script>window.location.href = '/cart?act=Makeordererror&cart'</script>")
    return templates.TemplateResponse(
        request=request, name="order_detail.html", context={"customer": customer, "order": order, "cart": cart}
    )


#  cancel order
@app.post("/order/delete", tags=["Order"] ,response_class=HTMLResponse)
async def cancel_order(request: Request , order_id : Annotated[int, Form()] ):
    user_email = apple.check_session(request)
    if user_email is not None:
        if apple.search_customer_from_email(user_email) is not None:
            customer = apple.search_customer_from_email(user_email)
            if customer.delete_order_from_id(str(order_id)) :
                return HTMLResponse("<script>window.location.href = '/order'</script>")

    return HTMLResponse("<script>window.location.href = '/order?erororoor'</script>")


# --------payment --------------

# choose payment
@app.get("/payment/{order_id}", tags=["payment"] ,response_class=HTMLResponse)
async def choose_payment(request: Request , order_id : int):
    user_email = apple.check_session(request)
    if user_email is not None:
        if apple.search_customer_from_email(user_email) is not None:
            customer = apple.search_customer_from_email(user_email)
            order = customer.search_order_from_id(str(order_id))
            payment_list = apple.get_payment_list()
            if order is not None:
                return templates.TemplateResponse(
                    request=request, name="payment_choose.html", context={"customer":customer , "order":order , "payment_list":payment_list} 
                )
    return HTMLResponse("<script>window.location.href = '/order'</script>")

# go to payment
@app.get("/payment/{order_id}/{payment_id}", tags=["payment"] ,response_class=HTMLResponse)
async def payment(request: Request , order_id : int , payment_id : int):
    user_email = apple.check_session(request)
    if user_email is not None:
        if apple.search_customer_from_email(user_email) is not None:
            customer = apple.search_customer_from_email(user_email)
            order = customer.search_order_from_id(str(order_id))
            payment = apple.search_payment_from_id(payment_id)
            if order is not None:
                order_amount = order.get_cart().get_amount()
                if payment.get_payment_type() == "Card" :
                    return templates.TemplateResponse(
                        request=request, name="payment_card.html", context={"customer":customer ,"order":order , "payment":payment , "order_amount" : order_amount} 
                    )
                elif payment.get_payment_type() == "QR" :
                    return templates.TemplateResponse(
                        request=request, name="payment_QR.html", context={"customer":customer ,"order":order , "payment":payment , "order_amount" : order_amount} 
                    )
                elif payment.get_payment_type() == "Bank" :
                    return templates.TemplateResponse(
                        request=request, name="payment_bank.html", context={"customer":customer ,"order":order , "payment":payment , "order_amount" : order_amount} 
                    )
    return HTMLResponse("<script>window.location.href = '/order'</script>")


@app.post("/payment", tags=["payment"] ,response_class=HTMLResponse)
async def payment(request: Request , customer_id : Annotated[int, Form()] , order_id : Annotated[int, Form()] , payment_id : Annotated[int, Form()] ):
    if apple.payment(customer_id , order_id, payment_id):
        url = "<script>window.location.href = '/order/"+ str(order_id) +"?act=PaymentSuccess'</script>"
        return HTMLResponse(url)
    else:
        url = "<script>window.location.href = '/payment/"+str(order_id)+"?act=PaymentUnsuccess'</script>"
        return HTMLResponse(url)
    
# -------- help --------------

# see help 
@app.get("/help", tags=["help"] ,response_class=HTMLResponse)
async def see_help(request: Request):
    help_list = apple.get_help_list()
    return templates.TemplateResponse(
        request=request, name="help.html", context={"help_list": help_list} 
    )
    
# see help details
@app.get("/help/{help_id}", tags=["help"] ,response_class=HTMLResponse)
async def see_help(request: Request , help_id: int):
    help = apple.search_help_from_id(help_id)
    if help is not None :
        return templates.TemplateResponse(
            request=request, name="help_detail.html", context={"help": help} 
        )
    return HTMLResponse("<script>window.location.href = '/help'</script>")
    
# ------- Contact --------------
# see Contact
@app.get("/contact.", tags=["contact"] ,response_class=HTMLResponse)
async def see_contact(request: Request ):
    return templates.TemplateResponse(
        request=request, name="contact.html"
    )
    

# -------Login---------------

# login form
@app.get("/login", tags=['login'])
async def login_form() -> FileResponse:
    return FileResponse("templates/login.html")

# login
@app.post("/login", tags=["login"] )
async def login(email: Annotated[str, Form()], password: Annotated[str, Form()] , request: Request):
    user_type = apple.login(email, password) 
    request.session.clear()
    if user_type is None:
        return HTMLResponse("<script>window.location.href = '/login?act=LoginFailure'</script>")
    elif user_type == "admin":
        user = apple.search_admin_from_email(email)
        request.session['user_email'] = user.get_email()
        request.session['user_type'] = "admin"
        return HTMLResponse("<script>window.location.href = '/admin?act=LoginSuccess'</script>")
    else:
        user = apple.search_customer_from_email(email)
        request.session['user_email'] = user.get_email()
        request.session['user_type'] = "customer"
        return HTMLResponse("<script>window.location.href = '/?act=LoginSuccess'</script>")

# -------signup ----------------

# signup form
@app.get("/signup", tags=['signup'])
async def signup_form() -> FileResponse:
    return FileResponse("templates/signup.html")

# signup 
@app.post("/signup", tags=['signup'] ,response_class=HTMLResponse)
async def signup(name: Annotated[str, Form()], email: Annotated[str, Form()] ,password: Annotated[str, Form()], birthday: Annotated[str, Form()] , request: Request):
    customer_id = generate_uuid_int_10_digits()
    apple.add_customer(Customer(customer_id, email, password, name, birthday ))
    print(customer_id)
    return HTMLResponse("<script>window.location.href = '/login?act=Signupsuccess'</script>")

# -------logout-----------------

# logout
@app.get("/logout", tags=["logout"])
async def logout(request: Request):
    request.session.clear()
    print("Logout")
    return RedirectResponse(url="/?act=LogoutSuccess")


# ------------------------------------------------------- Admin ----------------------------------------------------

# Admin Dashboard
@app.get("/admin", tags=['admin'], response_class=HTMLResponse)
async def admin(request: Request):
    user_email = apple.check_session(request)
    admin = apple.search_admin_from_email(user_email)
    user_type = apple.check_session_type(request)
    if admin is None:
        return HTMLResponse("<script>window.location.href = '/login'</script>")
    return templates.TemplateResponse(
        request=request, name="admin/index.html" ,context={"user_email": user_email , "user_type": user_type}
    )

# ----------products ----------
# Admin product
@app.get("/admin/product", tags=['admin_product'], response_class=HTMLResponse)
async def admin_see_all_product(request: Request):
    user_email = apple.check_session(request)
    admin = apple.search_admin_from_email(user_email)
    if admin is None:
        return HTMLResponse("<script>window.location.href = '/login'</script>")
    product_list = apple.get_product_list()
    category_list = apple.get_category_list()
    return templates.TemplateResponse(
        request=request, name="admin/product.html" ,context={"product_list": product_list , "category_list": category_list}
    )

# crete product
@app.post("/admin/product", tags=['admin_product'], response_class=HTMLResponse)
async def admin_crete_product(
        request: Request ,
        product_category_id : Annotated[int, Form()] ,
        product_name : Annotated[str, Form()] ,
        product_detail : Annotated[str, Form()] ,
        product_amount : Annotated[int, Form()] ,
        product_date_opening : Annotated[str, Form()] ,
        product_quantity : Annotated[int, Form()] ,
        product_img : Annotated[str, Form()] 
    ):
    user_email = apple.check_session(request)
    admin = apple.search_admin_from_email(user_email)
    if admin is None:
        return HTMLResponse("<script>window.location.href = '/login'</script>")
    category = apple.search_category_from_id(product_category_id)
    product_id = generate_uuid_int_8_digits()
    apple.add_product(Product(product_id , category , product_name , product_detail, product_amount , product_date_opening, product_quantity , product_img))
    return HTMLResponse("<script>window.location.href = '/admin/product'</script>")

# edit product form
@app.get("/admin/product/{product_id}", tags=['admin_product'], response_class=HTMLResponse)
async def admin_see_all_product(request: Request , product_id : int):
    user_email = apple.check_session(request)
    admin = apple.search_admin_from_email(user_email)
    if admin is None:
        return HTMLResponse("<script>window.location.href = '/login'</script>")
    product = apple.search_product_from_id(product_id)
    category_list = apple.get_category_list()
    return templates.TemplateResponse(
        request=request, name="admin/product_edit.html" ,context={"product": product , "category_list": category_list}
    )

# edit product
@app.post("/admin/product/edit", tags=['admin_product'], response_class=HTMLResponse)
async def admin_edit_product(
        request: Request ,
        product_id : Annotated[int, Form()] ,
        product_category_id : Annotated[int, Form()] ,
        product_name : Annotated[str, Form()] ,
        product_detail : Annotated[str, Form()] ,
        product_amount : Annotated[int, Form()] ,
        product_date_opening : Annotated[str, Form()] ,
        product_quantity : Annotated[int, Form()] ,
        product_img : Annotated[str, Form()] 
    ):
    user_email = apple.check_session(request)
    admin = apple.search_admin_from_email(user_email)
    if admin is None:
        return HTMLResponse("<script>window.location.href = '/login'</script>")
    category = apple.search_category_from_id(product_category_id)
    apple.edit_product_from_id(product_id , category , product_name , product_detail , product_amount , product_date_opening , product_quantity ,product_img)
    return HTMLResponse("<script>window.location.href = '/admin/product'</script>")

# delete product
@app.post("/admin/product/delete", tags=['admin_order'], response_class=HTMLResponse)
async def admin_delete_product(request: Request , product_id : Annotated[int, Form()] ):
    user_email = apple.check_session(request)
    admin = apple.search_admin_from_email(user_email)
    if admin is None:
        return HTMLResponse("<script>window.location.href = '/login'</script>")
    apple.delete_product_from_id(product_id)
    return HTMLResponse("<script>window.location.href = '/admin/product'</script>")


# -----------category------------
# Admin category
@app.get("/admin/category", tags=['admin_category'], response_class=HTMLResponse)
async def admin_see_all_category(request: Request):
    user_email = apple.check_session(request)
    admin = apple.search_admin_from_email(user_email)
    if admin is None:
        return HTMLResponse("<script>window.location.href = '/login'</script>")
    category_list = apple.get_category_list()
    return templates.TemplateResponse(
        request=request, name="admin/category.html" ,context={"category_list": category_list}
    )

# crete category
@app.post("/admin/category", tags=['admin_category'], response_class=HTMLResponse)
async def admin_crete_category(
        request: Request ,
        category_name : Annotated[str, Form()] ,
        category_detail : Annotated[str, Form()] ,
        category_img : Annotated[str, Form()]
    ):
    user_email = apple.check_session(request)
    admin = apple.search_admin_from_email(user_email)
    if admin is None:
        return HTMLResponse("<script>window.location.href = '/login'</script>")
    category_id = generate_uuid_int_8_digits()
    apple.add_category(Category(category_id , category_name , category_detail , category_img))
    return HTMLResponse("<script>window.location.href = '/admin/category'</script>")


# delete category
@app.post("/admin/category/delete", tags=['admin_order'], response_class=HTMLResponse)
async def admin_delete_category(request: Request , category_id : Annotated[int, Form()] ):
    user_email = apple.check_session(request)
    admin = apple.search_admin_from_email(user_email)
    if admin is None:
        return HTMLResponse("<script>window.location.href = '/login'</script>")
    apple.delete_category_from_id(category_id)
    return HTMLResponse("<script>window.location.href = '/admin/category'</script>")


# -----------Promotion------------
# Admin Promotion
@app.get("/admin/promotion", tags=['admin_promotion'], response_class=HTMLResponse)
async def admin_see_all_promotion(request: Request):
    user_email = apple.check_session(request)
    admin = apple.search_admin_from_email(user_email)
    if admin is None:
        return HTMLResponse("<script>window.location.href = '/login'</script>")
    promotion_list = apple.get_promotion_list()
    return templates.TemplateResponse(
        request=request, name="admin/promotion.html" ,context={"promotion_list": promotion_list}
    )

# crete promotion
@app.post("/admin/promotion", tags=['admin_promotion'], response_class=HTMLResponse)
async def admin_crete_promotion(
        request: Request ,
        promotion_name : Annotated[str, Form()] ,
        promotion_detail : Annotated[str, Form()] ,
        promotion_rate : Annotated[float, Form()] ,
        promotion_code : Annotated[str, Form()] 
    ):
    user_email = apple.check_session(request)
    admin = apple.search_admin_from_email(user_email)
    if admin is None:
        return HTMLResponse("<script>window.location.href = '/login'</script>")
    promotion_id = generate_uuid_int_8_digits()
    apple.add_promotion(Promotion(promotion_id, promotion_code  , promotion_detail ,promotion_name,  promotion_rate))
    return HTMLResponse("<script>window.location.href = '/admin/promotion'</script>")

# delete promotion
@app.post("/admin/promotion/delete", tags=['admin_order'], response_class=HTMLResponse)
async def admin_delete_promotion(request: Request , promotion_id : Annotated[int, Form()] ):
    user_email = apple.check_session(request)
    admin = apple.search_admin_from_email(user_email)
    if admin is None:
        return HTMLResponse("<script>window.location.href = '/login'</script>")
    apple.delete_promotion_from_id(promotion_id)
    return HTMLResponse("<script>window.location.href = '/admin/promotion'</script>")




# -----------Customer------------
# Admin customer
@app.get("/admin/customer", tags=['admin_customer'], response_class=HTMLResponse)
async def admin_see_all_customer(request: Request):
    user_email = apple.check_session(request)
    admin = apple.search_admin_from_email(user_email)
    if admin is None:
        return HTMLResponse("<script>window.location.href = '/login'</script>")
    customer_list = apple.get_customer_list()
    return templates.TemplateResponse(
        request=request, name="admin/customer.html" ,context={"customer_list": customer_list}
    )

# -----------order------------
# Admin order
@app.get("/admin/order", tags=['admin_order'], response_class=HTMLResponse)
async def admin_see_all_order(request: Request):
    user_email = apple.check_session(request)
    admin = apple.search_admin_from_email(user_email)
    if admin is None:
        return HTMLResponse("<script>window.location.href = '/login'</script>")
    order_list = apple.get_all_order_list()
    return templates.TemplateResponse(
        request=request, name="admin/order.html" ,context={"order_list": order_list}
    )

# Admin order details page
@app.get("/admin/order/{order_id}", tags=['admin_order'], response_class=HTMLResponse)
async def admin_see_order_detail(request: Request , order_id:int):
    user_email = apple.check_session(request)
    admin = apple.search_admin_from_email(user_email)
    if admin is None:
        return HTMLResponse("<script>window.location.href = '/login'</script>")
    order = apple.search_order_from_id(str(order_id))
    cart =  order.get_cart()
    return templates.TemplateResponse(
        request=request, name="admin/order_detail.html" ,context={"order": order , "cart" : cart}
    ) 

# Admin order update status
@app.post("/admin/order/updatestatus", tags=['admin_order'], response_class=HTMLResponse)
async def admin_update_order_status(request: Request , order_id : Annotated[int, Form()] , tracking_number : Annotated[str, Form()] , logistic : Annotated[str, Form()]):
    user_email = apple.check_session(request)
    admin = apple.search_admin_from_email(user_email)
    if admin is None:
        return HTMLResponse("<script>window.location.href = '/login'</script>")
    order = apple.search_order_from_id(str(order_id))
    order.set_status(2)
    order.set_logistic(logistic)
    order.set_tracking_number(tracking_number)
    url = "<script>window.location.href = '/admin/order/" + str(order_id) + "'</script>"
    return HTMLResponse(url)

# Admin cancel order
@app.post("/admin/order/cancel", tags=['admin_order'], response_class=HTMLResponse)
async def admin_cancel_order(request: Request , order_id : Annotated[int, Form()] ):
    user_email = apple.check_session(request)
    admin = apple.search_admin_from_email(user_email)
    if admin is None:
        return HTMLResponse("<script>window.location.href = '/login'</script>")
    apple.delete_order_from_id(str(order_id)) 
    return HTMLResponse("<script>window.location.href = '/admin/order'</script>")


# -----------help------------
# Admin help
@app.get("/admin/help", tags=['admin_help'], response_class=HTMLResponse)
async def admin_see_all_help(request: Request):
    user_email = apple.check_session(request)
    admin = apple.search_admin_from_email(user_email)
    if admin is None:
        return HTMLResponse("<script>window.location.href = '/login'</script>")
    help_list = apple.get_help_list()
    return templates.TemplateResponse(
        request=request, name="admin/help.html" ,context={"help_list": help_list}
    )

# crete help
@app.post("/admin/help", tags=['admin_help'], response_class=HTMLResponse)
async def admin_crete_help(
        request: Request ,
        help_name : Annotated[str, Form()] ,
        help_detail : Annotated[str, Form()] 
       
    ):
    user_email = apple.check_session(request)
    admin = apple.search_admin_from_email(user_email)
    if admin is None:
        return HTMLResponse("<script>window.location.href = '/login'</script>")
    help_id = generate_uuid_int_8_digits()
    apple.add_help(Help(help_id, help_name ,help_detail))
    return HTMLResponse("<script>window.location.href = '/admin/help'</script>")

# delete help
@app.post("/admin/help/delete", tags=['admin_order'], response_class=HTMLResponse)
async def admin_delete_help(request: Request , help_id : Annotated[int, Form()] ):
    user_email = apple.check_session(request)
    admin = apple.search_admin_from_email(user_email)
    if admin is None:
        return HTMLResponse("<script>window.location.href = '/login'</script>")
    apple.delete_help_from_id(help_id)
    return HTMLResponse("<script>window.location.href = '/admin/help'</script>")


# -------Error-----------------

 # เพิ่ม middleware สำหรับจัดการข้อผิดพลาดทั้งหมด
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return HTMLResponse(f"<h1>Error: {exc.detail}</h1>", status_code=exc.status_code)

# เพิ่ม middleware สำหรับจัดการข้อผิดพลาดทั่วไป
@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return HTMLResponse("<h1>Internal Server Error</h1>", status_code=500)



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
