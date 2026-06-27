# Week 9 Handout - Modular Thinking: Breaking Systems into Parts

**Course:** 10-152-118 Web Development Foundations  
**Purpose:** Prepare for Week 9 lecture and lab by understanding how larger web projects can be organized into smaller, clearer parts.

---

## 1. Modularity First, Modules Later

Modularity means organizing a project into smaller parts with clear
responsibilities.

A module is a specific file or code unit that can provide functionality to
another file.

These ideas are related, but they are not exactly the same.

```text
Modularity is the habit:
Break a larger system into understandable parts.

A module is one possible tool:
Use one file or code unit from another file.
```

You can practice modularity before you use JavaScript `import` or `export`.

For this week, the main goal is not to master every rule of JavaScript modules.
The main goal is to make code easier to find, explain, reuse, and change.

---

## 2. From One File To A Small Project

Early web examples often start small. A beginner demo might place everything in
one HTML file:

```html
<style>
  body {
    font-family: Arial, sans-serif;
  }
</style>

<button id="save">Save</button>

<script>
  document.querySelector("#save").addEventListener("click", function () {
    console.log("Saved");
  });
</script>
```

This can be useful while learning. But as the page grows, it becomes harder to
find the structure, style, and behavior.

A common next step is a small project folder:

```text
project-folder/
  index.html
  css/
    style.css
  js/
    script.js
  images/
    logo.png
```

This structure keeps related work near related work.

```text
index.html describes the page.
css/style.css controls how the page looks.
js/script.js controls what the page does.
images/ stores visual assets.
```

Splitting files is not about making the project look professional on the
surface. It is about making the project easier to manage.

---

## 3. Separation Of Concerns

Separation of concerns means each part of a project should have a clear job.

For beginner web development, a useful starting point is:

```text
HTML: structure and content
CSS: appearance and layout
JS: behavior and interaction
```

This does not mean the parts never connect. They do connect.

For example, JavaScript may select an HTML element and change a CSS class:

```js
const message = document.querySelector("#message");

message.classList.add("visible");
```

But the responsibilities are still different.

- HTML provides the element.
- CSS defines what `.visible` looks like.
- JavaScript decides when the class should be added.

When responsibilities are mixed together too much, the project becomes harder to
debug. A small change in one place may unexpectedly affect something somewhere
else.

---

## 4. Functions As Named Responsibilities

Functions are one of the first modularity tools you will use.

A function gives a piece of behavior a name.

```js
function calculateTotal(price, quantity) {
  return price * quantity;
}

function displayTotal(total) {
  document.querySelector("#total").textContent = total;
}
```

Each function should have a job you can explain in one sentence.

```text
calculateTotal figures out the total.
displayTotal shows the total on the page.
```

That may feel simple, but it matters. Larger programs become easier when they
are made from smaller named pieces.

### A Less Clear Version

```js
document.querySelector("#total").textContent =
  Number(document.querySelector("#price").value) *
  Number(document.querySelector("#quantity").value);
```

This works, but several ideas are packed into one line:

- Find the price.
- Find the quantity.
- Convert text to numbers.
- Calculate the total.
- Display the total.

### A Clearer Version

```js
function getNumberFromInput(selector) {
  return Number(document.querySelector(selector).value);
}

function calculateTotal(price, quantity) {
  return price * quantity;
}

function displayTotal(total) {
  document.querySelector("#total").textContent = total;
}

const price = getNumberFromInput("#price");
const quantity = getNumberFromInput("#quantity");
const total = calculateTotal(price, quantity);

displayTotal(total);
```

This version is longer, but the parts are easier to read and discuss.

---

## 5. Next Step: A Larger Project Shape

As you move toward the capstone project, your work may grow beyond one page.
A larger project may have multiple HTML pages that share the same CSS and some
of the same JavaScript.

This is a next-step model, not a checklist for every assignment.

One possible shape is:

```text
capstone-project/
  index.html
  about.html
  contact.html
  css/
    style.css
  js/
    navigation.js
    validation.js
    data.js
    script.js
  images/
    hero.jpg
    gallery/
      project-1.jpg
      project-2.jpg
```

This is not the only correct structure. The important idea is that names should
communicate responsibility.

```text
navigation.js controls navigation behavior.
validation.js checks form input.
data.js stores or prepares data.
script.js connects the page behavior together.
```

In a multi-page project:

- Several pages can use the same CSS file.
- Several pages can use the same navigation script.
- Images can be grouped in an images folder.
- Repeated behavior can be placed in a shared JavaScript file.

A larger project is easier when a future reader can answer:

```text
Where is the page structure?
Where is the visual styling?
Where is the behavior?
Where would I change this feature?
```

---

## 6. Modern JavaScript Modules: Recognition Only

Modern JavaScript can formally connect files with `import` and `export`.

You may see an HTML file load JavaScript like this:

```html
<script type="module" src="js/script.js"></script>
```

You may also see one JavaScript file import something from another file:

```js
import { formatPrice } from "./format.js";

const result = formatPrice(19.99);
```

For now, read this pattern as:

```text
This file is using a named piece of code from another file.
```

That is the connection to modularity. One file has a responsibility, and another
file can reuse that responsibility when needed.

You do not need to master all module rules this week. The important thing is to
recognize the pattern and understand why larger projects often separate code
into named files.

---

## 7. What To Focus On / What To Ignore For Now

Focus on:

- The difference between modularity and a module.
- Clear file names.
- Clear function names.
- One main responsibility per function when reasonable.
- HTML, CSS, and JavaScript having different jobs.
- Shared CSS and JavaScript across multiple pages.
- Folder structures that someone else can navigate.

Ignore for now:

- Build tools.
- Bundlers.
- npm package workflows.
- Framework folder structures.
- Advanced `import` and `export` patterns.
- Optimizing file size.
- Designing the "perfect" folder structure.

The goal is not perfection. The goal is a project that is easier to understand
next week than it was this week.

---

## Reference Link

- MDN JavaScript Modules: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules
