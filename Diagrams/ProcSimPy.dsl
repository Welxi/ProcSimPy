Process = softwareSystem "Process SimPy"{
    ProcSimPy = container "ProcSimPy"{
        base = component "BaseObject"{
            description "Ensures unique id and output Tracing"
        }
        store = component "StoreNode"{
            description "Node in the Process of consideration"
        }
        res = component "ResourceObject"{
            description "A Limitied Resource a StoreNode may need to preform its step"
        }
        entity = component "Entity"{
            description "Generic for the item the Process is being preform on, Manufactured Part or Customer engaging is service"
        }
        exit = component "Exit"{
            description "Abstract for the end of the Process"
        }
        machine = component "Machine"{
            description "Node that requires time to complete its process"
        }
        queue = component "Queue"{
            description "Buffer or Routing Node"
        }
        source = component "Source"{
            description "Abstract for the begining of the Process, Customer initial engagement or warehouse of stock"
        }
        experiment = component "Experiment"{
            description "Cordinator for running experiment iteration and output of data"
        }
        line = component "Line"{
            description "State tracker and Broker between nodes"
        }

        operator = component "Operator"{
            description "Personnel Resource Required for task"
        }
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

        shift -> store "Influences operating times"
        shift -> res "Influences operating times"

        operator -> res "Is a Resource"
        repair -> res "Is a Resource"

        operator -> store "Can be required by"

        interruption -> store "Non Ideal situation to deal with"
        failure -> interruption "Interruption to stop Node until repair"
        failure -> store "Stops Process until repaired"
        repair -> failure "Able to correct cause of failure"

        repair -> store "Repairs Failure"

        entity -> base "Inherits"

        store -> base "Inherits"
        res -> base "Inherits"

        exit -> store "Is a Node"
        machine -> store "Is a Node"
        queue -> store "Is a Node"
        source -> store "Is a Node"

        experiment -> line "Creates a line to run experiment"

        line -> source "Manages"
        line -> queue "Manages"
        line -> machine "Manages"
        line -> exit "Manages"

        exit -> entity "Consumes"
        machine -> entity "Consumes"
        queue -> entity "Consumes"
        source -> entity "Consumes"

        #TODO Statistics
        #TODO Sub processes (Entity createion, process entity)
    }

    simpyV4 = container "SimPy Version 4"{
        store = component "Store"
        res = component "Resource"
        env = component "Environment"
    }

    ProcSimPy.store -> simpyV4.store "Depends"
    ProcSimPy.res -> simpyV4.res "Depends"
    
    ProcSimPy.source -> ProcSimPy.queue "has Successor"
    ProcSimPy.queue -> ProcSimPy.machine "has Successor"
    ProcSimPy.machine -> ProcSimPy.exit "has Successor"
}
