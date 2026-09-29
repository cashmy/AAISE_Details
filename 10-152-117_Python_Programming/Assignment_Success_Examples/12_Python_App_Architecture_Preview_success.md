# Assignment 12 Success Example - Study Task MVT Inspection

This is one example of a short, evidence-based response to the
`07_mvt_study_task_app/ASSIGNMENT_12_WORKSHEET.md` prompts.

1. The add-task address is `/add/`. `tasks/urls.py` connects it to
   `add_task` in `tasks/views.py`.
2. The user types values in the form displayed by
   `tasks/templates/tasks/task_form.html`. Its HTML `<form method="post">`
   sends the values to the server.
3. `StudyTaskForm` in `tasks/forms.py` checks the submission when
   `add_task` calls `form.is_valid()`. Text such as `not-a-number` in the
   estimated-minutes field causes an error; `form.save()` is not called.
4. `StudyTask` in `tasks/models.py` defines the stored record. Two fields
   are `title` and `estimated_minutes`.
5. After saving, the app redirects to `/`. The `task_list` view retrieves
   records, and `tasks/templates/tasks/task_list.html` displays them.
6. Clicking **Save task** sends a POST request to `/add/`. The `add_task`
   view gives the submitted data to `StudyTaskForm`. If valid, the form saves
   a `StudyTask` model record. The browser then requests `/`, where
   `task_list` passes the records to the list template for display.
7. A small console script may take input and print output during one run.
   This app responds to separate browser requests. URLs select views, forms
   validate input, a model stores data, and templates display HTML.
8. No AI used.

If the optional edit changes only the heading in `task_list.html`, it changes
the presentation layer, not the model or validation rules.
