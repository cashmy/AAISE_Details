# Week 15 Handout - Basic Simulated Login Forms

**Course:** 10-152-118 Web Development Foundations  
**Purpose:** Prepare for Week 15 lecture and lab by building a simple login-like form interaction while understanding its limits.

---

## 1. What This Handout Is And Is Not

This handout shows a basic simulated login pattern for a beginner browser
project.

It is useful for practicing:

- form structure
- labels and inputs
- submit events
- validation
- success and error feedback
- logged-in and logged-out interface states
- simple state changes

It is not real authentication.

```text
Simulated login = a classroom pattern for learning form behavior.
Real login = server-side authentication, secure session handling, and protected credentials.
```

Do not use real passwords in this example.

Do not present this as production security.

---

## 2. Why Simulate Login In A Front-End Course?

Many capstone ideas need a user-facing account or login-like experience:

- a dashboard
- a saved preference page
- a profile screen
- a restricted-looking section
- a project tracker
- a mock admin panel

In this course, the goal is not to build real user accounts.

The goal is to understand how the interface behaves when the user appears to be
logged out or logged in.

Useful mental model:

```text
The login form collects input.
JavaScript checks the input.
The page shows success or error feedback.
The UI changes to match the current login state.
```

---

## 3. The Basic Page Structure

A simple login form needs:

- a form
- labels
- inputs
- a submit button
- a message area
- a place to show logged-in content

Example HTML:

```html
<form id="loginForm">
  <label for="username">Username</label>
  <input id="username" name="username" type="text" autocomplete="username">

  <label for="password">Password</label>
  <input id="password" name="password" type="password" autocomplete="current-password">

  <button type="submit">Sign in</button>
</form>

<p id="loginMessage"></p>

<section id="accountPanel" hidden>
  <h2>Account</h2>
  <p>Welcome back.</p>
  <button id="logoutButton" type="button">Sign out</button>
</section>
```

Notice:

- Labels are connected to inputs with `for` and `id`.
- The password field uses `type="password"`.
- The message area is separate from the form.
- The account panel starts hidden.

---

## 4. Prevent The Default Submit Behavior

HTML forms normally submit and reload or navigate the page.

For a JavaScript-controlled classroom example, prevent that default behavior.

```js
const loginForm = document.querySelector("#loginForm");

loginForm.addEventListener("submit", function (event) {
  event.preventDefault();
});
```

This lets JavaScript inspect the form values and update the page without a page
reload.

---

## 5. Validate Before Checking Login

Validation checks whether the input is reasonable before the program uses it.

For a beginner simulated login:

- username should not be empty
- password should not be empty
- password can have a minimum length

Example:

```js
function validateLogin(username, password) {
  if (username === "") {
    return "Username is required.";
  }

  if (password === "") {
    return "Password is required.";
  }

  if (password.length < 6) {
    return "Password must be at least 6 characters.";
  }

  return "";
}
```

This does not prove the user is real.

It only checks whether the input is reasonable enough for the next step.

---

## 6. Simulate A Login Check

A classroom simulation may compare input to simple demo values.

```js
function checkLogin(username, password) {
  return username === "student" && password === "practice";
}
```

Important:

```text
This is not secure.
Anyone can inspect front-end JavaScript.
```

This pattern is only for practicing form behavior and UI state.

---

## 7. Update The UI State

The page should show a different state after success or failure.

```js
const message = document.querySelector("#loginMessage");
const accountPanel = document.querySelector("#accountPanel");
const logoutButton = document.querySelector("#logoutButton");

function showLoggedIn() {
  message.textContent = "You are signed in for this demo.";
  accountPanel.hidden = false;
  loginForm.hidden = true;
}

function showLoggedOut() {
  message.textContent = "You are signed out.";
  accountPanel.hidden = true;
  loginForm.hidden = false;
}
```

This connects to Week 11:

```text
State is what the app currently knows.
The UI is what the app currently shows.
```

If the simulated login state changes, the page should change too.

---

## 8. Put The Pieces Together

```js
const loginForm = document.querySelector("#loginForm");
const message = document.querySelector("#loginMessage");
const accountPanel = document.querySelector("#accountPanel");
const logoutButton = document.querySelector("#logoutButton");

function validateLogin(username, password) {
  if (username === "") {
    return "Username is required.";
  }

  if (password === "") {
    return "Password is required.";
  }

  if (password.length < 6) {
    return "Password must be at least 6 characters.";
  }

  return "";
}

function checkLogin(username, password) {
  return username === "student" && password === "practice";
}

function showLoggedIn() {
  message.textContent = "You are signed in for this demo.";
  accountPanel.hidden = false;
  loginForm.hidden = true;
}

function showLoggedOut() {
  message.textContent = "You are signed out.";
  accountPanel.hidden = true;
  loginForm.hidden = false;
}

loginForm.addEventListener("submit", function (event) {
  event.preventDefault();

  const username = document.querySelector("#username").value.trim();
  const password = document.querySelector("#password").value;
  const validationMessage = validateLogin(username, password);

  if (validationMessage !== "") {
    message.textContent = validationMessage;
    return;
  }

  if (checkLogin(username, password)) {
    showLoggedIn();
  } else {
    message.textContent = "Username or password was not recognized.";
  }
});

logoutButton.addEventListener("click", function () {
  showLoggedOut();
});
```

Read this example for shape, not memorization.

The important pattern is:

```text
submit -> prevent reload -> read values -> validate -> check -> update UI
```

---

## 9. Should This Use localStorage?

Sometimes a demo uses `localStorage` to remember that a user appears signed in.

For example:

```js
localStorage.setItem("demoLoggedIn", "true");
```

This may be useful for showing persistence across a refresh.

But be careful:

```text
localStorage is not secure storage for real passwords, secrets, or tokens.
```

For this course, if you use `localStorage` with a simulated login, store only a
simple mock flag or harmless display preference.

Acceptable classroom example:

```text
demoLoggedIn = true
```

Do not store:

- real passwords
- real tokens
- API keys
- private account information

---

## 10. Capstone Guidance

If your capstone includes login-like behavior, describe it accurately.

Appropriate wording:

```text
This project includes a simulated login interface for practicing form validation
and logged-in/logged-out UI states.
```

Avoid wording like:

```text
This project has secure authentication.
```

Unless you are using real server-side authentication, do not claim real security.

Front-end-only login-like behavior can support a class project interface, but it
does not protect real data.

---

## 11. What To Focus On / What To Ignore For Now

Focus on:

- form structure
- labels and input types
- submit event handling
- validation
- success and error feedback
- logged-in and logged-out UI states
- honest explanation of simulated login limits

Ignore for now:

- real password storage
- user registration systems
- server-side authentication
- password hashing
- OAuth
- JWT implementation
- session cookie configuration
- production access control

The goal is a clear, honest interface pattern that prepares you for capstone
work without pretending to be real authentication.
