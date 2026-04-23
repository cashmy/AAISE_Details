# API GUIDANCE FOR PYTHON

**Week 6 - APIs, External Data, and Python App Architecture**

---

## Purpose

This course uses a shared approved API list so that students can focus on:

* requesting or loading external-style data
* reading JSON structure
* selecting useful values
* validating results
* handling likely problems responsibly

The canonical list lives here:

* [Approved_API_List.md](D:/@Artifact_Generation/108_AAISE_Details/Approved_API_List.md)

This wrapper explains how to use that list in the Python course.

---

## Course Rules

You must:

* use one API from the shared approved list unless another API is approved
* retrieve live data or use an instructor-approved simulated response
* display selected meaningful values rather than raw JSON only
* explain the structure of the response at a beginner level

You may:

* use a simulated JSON fallback when the instructor allows it
* compare a live response to a saved response file

You may not:

* rely on an API you have not inspected
* trust generated code without validating the response structure
* use APIs that require keys or accounts unless approved

---

## Python Emphasis

In this course, the API lesson is not primarily about UI updates.

It is about:

* request and response thinking
* JSON parsing
* structure inspection
* extracting selected values
* validating output
* handling error cases

This means that a clean simulated JSON example may sometimes be better than a fragile live request during instruction.

---

## Recommended Default

For the Python course, `JSONPlaceholder` remains the recommended default because:

* it is stable
* it has predictable JSON
* it supports lists and object access
* it works well for selected-value extraction and filtering

`Agify` is also a strong early option when students need a very small JSON example.

---

## Simulated JSON Fallback

A simulated response is fully acceptable when:

* network reliability is uncertain
* the lesson focus is JSON structure
* time is limited
* the live API becomes unavailable

The key point is not whether the data came from the internet in that exact moment.

The key point is whether the student can read the structure, choose useful values, and explain the flow responsibly.

See also:

* [Week 6 fallback demo](D:/@Artifact_Generation/108_AAISE_Details/10-152-117_Python_Programming/Demos/Week_06_APIs_External_Data_and_App_Architecture/08_simulated_json_fallback_demo.py)

---

## Success Looks Like

* your program retrieves or loads API-style data successfully
* you display selected values clearly
* you can explain the shape of the response
* you handle at least one likely problem when appropriate
* you validate the code rather than blindly trusting it

---

## Final Guidance

If you are stuck:

1. Print the loaded JSON structure carefully.
2. Identify one field or nested field.
3. Display that one value first.
4. Add more only after the first path works.
