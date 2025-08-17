from fastapi import Request, Form, APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
import sqlite3

router = APIRouter()
templates = Jinja2Templates(directory="templates")


def get_db_connection():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row  
    return conn


@router.get("/")
def landing_redirect():
    return RedirectResponse(url="/register")


@router.get("/index", response_class=HTMLResponse)
async def home(request: Request):
    user = request.session.get("username")
    is_logged_in = bool(user)
    return templates.TemplateResponse("index.html", {"request": request, "is_logged_in": is_logged_in, "user": user})


@router.get("/shop", response_class=HTMLResponse)
async def shop_page(request: Request):
    user = request.session.get("username")
    is_logged_in = bool(user)
    return templates.TemplateResponse("shop.html", {"request": request, "is_logged_in": is_logged_in, "user": user})


@router.get("/blog", response_class=HTMLResponse)
async def blog_page(request: Request):
    user = request.session.get("username")
    is_logged_in = bool(user)
    return templates.TemplateResponse("blog.html", {"request": request, "is_logged_in": is_logged_in, "user": user})


@router.get("/contact", response_class=HTMLResponse)
async def contact_page(request: Request):
    user = request.session.get("username")
    is_logged_in = bool(user)
    return templates.TemplateResponse("contact.html", {"request": request, "is_logged_in": is_logged_in, "user": user})


@router.post("/contact")
async def handle_contact_form(request: Request, email: str = Form(...), message: str = Form(...)):
    conn = get_db_connection()
    conn.execute("INSERT INTO contacts (email, message) VALUES (?, ?)", (email, message))
    conn.commit()
    conn.close()
    return RedirectResponse(url="/contact", status_code=303)


@router.get("/about", response_class=HTMLResponse)
async def about_page(request: Request):
    user = request.session.get("username")
    is_logged_in = bool(user)
    return templates.TemplateResponse("about.html", {"request": request, "is_logged_in": is_logged_in, "user": user})


@router.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.post("/register")
def register_user(request: Request, username: str = Form(...), email: str = Form(...), password: str = Form(...)):
    conn = get_db_connection()
    try:
        conn.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        conn.commit()
        return RedirectResponse("/login", status_code=303)
    except Exception as e:
        return templates.TemplateResponse("register.html", {"request": request, "error": f"Registration failed: {str(e)}"})
    finally:
        conn.close()


@router.get("/login", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login")
def login_user(request: Request, username: str = Form(...), password: str = Form(...)):
    conn = get_db_connection()
    user = conn.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password)).fetchone()
    conn.close()
    if user:
        request.session["user_id"] = user["id"]
        request.session["username"] = user["username"]
        return RedirectResponse("/index", status_code=303)
    return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})


@router.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/register", status_code=303)


@router.post("/add-to-cart")
async def add_to_cart(request: Request, title: str = Form(...), price: str = Form(...), image: str = Form(...)):
    cart = request.session.get("cart", [])

    for item in cart:
        if item["title"] == title:
            item["quantity"] += 1
            break
    else:
        cart.append({"title": title, "price": price, "image": image, "quantity": 1})

    request.session["cart"] = cart
    return RedirectResponse(url="/cart", status_code=303)


@router.get("/cart", response_class=HTMLResponse)
async def view_cart(request: Request):
    cart = request.session.get("cart", [])
    total = sum(int(item["price"].replace("₹", "").replace(",", "")) * item["quantity"] for item in cart)
    return templates.TemplateResponse("cart.html", {"request": request, "cart": cart, "total": total})


@router.get("/wishlist", response_class=HTMLResponse)
async def wishlist_page(request: Request):
    wishlist = request.session.get("wishlist", [])
    user = request.session.get("username")
    return templates.TemplateResponse("wishlist.html", {"request": request, "wishlist": wishlist, "user": user})


@router.get("/profile", response_class=HTMLResponse)
async def profile(request: Request):
    user_id = request.session.get("user_id")
    if not user_id:
        return RedirectResponse("/login", status_code=303)

    conn = get_db_connection()
    user = conn.execute("SELECT username, email, password FROM users WHERE id = ?", (user_id,)).fetchone()
    conn.close()

    if not user:
        return RedirectResponse("/login", status_code=303)

    return templates.TemplateResponse("profile.html", {"request": request, "user_data": user})


@router.get("/forgot-password", response_class=HTMLResponse)
def show_password_reset_form(request: Request):
    if "user_id" not in request.session:
        return RedirectResponse("/login", status_code=303)
    return templates.TemplateResponse("forgot-password.html", {"request": request})


@router.post("/forgot-password", response_class=HTMLResponse)
def update_password(request: Request, new_password: str = Form(...), confirm_password: str = Form(...)):
    if "user_id" not in request.session:
        return RedirectResponse("/login", status_code=303)

    if new_password != confirm_password:
        return templates.TemplateResponse("forgot-password.html", {
            "request": request,
            "error": "Passwords do not match!"
        })

    conn = get_db_connection()
    conn.execute("UPDATE users SET password = ? WHERE id = ?", (new_password, request.session["user_id"]))
    conn.commit()
    conn.close()

    return templates.TemplateResponse("forgot-password.html", {
        "request": request,
        "success": "Password updated successfully!"
    })


@router.get("/features", response_class=HTMLResponse)
async def features(request: Request):
    return templates.TemplateResponse("features.html", {"request": request})
