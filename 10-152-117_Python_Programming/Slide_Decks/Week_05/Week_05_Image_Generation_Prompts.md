# Week 5 Image Generation Prompts

**Course:** 10-152-117 Python Programming  
**Week:** Week 5 - Files, Errors, and Data Persistence

---

# Prompt Use Notes

These prompts expand the image prompt notes in the Week 5 v2 deck sources.

Use them when PowerPoint Designer or a browser-based image model needs stronger
constraints. They are intentionally simple, instructional, and diagram-like.

Avoid:

- database-heavy imagery unless the slide specifically calls for a future preview
- cybersecurity or warning-screen imagery
- cluttered code screenshots
- cloud infrastructure diagrams
- unreadable tiny text

---

# Week 5 Day 1 - Programs That Remember

## Slide 1 - Programs Can Remember

Create a clean educational slide visual showing a small Python program window
closing while a saved text file remains visible beside it.

Labels:

- "program run ends"
- "saved file remains"

Style:

- simple vector-style illustration
- light background
- calm blue and green accents
- readable labels

Avoid:

- cloud storage icons
- database cylinders
- complex file explorer screenshots
- dramatic warning symbols

## Slide 3 - Today's Success Pattern

Create a clean instructional success-pattern visual for a beginner file-saving
lesson.

Show a five-step path:

1. "write to named file"
2. "confirm file exists"
3. "read saved data"
4. "show loaded output"
5. "explain what was saved"

Use a small cycle arrow behind the steps to suggest that save/load is a repeatable
pattern. Include a simple text-file icon labeled `note.txt`.

Keep the diagram spacious and easy to read.

Avoid:

- dense code
- cloud services
- database imagery
- more than five steps

## Slide 4 - What We Will Use Today

Create a simple "working set" visual showing a small tool tray with these items:

- file name
- `open()`
- `with`
- read mode
- write mode

The visual should feel like a short list of today's tools, not a full tutorial.

Avoid:

- long code snippets
- many file-mode options
- dark terminal screenshots

## Slide 5 - What We Will Skip For Now

Create a "parked for later" shelf with binary files, file compression, custom
JSON encoding, complex folders, and deployment issues.
Add a caption: "Useful later, not today's required target."

Avoid warning visuals.

## Slide 6 - Writing Stores Data Outside The Program

Create a minimal classroom slide diagram titled "Writing Stores Data Outside the Program".

Show only three main visual elements:

1. A simple program box labeled "Python program"
2. A right-facing arrow labeled "write"
3. A text file icon labeled `note.txt`

Inside the text file, show two short lines:

- "Study files"
- "Review notes"

Add one small caption under the diagram:

- "The file remains after the program ends."

Style:

- light background
- simple vector diagram
- soft blue and green accents
- large readable labels

Avoid:

- cloud storage
- database cylinders
- full file explorer screenshots
- dense code blocks
- server or network imagery

## Slide 7 - Reading Brings Saved Data Back

Create a minimal classroom slide diagram titled "Reading Brings Saved Data Back".

Show only three main visual elements:

1. A text file icon labeled `note.txt`
2. A left-to-right arrow labeled "read"
3. A Python program/output box labeled "Loaded output"

Inside the file, show:

- "Study files"
- "Review notes"

Inside the output box, show the same two lines as visible program output.

Add one small caption:

- "The program uses information that was already saved."

Style:

- light background
- simple vector diagram
- calm blue and green accents
- clear arrow direction from file to program output

Avoid:

- cloud storage
- database imagery
- file explorer screenshots
- terminal-heavy visuals
- extra file formats

## Slide 8 - Why `with` Matters

Create a simple process visual titled "The `with` Block Handles the File Safely".

Show a three-step horizontal sequence:

1. "Open file"
2. "Use file inside block"
3. "File closes after block"

Place a light outline around the middle step labeled:

- `with open(...) as file:`

Use a small file icon that appears in each step.

Add one small caption:

- "`with` gives the file a safe working space."

Style:

- clean instructional diagram
- light background
- readable labels
- simple arrows

Avoid:

- advanced context-manager terminology
- dense code
- lock/security imagery
- complex Python internals

## Slide 9 - File Modes Are Intent Signals

Create a clean two-card comparison visual titled "File Modes Signal Intent".

Left card:

- `"w"`
- "write"
- "put data into a file"

Right card:

- `"r"`
- "read"
- "bring saved data back"

Between the cards, include a small file icon labeled `note.txt`.

Add one small caption:

- "Choose the mode that matches what the program is trying to do."

Style:

- minimal educational diagram
- light background
- blue for read
- green for write
- large readable text

