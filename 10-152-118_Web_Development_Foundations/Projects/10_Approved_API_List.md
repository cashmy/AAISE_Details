# WEEK 10 - API GUIDANCE FOR HTML/CSS/JS

**Working with External Data**

---

## Purpose

This course uses a shared approved API list so that students can focus on:

* retrieving data
* understanding JSON structure
* selecting meaningful values
* displaying that data in the browser

The canonical list now lives here:

* [Approved_API_List.md](D:/@Artifact_Generation/108_AAISE_Details/Approved_API_List.md)

This wrapper explains how to use that list in the HTML/CSS/JS course.

---

## Course Rules

You must:

* use one API from the shared approved list unless another API is approved
* retrieve data using `fetch`
* display meaningful data in your application

You may:

* choose the approved API that interests you most
* expand your project in later iterations if instructed

You may not:

* use APIs that require accounts or keys unless approved
* use unapproved APIs without instructor approval

---

## HTML/CSS/JS Emphasis

In this course, the API lesson is not only about retrieving JSON.

It is also about:

* waiting for the response
* reading the returned structure
* updating the UI
* showing meaningful information in the page

The browser context makes the UI update part of the learning target.

---

## Recommended Default

For the HTML/CSS/JS course, `JSONPlaceholder` remains the recommended default because it is stable, easy to inspect, and well suited to list rendering.

---

## Starter Example

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

## Success Looks Like

* your application retrieves data successfully
* you display meaningful information instead of raw JSON only
* your UI updates based on that data

---

## Final Guidance

If you are stuck:

1. Log the data with `console.log(data)`.
2. Look at the structure carefully.
3. Choose one value to display first.
4. Build outward from that working path.

---

## Additional Support

Use the JSON reading worksheet artifacts in this folder if you need more structure when interpreting nested data.


