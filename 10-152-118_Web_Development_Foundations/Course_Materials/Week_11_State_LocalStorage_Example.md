# Week 11 Handout - State And localStorage: Things Persist

**Course:** 10-152-118 Web Development Foundations  
**Purpose:** Prepare for Week 11 lecture and lab by understanding how web applications remember information, lose information, and keep the interface consistent.

---

## 1. What Is State?

State is the information an application is currently using to decide what should
be shown or what should happen next.

A page may look static, but an interactive page often has remembered information
behind it.

Examples:

- Is the menu open or closed?
- Which tab is selected?
- What text has the user typed?
- Which filter is active?
- Has the user chosen dark mode?
- What items are in a saved list?

Useful mental model:

```text
State is what the app currently knows.
The UI is what the app currently shows.
Good interactive pages keep those two connected.
```

---

## 2. State Changes Over Time

State is not just data. It is data that can change.

```text
User clicks a button.
A value changes.
The page updates to match the new value.
```

Example:

```text
Before click: menuOpen = false
After click:  menuOpen = true
```

The visible page should match the current state.

If the state says the menu is open, the menu should look open.

If the state says the cart has three items, the page should not show zero items.

---

## 3. Where State Can Live

For beginner web projects, state may live in a few places:

```text
In the page: input values, selected options, visible text, CSS classes
In JavaScript: variables, arrays, objects
In the browser: localStorage or sessionStorage
```

These places are connected, but they are not the same.

For example, a CSS class may show the current visual state:

```js
document.body.classList.add("dark");
```

A JavaScript variable may store the current logical state:

```js
let currentTheme = "dark";
```

The browser may store a value so it can be found later:

```js
localStorage.setItem("theme", "dark");
```

The tricky part is keeping these connected intentionally.

---

## 4. State Is Not Automatically Persistent

State does not automatically last forever.

If you do not store it somewhere durable, it can disappear.

This matters more as projects become modular, use multiple JavaScript files, or
move across multiple HTML pages.

```text
Modularity helps organize code.
It does not automatically share or preserve state.
```

### Scope Loss

A variable exists only where it was created.

```js
function saveName() {
  let name = "Ava";
}

console.log(name); // name is not available here
```

The variable `name` was created inside the function. Code outside that function
cannot automatically use it.

### Reload Loss

Normal JavaScript variables reset when the page reloads.

```js
let counter = 3;
```

After refresh, the script starts over and `counter` is recreated.

### Navigation Loss

Moving from one HTML page to another usually starts a new page context.

```text
index.html -> details.html
```

Unless the state is passed, stored, or rebuilt, the next page does not
automatically know what the previous page knew.

### Multi-File Confusion

Using multiple JavaScript files can make projects clearer, but one file does not
magically know every value from another file.

If multiple files need the same information, the project needs a clear plan for
where that information lives and how other code accesses it.

---

## 5. State, Persistence, And localStorage

These three ideas are related, but they are not the same.

```text
State = information the app currently uses.
Persistence = keeping some information available later.
localStorage = one browser tool for persistence.
```

Some state only needs to exist while the page is open.

Some state should survive a refresh.

Some state may need to move from one page to another.

Persistence means choosing where remembered information should live.

For beginner projects, that might mean:

- Keeping a value in a variable while the page is open.
- Reading a value from the page when needed.
- Passing a value into a function.
- Storing a small value in `localStorage`.
- Rebuilding state from JSON or another data source.

---

## 6. Tiny Example: Saved Theme Preference

This example saves a small theme preference.

HTML:

```html
<button id="themeButton">Use dark theme</button>
```

JavaScript:

```js
const themeButton = document.querySelector("#themeButton");

function applyTheme(theme) {
  document.body.className = theme;
  localStorage.setItem("theme", theme);
}

themeButton.addEventListener("click", function () {
  applyTheme("dark");
});
```

When the button is clicked:

```text
The user takes an action.
JavaScript changes the page.
JavaScript saves the preference in localStorage.
```

---

## 7. What Happens When The Page Reloads?

The previous example saves the value, but the page still needs to read it later.

```js
const savedTheme = localStorage.getItem("theme");

if (savedTheme) {
  document.body.className = savedTheme;
}
```

This code asks the browser:

```text
Did we save a theme earlier?
If yes, apply that theme again.
```

The browser remembered the value after refresh because it was stored in
`localStorage`.

The JavaScript variable did not remember it by itself.

---

## 8. State Flow Mental Model

Use this flow when thinking through stateful behavior:

```text
User action
    ↓
JavaScript changes a value
    ↓
JavaScript updates the page
    ↓
Optional: JavaScript saves the value
    ↓
Page can restore the value later
```

Ask these questions:

- What value is being remembered?
- Where does that value live right now?
- When does the value change?
- How does the UI show the current value?
- Does the value need to survive refresh or navigation?

---

## 9. What To Focus On / What To Ignore For Now

Focus on:

- State as remembered application information.
- The difference between state and persistence.
- The fact that state is not automatically persistent.
- Scope loss, reload loss, and navigation loss.
- Small `localStorage` values such as preferences or simple progress.
- Keeping the UI consistent with the current state.

Ignore for now:

- Complex state management systems.
- Framework state such as React state.
- Syncing state across browser tabs.
- Storage quotas.
- Service workers.
- Authentication tokens.
- Storing sensitive data in the browser.

The goal is to understand where information lives, when it changes, and whether
the app needs to remember it later.
