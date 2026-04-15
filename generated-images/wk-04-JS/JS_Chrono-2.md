``` mermaid
flowchart LR
    A["JavaScript / ECMAScript<br/>Core Language"]

    B["Early Browser Scripting<br/>DOM manipulation, events, AJAX"]
    C["jQuery Era<br/>Simplified browser scripting"]
    D["SPA Pattern Emerges<br/>Client-side application architecture"]

    E["AngularJS<br/>Early full SPA framework"]
    F["React<br/>Component-based UI library"]
    G["Vue<br/>Progressive UI framework"]
    H["Angular<br/>Modern rewrite<br/>TypeScript-first"]

    I["Next.js<br/>React meta-framework"]
    J["Nuxt<br/>Vue meta-framework"]
    K["Remix / Gatsby / Others<br/>Specialized React ecosystem"]

    L["Node.js<br/>Server-side JavaScript"]
    M["Express<br/>Minimal Node web framework"]
    N["NestJS<br/>Structured backend framework"]

    O["TypeScript<br/>Typed superset of JavaScript"]

    A --> B
    B --> C
    C --> D

    D --> E
    D --> F
    D --> G
    E --> H

    F --> I
    F --> K
    G --> J

    A --> L
    L --> M
    M --> N

    A --> O
    O --> H
    O --> I
    O --> N
```