#  quote-api-for-python

## A minimal RESTful API built with Python and Flask to manage inspirational quotes.

Supports `GET` and `POST` requests using in-memory storage.

---

###  `GET /quotes` — Retrieve all quotes

Returns a list of all saved quotes.

---

###  `POST /quotes` — Add a new quote with basic validation

**Request Body:**

```json
{
  "author": "Maya Angelou",
  "content": "Try to be a rainbow in someone’s cloud."
}



