workspace {

    !identifiers hierarchical

    model {
        !include ProcSimPy.dsl

        user = person "User"
        superuser = person "Super User"
        developer = person "Developer"

        simModel = softwareSystem "Simulation Model"
        simModel -> ProcessSimPy.ProcSimPy.experiment "Implements"

        user -> simModel "Uses"

        superUser -> simModel "Creates"
        superUser -> ProcessSimPy.ProcSimPy "Extends"

        developer -> ProcessSimPy.ProcSimPy "Creates"
    }


    views {
        
        theme default

        container ProcessSimPy "UserInteraction" {
            include *
            include ->simModel
            autolayout lr
        }

        component ProcessSimPy.ProcSimPy "AllComponents"{
            include *
        }

        # dynamic ProcessSimPy.ProcSimPy "Operation"{
        #     title "Operation Process"
        # }

        dynamic ProcessSimPy.ProcSimPy "Handover"{
            title "Handover Process"
            ProcessSimPy.ProcSimPy.queue -> ProcessSimPy.ProcSimPy.node "Requests Availability Token"
            ProcessSimPy.ProcSimPy.node -> ProcessSimPy.ProcSimPy.queue "Has no availability so request is not resolved"
            ProcessSimPy.ProcSimPy.queue -> ProcessSimPy.ProcSimPy.server "Requests Availability Token"
            ProcessSimPy.ProcSimPy.server -> ProcessSimPy.ProcSimPy.queue "Has Availability Token to give"
            ProcessSimPy.ProcSimPy.queue -> ProcessSimPy.ProcSimPy.server "Routes Entity based on availability Tokens"
            # autolayout lr
        }
    }
    
}