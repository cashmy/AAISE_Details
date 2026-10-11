# Learning Resource Navigator: Data Sourcing Plan

Instructor planning proposal v1 | October 8, 2026

## Recommendation

Use real, reviewed learning-resource links as the application's initial catalog. Begin with a frozen local JSON snapshot so filtering, searching, ranking, and export work without live discovery calls. Add search/API imports later if they support the learning outcomes.

Target approximately 30-50 reviewed resources for the first full demonstration catalog, with a small 8-12 record subset for hand-checkable demos. This is a proposed target; the candidate list below is an initial source check, not a completed catalog.

Include Python foundations and reference material, selected JavaScript connections, and introductory algorithm explanations or lecture resources. Vary topic, format, scope, and teaching difficulty enough to make selection and ranking meaningful. Do not require every resource to be an assigned course reading.

## Source Selection

| Source | Role in the Catalog | Selection Guidance |
| --- | --- | --- |
| Python documentation | Python collections, filtering, modules, sorting, timing, caching, and hashing references | Use specific pages or sections; distinguish a tutorial from an API reference |
| MDN Web Docs | Occasional JavaScript comparisons and prerequisite refreshers | Select collections/modules and other relevant topics rather than a broad web-development syllabus |
| MIT OpenCourseWare | Algorithm lecture notes and videos | Select accessible excerpts; review prerequisite demands before recommending full lectures |
| Instructor-created materials | Course-specific tests, traces, examples, and explanations | Identify these as local instructional resources, not externally sourced publications |

Primary sources should establish resource identity and technical content. Search results and research LLMs can locate candidates; acceptance requires opening the actual resource and checking relevance.

## Initial Candidate List

The links below were accessible through browsing on October 8, 2026. Titles and broad topic coverage were checked at the page level. Estimated study time, difficulty, exact excerpts, and instructional suitability remain to be reviewed. Accessibility today does not guarantee future availability.

| Candidate | Provider / Format | Potential Course Use |
| --- | --- | --- |
| [Data Structures](https://docs.python.org/3/tutorial/datastructures.html) | Python documentation / tutorial | Lists, stacks, queues, comprehensions/filtering, sets, and dictionaries |
| [Sorting Techniques](https://docs.python.org/3/howto/sorting.html) | Python documentation / how-to | Key-based sorting and ordering comparisons |
| [timeit](https://docs.python.org/3/library/timeit.html) | Python documentation / reference | Controlled timing support |
| [functools](https://docs.python.org/3/library/functools.html) | Python documentation / reference | Caching/memoization support |
| [hashlib](https://docs.python.org/3/library/hashlib.html) | Python documentation / reference | Library-based digest/integrity demonstrations |
| [Indexed collections](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections) | MDN / guide | Array operations and Python/JS comparisons |
| [Keyed collections](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Keyed_collections) | MDN / guide | JavaScript Map/Set comparisons |
| [JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules) | MDN / guide | Modularity connections |
| [6.006 Lecture Notes](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/pages/lecture-notes/) | MIT OCW / resource index | Locate specific sorting, BFS, DFS, and memoization notes; create separate records for selected resources later |
| [Lecture 13: Breadth-First Search](https://www.youtube.com/watch?v=s-CYnVz-uh4) | MIT OpenCourseWare / video | Optional graph-traversal support; verify appropriate segments before assigning |

Prefer selected-resource URLs over broad indexes in the final catalog. A whole tutorial chapter can also have a narrower section record if that gives students a clearer learning task. Store a stable resource ID and the page/section relationship to avoid treating overlapping sections as independent publications.

## Metadata and Provenance

Distinguish source facts from instructional judgments. The application can rank on both, but should show which fields were assigned by the instructor.

| Field | Origin / Treatment |
| --- | --- |
| `id` | Locally assigned stable catalog identifier |
| `title`, `url`, `provider` | Verified against the source |
| `format`, `language` | Checked source attributes; distinguish text, video, PDF, guide, reference, and resource index |
| `source_version` | Documented version or course offering where available; otherwise null |
| `source_duration_minutes` | Publisher-provided duration where available; otherwise null |
| `topics`, `tags` | Instructor-curated classification; use a controlled vocabulary |
| `difficulty` | Instructor judgment for this cohort, not an asserted publisher rating |
| `estimated_study_minutes` | Instructor estimate for the selected task or excerpt; nullable until reviewed |
| `prerequisite_topics` | Instructor-defined learning relationships unless explicitly supplied by the source |
| `selection_notes` | Short original notes identifying useful sections, scope, and limitations |
| `discovery_method` | Direct documentation, web search, LLM suggestion, or API import |
| `verified_on`, `review_status` | Link-check date and distinction between candidate, reviewed, and excluded |

Do not fill unknown fields with invented facts. In particular, a video's runtime is not the same as the time needed to study and practice its content. Instructor-authored prerequisite links form a teaching model, not a claim that the publisher specifies that dependency graph.

## Acquisition Workflow

1. Use the daily topic map to identify coverage needs.
2. Discover candidates through official site navigation, web search, a research LLM, or an API.
3. Open the source; confirm identity, access, format, relevant content, and version where applicable.
4. Add verified source metadata and a short original description.
5. Assign instructional tags, estimated effort, difficulty, and prerequisites with explicit provenance.
6. Review duplicates, coverage balance, and suitability for the cohort.
7. Save an approved local snapshot for deterministic demos and tests.

If a research LLM returns titles/links or structured records, treat them as unverified candidates. Search snippets should not replace source review. Store links and original summaries rather than copying entire resource contents into the catalog.

## Optional API or Search Integration

An API is a possible acquisition method, not a prerequisite for the first application version. Evaluate a provider later for relevant resource coverage, usable metadata, stable identifiers, access requirements, and import reliability before selecting it.

If adopted, use this boundary:

`external discovery -> candidate records -> normalization -> instructor review -> local catalog`

The navigator's core algorithms should consume the same local schema whether records were entered manually or imported. Preserve the snapshot if the external service is unavailable. Do not make search-result ordering the app's recommendation score; students should define and explain the app's ranking independently.

Live refresh/import can provide a later connection to APIs and asynchronous workflows, while core course work stays focused on algorithmic decisions. Avoid making direct scraping of Google result pages the acquisition mechanism.

## Real Catalog and Experimental Data

Maintain three distinct data purposes:

- **Real catalog:** reviewed actual resources used for meaningful navigation and exported study guides.
- **Small fixtures:** selected real records for hand-verifiable traces, tests, and score calculations.
- **Generated experimental datasets:** clearly labeled synthetic records for growth/benchmark experiments and deliberate edge cases.

Do not present replicated or synthetic benchmark records as thousands of distinct real resources. Synthetic links should not appear in a usable exported study guide. Tests may deliberately include invalid records, ties, missing fields, or duplicate IDs without claiming those defects came from a real provider.

## Next Deliverable

Create a reviewed seed catalog and its metadata dictionary before building the basic/full reference application. Start with small fixtures, then expand toward the 30-50 resource target. Use the catalog to validate that filtering, ordering, similarity, prerequisite relationships, and export produce useful results.

This artifact records the sourcing recommendation and initial candidates. It does not implement an importer, populate a completed JSON catalog, or change the course reading requirements.
