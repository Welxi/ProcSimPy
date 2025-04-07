workspace {

    !identifiers hierarchical

    model {
        !include ProcSimPy.dsl  
        !include ManPyDream.dsl

        user = person "User"
        superuser = person "Super User"
        developer = person "Developer"

        simModel = softwareSystem "Simulation Model"
        simModel -> Process.ProcSimPy "Implements"
        simModel -> Process.ProcSimPy.experiment "Implements"
        simModel -> dream.simDream "Implements"

        # user -> simModel "Creates"
        user -> dream.webUI "Uses"
        user -> dream.ket "Uses"

        superUser -> simModel "Creates"
        superUser -> Process.ProcSimPy "Extends"
        superUser -> dream.simDream "Extends"

        developer -> Process.ProcSimPy "Creates"
        developer -> dream.simDream "Creates"
    }


    views {
        
        theme default

        # systemContext simModel "simModelsc" {
        #     include *
        #     autolayout tb
        # }

        # systemContext Neil "Neilsc" {
        #     include *
        #     autolayout lr
        # }

        # systemContext dream "Dreamsc" {
        #     include *
        #     autolayout lr
        # }


        container Process "UserInteraction" {
            include *
            include ->simModel
            autolayout lr
        }


        # container dream "dreamcc" {
        #     include *
        #     autolayout lr
        # }

        component Process.ProcSimPy "AllComponents"{
            include *
            # autolayout lr
        }
 
        # component dream.simDream "simDream" {
        #     include *
        #     autolayout bt
        # }

        dynamic Process.ProcSimPy "HandoverWithCapacity"{
            title "Core Handover of Entity, Machine is waiting"
            Process.ProcSimPy.source -> Process.ProcSimPy.entity "Entity is created by Source"
            Process.ProcSimPy.entity -> Process.ProcSimPy.source "Entity is assigned to Source"
            Process.ProcSimPy.source -> Process.ProcSimPy.queue "Source asks if reciver canRecieve"
            Process.ProcSimPy.queue -> Process.ProcSimPy.source "If not at Capacity returns True"
            Process.ProcSimPy.source -> Process.ProcSimPy.queue "Triggers isRequested Event on Queue"

            Process.ProcSimPy.queue -> Process.ProcSimPy.machine "Queue asks if reciver canRecieve"
            Process.ProcSimPy.machine -> Process.ProcSimPy.queue "Machine is waiting so returns true"
            Process.ProcSimPy.queue -> Process.ProcSimPy.machine "Triggers isRequested Event on Machine"

            Process.ProcSimPy.machine -> Process.ProcSimPy.exit "Machine asks if reciver canRecieve"
            Process.ProcSimPy.exit -> Process.ProcSimPy.machine "Exit can always recive"
            Process.ProcSimPy.machine -> Process.ProcSimPy.exit "Triggers isRequested Event on Exit"
        }

        dynamic Process.ProcSimPy "HandoverWithoutCapacity"{
            title "Core Handover of Entity, Machine is working"
            Process.ProcSimPy.source -> Process.ProcSimPy.entity "Entity is created by Source"
            Process.ProcSimPy.entity -> Process.ProcSimPy.source "Entity is assigned to Source"
            Process.ProcSimPy.source -> Process.ProcSimPy.queue "Source asks if reciver canRecieve"
            Process.ProcSimPy.queue -> Process.ProcSimPy.source "If not at Capacity returns True"
            Process.ProcSimPy.source -> Process.ProcSimPy.queue "Triggers isRequested Event on Queue"

            Process.ProcSimPy.queue -> Process.ProcSimPy.machine "Queue asks if reciver canRecieve"
            Process.ProcSimPy.machine -> Process.ProcSimPy.queue "Machine is working so returns false"
            Process.ProcSimPy.machine -> Process.ProcSimPy.queue "After some time asks if giver canGive"
            Process.ProcSimPy.queue -> Process.ProcSimPy.machine "if has Entity returns ture"
            Process.ProcSimPy.machine -> Process.ProcSimPy.queue "Triggers canGispose Event on Queue"

            Process.ProcSimPy.machine -> Process.ProcSimPy.exit "Machine asks if reciver canRecieve"
            Process.ProcSimPy.exit -> Process.ProcSimPy.machine "Exit can always recive"
            Process.ProcSimPy.machine -> Process.ProcSimPy.exit "Triggers isRequested Event on Exit"
        }
    }
    
}