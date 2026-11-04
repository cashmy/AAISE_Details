``` mermaid
flowchart LR
    ES["ECMAScript / JavaScript (Core Language)"]

    JQuery["jQuery Era<br/>DOM-heavy UI development"]
    SPA["Single Page App Pattern"]
    AngularJS["AngularJS<br/>(2010, JS)"]
    Angular["Angular<br/>(2016+, TypeScript-first)"]
    React["React<br/>(2013, component-based UI)"]
    Vue["Vue<br/>(2014, progressive framework)"]
    Svelte["Svelte<br/>(compiler-based approach)"]

    Next["Next.js<br/>(React meta-framework)"]
    Gatsby["Gatsby<br/>(React static/meta framework)"]
    Remix["Remix<br/>(React full-stack framework)"]

    Nuxt["Nuxt<br/>(Vue meta-framework)"]
    Quasar["Quasar<br/>(Vue app framework)"]

    Node["Node.js<br/>(server-side JavaScript)"]
    Express["Express<br/>(Node web framework)"]
    Nest["NestJS<br/>(Node/TypeScript backend framework)"]

    TS["TypeScript<br/>(typed superset of JS)"]

    ES --> JQuery
    ES --> SPA
    ES --> Node
    ES --> TS

    SPA --> AngularJS
    AngularJS --> Angular

    SPA --> React
    SPA --> Vue
    SPA --> Svelte

    React --> Next
    React --> Gatsby
    React --> Remix

    Vue --> Nuxt
    Vue --> Quasar

    Node --> Express
    Node --> Nest

    TS --> Angular
    TS --> Nest
    TS --> Next
```