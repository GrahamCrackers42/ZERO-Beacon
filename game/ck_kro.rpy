
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Kro Zalva Ross

label ck_kro:
    show kro at char_pos
    if plot_state.kro_met:
        $last_dialog = "Greetings (Mr. or Ms.) $AGENT_LAST_NAME."
        kro '[last_dialog]'

    else:
        kro "Salutations. I am Flight Commander Kro Zalva. Welcome to Vivarioss"

        p "Nice to meet you Commander, I\’m $AGENT_FIRST_NAME $AGENT_LAST_NAME"

        $last_dialog = "Likewise. Now, if there is anything you would like to know, please ask. Else move on."
        $plot_state.kro_met = True
        kro '[last_dialog]'

    label menu_kro:
        menu:
            kro '[last_dialog]'
            '[[Jon sent me]' if plot_state.jon_talk_kro and plot_state.stage == PlotStage.VL_INFO:
                jump kro_jon_tree_start
            '[[flatter]' if plot_state.stage == PlotStage.VL_INFO:
                call kro_flatter
            '[[ask for advice]':
                call kro_advice
            '[[ask about opinions on events]' :
                call kro_events
            '[[Ask about her background]' :
                call kro_background
            '[[ask about VL]' if plot_state.stage == PlotStage.VL_PLANS:
                call kro_VL_tree_start
            '[[Done talking]':
                hide kro
                return
        jump menu_kro

        label kro_flatter:
            p '[[your ship is so big.]'
            kro '[[slightly amused. Thanks you for your attempt. Schools you a bit on Kaldrean culture and flattery.]'
            $last_dialog = '[Keep the sweet-talk to a minimum.]'
            $plot_state.kro_flatter_info = True
            return

        label kro_advice:
            p "Could you offer any advice to someone new to Concord?"

            kro "I will tell you what I have told others before you, and what I was told early on in my training: By choosing to come here you have agreed to change yourself. 
            You will be judged by a new set of rules and regulations, and who you become will be no one like who you left behind."

            p "That seems a little intense."

            kro "It is quite true. I recognize it in myself and those close to me."

            p "And how does that affect you?"

            kro "I have yet to understand."

            p "Well… thank you for your words of advice."

            $last_dialog = '[is there anything else I can help you with?]'
            return

        label kro_events:
            p "Have you heard about this so-called tension between the humans and kaldreans here?"

            kro "I do not spend too much of my operational time actually on Concord, I am simply here for the remainder of the week 
            as my starship receives routine maintenance. You are likely much better informed that I am on these matters."

            p "You\’re probably right."

            kro "Just ask around, if you have heard of these “rumors” then I am sure others have heard the same word. If you have not already talked to Elder Vollk in the Grand Marketplace then I recommend you do so. If not then perhaps Elder Demeter in the residences."

            p "Thanks for the direction."

            $last_dialog =  "No need to thank me. Do you have any other questions?"
            return

        label kro_background:
            p '[[ask Kro about her background]'
            kro '[[explains about her military history, her position as a Flight Commander, and what that means.]'
            $last_dialog = '[is there anything else I can help you with?]'
            return

        label kro_jon_tree_start:
            p '[[Jon sent me]'
            menu:
                kro '[[Acknowledges that Jon is a diligent and respectable man. Kro notes that she is worried about his obsession with weapons.]'
                '[[Jon mentioned something about VL. Ask Kro about VL.]':
                    jump kro_jon_tree_VL
                '[[why does obsession worry Kro?]':
                    jump kro_jon_tree_obsession

            label kro_jon_tree_VL:
                p '[[Jon mentioned something about VL. Ask Kro about VL.]'
                kro '[[responds genuinely that she is not familiar with the word\'s meaning. Ask an elder or talk to Lorisk]'
                $last_dialog = '[If there is anything you need, I am at your service (Mr. or Ms.) $AGENT_LAST_NAME].'
                jump menu_kro

            label kro_jon_tree_obsession:
                p '[[why does obsession worry you?]'
                kro '[[in my experience, obsessions are the result of a buried information]'
                $last_dialog = '[If there is anything you need, I am at your service (Mr. or Ms.) $AGENT_LAST_NAME].'
                $plot_state.kro_obsession_info = True
                jump menu_kro

        label kro_VL_tree_start:
            p '[[ask about VL]'
            menu:
                kro '[[I do not know this group as well as you would like me to.]'
                '[[I just need an idea]':
                    jump kro_VL_tree_idea
                '[[Who do you think it is.]':
                    jump kro_VL_tree_who

            label kro_VL_tree_idea:
                p '[[I just need an idea]'
                lorisk '[[Clearly they are a rebel group with an obsession for change. More info on what she thinks]'
                $last_dialog = '[Take care what you say, not all will be so willing to speak on sensitive matters. If you require anything further, (Mr. or Ms.) $AGENT_LAST_NAME], Let me know.'
                jump menu_kro


            label kro_VL_tree_who:
                p '[[Who do you think could be a rebel.]'
                kro '[[Suggest that the people she\'d most expect to be rebels would be Cole (due to his unfortunate experience in the first contact), 
                Noq (due to his eccentric nature and hate of the military), and Lorisk (due to her general progressive and sympathetic attitude)]'
                $last_dialog = '[Take care what you say, not all will be so willing to speak on sensitive matters. If you require anything further, (Mr. or Ms.) $AGENT_LAST_NAME], Let me know.'
                jump menu_kro

            
            