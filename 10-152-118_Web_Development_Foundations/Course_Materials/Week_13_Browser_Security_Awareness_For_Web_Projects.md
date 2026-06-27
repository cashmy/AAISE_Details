# Week 13 Handout - Browser Security Awareness For Web Projects

**Course:** 10-152-118 Web Development Foundations  
**Purpose:** Prepare for Week 13 lecture and lab by recognizing common browser-facing security risks in beginner web projects.

---

## 1. Security Awareness In The Browser

This course is not replacing your security course.

In Web Development Foundations, the security focus is narrower:

```text
What can go wrong when a browser page accepts input, talks to other sites,
stores values, or handles login-like data?
```

The goal is awareness and safer habits, not full cybersecurity specialization.

This week focuses on browser-based risks such as:

- untrusted input
- unsafe output
- cross-site scripting (XSS)
- cross-site request forgery (CSRF)
- cross-origin resource sharing (CORS)
- browser storage
- login-like data such as tokens or session values

Useful mental model:

```text
"It works" is not the same as "it is safe."
```

---

## 2. Browser Trust Boundaries

A trust boundary is a place where information crosses from one context into
another.

In browser projects, do not automatically trust:

- user input
- URL parameters
- API responses
- copied or pasted text
- values from `localStorage` or `sessionStorage`
- cookies or session-related values
- third-party scripts
- content inserted into the page

Beginner rule:

```text
If the information came from outside your code, slow down before using it.
```

This does not mean every outside value is dangerous. It means outside values
should be handled intentionally.

---

## 3. XSS: When Untrusted Content Becomes Code

XSS stands for cross-site scripting.

Attackers used XSS by finding places where websites displayed user-controlled
content and then causing the browser to treat that content like trusted page
code. A comment box, profile field, search result, or message area could become
dangerous if the site inserted untrusted content into the page unsafely.

For this course, think of XSS this way:

```text
XSS risk appears when untrusted input becomes page output in an unsafe way.
```

The dangerous pattern is not simply collecting input. The dangerous pattern is
allowing untrusted content to become executable page content.

### Safer Plain Text Output

If you want to display user text as text, prefer `textContent`.

```js
const output = document.querySelector("#message");

output.textContent = userInput;
```

This treats the value as text.

### Riskier HTML Output

Be careful with `innerHTML`.

```js
const output = document.querySelector("#message");

output.innerHTML = userInput;
```

This tells the browser to interpret the value as HTML. That can be risky if the
value came from a user or an outside system.

Beginner rule:

```text
Do not treat user input as trusted HTML.
```

---

## 4. CSRF: When A Browser Sends A Request The User Did Not Intend

CSRF stands for cross-site request forgery.

Attackers used CSRF by taking advantage of the fact that a browser may already
be logged in to another site. The attacker tried to trigger a request from the
victim's browser so the trusted site would receive an action the user did not
intend.

For this course, keep it conceptual:

```text
CSRF is about an unwanted action being sent from a user's browser while the
user is already logged in somewhere.
```

If a user is logged in, the browser may automatically include cookies or session
credentials with some requests.

That means:

```text
"The request came from the browser" does not always prove the user intended it.
```

In real applications, state-changing actions need protection.

Examples of state-changing actions:

- changing a password
- deleting an account
- submitting an order
- changing an email address
- transferring money

You do not need to implement CSRF protection in this course. You should
recognize why login state and browser requests can create risk.

---

## 5. CORS: Why Some Browser Requests Are Blocked

CORS stands for cross-origin resource sharing.

Students often meet CORS through an error message when trying to use an API.

CORS exists because websites once had few safe ways to share data across
different origins. Without browser-enforced boundaries, a malicious page could
try to read data from another site the user was logged in to.

For this course:

```text
CORS is the browser enforcing rules about which sites are allowed to read
responses from other origins.
```

An origin includes the protocol, domain, and port.

Examples:

```text
https://example.com
https://api.example.com
http://localhost:3000
```

These may be treated as different origins.

Important beginner correction:

```text
CORS is usually not fixed by random JavaScript in your page.
It is usually controlled by the server or API configuration.
```

If an API blocks your browser request because of CORS, that does not always mean
your code is wrong. It may mean the API is not configured for browser access
from your page.

---

## 6. Tokens, Cookies, And Browser Storage

Login-like data is sensitive.

Examples:

- passwords
- session cookies
- access tokens
- API keys
- authorization headers
- private account identifiers

For this course, think of a token as a proof-like value.

```text
If someone gets the token, they may be able to act like the user or application.
```

Beginner safety habits:

- Do not store real passwords in JavaScript.
- Do not store real passwords in `localStorage`.
- Do not paste real tokens into public code.
- Do not commit API keys or secrets.
- Do not assume front-end code is private.
- Treat browser storage as visible to someone using that browser.

Important:

```text
Front-end code is delivered to the user's browser.
Do not put secrets in code that runs in the browser.
```

---

## 7. Validation And Safer Output

Validation and safe output are related, but they are not the same.

```text
Validation checks whether input is reasonable.
Safe output controls how data is placed back into the page.
```

Validation examples:

- required fields
- expected format
- reasonable length
- expected number range
- allowed choices

Safer output examples:

- use `textContent` for plain text
- avoid `innerHTML` for untrusted content
- show clear error messages
- do not expose sensitive values in the page

Validation helps reduce bad input.

Safe output helps reduce risky display behavior.

You often need both.

---

## 8. Simulated Login Is Not Real Authentication

Later in the course, you may build a simple simulated login form.

That kind of example is useful for learning:

- form structure
- input validation
- success and error messages
- logged-in and logged-out interface states
- basic state changes

But a simulated login is not real authentication.

```text
Real authentication normally requires server-side checks, secure session
handling, and careful protection of credentials or tokens.
```

For this course:

- Do not store real passwords.
- Do not claim a simulated login is secure.
- Do not use real credentials in a class demo.
- Do not treat a front-end-only login as real access control.

The purpose is to learn interface and form behavior, not to build production
login security.

---

## 9. What To Focus On / What To Ignore For Now

Focus on:

- browser trust boundaries
- XSS awareness
- CSRF as a login/session risk concept
- CORS as a browser/server permission concept
- safer text output
- validation
- tokens and browser storage as sensitive
- the limits of front-end-only simulated login

Ignore for now:

- full authentication system design
- JWT implementation details
- cryptography
- server hardening
- penetration testing
- CSRF token implementation details
- CORS header configuration details
- enterprise security frameworks

The goal is to build safer habits while keeping the project scope beginner
appropriate.

---

## Reference Links

- MDN Cross-site scripting (XSS): https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting
- MDN CORS Guide: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS
- OWASP CSRF Prevention Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html
- OWASP JSON Web Token Testing: https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/10-Testing_JSON_Web_Tokens
