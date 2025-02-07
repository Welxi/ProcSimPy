workspace {

    !identifiers hierarchical

    model {
        !include ManPyNeil.dsl  
        !include ManPyDream.dsl

        user = person "User"
        superuser = person "Super User"
        developer = person "Developer"

        simModel = softwareSystem "Simulation Model"
        simModel -> neil.simNeil "Implements"
        simModel -> neil.simNeil.experiment "Implements"
        simModel -> dream.simDream "Implements"

        # user -> simModel "Creates"
        user -> dream.webUI "Uses"
        user -> dream.ket "Uses"

        superUser -> simModel "Creates"
        superUser -> neil.simNeil "Extends"
        superUser -> dream.simDream "Extends"

        developer -> neil.simNeil "Creates"
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


        container neil "neilcc" {
            include *
            include ->simModel
            autolayout lr
        }


        container dream "dreamcc" {
            include *
            autolayout lr
        }

        component neil.simNeil "simNeil"{
            include *
            autolayout tb
        }
 
        component dream.simDream "simDream" {
            include *
            autolayout bt
        }

        dynamic neil.simNeil "CoreHandover1"{
            title "Core Handover of Entity, Machine is waiting"
            neil.simNeil.source -> neil.simNeil.entity "Entity is created by Source"
            neil.simNeil.entity -> neil.simNeil.source "Entity is assigned to Source"
            neil.simNeil.source -> neil.simNeil.queue "Source asks if reciver canRecieve"
            neil.simNeil.queue -> neil.simNeil.source "If not at Capacity returns True"
            neil.simNeil.source -> neil.simNeil.queue "Triggers isRequested Event on Queue"

            neil.simNeil.queue -> neil.simNeil.machine "Queue asks if reciver canRecieve"
            neil.simNeil.machine -> neil.simNeil.queue "Machine is waiting so returns true"
            neil.simNeil.queue -> neil.simNeil.machine "Triggers isRequested Event on Machine"

            neil.simNeil.machine -> neil.simNeil.exit "Machine asks if reciver canRecieve"
            neil.simNeil.exit -> neil.simNeil.machine "Exit can always recive"
            neil.simNeil.machine -> neil.simNeil.exit "Triggers isRequested Event on Exit"
        }

        dynamic neil.simNeil "CoreHandover2"{
            title "Core Handover of Entity, Machine is working"
            neil.simNeil.source -> neil.simNeil.entity "Entity is created by Source"
            neil.simNeil.entity -> neil.simNeil.source "Entity is assigned to Source"
            neil.simNeil.source -> neil.simNeil.queue "Source asks if reciver canRecieve"
            neil.simNeil.queue -> neil.simNeil.source "If not at Capacity returns True"
            neil.simNeil.source -> neil.simNeil.queue "Triggers isRequested Event on Queue"

            neil.simNeil.queue -> neil.simNeil.machine "Queue asks if reciver canRecieve"
            neil.simNeil.machine -> neil.simNeil.queue "Machine is working so returns false"
            neil.simNeil.machine -> neil.simNeil.queue "After some time asks if giver canGive"
            neil.simNeil.queue -> neil.simNeil.machine "if has Entity returns ture"
            neil.simNeil.machine -> neil.simNeil.queue "Triggers canGispose Event on Queue"

            neil.simNeil.machine -> neil.simNeil.exit "Machine asks if reciver canRecieve"
            neil.simNeil.exit -> neil.simNeil.machine "Exit can always recive"
            neil.simNeil.machine -> neil.simNeil.exit "Triggers isRequested Event on Exit"
        }
    }
    
}