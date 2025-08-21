# 🛒 Secure Shopping Cart API with Admin Access

A simple **FastAPI** project that demonstrates **role-based access control (RBAC)** for a shopping cart system.  
Admins can manage products, while customers can browse and add products to their cart.

---

## 🚀 Features

- **Authentication & Authorization**
  - Token-based authentication (dummy tokens for demo)
  - Role checking (Admin vs Customer)

- **Endpoints**
  - `POST /admin/add_product/` → Admin only
  - `GET /products/` → Public (no authentication required)
  - `POST /cart/add/` → Authenticated users only

- **Persistence**
  - Products saved in `products.json`
  - Carts saved in `cart.json`

- **Dependency Injection**
  - Role-based access enforced using `Depends`

---

## 🔑 Authentication

This demo uses **dummy tokens**.
Use them in the `Authorization: Bearer <token>` header:

| Role     | Token            |
| -------- | ---------------- |
| Admin    | `admin-token`    |
| Customer | `customer-token` |

---

## 📌 API Endpoints

### 1. Add Product (Admin only)

```http
POST /admin/add_product/
Authorization: Bearer admin-token
Content-Type: application/json
```

**Body:**

```json
{
  "id": 1,
  "name": "Laptop",
  "price": 1200.50
}
```

---

### 2. Get Products (Public)

```http
GET /products/
```

**Response:**

```json
[
  {
    "id": 1,
    "name": "Laptop",
    "price": 1200.50
  }
]
```

---

### 3. Add to Cart (Customer only)

```http
POST /cart/add/
Authorization: Bearer customer-token
Content-Type: application/json
```

**Body:**

```json
{
  "product_id": 1,
  "quantity": 2
}
```
