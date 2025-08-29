# 🛍️ E-Commerce API (FastAPI + SQLModel)

A modular **FastAPI** project implementing a simple **E-Commerce API** with:
- Product management (admin only)
- Shopping cart & checkout system
- JWT authentication
- Middleware to measure response time
- Orders backed up to `orders.json`

<img width="958" height="654" alt="image" src="https://github.com/user-attachments/assets/ad3d7b44-74dd-4cb4-a527-58e8f48dbf07" />

---

## ⚙️ Setup & Installation

1. Clone this repo or copy the files into a folder.
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
````

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Start the server:

   ```bash
   uvicorn main:app --reload
   ```
5. Visit API docs:
   👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🔑 Default Admin User

On first startup, a default admin account is created for testing:

```
username: admin
password: adminpass
```

⚠️ Change or remove this in production.

---

## 📦 Features

* **JWT Authentication**

  * Users can register & login
  * Admin-only endpoints protected
* **Products**

  * Admin can create products
  * Public can list all products
* **Cart**

  * Add products to cart
  * View cart
  * Checkout (deducts stock, creates order)
* **Orders**

  * Orders are saved in DB and appended to `orders.json`
* **Middleware**

  * Each response includes header: `X-Process-Time-ms`

---

## 🔗 API Endpoints

### 👤 Users

* `POST /users/register` → Register a new user
* `POST /users/token` → Login (returns JWT token)
* `GET /users/me` → Get current user info

### 📦 Products

* `POST /admin/products/` → Create product (admin only)
* `GET /products/` → List all products

### 🛒 Cart

* `POST /cart/add/?product_id={id}&quantity={n}` → Add product to cart
* `GET /cart/` → View current user’s cart
* `POST /cart/checkout/` → Checkout and create order

---

## 🚀 Example Workflow with Postman

1. **Login as admin**
   `POST /users/token`
   Body (x-www-form-urlencoded):

   ```
   username=admin
   password=adminpass
   ```

   Copy `access_token`.

2. **Create product**
   `POST /admin/products/`
   Headers:

   ```
   Authorization: Bearer <ADMIN_TOKEN>
   Content-Type: application/json
   ```

   Body (raw JSON):

   ```json
   {
     "name": "Laptop",
     "price": 1200.50,
     "stock": 10
   }
   ```

3. **Register buyer**
   `POST /users/register`

   ```
   username=alice
   password=alicepass
   ```

4. **Login buyer**
   `POST /users/token` → Copy `<ALICE_TOKEN>`

5. **Add to cart**
   `POST /cart/add/?product_id=1&quantity=2`
   Header:

   ```
   Authorization: Bearer <ALICE_TOKEN>
   ```

6. **Checkout**
   `POST /cart/checkout/`
   Header:

   ```
   Authorization: Bearer <ALICE_TOKEN>
   ```

📂 Result: Order saved in DB + appended to `orders.json`

---

## 🛠️ Notes

* `SECRET_KEY` in `auth.py` should be set via environment variable in production.
* For persistence, the DB uses **SQLite** (`database.db`).
* Middleware adds processing time:
  Example header → `X-Process-Time-ms: 3.12`
* Extend this API with pagination, product search, payment gateway, etc.

---

## 🧪 Run with cURL (alternative to Postman)

```bash
# Login as admin
curl -X POST "http://127.0.0.1:8000/users/token" \
  -F "username=admin" -F "password=adminpass"
```

```bash
# List products
curl http://127.0.0.1:8000/products/
```

```bash
# Checkout (with buyer token)
curl -X POST "http://127.0.0.1:8000/cart/checkout/" \
  -H "Authorization: Bearer <ALICE_TOKEN>"
```
