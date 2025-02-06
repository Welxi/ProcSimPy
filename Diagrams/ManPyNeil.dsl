neil = softwareSystem "ManPy Neil"{
    simNeil = container "ManPy Neil Simulation"{
        core = component "CoreObject"
        store = component "StoreObject"
        res = component "ResourceObject"
        entity = component "Entity"
        exit = component "Exit"
        machine = component "Machine"
        manpyObject = component "ManPyObject"
        queue = component "Queue"
        source = component "Source"
        experiment = component "Experiment"
        line = component "Line"

        core -> manpyObject "Inherits"
        entity -> manpyObject "Inherits"

        store -> core "Inherits"
        res -> core "Inherits"

        exit -> store "Inherits"
        machine -> store "Inherits"
        queue -> store "Inherits"
        source -> store "Inherits"

        experiment -> line "Creates a line to run experiment"

        line -> source "Manages"
        line -> queue "Manages"
        line -> machine "Manages"
        line -> exit "Manages"

        exit -> entity "Consumes"
        machine -> entity "Consumes"
        queue -> entity "Consumes"
        source -> entity "Consumes"
    }

    simpyV4 = container "SimPy Version 4"{
        store = component "Store"
        res = component "Resource"
        env = component "Environment"
    }

    simNeil.manpyObject -> simpyV4.env "Depends" 
    simNeil.store -> simpyV4.store "Depends"
    simNeil.res -> simpyV4.res "Depends"

    simNeil.core -> simNeil.core "Has Successors and Precursours of Inheritors"
    
    simNeil.source -> simNeil.queue "has Successor"
    simNeil.queue -> simNeil.machine "has Successor"
    simNeil.machine -> simNeil.exit "has Successor"
}
