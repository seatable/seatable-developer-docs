## just to test ...

``` mermaid
graph LR
  A[Start] --> B{Error?};
  B -->|Yes| C[Hmm...];
  C --> D[Debug];
  D --> B;
  B ---->|No| E[Yay!];
```

``` mermaid
gitGraph
   commit
   commit
   branch develop
   checkout develop
   commit
   commit
   checkout main
   merge develop
   commit
   commit
```

``` mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
    E-->C;
    F-->E;
    G-->F;
```

``` mermaid 
pie title Pets adopted by volunteers
    "Dogs" : 386
    "Cats" : 85
    "Rats" : 15
```

``` mermaid
gantt
    title A Gantt Diagram
    dateFormat YYYY-MM-DD
    section Section
        A task          :a1, 2014-01-01, 4d
        Another task    :after a1, 10d
    section Another
        Task in Another :2014-01-12, 2d
        another task    :4d
```
