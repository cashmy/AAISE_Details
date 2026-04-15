# 🧭 WEEK 10 — APPROVED API LIST

**Working with External Data**

---

## 🔹 Why This List Exists

This week is about learning how to:

* retrieve data
* understand its structure
* use it in your application

> You are **not** being asked to search for or evaluate APIs.

To keep the focus clear, you must use **one of the approved APIs below**.

---

## 🔹 Rules

You must:

* use **one API from this list**
* retrieve data using `fetch`
* display meaningful data in your application

You may:

* choose the API that interests you most
* expand your project in Iteration 2

You may NOT:

* use APIs that require API keys or accounts
* use APIs not listed here (unless approved)

---

# 🟢 APPROVED APIS (RECOMMENDED)

---

## 1. JSONPlaceholder (Recommended Default)

**Base URL:**
[https://jsonplaceholder.typicode.com/](https://jsonplaceholder.typicode.com/)

### What it provides:

* users
* posts
* todos

### Example endpoints:

* `/users`
* `/posts`
* `/todos`

### Example use:

* display a list of users
* show post titles
* filter completed tasks

---

## 2. Bored API

**Endpoint:**
[https://www.boredapi.com/api/activity](https://www.boredapi.com/api/activity)

### What it provides:

* a random activity suggestion

### Example use:

* button → get activity
* display activity + type

---

## 3. Agify API

**Example:**
[https://api.agify.io?name=michael](https://api.agify.io?name=michael)

### What it provides:

* predicted age based on name

### Example use:

* user enters a name
* display predicted age

---

## 4. Dog API

**Endpoint:**
[https://dog.ceo/api/breeds/image/random](https://dog.ceo/api/breeds/image/random)

### What it provides:

* random dog images

### Example use:

* button → load image
* display image dynamically

---

# 🟡 OPTIONAL (MORE CHALLENGING)

Use these only if you are comfortable reading more complex data.

---

## 5. REST Countries

**Endpoint:**
[https://restcountries.com/v3.1/all](https://restcountries.com/v3.1/all)

### What it provides:

* country data (name, population, flags, etc.)

### Example use:

* display list of countries
* show country details

---

## 6. Open Meteo (Weather)

**Base URL:**
[https://api.open-meteo.com/](https://api.open-meteo.com/)

### What it provides:

* weather data

### Example use:

* display temperature for a location

---

# 🔧 Starter Example

```javascript
fetch("https://jsonplaceholder.typicode.com/users")
  .then(response => response.json())
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error("Error:", error);
  });
```

---

# 🧠 Key Reminder

> Data from an API does not arrive instantly.

Your job is to:

* wait for the data
* understand its structure
* use it correctly

---

# 🔑 Success Looks Like

* your application retrieves data successfully
* you display meaningful information (not raw JSON)
* your UI updates based on that data

---

# 🔥 Final Guidance

If you are stuck:

1. Log the data (`console.log(data)`)
2. Look at its structure
3. Choose one value to display
4. Build from there

---

> “Start simple. Get one piece of data working. Then expand.”

---

## 🧭 Additional Support (High Leverage)

> **“How to Read JSON”** - JSON READING WORKSHEET

---

