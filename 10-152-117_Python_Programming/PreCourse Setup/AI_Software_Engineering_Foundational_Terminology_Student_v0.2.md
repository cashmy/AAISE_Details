# Thinking Like an AI Software Engineer

## A Small Vocabulary for Seeing the Bigger Picture

Software engineering is more than learning syntax, frameworks, and tools. As you build software, you will also learn how to **understand problems, make choices, test what is actually happening, and decide what to do next**.

This handout introduces a small set of terms we will use throughout the program. You do **not** need to memorize them. You are not expected to understand everything behind them yet.

For now, the goal is simple:

> **Recognize the terms and begin noticing them in the work you do.**

Their meaning will grow as your experience grows.

---

## Meaning Matters: Semantic Awareness & Semantic Precision

As you learn software development, you will encounter many words that look or sound similar but mean different things depending on the context.

Learning to notice those differences—and to communicate them accurately—is an important engineering skill.

### Semantic Awareness — Notice What a Term Means Here

**Plain meaning:** Recognizing that words, symbols, and phrases have meaning within a particular context, and that similar-looking terms may refer to very different concepts.

**Software example:**  
In Python, **Type Awareness** is about recognizing the data type of a value. A lesson about **typing vs. copy/paste** is about how you enter or produce code.

Both use forms of the word *type*, but they are talking about different things.

Semantic Awareness helps you notice:

> “These words look related, but what does each one actually mean in this context?”

**Everyday example:**  
A *bank* can hold money or describe the side of a river. The word alone does not determine the meaning—the context helps you understand it.

---

### Semantic Precision — Say What You Actually Mean

**Plain meaning:** Choosing and using words, names, and concepts carefully enough to communicate the meaning you actually intend.

Semantic Precision becomes especially useful when a small difference in wording represents an important difference in the system.

**Software example:**  
Compare:

> “Python changed my variable.”

with:

> “I reassigned the variable to a string value.”

The second statement gives us more precise information about what happened and makes the problem easier to understand and investigate.

**AI example:**  
Suppose you tell an AI:

> “Change the component.”

Which component? What kind of change?

You might instead say:

> “Change the React `StudentCard` component so it displays the student's program beneath their name.”

Greater Semantic Precision gives the AI a clearer representation of your Intent.

---

### How They Work Together

You can think of the relationship this way:

```text
SEMANTIC AWARENESS
What does this actually mean here?
          ↓
SEMANTIC PRECISION
How can I express that meaning accurately?
          ↓
CLEARER UNDERSTANDING & COMMUNICATION
          ↓
BETTER PROBLEM SOLVING & FEEDBACK
```

You will use these capabilities when reading instructions, naming variables and functions, debugging, discussing requirements, writing documentation, communicating with teammates, and working with AI.

You do not need perfect technical vocabulary before you can begin.

The important habit is to notice when **meaning matters** and become increasingly precise as your understanding grows.

---

## SKY, CORE, and BASE

One useful way to think about a problem is to look at it from three different levels.

### SKY — The Bigger Picture

**Plain meaning:** What are we really trying to accomplish, and how does this fit into the larger system?

SKY helps you look beyond the immediate task.

**Software example:**  
Before building a login page, you might ask:

> Why does this application need users to log in? What are we protecting? What should a logged-in user be able to do?

Those questions are more SKY than questions about button colors or Python syntax.

**Everyday example:**  
If you are planning a trip, SKY is the reason for the trip and what you want the overall experience to accomplish—not which road you will take.

---

### CORE — What Makes It Work

**Plain meaning:** The important ideas, relationships, rules, and capabilities that connect the bigger purpose to what you actually build.

CORE helps organize your approach.

**Software example:**  
For a login system, CORE might include understanding authentication, deciding what information must be protected, and knowing how the parts of the application should work together.

**Everyday example:**  
For your trip, CORE includes the route, budget, schedule, transportation, and other important decisions that make the trip possible.

---

### BASE — Where You Do the Work

**Plain meaning:** The actual implementation, action, code, test, or specific detail in front of you.

BASE is where ideas encounter reality.

**Software example:**  
Writing the HTML form, creating a Python function, fixing a CSS rule, running a test, or reading an error message are all BASE activities.

**Everyday example:**  
Getting in the car, turning onto a particular street, or buying the ticket is BASE.

---

### Moving Between Them

SKY, CORE, and BASE are not three boxes that you move through once.

You will move among them.

```text
SKY
What are we trying to accomplish?
        ↓
CORE
What needs to be understood or organized?
        ↓
BASE
What do I actually build or do?
        │
        └──── something unexpected happens
                         ↓
                   look upward again
```

Sometimes you will be deep in code and realize that the real problem is not the line you are editing. You may need to move back toward CORE or SKY, reconsider what is happening, and then return to the code.

