``` mermaid
flowchart LR
    JS["JavaScript / ECMAScript"]

    subgraph Frontend["Frontend UI Ecosystem"]
        AngularJS["AngularJS"]
        Angular["Angular"]
        React["React"]
        Vue["Vue"]
        Svelte["Svelte"]
    end

    subgraph Meta["Meta-Frameworks / App Frameworks"]
        Next["Next.js"]
        Nuxt["Nuxt"]
        Gatsby["Gatsby"]
        Remix["Remix"]
    end

    subgraph Backend["Backend / Server Ecosystem"]
        Node["Node.js"]
        Express["Express"]
        Nest["NestJS"]
    end

    TS["TypeScript"]

    JS --> AngularJS
    AngularJS --> Angular
    JS --> React
    JS --> Vue
    JS --> Svelte
    JS --> Node
    JS --> TS

    React --> Next
    React --> Gatsby
    React --> Remix
    Vue --> Nuxt

    Node --> Express
    Node --> Nest

    TS --> Angular
    TS --> Next
    TS --> Nest
```