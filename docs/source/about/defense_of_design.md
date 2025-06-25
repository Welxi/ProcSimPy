In many cases when setting up ProcSimPy objects accessing prebuilt functionality is done in the constructor method. the preferred method is to use the enums provided, this allows for greater static analysis done by your editor and ensuring the requested functionality is supported. If there is missing functionality please open an Issue on the GitHub Page


>Note on Time
>The Library relies on [SimPy time scheduling](https://simpy.readthedocs.io/en/latest/topical_guides/time_and_scheduling.html). It is agnostic to the time scale of the model, what one time unit means in your system is up to you (1 second/minute/hour/etc.)
>
>It is important to note that you keep the same base when inputting values 