We will sometimes call this movement **Sky-Bounce**.

---

## Intent

**Plain meaning:** What you are actually trying to accomplish.

Intent gives direction to your choices.

**Software example:**  
If you tell an AI, “Make this function better,” the Intent is unclear.

Do you want it to be faster? Easier to read? More secure? Easier to maintain?

Clarifying the Intent can change the solution.

**Everyday example:**  
“I need food” and “I need a quick meal before class” have related but different Intent. The second gives you much better guidance for deciding what to do.

---

## Agency

**Plain meaning:** Your ability to make meaningful choices and take action.

Having Agency means you are participating in the decision rather than simply following instructions.

**Software example:**  
An instructor may give you a problem without telling you exactly how to solve it. Choosing an approach, trying it, and changing direction when needed are exercises of your Agency.

AI can also be given limited Agency—for example, permission to modify several files rather than merely suggest code.

**Everyday example:**  
A GPS can recommend a route. You still decide whether to follow it.

---

## Responsibility

**Plain meaning:** What you are accountable for evaluating, deciding, doing, or verifying.

Agency and Responsibility often belong together.

**Software example:**  
AI may generate code for you, but using AI does not automatically transfer Responsibility for your application to the AI.

If you choose to use the code, you still need to determine whether it works and whether it belongs in your application.

**Everyday example:**  
A calculator can perform the arithmetic. You are still responsible for deciding whether you entered the right numbers and whether the answer makes sense.

---

## Reality Contact

**Plain meaning:** Evidence from what is actually happening.

Your expectations, assumptions, and explanations matter—but Reality Contact gives you something concrete to compare them against.

**Software example:**  
You believe your function returns a user object.

You run it.

It returns `None`.

That result is Reality Contact.

Instead of arguing with the program about what it *should* have done, you now have evidence that can help you investigate what it actually did.

**Everyday example:**  
The weather forecast says sunshine. You walk outside and it is raining.

The rain wins. 😄

---

## Feedback

**Plain meaning:** Information produced by an action or result that can help you decide what to do next.

Feedback makes learning and development recursive: what happens now can change your next action.

**Software example:**

```text
Write code
   ↓
Run it
   ↓
Observe the result
   ↓
Learn something
   ↓
Change the code
   ↓
Run it again
```

An error message is Feedback. A failing test is Feedback. A user struggling with your interface is Feedback. A successful result is Feedback too.

**Everyday example:**  
You are learning to shoot a basketball. Each shot gives you information that can affect the next one.

---

## Relationships Matter

Software is made of individual pieces, but the pieces do not operate alone.

**Plain meaning:** Understanding how things relate is often more useful than understanding each thing separately.

**Software example:**  
You may correctly write:

- an HTML button,
- a JavaScript function,
- and an event listener.

But if the event listener is not connected to the correct button, the application still does not work.

Each piece can be correct while the **relationship between the pieces** is wrong.

This idea will become increasingly important as the systems you build become larger.

---

# Putting the Ideas Together

Imagine you are debugging an application and a button does nothing.

At **BASE**, you inspect the button, JavaScript, browser console, and actual behavior.

That gives you **Reality Contact**.

The browser's error message provides **Feedback**.

You use your **Agency** to decide what to investigate next while retaining **Responsibility** for verifying the result.

If the local code looks correct, you may move upward:

> Is the event connected correctly?  
> Is this component supposed to behave this way?  
> What was our original **Intent**?

You have moved from BASE toward CORE or SKY.

Then you return to BASE and try another solution.

That movement is part of software engineering.

---

# As AI Becomes Part of Your Work

Early in the program, you may use AI to explain something, answer a question, or help you find an error.

Later, you will use AI in increasingly capable ways.

Eventually, you may build applications in which AI itself can make decisions or take actions.

The same questions will continue to matter:

> **What are we trying to accomplish?** — Intent  
>
> **Who or what can take action?** — Agency  
>
> **Who is responsible for the result?** — Responsibility  
>
> **What does the evidence actually show?** — Reality Contact  
>
> **What did we learn from the result?** — Feedback  
>
> **Are we stuck in a detail and need to look at the larger system?** — SKY / CORE / BASE

You do not need complete answers to those questions today.

You will encounter them repeatedly as you learn web development, Python, algorithms, software design, AI-assisted development, and eventually AI integrated into applications.

---

## One Thing to Remember

You do not need to memorize this sheet.

Use it.

When one of these terms appears in class, an assignment, a debugging session, or a conversation with AI, notice what it means **in that situation**.

Over time, the words should become less important than the way of thinking they help you develop.

> **The goal is not to know the vocabulary. The goal is to become better at seeing what is happening, understanding how the pieces relate, making responsible choices, and deciding what to do next.**