Avoid:

- showing many file modes
- long code examples
- warning-heavy design
- implying one mode is better than the other

## Slide 10 - Demo 1: Write A Text File

Create an instructional diagram showing a small code card labeled "write text"
pointing to a newly created file labeled `notes.txt`.

Inside the file, show two short lines:

- "Remember this task"
- "Review later"

Keep the diagram simple and readable.

Avoid:

- real IDE screenshots
- hidden automation imagery
- database or network symbols

## Slide 11 - Demo 2: Read A Text File

Create an instructional diagram showing a small code card labeled "read text"
pointing to a newly created file labeled `notes.txt`.

Inside the file, are already present two short lines, which will be read by the "read text" code card.

- "Remember this task"
- "Review later"

Keep the diagram simple and readable.

Avoid:

- real IDE screenshots
- hidden automation imagery
- database or network symbols

## Slide 14 - Evidence For A8

Create a clean checklist visual titled "Assignment 8 Evidence".

Checklist items:

- Python file
- saved data file
- run output
- README explanation
- AI-use note, if used

Style:

- simple instructional checklist
- light background
- small icons beside each item

Avoid:

- legal contract imagery
- audit/compliance visuals
- excessive decoration

---

# Week 5 Day 2 - Structured Data And Basic Error Handling

## Slide 1 - Saved Data Has Shape

Create a side-by-side instructional visual comparing three tiny data shapes:

- Plain text note
- CSV table with two columns
- JSON object with two labeled values

Use labels:

- "plain text"
- "CSV"
- "JSON"

Keep examples tiny and readable.

Avoid:

- large datasets
- spreadsheet software interface
- deeply nested JSON

## Slide 2 - Review: The File Is Part Of The Program's World

Create a simple educational diagram titled "The File Is Part of the Program's World".

Show three connected elements:

1. A Python program box
2. A small file icon labeled `data file`
3. A response area labeled "program response"

Near the file icon, show two small possible problem tags:

- "missing"
- "wrong shape"

Add one small caption:

- "The program must respond clearly when the file is not what it expected."

Style:

- light background
- simple arrows
- calm blue and orange accents
- readable labels

Avoid:

- red alert screens
- broken computer imagery
- cybersecurity visuals
- scary error symbols

## Slide 3 - Today's Success Pattern

Create a clean instructional success-pattern visual for reading structured data.

Show a five-step path:

1. "identify file shape"
2. "read the file"
3. "select useful values"
4. "handle one likely problem"
5. "explain what the program did"

Include three small file-shape icons beneath the path:

- plain text
- CSV
- JSON

Add a small footer:

- "The file shape affects the program's choices."

Avoid:

- large datasets
- deeply nested JSON
- spreadsheet software interface
- long code blocks

## Slide 4 - What We Will Use Today

Create a simple working-set visual titled "Today's Structured Data Tools".

Show five small tool cards:

- CSV rows and columns
- JSON labels and values
- `try` / `except`
- selected output
- one clear error path

Use clean icons or plain cards with readable text.

Avoid:

- dense syntax
- full code examples
- database imagery
- dashboard-style layout

## Slide 5 - What We Will Save For Later

Create a calm "parked for later" shelf titled "Save For Later".

Place these items on the shelf:

- databases
- custom JSON encoding
- large data pipelines
- advanced exceptions
- configuration systems

Add caption:

- "Useful later, not today's required target."

Avoid:

- warning signs
- red X marks
- making advanced topics look forbidden or scary

## Slide 6 - JSON Uses Labels

Create a simple diagram showing a JSON object on the left and selected output on
the right.

JSON labels to show:

- `"task"`
- `"priority"`
- `"done"`

Right-side output:

- "Task: Review notes"
- "Priority: high"

Highlight the labels and draw arrows to the displayed values.

Avoid:

- deeply nested data
- syntax errors
- too much punctuation detail

## Slide 7 - CSV Uses Rows And Columns

Create a small table diagram labeled "CSV".

Columns:

- Date
- Minutes
- Topic

Rows:

- Mon, 30, Python
- Tue, 20, Files

Highlight one row and one column with different soft colors.

Avoid:

- Excel interface
- complex charts
- more than three rows

## Slide 8 - Loading Is Not The Finished Result

Create a simple transformation visual titled "Loaded Data Becomes Useful Output".

Left side:

- raw file contents card labeled "Loaded data"
- show a tiny mix of rows or labels

Center:

- arrow labeled "select / summarize / format"

Right side:

- clean output card labeled "Useful output"
- show two selected lines:
  - "Tasks completed: 3"
  - "Next task: Review notes"

Add caption:

