``` mermaid
flowchart LR
    A["JavaScript<br/>Core Language"]
    B["jQuery<br/>Browser Utility Era"]
    C["AngularJS<br/>MVC / SPA Framework"]
    D["React<br/>Component Model"]
    E["Vue<br/>Progressive Components"]
    F["Angular<br/>Modern TS Framework"]
    G["Next.js<br/>React Full-Stack / SSR"]
    H["Nuxt<br/>Vue Full-Stack / SSR"]
    I["Node.js<br/>Server-Side JavaScript"]
    J["Express / NestJS<br/>Backend Frameworks"]
    K["TypeScript<br/>Typed JavaScript Ecosystem"]

    A --> B
    B --> C
    C --> D
    D --> E
    C --> F
    D --> G
    E --> H
    A --> I
    I --> J
    A --> K
    K --> F
    K --> G
    K --> J
```