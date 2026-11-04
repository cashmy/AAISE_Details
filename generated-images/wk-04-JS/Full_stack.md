``` mermaid
flowchart TD
    User["User (Browser)"]

    subgraph Frontend["Frontend"]
        UI["HTML / CSS"]
        React["JavaScript / React"]
    end

    HTTP["HTTP Requests<br/>(Fetch / AJAX / Axios)"]

    subgraph Backend["Backend"]
        API["API Layer"]
        Logic["Business Logic"]
        DBAccess["Data Access Layer<br/>(ORM / Queries)"]
    end

    subgraph Database["Database"]
        DB["Database"]
    end

    User --> UI
    UI --> React
    React --> HTTP
    HTTP --> API
    API --> Logic
    Logic --> DBAccess
    DBAccess --> DB

    DB --> DBAccess
    DBAccess --> Logic
    Logic --> API
    API --> HTTP
    HTTP --> React
```