- "Reading the file is only the first step."

Avoid:

- implying raw output is enough
- dashboards or charts
- large datasets
- dense code

## Slide 9 - Demo 1: Save And Load JSON Tasks

Create a minimal visual titled "JSON Tasks: Save, Load, Select".

Show a small JSON-like task list on the left with two task cards:

- task: "study files", done: false
- task: "review notes", done: true

Show an arrow labeled "load JSON".

On the right, show selected output:

- "2 tasks loaded"
- "Completed: review notes"

Keep the JSON tiny and readable.

Avoid:

- deeply nested JSON
- full code blocks
- too much punctuation detail
- app dashboard styling

## Slide 10 - Demo 2: Read A CSV Summary

Create a clean CSV summary visual titled "CSV Summary".

Left side:

- small CSV table with columns: Date, Minutes, Topic
- three short rows

Center:

- arrow labeled "summarize"

Right side:

- output card:
  - "Sessions: 3"
  - "Total minutes: 75"

Avoid:

- spreadsheet application interface
- complex charts
- business dashboard styling
- more than three rows

## Slide 11 - Not Every Failure Means The Same Thing

Create a two-path educational diagram titled "Different Problems, Different
Responses".

Left path:

- "File missing"
- "Tell the user what file was not found"

Right path:

- "Invalid data"
- "Tell the user the file contents need checking"

Use calm colors. The tone should be clear, not scary.

Avoid:

- red alert screens
- broken computer imagery
- cybersecurity visuals

## Slide 12 - Demo 3: Missing File And Invalid JSON

Create a two-panel educational visual titled "Two Different File Problems".

Left panel:

- file icon with dashed outline
- label: "Missing file"
- message: "File was not found."

Right panel:

- file icon with jumbled braces or a small caution mark
- label: "Invalid JSON"
- message: "File exists, but contents need checking."

Use calm colors and clear messages.

Avoid:

- red alert screens
- scary warning imagery
- broken laptop/computer visuals
- cybersecurity imagery

## Slide 13 - Common Failure: Raw Data Dumping

Create a before/after comparison titled "Raw Dump vs Useful Output".

Left side:

- messy raw data card labeled "Raw dump"
- show a few unreadable-looking rows or labels, but keep text minimal

Right side:

- clean output card labeled "Useful output"
- show:
  - "Selected record: Review notes"
  - "Status: complete"

Add caption:

- "A useful result shows that the program understood the structure."

Avoid:

- shaming tone
- red X marks
- huge raw data blocks
- dashboards

## Slide 14 - Assignment 9 Bridge

Create a simple assignment path visual titled "A9 Structured Data Reader".

Show four steps in a row:

1. "Open provided file"
2. "Identify shape"
3. "Select useful values"
4. "Display readable result"

Use small file, magnifier, selector, and output icons or plain cards.

Avoid:

- full data pipeline imagery
- database symbols
- complex code
- large datasets

## Slide 15 - Evidence For A8 And A9

Create a clean evidence checklist with these items:

- code file
- data file
- readable output
- data-shape explanation
- error-path note
- AI-use note, if used

Use a light background and simple check icons.

Avoid:

- legal document imagery
- audit stamps
- cluttered folder screenshots

---

# Week 5 Day 3 - Comparing Data Representations And App Structure

## Slide 1 - Same Information, Different Forms

Create a clean comparison visual showing the same "study task" represented four
ways:

- plain note
- CSV row
- JSON object
- table row

Use one consistent example:

- Task: Read chapter
- Topic: Files
- Minutes: 30

Keep each representation small and readable.

Avoid:

- database schema complexity
- many records
- tiny unreadable code

## Slide 2 - Review: Structured Data Has Shape

Create a simple review visual titled "Structured Data Has Shape".

Show two small panels:

Left panel:

- "CSV"
- rows and columns
- caption: "good for similar records"

Right panel:

- "JSON"
- labeled grouped values
- caption: "good for labeled structure"

Add footer:

- "Different shapes make different tasks easier."

Avoid:

- deep nesting
- spreadsheet software interface
- large datasets

## Slide 3 - Today's Success Pattern

Create a clean instructional success-pattern visual for comparing data
representations.

Show one central information card:

- Task: Read chapter
- Topic: Files
- Minutes: 30

Show four surrounding comparison cards:

- "recognize forms"
- "what gets easier?"
- "what gets harder?"
- "larger app need"

Add caption:

- "Representation choice depends on use."

Avoid:

- abstract theory imagery
- database schema complexity
- ranking one option as best

## Slide 4 - What We Will Use Today

Create a working-set visual titled "Today's Comparison Set".

Show five simple cards:

