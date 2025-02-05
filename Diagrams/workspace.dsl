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

        user -> simModel "Creates"
        user -> dream.webUI "Uses"

        superUser -> simModel "Creates"
        superUser -> neil.simNeil "Extends"
        superUser -> dream.simDream "Extends"

        developer -> neil.simNeil "Creates"
        developer -> dream.simDream "Creates"
    }


    views {
        
        theme default

        systemContext simModel "simModelsc" {
            include *
            autolayout tb
        }

        systemContext Neil "Neilsc" {
            include *
            autolayout lr
        }

        systemContext dream "Dreamsc" {
            include *
            autolayout lr
        }


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
            autolayout lr
        }
 
        component dream.simDream "simDream" {
            include *
            autolayout lr
        }
    }
    
}