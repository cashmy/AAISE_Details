# Week 6 Demo 7 - Django MVT Recognition Preview

This is a recognition-level walkthrough, not a full build target. Use the
inspectable `07_mvt_study_task_app/` example beside this note. Students can
read its `MVT_TRACE.md` and `tasks/` files without running Django.

The purpose is to help students see where Python may live inside a larger web application.

## Core Idea

In a console script, one file often does almost everything:

* receives input
* stores values
* runs logic
* prints output

In a larger web application, those responsibilities are usually separated.

## Django MVT at a Beginner Level

### Model

Represents application data.

Example idea:

* a study task
* a course
* a due date
* a completion flag

### View

Handles the request and chooses what data should be prepared.

Example idea:

* get all study tasks
* filter incomplete tasks
* send them to a template

### Template

Displays information to the user.

Example idea:

* show a list of tasks in HTML
* show course names and due dates

### Form

Shapes and validates user input.

Example idea:

* require a task title
* require minutes to be a number
* reject missing fields

## Tiny Example Mapping

If a user submits a new study task:

1. `tasks/urls.py` routes `/add/` to `add_task` in `tasks/views.py`.
2. `tasks/templates/tasks/task_form.html` displays the input fields.
3. `StudyTaskForm` in `tasks/forms.py` validates the submitted values.
4. `add_task` saves a valid `StudyTask` defined in `tasks/models.py` and
   redirects to `/`.
5. `task_list` retrieves tasks, and `task_list.html` displays them.

Ask students what happens when estimated minutes is `not-a-number`. The form
shows an error and no task is saved. Forms and URLs support the MVT flow;
they are not separate letters in MVT.

The student's inspection prompts are in
`07_mvt_study_task_app/ASSIGNMENT_12_WORKSHEET.md`.

## Why This Matters

Students do not need to master Django here.

They do need to recognize that Python can move beyond console scripts into:

* request/response systems
* templates and forms
* structured application layers

That recognition helps later courses feel less abrupt.