- plain text
- CSV
- JSON
- list/dictionary
- table-like preview

Below them, show two question cards:

- "What becomes easier?"
- "What becomes harder?"

Avoid:

- implementation details
- database logos
- code-heavy layout

## Slide 5 - What We Will Save For Later

Create a calm scope-boundary visual with two lanes:

Lane 1: "Today: recognize and compare"

Lane 2: "Later: build databases or ORMs"

Use a bookmark or parking icon for the later lane. The tone should suggest
"saved for later," not "forbidden."

Avoid:

- warning signs
- red X marks
- making databases look scary

## Slide 6 - Plain Text Is Human Friendly

Create a two-side tradeoff visual titled "Plain Text".

Left side:

- simple note card with two readable lines
- label: "Easy for humans"

Right side:

- same note with field labels missing
- label: "Harder for programs to select fields"

Add caption:

- "Plain text is useful, but structure is limited."

Avoid:

- making plain text look wrong or bad
- dense paragraphs
- warning symbols

## Slide 7 - CSV Is Table Friendly

Create a simple tradeoff visual titled "CSV".

Show a small table with columns:

- Task
- Topic
- Minutes

Show three rows. Highlight one row and one column.

Add two small notes:

- "Good for similar records"
- "Awkward for deeply nested data"

Avoid:

- spreadsheet software interface
- complex formulas
- charts or dashboards

## Slide 8 - JSON Is Structure Friendly

Create a simple tradeoff visual titled "JSON".

Show a small JSON-style card with labels:

- `"task"`
- `"topic"`
- `"minutes"`
- `"status"`

Next to it, show a small nested group labeled "details".

Add two small notes:

- "Good for labeled groups"
- "Can get hard to read if nesting grows"

Avoid:

- deeply nested JSON
- full code block
- syntax-heavy emphasis

## Slide 9 - Code Structures Can Mirror Data

Create a simple mapping visual titled "Code Can Mirror Data Shape".

Left side:

- stored data card labeled "task record"
- fields: task, topic, minutes

Right side:

- three possible Python structure cards:
  - dictionary
  - list of dictionaries
  - simple class

Show arrows from the data card to the structure cards.

Add caption:

- "The program's structure often follows the data's structure."

Avoid:

- advanced OOP diagrams
- inheritance trees
- dense code examples
- ranking one structure as best

## Slide 10 - Better Depends On Use

Create a four-card decision visual with these question cards:

- What needs to be read?
- What needs to be searched?
- What needs to be updated?
- What needs to be explained?

Use a simple neutral background and subtle color differences for each card.

Avoid:

- dashboard UI
- business analytics charts
- too many icons

## Slide 11 - Demo: Same Data, Different Representations

Create a diagram showing one information set in the center flowing into four
boxes:

- plain text
- CSV
- JSON
- dictionary/list

Center label:

- "same information"

Use arrows outward from the center. Keep all text large and readable.

Avoid:

- complex schema
- web app interface
- database implementation details

## Slide 12 - Preview: Larger Apps Need Stronger Structure

Create a simple bridge visual titled "Larger Apps May Need Stronger Structure".

Left side:

- small project with a single file and simple data

Right side:

- larger application flow with organized data blocks

Between them:

- arrow labeled "future need"

Add caption:

- "Recognition today, not database building."

Avoid:

- database implementation details
- full web app interface
- server/cloud architecture
- implying students must build this now

## Slide 13 - Common Failure: Bigger Is Not Automatically Better

Create a comparison visual titled "Right-Sized Beats Advanced-Looking".

Left side:

- advanced-looking option labeled "too much for this problem"
- include small icons/cards for database, class, API

Right side:

- right-sized option labeled "fits the task"
- show a simple file or dictionary solution

Add caption:

- "Choose the representation that fits the problem."

Avoid:

- making advanced tools look bad or forbidden
- red X marks
- ranking advanced tools as always wrong

## Slide 14 - Assignment 10 Bridge

Create a simple response-planning visual titled "A10: Compare and Explain".

Show a worksheet-style flow:

1. "Representation 1"
2. "Representation 2"
3. "What became easier?"
4. "What became harder?"
5. "Where might a larger app need more structure?"

Keep the layout clean and readable.

Avoid:

- legal rubric styling
- dense paragraphs
- database schema imagery

## Slide 15 - Evidence For A10

Create a simple comparison worksheet visual titled "A10 Evidence".

Sections:

- Representation 1
- Representation 2
- What became easier?
- What became harder?
- Larger app connection

Use a clean classroom handout style.

Avoid:

- legal rubric styling
- dense paragraphs
- decorative clutter
