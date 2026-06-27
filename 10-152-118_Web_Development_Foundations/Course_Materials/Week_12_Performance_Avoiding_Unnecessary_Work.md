# Week 12 Handout - Performance: Avoiding Unnecessary Work

**Course:** 10-152-118 Web Development Foundations  
**Purpose:** Prepare for Week 12 lecture and lab by understanding how working web projects can be improved for speed, responsiveness, and efficiency.

---

## 1. Performance Means Avoiding Unnecessary Work

A page can be technically correct and still feel slow.

For this course, think about performance in three beginner-friendly ways:

```text
Download less.
Show less at one time.
Do work less often.
```

These ideas connect to common web performance strategies:

- **Image optimization:** avoid making the browser download files that are larger
  than needed.
- **Pagination/chunking:** avoid showing too much information all at once.
- **Debounce:** wait until repeated activity has stopped for a short time before
  running a function.
- **Throttle:** allow work to happen only once per set amount of time during
  repeated activity.

Useful distinction:

```text
Debounce waits for a pause.
Throttle controls the pace.
```

Examples:

- Debounce can help with a search box because the app can wait until the user
  pauses typing.
- Throttle can help with scrolling or resizing because the app can respond at a
  controlled rate instead of reacting to every tiny event.

| Pattern | Plain Meaning | Good For |
|---|---|---|
| Image optimization | Use appropriately sized files | photos, galleries, hero images |
| Pagination | Split large results into smaller groups | lists, tables, cards, search results |
| Debounce | Wait until the user pauses | search boxes, input validation, autosave |
| Throttle | Limit how often work runs | scroll, resize, repeated progress updates |

---

## 2. Performance Is User Experience

Performance is not only a technical detail.

It affects how a page feels.

When a page is slow, users may think:

- The page is broken.
- The button did not work.
- The site is poorly built.
- Their device or connection is the problem.

When a page responds clearly and quickly, users have more confidence in the
application.

This week is not about becoming a performance specialist. The goal is to notice
obvious inefficiencies and improve them in visible, explainable ways.

---

## 3. Images: Download Less

Images often affect performance because they can be large files.

Key idea:

```text
Larger image files take longer to download.
Longer downloads make pages feel slower.
```

An image may look small on the page but still have a large file size.

For example:

```text
Displayed size: 300px wide
Actual file:    4000px wide
```

The browser may still need to download the large file before shrinking it on the
page. That wastes time and bandwidth.

Beginner image performance habits:

- Use image dimensions that fit the actual design need.
- Compress images when appropriate.
- Avoid using very large images as small thumbnails.
- Consider smaller versions of images for smaller screens.
- Add image dimensions when possible so the browser can reserve space.
- Use lazy loading for images that do not need to appear immediately.

Example:

```html
<img src="gallery-photo.jpg" alt="Student project example" loading="lazy">
```

The `loading="lazy"` attribute tells the browser it may wait to load the image
until the image is closer to being needed.

Do not assume students will automatically connect "images" to "performance."
For this week, make the connection explicit:

```text
Image choices affect download size.
Download size affects load time.
Load time affects user experience.
```

---

## 4. Pagination And Chunking: Show Less At One Time

Sometimes a page feels slow because it tries to show too much at the same time.

Examples:

- 500 search results.
- A long product list.
- Many image cards.
- A large table.
- A long list fetched from an API.

Pagination means splitting a large set of results into smaller pages.

```text
Instead of showing 500 items at once:
Show 10, 20, or 50 at a time.
```

This can help because:

- The browser has less to display at once.
- The user has less to scan at once.
- The page can feel more responsive.
- The design can guide users through the information.

Pagination is not only a programming technique. It is also a design decision.

```text
How much information should the user see right now?
What can wait until later?
```

Related patterns:

- **Pagination:** page 1, page 2, page 3.
- **Load more:** show more when the user asks.
- **Filtering/searching:** reduce the list before displaying it.
- **Lazy loading:** wait to load something until it is needed.

You do not need to build full pagination this week unless assigned.

For now, recognize why large lists are often split into smaller parts.

---

## 5. Repeated Events: Do Work Less Often

Some browser events can happen many times in a short period.

Examples:

- A user types into a search box.
- A user scrolls down the page.
- A user resizes the browser window.
- A filter updates a long list.
- A button is clicked repeatedly.

If a function runs every single time, the page may do unnecessary work.

```text
Event fires.
Function runs.
Event fires again.
Function runs again.
Event fires again.
Function runs again.
```

Sometimes that is fine. Sometimes it becomes sluggish.

Performance thinking asks:

```text
Does this work need to happen every time?
Could it happen less often and still feel correct?
```

---

## 6. Debounce: Wait For A Pause

Debounce delays work until repeated activity has stopped for a short time.

Plain-language version:

```text
Wait until the user pauses.
Then do the work.
```

Debounce is useful when the final input matters more than every small change.

Common examples:

- Search after the user pauses typing.
- Validate a form field after typing stops.
- Autosave after the user stops editing for a moment.

Conceptual timeline:

```text
type -> type -> type -> pause -> run search
```

Without debounce, a search feature might run after every letter.

With debounce, the search waits until the user pauses.

This can reduce unnecessary work and make the page feel calmer.

---

## 7. Throttle: Control The Pace

Throttle limits how often work can happen during repeated activity.

Plain-language version:

```text
Do the work at a controlled rate.
```

Throttle is useful when activity continues for a while but the page still needs
to respond periodically.

Common examples:

- Responding to scroll position.
- Responding to window resize.
- Updating progress during a repeated action.

Conceptual timeline:

```text
scroll scroll scroll scroll scroll
run       run       run       run
```

Without throttle, a scroll handler might run constantly.

With throttle, the work runs at a limited pace.

This can keep the page responsive while still reacting to the user's action.

---

## 8. Before / After Thinking

Performance improvement should be visible or explainable.

Before:

```text
The page downloads images that are larger than needed.
The page shows every item at once.
The function runs every time an event fires.
```

After:

```text
The page uses appropriately sized images.
The page shows a smaller set of items at a time.
The function runs only when useful.
```

A good Week 12 explanation should sound like:

```text
This version is better because it avoids unnecessary work.
```

Then name the work:

- fewer or smaller downloads
- fewer visible items at once
- fewer repeated function calls
- clearer user feedback while loading or updating

---

## 9. What To Focus On / What To Ignore For Now

Focus on:

- Performance as part of user experience.
- Image file size affecting load time.
- Large lists being split into smaller parts.
- Repeated event work making pages sluggish.
- Debounce waiting for a pause.
- Throttle controlling the pace.
- Comparing before and after behavior.
- Explaining why the optimized version is better.

Ignore for now:

- Deep browser rendering internals.
- Core Web Vitals in detail.
- Build tools.
- Bundlers.
- Advanced profiling.
- Complex caching strategies.
- Backend pagination logic.
- Perfect optimization.

The goal is practical judgment: notice waste, reduce it, and explain the
improvement clearly.

---

## Reference Links

- MDN Throttle Glossary: https://developer.mozilla.org/en-US/docs/Glossary/Throttle
- MDN Lazy Loading: https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Lazy_loading
- MDN Image Loading Property: https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/loading
- MDN Responsive Images: https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images
- MDN `<img>` Element: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img
