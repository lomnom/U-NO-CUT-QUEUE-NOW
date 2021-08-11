diagram:
┌───────────────────────────────┐
│                               │
│                               │
│                               │
│                               │
│           deli inn            │
│                               │
│                               │
│                               │
│                               │
│                               │
└────────────┬────┬─────────────┘
microbit 2  x│    │x master
             │ ┌┐ │
             │ └┘ │
             │    │
             │    │
             │    │queue
             │    │
            ▲│    │▲
     lazer 2││    ││ lazer 1
            └┴────┴┘
            
             data
microbit 2 -------> master
master keeps track of lazer status
master rings buzzer
