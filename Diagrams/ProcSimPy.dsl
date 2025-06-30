ProcessSimPy = softwareSystem "Process SimPy"{
    ProcSimPy = container "ProcSimPy"{
        experiment = component "Experiment"{
            description "Cordinator for running experiment iteration and output of data"
        }
        line = component "Line"{
            description "State tracker and Broker between Nodes"
        }

        base = component "Base"{
            description "Ensures unique id, connection to SimPy Environment and output tracing"
        }

        entity = component "Entity"{
            description "Generic for the item the Process is being preformed on, Manufactured Part or Customer engaging is service"
        }

        node = component "Node"{
            description "Generic Node for a Step in a Process"
        }

        source = component "Source"{
            description "Abstract for the beginning of the Process, Customer initial engagement or warehouse of stock"
        }
        queue = component "Queue"{
            description "Buffer or Routing Node"
        }
        server = component "Server"{
            description "Node that requires time to complete its work"
        }
        exit = component "Exit"{
            description "Abstract for the end of the Process"
        }

        res = component "Resource"{
            description "A Limiting Factor for the process, eg Number of Repair Technicians"
        }
        # operator = component "Operator"{
        #     description "Personnel Resource Required for task"
        # }
        repair = component "Repair Technician" {
            description "Personnel Resource With ability to repair failures"
        }

        interruption = component "Interruption"{
            description "Non Ideal situation to deal with"
        }

        failure = component "Node Failure"{
            description "Interruption to stop Node until repair"
        }

        shift = component "Shift Scheduler"{
            description "Controls timing for Shifts and breaks"
        }

        stats = component "Statistics"{
            description "Records stats for model component"
        }

        experiment -> line "Creates a line to run experiment"

        line -> source "Manages"
        line -> queue "Manages"
        line -> server "Manages"
        line -> exit "Manages"

        entity -> base "Inherits"

        node -> base "Inherits"
        res -> base "Inherits"

        exit -> node "Is a Node"
        server -> node "Is a Node"
        queue -> node "Is a Node"
        source -> node "Is a Node"

        exit -> entity "Consumes"
        server -> entity "Consumes"
        queue -> entity "Consumes"
        source -> entity "Consumes"

        repair -> node "Repairs Failure"

        shift -> node "Influences operating times"
        # shift -> res "Influences operating times"

        # operator -> res "Is a Resource"
        repair -> res "Is a Resource"

        # operator -> node "Can be required by"

        # interruption -> node "Non Ideal situation to deal with"
        failure -> interruption "Interruption until repair"
        failure -> node "Stops Process until repaired"
        repair -> failure "Able to correct cause of failure"

        stats -> node "Records stats"

        queue -> server "Has Successor"

    }
    
    simpyV4 = container "SimPy Version 4"{
        store = component "Store"
        res = component "Resource"
        env = component "Environment"
    }

    ProcSimPy.node -> simpyV4.store "Depends"
    ProcSimPy.res -> simpyV4.res "Depends"
}
