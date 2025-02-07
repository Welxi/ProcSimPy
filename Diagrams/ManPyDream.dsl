dream = softwareSystem "Dream Project" {
        simDream = container "ManPy Dream Simulation" {
            core = component "CoreObject"
            entity = component "Entity"
            exit = component "Exit"
            globals = component "Global 'G'"
            machine = component "Machine"
            manpyObject = component "ManPyObject"
            interupt = component "ObjectInteruption"
            objectRes = component "Object Resource"
            operator = component "Operator"
            operatorPool = component "OperatorPool"
            broker = component "Broker"
            router = component "Router"
            part = component "Part"
            queue = component "Queue"
            source = component "Source"

            core -> globals "Depends"
            entity -> globals "Depends"
            exit -> globals "Depends"
            machine  -> globals "Depends"
            operator -> globals "Depends"
            router -> globals "Depends"
            part -> globals "Depends"
            queue -> globals "Depends"
            source -> globals "Depends"

            core -> manpyObject "Inherits"
            entity -> manpyObject "Inherits"
            interupt -> manpyObject "Inherits"
            objectRes -> manpyObject "Inherits"

            broker -> interupt "Inherits"
            router -> interupt "Inherits"
            operator -> objectRes "Inherits"
            operatorPool -> objectRes "Inherits"

            exit -> core "Inherits"
            machine -> core "Inherits"
            queue -> core "Inherits"
            source -> core "Inherits"

            part -> entity "Inherits"
        }
        simpyV2 = container "Simpy V2"{
            env = component "Environment"
            res = component "Resource"
        }
        ket = container "Knowledge Extraction Tool"
        webUI = container "Web User Interface"

        simDream -> simpyV2.env "Depends"
        simDream -> simpyV2.res "Depends"

        ket -> simDream "Feeds Model Data"
        webUI -> simDream "Gets Simulation Data from"
}