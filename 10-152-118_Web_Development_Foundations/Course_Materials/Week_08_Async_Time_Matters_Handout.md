# Week 8 Handout - Async: Time Matters

**Course:** 10-152-118 Web Development Foundations  
**Purpose:** Prepare for Week 8 lecture and lab by understanding why some browser behavior happens later.

---

## 1. Async Is About Time, Not Magic

Most beginner code feels like it runs one line at a time:

```js
console.log("First");
console.log("Second");
console.log("Third");
```

That code is synchronous. Each line finishes before the next line runs.

Asynchronous code is different. Some work starts now but finishes later. The
browser needs a way to keep the page responsive while it waits for things such
as timers, files, network requests, or user actions.

The main question is:

```text
What happens now, and what happens later?
```

You may have already seen async ideas in Python. The syntax is different in
JavaScript, but the timing problem is familiar. Some operations take time, and
the program needs a way to keep going or wait cleanly.

### Three Related Ideas

`fetch` starts a request.

- It asks for a resource, often from another file, API, or server.
- The response is not available immediately.

A `Promise` represents a future result.

- It is JavaScript's way of saying, "this operation is not finished yet, but it
  should eventually succeed or fail."
- A Promise is not the final data. It is a placeholder for the future result.

`async`/`await` makes Promise-based code easier to read.

- `async` marks a function that can use `await`.
- `await` pauses that async function until a Promise settles.
- Waiting still happens even when the syntax looks cleaner.

Useful summary:

```text
fetch starts the request.
A Promise represents the future result.
async/await is a cleaner way to write code that waits for that result.
```

---

## 2. Why The Web Needed Async

Early web pages were mostly document-like. If the page needed new information,
the browser often loaded a whole new page.

That was simple, but it could be disruptive:

- the page disappeared and reloaded
- the user lost their current visual context
- small updates required large refreshes

Later, browsers gained ways to request data without reloading the whole page.
That made web pages feel more interactive and app-like.

### Mini-Timeline

**Full-page reload era**

Pages commonly changed by navigating to a new page or reloading the current
one. The browser waited for the server and then displayed a new document.

**XMLHttpRequest / Ajax**

`XMLHttpRequest` made it possible for a page to request data from a server and
update part of the page without a full reload. The "Ajax" pattern became an
important step toward interactive web applications.

**Promises / ES2015**

Promises became JavaScript's standard way to represent an operation that may
finish in the future. They gave code a more consistent way to handle eventual
success or failure.

**Fetch API**

`fetch()` became a cleaner browser API for making requests. It returns a
Promise, which means the response is handled as a future result.

**async/await**

`async` and `await` made Promise-based code easier to read in order. The code
can look more step-by-step, but it is still dealing with work that takes time.

---

## 3. The Four Pieces: Delay, Request, Promise, Await

### Delay

A delay is a simple way to see async behavior without using a server.

`setTimeout()` tells the browser:

```text
Run this function later, after this many milliseconds.
```

### Request

A request asks for something, usually from another file, server, or API.

With `fetch`, the request starts now, but the response comes later.

### Promise

A Promise represents the future result of asynchronous work.

At a beginner level, read a Promise as:

```text
Something is happening.
The result is not ready yet.
JavaScript will continue when the result is available.
```

### Await

`await` is used inside an `async` function. It tells JavaScript:

```text
Wait here inside this async function until the Promise has a result.
```

Important: `await` does not make the browser freeze. It helps your async
function pause cleanly while the browser continues managing other work.

---

## 4. Tiny Examples To Read, Not Memorize

These examples are for reading and discussion. Do not try to memorize every
symbol yet. Focus on order and timing.

### Example 1 - Normal Order

```js
console.log("A");
console.log("B");
console.log("C");
```

Expected order:

```text
A
B
C
```

Everything runs now.

### Example 2 - Something Happens Later

```js
console.log("A");

setTimeout(function () {
  console.log("B");
}, 1000);

console.log("C");
```

Likely order:

```text
A
C
B
```

Why?

- `A` runs now.
- `setTimeout` schedules `B` for later.
- `C` runs now.
- after about 1 second, `B` runs.

The key idea is not the exact timer syntax. The key idea is that scheduled work
can finish after later lines have already run.

### Example 3 - The Shape Of A Fetch

```js
async function loadData() {
  const response = await fetch("data.json");
  const data = await response.json();

  console.log(data);
}
```

Read this as:

```text
Start a request for data.json.
Wait for the response.
Convert the response into JSON data.
Use the data.
```

For now, focus on the shape:

- `fetch` starts a request
- `await` marks a waiting point
- `response` is not the final data yet
- `.json()` prepares the response body as usable data

---

## 5. What To Focus On / What To Ignore For Now

### Focus On

- What happens now vs what happens later
- Why a page should not freeze while waiting
- How a delay can be visible
- How loading data is different from already having data
- Why a loading message or placeholder can help users
- The relationship between `fetch`, Promise, and `async`/`await`

### Ignore For Now

- Full Promise chaining
- Advanced error handling
- CORS details
- API authentication
- service workers
- upload/download progress
- complex API design
- memorizing every async syntax pattern

For Week 8, the goal is conceptual:

```text
Some browser work takes time.
Good web code recognizes that delay and responds clearly.
```

---

## Reference Links

- MDN `setTimeout()`: https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout
- MDN `fetch()`: https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch
- MDN Fetch API: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
- MDN `Promise`: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise
- MDN `async function`: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function
