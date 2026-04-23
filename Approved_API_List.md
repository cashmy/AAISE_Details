# APPROVED API LIST

**Shared External Data Resource**

---

## Purpose

This is the canonical approved API list for introductory AAISE course work that uses external JSON data.

It exists to:

* reduce time lost searching for APIs
* keep the focus on data retrieval, structure, and use
* avoid unnecessary API-key friction
* provide a stable cross-course reference
* support both browser-based and Python-based coursework

This artifact is shared across courses.

Course-specific wrappers should explain how the APIs are used in a particular class.

---

## Core Rules

Students must:

* use one API from this list unless another API is explicitly approved
* retrieve meaningful data rather than only raw JSON
* inspect the data structure before choosing values to display or use

Students may not:

* use APIs that require accounts or API keys unless specifically approved
* use APIs outside this list without instructor approval

---

## Instructional Guidance

This list is not primarily about finding the "best" API.

It is about keeping the technical surface area manageable so that the real lesson remains:

* retrieving data
* reading JSON structure
* selecting useful values
* handling errors or unusual cases
* validating results

---

# APPROVED APIS

---

## 1. JSONPlaceholder (Recommended Default)

**Base URL:**

`https://jsonplaceholder.typicode.com/`

### What it provides

* users
* posts
* todos

### Example endpoints

* `/users`
* `/posts`
* `/todos`

### Example use

* display a list of users
* show post titles
* filter completed tasks

### Why it is approved

This is one of the safest default choices for beginner work because it is predictable, public, and designed for testing and prototyping.

---

## 2. Agify API

**Example endpoint:**

`https://api.agify.io?name=michael`

### What it provides

* predicted age based on a name

### Example use

* user enters a name
* program displays predicted age

### Why it is approved

The JSON response is small and easy to inspect, which makes it useful for early API practice.

---

## 3. Dog API

**Example endpoint:**

`https://dog.ceo/api/breeds/image/random`

### What it provides

* random dog images

### Example use

* button or script retrieves a random image URL
* application displays or prints the selected image value

### Why it is approved

This is a simple and engaging media-oriented JSON example.

---

## 4. Advice Slip JSON API

**Example endpoint:**

`https://api.adviceslip.com/advice`

### What it provides

* random advice text

### Example use

* retrieve one piece of advice
* display the advice text and ID

### Why it is approved

This replaces the older Bored API entry. It provides simple JSON, requires no key, and offers a beginner-friendly structure for parsing.

---

## 5. REST Countries

**Example endpoint:**

`https://restcountries.com/v3.1/all?fields=name,population,region,capital`

### What it provides

* country names
* population
* region
* capital data

### Example use

* display a list of countries
* show a selected country detail
* summarize regional information

### Why it is approved

This is useful when students are ready to work with more complex nested data.

### Important note

Use the `fields=` query when appropriate so the response stays focused and easier to inspect.

---

## 6. Open-Meteo

**Example endpoint:**

`https://api.open-meteo.com/v1/forecast?latitude=43.75&longitude=-87.71&current=temperature_2m`

### What it provides

* weather data

### Example use

* display current temperature for a location
* compare selected weather values

### Why it is approved

This gives students a more realistic external-data example while still avoiding API-key setup.

### Important note

This API requires meaningful query parameters. Do not use the base URL by itself as the assignment target.

---

# Optional Use Guidance

## Simulated JSON Fallback

Whenever an assignment or demo uses a live API, the instructor may also provide a simulated JSON fallback.

This is strongly recommended when:

* network stability is uncertain
* class time is limited
* the lesson focus is JSON structure rather than networking
* the live API becomes unavailable or changes unexpectedly

---

## General Success Pattern

When using an API:

1. Retrieve the data.
2. Inspect the JSON structure.
3. Select one or two useful values first.
4. Display or use those values clearly.
5. Expand only after the basic path works.

---

## Final Reminder

Start simple.

Get one useful value working first.

Then build outward.

