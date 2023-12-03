label day4:     
        scene day4
        with Fade(1,1,2)

        pause(2)

        label Studing1:
            
            voice "Давайте опустим всё лишнее по типу того, как наш герой снова проснулся у себя"
            scene progaudit
            with Fade(0.5,0.5,1)

            show prepod1

            Prepod "Уважаемые студенты, сегодня мы пройдем с вами **ТЕМА**, просьба не отвлекаться, так как тема очень важна для последующих занятий. В конце занятия вы пройдете небольшой тест."

            "Вставьте тест сюда"

            gg "хммммммм. Поговаривают что сегодня вечером будет мероприятие"

            gg "Может сходить?"

            menu:
                "Идём":
                    jump SvoiaIgra
                "Да ну его. Пойду в доту":
                    jump GoToHome

        label SvoiaIgra:
            

            $ timer_onoff = True

            scene coworking1
            with Fade(0.5,0.5,1)
            
            voice "На удивление день нашего обалдуя прошёл без происшествий. Так что он пошёл на мероприятие"

            gg "Хм... А сегодня тут очень даже шумно. Наконец-то я дождался мероприятий. Интересно, что меня ожидает сегодня?"

            voice "хмммм, а где же сокомандники. Наш герой стоит, ждёт, а их нет"

            gg "Блин, да где они? Обещали прийти"

            voice "Спустя минуту, которая для него длилась чуть ли не вечность, ожиданий ваша команда наконец-то подошла. Он здоровается со всеми и отправляется на мероприятие"

            scene coworking2
            with Fade(0.5,0.5,1)

            show sexMan

            $ PlayerteamName = renpy.input("Как называеться твоя команда")
            $ PlayerteamName = PlayerteamName.strip() or "Гослята"

            "Твоя команда называеться [PlayerteamName]"

            leader "Приветсвую всех пришёдших, мы начинам наше мероприятие под названием СУП или Самый Умный Первокурсник"

            leader "И вот правила нашей игры"
            
            leader "Игрок, тебе будут даны 4 категории в по 5 вопросов разного номинала"

            leader "чтобы выбрать категорию нажни на её название, также с вопросом"

            leader "Дальше его озвучат и тебе будет дано 4 варианта ответа, один из правильный"

            leader "Помимо тебя есть ещё 3 команды(бота), которые выбираю вопросчы и ответы на ниш случайно"

            leader "Победит та команда у которой будет больше всего очков"

            hide sexMen 

            $ Turn = 1

            $ OurTeamPoints = 0
            $ Team1Points = 0
            $ Team2Points = 0
            $ Team3Points = 0

            $ R1Categories = 4
            $ R2Categories = 4                
                
            $ R1Cat1Status = True
            $ R1Cat1Quest1Status = True
            $ R1Cat1Quest2Status = True
            $ R1Cat1Quest3Status = True
            $ R1Cat1Quest4Status = True             
            $ R1Cat1Quest5Status = True

            $ R1Cat2Status = True
            $ R1Cat2Quest1Status = True
            $ R1Cat2Quest2Status = True
            $ R1Cat2Quest3Status = True
            $ R1Cat2Quest4Status = True             
            $ R1Cat2Quest5Status = True

            $ R1Cat3Status = True
            $ R1Cat3Quest1Status = True
            $ R1Cat3Quest2Status = True
            $ R1Cat3Quest3Status = True
            $ R1Cat3Quest4Status = True             
            $ R1Cat3Quest5Status = True

            $ R1Cat4Status = True
            $ R1Cat4Quest1Status = True
            $ R1Cat4Quest2Status = True
            $ R1Cat4Quest3Status = True
            $ R1Cat4Quest4Status = True             
            $ R1Cat4Quest5Status = True

            $ R2Cat1Status = True
            $ R2Cat1Quest1Status = True
            $ R2Cat1Quest2Status = True
            $ R2Cat1Quest3Status = True
            $ R2Cat1Quest4Status = True             
            $ R2Cat1Quest5Status = True

            $ R2Cat2Status = True
            $ R2Cat2Quest1Status = True
            $ R2Cat2Quest2Status = True
            $ R2Cat2Quest3Status = True
            $ R2Cat2Quest4Status = True             
            $ R2Cat2Quest5Status = True

            $ R2Cat3Status = True
            $ R2Cat3Quest1Status = True
            $ R2Cat3Quest2Status = True
            $ R2Cat3Quest3Status = True
            $ R2Cat3Quest4Status = True             
            $ R2Cat3Quest5Status = True

            $ R2Cat4Status = True
            $ R2Cat4Quest1Status = True
            $ R2Cat4Quest2Status = True
            $ R2Cat4Quest3Status = True
            $ R2Cat4Quest4Status = True             
            $ R2Cat4Quest5Status = True

            $ cost = 0


            label Round1:

                $ timez = 300
                $ time_range = 300 

                $TeamCat = renpy.random.randint(1,4)
                if R1Cat1Status==1 and TeamCat == 1:
                    $ marker = 'Round1Cat1'

                elif R1Cat2Status==1 and TeamCat == 2:
                    $ marker = 'Round1Cat2'

                elif R1Cat3Status==1 and TeamCat == 3:
                    $ marker = 'Round1Cat3'

                elif R1Cat4Status==1 and TeamCat == 4:
                    $ marker = 'Round1Cat4'
                

                if R1Categories == 1:
                    leader "Итак начинием второй раунд"

                    leader "Текущий счёт команд: Прилагательные [Team2Points], Стрелки [Team1Points], Бикини Боттом [Team3Points], [PlayerteamName] [OurTeamPoints]"

                    $ Turn = 1

                    jump Round2

                if R1Cat1Quest1Status == False and R1Cat1Quest2Status == False and R1Cat1Quest3Status == False and R1Cat1Quest4Status == False and R1Cat1Quest5Status == False:
                    $ R1Cat1Status = False
                    $ R1Categories -=1
                
                if R1Cat2Quest1Status == False and R1Cat2Quest2Status == False and R1Cat2Quest3Status == False and R1Cat2Quest4Status == False and R1Cat2Quest5Status == False:
                    $ R1Cat2Status = False
                    $ R1Categories -=1

                if R1Cat3Quest1Status == False and R1Cat3Quest2Status == False and R1Cat3Quest3Status == False and R1Cat3Quest4Status == False and R1Cat3Quest5Status == False:
                    $ R1Cat3Status = False
                    $ R1Categories -=1

                if R1Cat4Quest1Status == False and R1Cat4Quest2Status == False and R1Cat4Quest3Status == False and R1Cat4Quest4Status == False and R1Cat4Quest5Status == False:
                    $ R1Cat4Status = False
                    $ R1Categories -=1

                if Turn == 1:
                    menu:
                        "Георафия" if R1Cat1Status == True:
                            jump Round1Cat1
                        "История" if R1Cat2Status == True:
                            jump Round1Cat2
                        "Биология" if R1Cat2Status == True:
                            jump Round1Cat3
                        "Мультфильмы" if R1Cat2Status == True:
                            jump Round1Cat4

                elif Turn == 2 : 
                        $TeamCat = renpy.random.randint(1,4)
                        if R1Cat1Status==1 and TeamCat == 1:
                            jump Round1Cat1

                        elif R1Cat2Status==1 and TeamCat == 2:
                            jump Round1Cat2

                        elif R1Cat3Status==1 and TeamCat == 3:
                            jump Round1Cat3

                        elif R1Cat4Status==1 and TeamCat == 4:
                            jump Round1Cat4    

                elif Turn == 3: 
                    $TeamCat = renpy.random.randint(1,4)
                    if R1Cat1Status==1 and TeamCat == 1:
                        jump Round1Cat1

                    elif R1Cat2Status==1 and TeamCat == 2:
                        jump Round1Cat2

                    elif R1Cat3Status==1 and TeamCat == 3:
                        jump Round1Cat3

                    elif R1Cat4Status==1 and TeamCat == 4:
                        jump Round1Cat4

                elif Turn == 4: 
                    $TeamCat = renpy.random.randint(1,4)
                    if R1Cat1Status==1 and TeamCat == 1:
                        jump Round1Cat1

                    elif R1Cat2Status==1 and TeamCat == 2:
                        jump Round1Cat2

                    elif R1Cat3Status==1 and TeamCat == 3:
                        jump Round1Cat3

                    elif R1Cat4Status==1 and TeamCat == 4:
                        jump Round1Cat4 

                label costing:
                    $OurTeamPoints -= cost
                    "ТЫ ЕБЛАН, ТЫ НЕ ВЫБРАЛ ЛОВИ МИНУС НА СЧЁТ"
                    $ Turn = 2
                    jump Round1
                
                label Round1Cat1:
                    
                    $ timez = 300
                    $ time_range = 300

                    $TeamCat = renpy.random.randint(1,5)
                    if R1Cat1Status==1 and TeamCat == 1:
                        $ marker = 'R1Cat1Quest1'

                    elif R1Cat2Status==1 and TeamCat == 2:
                        $ marker = 'R1Cat1Quest2'

                    elif R1Cat3Status==1 and TeamCat == 3:
                        $ marker = 'R1Cat1Quest3'

                    elif R1Cat4Status==1 and TeamCat == 4:
                        $ marker = 'R1Cat1Quest4'
                    
                    elif R1Cat4Status==1 and TeamCat == 5:
                        $ marker = 'R1Cat1Quest5'

                    if Turn == 1: 
                        gg "Георафия"
                        menu: 
                            "100" if R1Cat1Quest1Status == True:
                                jump R1Cat1Quest1

                            "200" if R1Cat1Quest2Status==1:
                                jump R1Cat1Quest2

                            "300" if R1Cat1Quest3Status==1:
                                jump R1Cat1Quest3

                            "400" if R1Cat1Quest4Status==1:
                                jump R1Cat1Quest4

                            "500" if R1Cat1Quest5Status==1:
                                jump R1Cat1Quest5

                    elif Turn == 2 : 
                        team1 "Георафия"
                        $Team1Qestion = renpy.random.randint(1,5)
                        if R1Cat1Quest1Status==1 and Team1Qestion == 1:
                            team1 "Вопрос за 100"
                            jump R1Cat1Quest1

                        elif R1Cat1Quest2Status==1 and Team1Qestion == 2:
                            team1 "Вопрос за 200"
                            jump R1Cat1Quest2

                        elif R1Cat1Quest3Status==1 and Team1Qestion == 3:
                            team1 "Вопрос за 300"
                            jump R1Cat1Quest3

                        elif R1Cat1Quest4Status==1 and Team1Qestion == 4:
                            team1 "Вопрос за 400"
                            jump R1Cat1Quest4

                        elif R1Cat1Quest5Status==1 and Team1Qestion == 5:
                            team1 "Вопрос за 500"
                            jump R1Cat1Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat1    

                    elif Turn == 3: 
                        team2 "Категория 1"
                        $Team1Qestion = renpy.random.randint(1,5)
                        if R1Cat1Quest1Status==1 and Team1Qestion == 1:
                            team2 "Вопрос за 100"
                            jump R1Cat1Quest1

                        elif R1Cat1Quest2Status==1 and Team1Qestion == 2:
                            team2 "Вопрос за 200"
                            jump R1Cat1Quest2

                        elif R1Cat1Quest3Status==1 and Team1Qestion == 3:
                            team2 "Вопрос за 300"
                            jump R1Cat1Quest3

                        elif R1Cat1Quest4Status==1 and Team1Qestion == 4:
                            team2 "Вопрос за 400"
                            jump R1Cat1Quest4

                        elif R1Cat1Quest5Status==1 and Team1Qestion == 5:
                            team2 "Вопрос за 500"
                            jump R1Cat1Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat1 

                    elif Turn == 4: 
                        team3 "Гегорафия"
                        $Team1Qestion = renpy.random.randint(1,5)
                        if R1Cat1Quest1Status==1 and Team1Qestion == 1:
                            team3 "Вопрос за 100"
                            jump R1Cat1Quest1

                        elif R1Cat1Quest2Status==1 and Team1Qestion == 2:
                            team3 "Вопрос за 200"
                            jump R1Cat1Quest2

                        elif R1Cat1Quest3Status==1 and Team1Qestion == 3:
                            team3 "Вопрос за 300"
                            jump R1Cat1Quest3

                        elif R1Cat1Quest4Status==1 and Team1Qestion == 4:
                            team3 "Вопрос за 400"
                            jump R1Cat1Quest4

                        elif R1Cat1Quest5Status==1 and Team1Qestion == 5:
                            team3 "Вопрос за 500"
                            jump R1Cat1Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat1 
                    
                    label R1Cat1Quest1:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 100

                        leader "Вопрос за 100"
                        "Именно он возглавлял экспедицию, совершившую первое плавание вокруг света."
                        if Turn == 1 :
                            menu: 
                                "Ф. Магеллан":
                                    "верно"
                                    $OurTeamPoints += 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest1Status = False
                                    jump Round1 

                                "Черчиль":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest1Status = False
                                    jump Round1 

                                "Бенитто Муссолини":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest1Status = False
                                    jump Round1 

                                "Абрам Евгениевич":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest1Status = False
                                    jump Round1
 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Ф. Магеллан"
                                "верно"
                                $Team1Points += 100
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest1Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Черчиль"
                                "неверно"
                                "Ф. Магеллан"
                                $OurTeamPoints -= 100
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest1Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "Бенитто Муссолини"
                                "неверно"
                                "Ф. Магеллан"
                                $Team1Points -= 100
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest1Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "Абрам Евгениевич"
                                "неверно"
                                "Ф. Магеллан"
                                $Team1Points -= 100
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest1Status = False
                                jump Round1 

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Ф. Магеллан"
                                "верно"
                                $Team2Points += 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest1Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Черчиль"
                                "неверно"
                                "Ф. Магеллан"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest1Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Бенитто Муссолини"
                                "неверно"
                                "Ф. Магеллан"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest1Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Абрам Евгениевич"
                                "неверно"
                                "Ф. Магеллан"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest1Status = False
                                jump Round1 

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Ф. Магеллан"
                                "верно"
                                $Team3Points += 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest1Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Черчиль"
                                "неверно"
                                "Ф. Магеллан"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest1Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Бенитто Муссолини"
                                "неверно"
                                "Ф. Магеллан"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest1Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Абрам Евгениевич"
                                "неверно"
                                "Ф. Магеллан"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest1Status = False
                                jump Round1

                    label R1Cat1Quest2:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 200
                        leader "Вопрос за 200"
                        "Этот вулкан уничтожил Помпеи "
                        if Turn == 1 :
                            menu: 
                                "Магелан":
                                    "неверно"
                                    "Везувий"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest2Status = False
                                    jump Round1 

                                "Уайна Путина":
                                    "неверно"
                                    "Везувий"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest2Status = False
                                    jump Round1 

                                "Везувий":
                                    "верно"
                                    $OurTeamPoints += 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest2Status = False
                                    jump Round1 

                                "Дотер??":    
                                    "неверно"
                                    "Везувий"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest2Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Магелан"
                                "неверно"
                                "Везувий"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest2Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Уайна Путина"
                                "неверно"
                                "Везувий"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest2Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "Везувий"
                                "неверно"
                                "ответ"
                                $Team1Points += 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest2Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "Дотер??"
                                "неверно"
                                "Везувий"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest2Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Магелан"
                                "неверно"
                                "Везувий"
                                $Team1Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest2Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Уайна Путина"
                                "неверно"
                                "Везувий"
                                $Team1Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest2Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Везувий"
                                "неверно"
                                "ответ"
                                $Team1Points += 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest2Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Дотер??"
                                "неверно"
                                "Везувий"
                                $Team1Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest2Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Магелан"
                                "неверно"
                                "Везувий"
                                $Team1Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest2Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "Уайна Путина"
                                "неверно"
                                "Везувий"
                                $Team1Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest2Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "Везувий"
                                "неверно"
                                "ответ"
                                $Team1Points += 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest2Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "Дотер??"
                                "неверно"
                                "Везувий"
                                $Team1Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest2Status = False
                                jump Round1

                    label R1Cat1Quest3:
                        
                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 300
                        leader "Вопрос за 300"
                        "Этот мифической остров дал название океану"
                        if Turn == 1 :
                            menu: 
                                "Атлантида":
                                    "верно"
                                    $OurTeamPoints += 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest3Status = False
                                    jump Round1 

                                "Гренландия":
                                    "неверно"
                                    "Атлантида"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest3Status = False
                                    jump Round1 

                                "ОЛЕГ????":
                                    "неверно"
                                    "Атлантида"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest3Status = False
                                    jump Round1 

                                "Мадагаскар":    
                                    "неверно"
                                    "Атлантида"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest3Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Атлантида"
                                "верно"
                                $Team1Points += 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest3Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Гренландия"
                                "неверно"
                                "Атлантида"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest3Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "ОЛЕГ????"
                                "неверно"
                                "Атлантида"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest3Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "Мадагаскар"    
                                "неверно"
                                "Атлантида"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest3Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Атлантида"
                                "верно"
                                $Team2Points += 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest3Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Гренландия"
                                "неверно"
                                "Атлантида"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest3Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "ОЛЕГ????"
                                "неверно"
                                "Атлантида"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest3Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Мадагаскар"    
                                "неверно"
                                "Атлантида"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest3Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Атлантида"
                                "верно"
                                $Team3Points += 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest3Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "Гренландия"
                                "неверно"
                                "Атлантида"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest3Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "ОЛЕГ????"
                                "неверно"
                                "Атлантида"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest3Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "Мадагаскар"    
                                "неверно"
                                "Атлантида"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest3Status = False
                                jump Round1
                    
                    label R1Cat1Quest4:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 400
                        leader "Вопрос за 400"
                        "В этой «Зеленой стране» холоднее, чем в «Ледяной» "
                        if Turn == 1 :
                            menu: 
                                "Виндланд":
                                    "неверно"
                                    "Гренландия"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest4Status = False
                                    jump Round1 

                                "Женева":
                                    "неверно"
                                    "Гренландия"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest4Status = False
                                    jump Round1 

                                "Сердечко":
                                    "неверно"
                                    "Гренландия"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest4Status = False
                                    jump Round1 

                                "Гренландия":    
                                    "верно"
                                    $OurTeamPoints += 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest4Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Виндланд"
                                "неверно"
                                "Гренландия"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest4Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Женева"
                                "неверно"
                                "Гренландия"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest4Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "Сердечко"
                                "неверно"
                                "Гренландия"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest4Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "Гренландия"  
                                "верно"
                                $Team1Points += 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest4Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Виндланд"
                                "неверно"
                                "Гренландия"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest4Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Женева"
                                "неверно"
                                "Гренландия"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest4Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Сердечко"
                                "неверно"
                                "Гренландия"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest4Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Гренландия"  
                                "верно"
                                $Team1Points += 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest4Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Виндланд"
                                "неверно"
                                "Гренландия"
                                $Team1Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest4Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "Женева"
                                "неверно"
                                "Гренландия"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest4Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "Сердечко"
                                "неверно"
                                "Гренландия"
                                $Team1Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest4Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "Гренландия"  
                                "верно"
                                $Team1Points += 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest4Status = False
                                jump Round1

                    label R1Cat1Quest5:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 500
                        leader "Вопрос за 500"
                        "Какая страна первая в мире по плотности населения"
                        if Turn == 1 :
                            menu: 
                                "Монако":
                                    "верно"
                                    $OurTeamPoints += 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest5Status = False
                                    jump Round1 

                                "Кыргистан":
                                    "неверно"
                                    "Монако"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest5Status = False
                                    jump Round1 

                                "Россия":
                                    "неверно"
                                    "Монако"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest5Status = False
                                    jump Round1 

                                "Китай":    
                                    "неверно"
                                    "Монако"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest5Status = False
                                    jump Round1 

                        elif Turn == 2: 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Монако"
                                "верно"
                                $Team1Points += 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest5Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Кыргистан"
                                "неверно"
                                "Монако"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest5Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "Россия"
                                "неверно"
                                "Монако"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest5Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "Китай"    
                                "неверно"
                                "Монако"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest5Status = False
                                jump Round1

                        elif Turn == 3: 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Монако"
                                "верно"
                                $Team2Points += 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest5Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Кыргистан"
                                "неверно"
                                "Монако"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest5Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Россия"
                                "неверно"
                                "Монако"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest5Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Китай"    
                                "неверно"
                                "Монако"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest5Status = False
                                jump Round1

                        elif Turn == 4: 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Монако"
                                "верно"
                                $Team3Points += 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest5Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "Кыргистан"
                                "неверно"
                                "Монако"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest5Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "Россия"
                                "неверно"
                                "Монако"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest5Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "Китай"    
                                "неверно"
                                "Монако"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest5Status = False
                                jump Round1

                label Round1Cat2:
                    
                    $ timez = 300
                    $ time_range = 300
                    
                    $TeamCat = renpy.random.randint(1,5)
                    if R1Cat1Status==1 and TeamCat == 1:
                        $ marker = 'R1Cat2Quest1'

                    elif R1Cat2Status==1 and TeamCat == 2:
                        $ marker = 'R1Cat2Quest2'

                    elif R1Cat3Status==1 and TeamCat == 3:
                        $ marker = 'R1Cat2Quest3'

                    elif R1Cat4Status==1 and TeamCat == 4:
                        $ marker = 'R1Cat2Quest4'
                    
                    elif R1Cat4Status==1 and TeamCat == 5:
                        $ marker = 'R1Cat2Quest5'

                    if Turn == 1: 
                        gg "История"
                        menu: 
                            "100" if R1Cat2Quest1Status == True:
                                jump R1Cat2Quest1

                            "200" if R1Cat2Quest2Status==1:
                                jump R1Cat2Quest2

                            "300" if R1Cat2Quest3Status==1:
                                jump R1Cat2Quest3

                            "400" if R1Cat2Quest4Status==1:
                                jump R1Cat2Quest4

                            "500" if R1Cat2Quest5Status==1:
                                jump R1Cat2Quest5

                    elif Turn == 2 : 
                        team1 "История"
                        $Team1Qestion = renpy.random.randint(1,5)
                        if R1Cat2Quest1Status==1 and Team1Qestion == 1:
                            team1 "Вопрос за 100"
                            jump R1Cat2Quest1

                        elif R1Cat2Quest2Status==1 and Team1Qestion == 2:
                            team1 "Вопрос за 200"
                            jump R1Cat2Quest2

                        elif R1Cat2Quest3Status==1 and Team1Qestion == 3:
                            team1 "Вопрос за 300"
                            jump R1Cat2Quest3

                        elif R1Cat2Quest4Status==1 and Team1Qestion == 4:
                            team1 "Вопрос за 400"
                            jump R1Cat2Quest4

                        elif R1Cat2Quest5Status==1 and Team1Qestion == 5:
                            team1 "Вопрос за 500"
                            jump R1Cat2Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat2    

                    elif Turn == 3: 
                        team2 "История"
                        $Team2Qestion = renpy.random.randint(1,5)
                        if R1Cat2Quest1Status==1 and Team2Qestion == 1:
                            team2 "Вопрос за 100"
                            jump R1Cat2Quest1

                        elif R1Cat2Quest2Status==1 and Team2Qestion == 2:
                            team2 "Вопрос за 200"
                            jump R1Cat2Quest2

                        elif R1Cat2Quest3Status==1 and Team2Qestion == 3:
                            team2 "Вопрос за 300"
                            jump R1Cat2Quest3

                        elif R1Cat2Quest4Status==1 and Team2Qestion == 4:
                            team2 "Вопрос за 400"
                            jump R1Cat2Quest4

                        elif R1Cat2Quest5Status==1 and Team2Qestion == 5:
                            team2 "Вопрос за 500"
                            jump R1Cat2Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat2

                    elif Turn == 4: 
                        team3 "История"
                        $Team3Qestion = renpy.random.randint(1,5)
                        if R1Cat2Quest1Status==1 and Team3Qestion == 1:
                            team3 "Вопрос за 100"
                            jump R1Cat2Quest1

                        elif R1Cat2Quest2Status==1 and Team3Qestion == 2:
                            team3 "Вопрос за 200"
                            jump R1Cat2Quest2

                        elif R1Cat2Quest3Status==1 and Team3Qestion == 3:
                            team3 "Вопрос за 300"
                            jump R1Cat2Quest3

                        elif R1Cat2Quest4Status==1 and Team3Qestion == 4:
                            team3 "Вопрос за 400"
                            jump R1Cat2Quest4

                        elif R1Cat2Quest5Status==1 and Team3Qestion == 5:
                            team3 "Вопрос за 500"
                            jump R1Cat2Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat2
                    
                    label R1Cat2Quest1:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 100

                        leader "Вопрос за 100"
                        "Он стал последним, кто открыл Америку "
                        if Turn == 1 :
                            menu: 
                                "Колумб":
                                    "верно"
                                    $OurTeamPoints += 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest1Status = False
                                    jump Round1 

                                "Егорик":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest1Status = False
                                    jump Round1 

                                "Магелан":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest1Status = False
                                    jump Round1 

                                "Пётр I":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest1Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Колумб"
                                "верно"
                                $Team1Points += 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat2Quest1Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Егорик"
                                "неверно"
                                "Колумб"
                                $OurTeamPoints -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat2Quest1Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "Магелан"
                                "неверно"
                                "Колумб"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat2Quest1Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "Пётр I"   
                                "неверно"
                                "Колумб"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat2Quest1Status = False
                                jump Round1 

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Колумб"
                                "верно"
                                $Team2Points += 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat2Quest1Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Егорик"
                                "неверно"
                                "Колумб"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat2Quest1Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Магелан"
                                "неверно"
                                "Колумб"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat2Quest1Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Пётр I"   
                                "неверно"
                                "Колумб"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat2Quest1Status = False
                                jump Round1 

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Колумб"
                                "верно"
                                $Team3Points += 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat2Quest1Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Егорик"
                                "неверно"
                                "Колумб"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat2Quest1Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Магелан"
                                "неверно"
                                "Колумб"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat2Quest1Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Пётр I"   
                                "неверно"
                                "Колумб"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat2Quest1Status = False
                                jump Round1

                    label R1Cat2Quest2:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 200

                        leader "Вопрос за 200"
                        "Этот остров раньше назывался Цейлоном "
                        if Turn == 1 :
                            menu: 
                                "Шри-Ланка":
                                    "верно"
                                    $OurTeamPoints += 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest2Status = False
                                    jump Round1 

                                "Новая Зеландия":
                                    "неверно"
                                    "Шри-Ланка"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest2Status = False
                                    jump Round1 

                                "Курилы":
                                    "неверно"
                                    "Шри-Ланка"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest2Status = False
                                    jump Round1 

                                "Исландия":    
                                    "неверно"
                                    "Шри-Ланка"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest2Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Шри-Ланка"
                                "верно"
                                $Team1Points += 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ Cat2Quest2Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Новая Зеландия"
                                "неверно"
                                "Шри-Ланка"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ Cat2Quest2Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "Курилы"
                                "неверно"
                                "Шри-Ланка"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ Cat2Quest2Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "Исландия"  
                                "неверно"
                                "Шри-Ланка"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ Cat2Quest2Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Шри-Ланка"
                                "верно"
                                $Team2Points += 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ Cat2Quest2Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Новая Зеландия"
                                "неверно"
                                "Шри-Ланка"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ Cat2Quest2Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Курилы"
                                "неверно"
                                "Шри-Ланка"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ Cat2Quest2Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Исландия"  
                                "неверно"
                                "Шри-Ланка"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ Cat2Quest2Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Шри-Ланка"
                                "верно"
                                $Team3Points += 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ Cat2Quest2Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "Новая Зеландия"
                                "неверно"
                                "Шри-Ланка"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ Cat2Quest2Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "Курилы"
                                "неверно"
                                "Шри-Ланка"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ Cat2Quest2Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "Исландия"  
                                "неверно"
                                "Шри-Ланка"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ Cat2Quest2Status = False
                                jump Round1

                    label R1Cat2Quest3:
                        
                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 300

                        leader "Вопрос за 300"
                        "С этим городом связана дата 26 апреля 1986 года"
                        if Turn == 1 :
                            menu: 
                                "Чернобыль":
                                    "верно"
                                    $OurTeamPoints += 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest3Status = False
                                    jump Round1 

                                "Киев":
                                    "неверно"
                                    "Чернобыль"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest3Status = False
                                    jump Round1 

                                "Бостон":
                                    "неверно"
                                    "Чернобыль"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest3Status = False
                                    jump Round1 

                                "Берлин":    
                                    "неверно"
                                    "Чернобыль"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest3Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Чернобыль"
                                "верно"
                                $Team1Points += 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat2Quest3Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Киев"
                                "неверно"
                                "Чернобыль"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat2Quest3Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "Бостон"
                                "неверно"
                                "Чернобыль"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat2Quest3Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "Берлин"
                                "неверно"
                                "Чернобыль"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat2Quest3Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Чернобыль"
                                "верно"
                                $Team2Points += 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat2Quest3Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Киев"
                                "неверно"
                                "Чернобыль"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat2Quest3Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Бостон"
                                "неверно"
                                "Чернобыль"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat2Quest3Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Берлин"
                                "неверно"
                                "Чернобыль"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat2Quest3Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Чернобыль"
                                "верно"
                                $Team3Points += 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat2Quest3Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "Киев"
                                "неверно"
                                "Чернобыль"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat2Quest3Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "Бостон"
                                "неверно"
                                "Чернобыль"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat2Quest3Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "Берлин"
                                "неверно"
                                "Чернобыль"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat2Quest3Status = False
                                jump Round1
                    
                    label R1Cat2Quest4:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 400

                        leader "Вопрос за 400"
                        "Данную постройку ввели в работу в 1904 году в Америке"
                        if Turn == 1 :
                            menu: 
                                "Проект Манхеттен":
                                    "неверно"
                                    "Панамский канал"                                    
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest4Status = False
                                    jump Round1 

                                "Завод Жигулёвского":
                                    "неверно"
                                    "Панамский канал"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest4Status = False
                                    jump Round1 

                                "Панамский канал":
                                    "верно"
                                    $OurTeamPoints += 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest4Status = False
                                    jump Round1 

                                "АЭС":    
                                    "неверно"
                                    "Панамский канал"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest4Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Проект Манхеттен"
                                "неверно"
                                "Панамский канал" 
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat2Quest4Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Завод Жигулёвского"
                                "неверно"
                                "Панамский канал"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat2Quest4Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "Панамский канал"
                                "верно"
                                $Team1Points += 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat2Quest4Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "АЭС"    
                                "неверно"
                                "Панамский канал"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat2Quest4Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Проект Манхеттен"
                                "неверно"
                                "Панамский канал" 
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat2Quest4Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Завод Жигулёвского"
                                "неверно"
                                "Панамский канал"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat2Quest4Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Панамский канал"
                                "верно"
                                $Team2Points += 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat2Quest4Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "АЭС"    
                                "неверно"
                                "Панамский канал"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat2Quest4Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Проект Манхеттен"
                                "неверно"
                                "Панамский канал" 
                                $Team2Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat2Quest4Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "Завод Жигулёвского"
                                "неверно"
                                "Панамский канал"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat2Quest4Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "Панамский канал"
                                "верно"
                                $Team2Points += 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat2Quest4Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "АЭС"    
                                "неверно"
                                "Панамский канал"
                                $Team2Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat2Quest4Status = False
                                jump Round1

                    label R1Cat2Quest5:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 500

                        leader "Вопрос за 500"
                        "Именно он изобрел радио в 1895 году "
                        if Turn == 1 :
                            menu: 
                                "Попов":
                                    "верно"
                                    $OurTeamPoints += 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest5Status = False
                                    jump Round1 

                                "Ромка":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest5Status = False
                                    jump Round1 

                                "Николла Тесла":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest5Status = False
                                    jump Round1 

                                "Эйнштейн":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest5Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Попов"
                                "верно"
                                $Team1Points += 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ Cat2Quest5Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Ромка"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ Cat2Quest5Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "Николла Тесла"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ Cat2Quest5Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "Эйнштейн"  
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ Cat2Quest5Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Попов"
                                "верно"
                                $Team2Points += 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ Cat2Quest5Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Ромка"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ Cat2Quest5Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Николла Тесла"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ Cat2Quest5Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Эйнштейн"  
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ Cat2Quest5Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Попов"
                                "верно"
                                $Team3Points += 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ Cat2Quest5Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "Ромка"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ Cat2Quest5Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "Николла Тесла"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ Cat2Quest5Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "Эйнштейн"  
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ Cat2Quest5Status = False
                                jump Round1

                label Round1Cat3:
                    
                    $ timez = 300
                    $ time_range = 300

                    $TeamCat = renpy.random.randint(1,5)
                    if R1Cat1Status==1 and TeamCat == 1:
                        $ marker = 'R1Cat3Quest1'

                    elif R1Cat2Status==1 and TeamCat == 2:
                        $ marker = 'R1Cat3Quest2'

                    elif R1Cat3Status==1 and TeamCat == 3:
                        $ marker = 'R1Cat3Quest3'

                    elif R1Cat4Status==1 and TeamCat == 4:
                        $ marker = 'R1Cat3Quest4'
                    
                    elif R1Cat4Status==1 and TeamCat == 5:
                        $ marker = 'R1Cat3Quest5'

                    if Turn == 1: 
                        gg "Биология"
                        menu: 
                            "100" if R1Cat3Quest1Status == True:
                                jump R1Cat3Quest1

                            "200" if R1Cat3Quest2Status==1:
                                jump R1Cat3Quest2

                            "300" if R1Cat3Quest3Status==1:
                                jump R1Cat3Quest3

                            "400" if R1Cat3Quest4Status==1:
                                jump R1Cat3Quest4

                            "500" if R1Cat3Quest5Status==1:
                                jump R1Cat3Quest5

                    elif Turn == 2 : 
                        team1 "Биология"
                        $Team1Qestion = renpy.random.randint(1,5)
                        if R1Cat3Quest1Status==1 and Team1Qestion == 1:
                            team1 "Вопрос за 100"
                            jump R1Cat3Quest1

                        elif R1Cat3Quest2Status==1 and Team1Qestion == 2:
                            team1 "Вопрос за 200"
                            jump R1Cat3Quest2

                        elif R1Cat3Quest3Status==1 and Team1Qestion == 3:
                            team1 "Вопрос за 300"
                            jump R1Cat3Quest3

                        elif R1Cat3Quest4Status==1 and Team1Qestion == 4:
                            team1 "Вопрос за 400"
                            jump R1Cat3Quest4

                        elif R1Cat3Quest5Status==1 and Team1Qestion == 5:
                            team1 "Вопрос за 500"
                            jump R1Cat3Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat3    

                    elif Turn == 3: 
                        team2 "Биология"
                        $Team2Qestion = renpy.random.randint(1,5)
                        if R1Cat3Quest1Status==1 and Team2Qestion == 1:
                            team2 "Вопрос за 100"
                            jump R1Cat3Quest1

                        elif R1Cat3Quest2Status==1 and Team2Qestion == 2:
                            team2 "Вопрос за 200"
                            jump R1Cat3Quest2

                        elif R1Cat3Quest3Status==1 and Team2Qestion == 3:
                            team2 "Вопрос за 300"
                            jump R1Cat3Quest3

                        elif R1Cat3Quest4Status==1 and Team2Qestion == 4:
                            team2 "Вопрос за 400"
                            jump R1Cat3Quest4

                        elif R1Cat3Quest5Status==1 and Team2Qestion == 5:
                            team2 "Вопрос за 500"
                            jump R1Cat3Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat3

                    elif Turn == 4: 
                        team3 "Биология"
                        $Team3Qestion = renpy.random.randint(1,5)
                        if R1Cat3Quest1Status==1 and Team3Qestion == 1:
                            team3 "Вопрос за 100"
                            jump R1Cat3Quest1

                        elif R1Cat3Quest2Status==1 and Team3Qestion == 2:
                            team3 "Вопрос за 200"
                            jump R1Cat3Quest2

                        elif R1Cat3Quest3Status==1 and Team3Qestion == 3:
                            team3 "Вопрос за 300"
                            jump R1Cat3Quest3

                        elif R1Cat3Quest4Status==1 and Team3Qestion == 4:
                            team3 "Вопрос за 400"
                            jump R1Cat3Quest4

                        elif R1Cat3Quest5Status==1 and Team3Qestion == 5:
                            team3 "Вопрос за 500"
                            jump R1Cat3Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat3
                    
                    label R1Cat3Quest1:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 100

                        leader "Вопрос за 100"
                        "Именно это животное черного цвета неблагоприятно для человека (суеверие) "
                        if Turn == 1 :
                            menu: 
                                "Кот/Кошка":
                                    "верно"
                                    $OurTeamPoints += 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest1Status = False
                                    jump Round1 

                                "Корова/Бык":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest1Status = False
                                    jump Round1 

                                "Лошадь":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest1Status = False
                                    jump Round1 

                                "Мишка":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest1Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Кот/Кошка"
                                "верно"
                                $Team1Points += 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Корова/Бык"
                                "неверно"
                                "ответ"
                                $OurTeamPoints -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "Лошадь"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "Мишка"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat3Quest1Status = False
                                jump Round1 

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Кот/Кошка"
                                "верно"
                                $Team2Points += 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Корова/Бык"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Лошадь"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Мишка"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest1Status = False
                                jump Round1 

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Кот/Кошка"
                                "верно"
                                $Team3Points += 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Корова/Бык"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Лошадь"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Мишка"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest1Status = False
                                jump Round1

                    label R1Cat3Quest2:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 200

                        leader "Вопрос за 200"
                        "Какая птица нередко ассоциируется со знаниями? "
                        if Turn == 1 :
                            menu: 
                                "Сова":
                                    "верно"
                                    $OurTeamPoints += 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest2Status = False
                                    jump Round1 

                                "Дятел":
                                    "неверно"
                                    "Сова"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest2Status = False
                                    jump Round1 

                                "Воробей":
                                    "неверно"
                                    "Сова"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest2Status = False
                                    jump Round1 

                                "Синица":    
                                    "неверно"
                                    "Сова"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest2Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Сова"
                                "верно"
                                $Team1Points += 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Дятел"
                                "неверно"
                                "Сова"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "Воробей"
                                "неверно"
                                "Сова"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "Синица" 
                                "неверно"
                                "Сова"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest2Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Сова"
                                "верно"
                                $Team2Points += 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Дятел"
                                "неверно"
                                "Сова"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Воробей"
                                "неверно"
                                "Сова"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Синица" 
                                "неверно"
                                "Сова"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest2Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Сова"
                                "верно"
                                $Team3Points += 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "Дятел"
                                "неверно"
                                "Сова"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "Воробей"
                                "неверно"
                                "Сова"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "Синица" 
                                "неверно"
                                "Сова"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest2Status = False
                                jump Round1

                    label R1Cat3Quest3:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 300

                        leader "Вопрос за 300"
                        "Это правда, что никотиновая кислота является витамином?"
                        if Turn == 1 :
                            menu: 
                                "Да":
                                    "верно"
                                    $OurTeamPoints += 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest3Status = False
                                    jump Round1 

                                "Нет":
                                    "неверно"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest3Status = False
                                    jump Round1  

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,2)
                            if Team1Answer == 1:
                                "Да"
                                "верно"
                                $Team1Points += 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Нет"
                                "неверно"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest3Status = False
                                jump Round1 

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,2)
                            if Team2Answer == 1:
                                "Да"
                                "верно"
                                $Team2Points += 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Нет"
                                "неверно"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest3Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,2)
                            if Team3Answer == 1:
                                "Да"
                                "верно"
                                $Team3Points += 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "Нет"
                                "неверно"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest3Status = False
                                jump Round1
                    
                    label R1Cat3Quest4:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 400

                        leader "Вопрос за 400"
                        "Не рыба, а птица, но крылья в чешуе. "
                        if Turn == 1 :
                            menu: 
                                "Пингвин":
                                    "верно"
                                    $OurTeamPoints += 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest4Status = False
                                    jump Round1 

                                "Рыба-Птица":
                                    "неверно"
                                    "Пингвин"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest4Status = False
                                    jump Round1 

                                "Кит":
                                    "неверно"
                                    "Пингвин"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest4Status = False
                                    jump Round1 

                                "Кашалот":    
                                    "неверно"
                                    "Пингвин"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest4Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Пингвин"
                                "верно"
                                $Team1Points += 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Рыба-Птица"
                                "неверно"
                                "Пингвин"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "Кит"
                                "неверно"
                                "Пингвин"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "Кашалот"   
                                "неверно"
                                "Пингвин"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest4Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Пингвин"
                                "верно"
                                $Team2Points += 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Рыба-Птица"
                                "неверно"
                                "Пингвин"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Кит"
                                "неверно"
                                "Пингвин"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Кашалот"   
                                "неверно"
                                "Пингвин"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest4Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Пингвин"
                                "верно"
                                $Team3Points += 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "Рыба-Птица"
                                "неверно"
                                "Пингвин"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "Кит"
                                "неверно"
                                "Пингвин"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "Кашалот"   
                                "неверно"
                                "Пингвин"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest4Status = False
                                jump Round1

                    label R1Cat3Quest5:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 500

                        leader "Вопрос за 500"
                        "Предок птиц "
                        if Turn == 1 :
                            menu: 
                                "Динозавры":
                                    "верно"
                                    $OurTeamPoints += 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest5Status = False
                                    jump Round1 

                                "Олежа":
                                    "неверно"
                                    "Динозавры"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest5Status = False
                                    jump Round1 

                                "Рептилия":
                                    "неверно"
                                    "Динозавры"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest5Status = False
                                    jump Round1 

                                "Рыба":    
                                    "неверно"
                                    "Динозавры"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest5Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Динозавры"
                                "верно"
                                $Team1Points += 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Олежа"
                                "неверно"
                                "Динозавры"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "Рептилия"
                                "неверно"
                                "Динозавры"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "Рыба"  
                                "неверно"
                                "Динозавры"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest5Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Динозавры"
                                "верно"
                                $Team2Points += 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Олежа"
                                "неверно"
                                "Динозавры"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Рептилия"
                                "неверно"
                                "Динозавры"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Рыба"  
                                "неверно"
                                "Динозавры"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest5Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Динозавры"
                                "верно"
                                $Team3Points += 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "Олежа"
                                "неверно"
                                "Динозавры"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "Рептилия"
                                "неверно"
                                "Динозавры"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "Рыба"  
                                "неверно"
                                "Динозавры"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest5Status = False
                                jump Round1

                label Round1Cat4:
                    
                    $ timez = 300
                    $ time_range = 300

                    $TeamCat = renpy.random.randint(1,5)
                    if R1Cat1Status==1 and TeamCat == 1:
                        $ marker = 'R1Cat4Quest1'

                    elif R1Cat2Status==1 and TeamCat == 2:
                        $ marker = 'R1Cat4Quest2'

                    elif R1Cat3Status==1 and TeamCat == 3:
                        $ marker = 'R1Cat4Quest3'

                    elif R1Cat4Status==1 and TeamCat == 4:
                        $ marker = 'R1Cat4Quest4'
                    
                    elif R1Cat4Status==1 and TeamCat == 5:
                        $ marker = 'R1Cat4Quest5'

                    if Turn == 1: 
                        gg "Мультфильмы"
                        menu: 
                            "100" if R1Cat4Quest1Status == True:
                                jump R1Cat4Quest1

                            "200" if R1Cat4Quest2Status==1:
                                jump R1Cat4Quest2

                            "300" if R1Cat4Quest3Status==1:
                                jump R1Cat4Quest3

                            "400" if R1Cat4Quest4Status==1:
                                jump R1Cat4Quest4

                            "500" if R1Cat4Quest5Status==1:
                                jump R1Cat4Quest5

                    elif Turn == 2 : 
                        team1 "Мультфильмы"
                        $Team1Qestion = renpy.random.randint(1,5)
                        if R1Cat4Quest1Status==1 and Team1Qestion == 1:
                            team1 "Вопрос за 100"
                            jump R1Cat4Quest1

                        elif R1Cat4Quest2Status==1 and Team1Qestion == 2:
                            team1 "Вопрос за 200"
                            jump R1Cat4Quest2

                        elif R1Cat4Quest3Status==1 and Team1Qestion == 3:
                            team1 "Вопрос за 300"
                            jump R1Cat4Quest3

                        elif R1Cat4Quest4Status==1 and Team1Qestion == 4:
                            team1 "Вопрос за 400"
                            jump R1Cat4Quest4

                        elif R1Cat4Quest5Status==1 and Team1Qestion == 5:
                            team1 "Вопрос за 500"
                            jump R1Cat4Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat4    

                    elif Turn == 3: 
                        team2 "Мультфильмы"
                        $Team2Qestion = renpy.random.randint(1,5)
                        if R1Cat4Quest1Status==1 and Team2Qestion == 1:
                            team2 "Вопрос за 100"
                            jump R1Cat4Quest1

                        elif R1Cat4Quest2Status==1 and Team2Qestion == 2:
                            team2 "Вопрос за 200"
                            jump R1Cat4Quest2

                        elif R1Cat4Quest3Status==1 and Team2Qestion == 3:
                            team2 "Вопрос за 300"
                            jump R1Cat4Quest3

                        elif R1Cat4Quest4Status==1 and Team2Qestion == 4:
                            team2 "Вопрос за 400"
                            jump R1Cat4Quest4

                        elif R1Cat4Quest5Status==1 and Team2Qestion == 5:
                            team2 "Вопрос за 500"
                            jump R1Cat4Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat4

                    elif Turn == 4: 
                        team3 "Мультфильмы"
                        $Team3Qestion = renpy.random.randint(1,5)
                        if R1Cat4Quest1Status==1 and Team3Qestion == 1:
                            team3 "Вопрос за 100"
                            jump R1Cat4Quest1

                        elif R1Cat4Quest2Status==1 and Team3Qestion == 2:
                            team3 "Вопрос за 200"
                            jump R1Cat4Quest2

                        elif R1Cat4Quest3Status==1 and Team3Qestion == 3:
                            team3 "Вопрос за 300"
                            jump R1Cat4Quest3

                        elif R1Cat4Quest4Status==1 and Team3Qestion == 4:
                            team3 "Вопрос за 400"
                            jump R1Cat4Quest4

                        elif R1Cat4Quest5Status==1 and Team3Qestion == 5:
                            team3 "Вопрос за 500"
                            jump R1Cat4Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat4
                    
                    label R1Cat4Quest1:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 100

                        leader "Вопрос за 100"
                        "Именно к этим грызунам относятся Чип и Дейл"
                        if Turn == 1 :
                            menu: 
                                "Бурундук":
                                    "верно"
                                    $OurTeamPoints += 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest1Status = False
                                    jump Round1 

                                "Хомяк":
                                    "неверно"
                                    "Бурундук"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest1Status = False
                                    jump Round1 

                                "Белка":
                                    "неверно"
                                    "Бурундук"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest1Status = False
                                    jump Round1 

                                "Крыса":    
                                    "неверно"
                                    "Бурундук"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest1Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Бурундук"
                                "верно"
                                $Team1Points += 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat4Quest1Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Хомяк"
                                "неверно"
                                "Бурундук"
                                $OurTeamPoints -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat4Quest1Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "Белка"
                                "неверно"
                                "Бурундук"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat4Quest1Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "Крыса"
                                "неверно"
                                "Бурундук"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat4Quest1Status = False
                                jump Round1 

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Бурундук"
                                "верно"
                                $Team2Points += 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest1Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Хомяк"
                                "неверно"
                                "Бурундук"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest1Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Белка"
                                "неверно"
                                "Бурундук"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest1Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Крыса"
                                "неверно"
                                "Бурундук"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest1Status = False
                                jump Round1 

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Бурундук"
                                "верно"
                                $Team3Points += 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest1Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Хомяк"
                                "неверно"
                                "Бурундук"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest1Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Белка"
                                "неверно"
                                "Бурундук"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest1Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Крыса"
                                "неверно"
                                "Бурундук"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest1Status = False
                                jump Round1

                    label R1Cat4Quest2:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 200

                        leader "Вопрос за 200"
                        "В каком мультфильме прозвучала фраза про ром"
                        if Turn == 1 :
                            menu: 
                                "Остров сокровищ":
                                    "верно"
                                    $OurTeamPoints += 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest2Status = False
                                    jump Round1 

                                "Гриффины":
                                    "неверно"
                                    "Остров сокровищ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest2Status = False
                                    jump Round1 

                                "Тайна третей планеты":
                                    "неверно"
                                    "Остров сокровищ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest2Status = False
                                    jump Round1 

                                "Смешарики":    
                                    "неверно"
                                    "Остров сокровищ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest2Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Остров сокровищ"
                                "верно"
                                $Team1Points += 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest2Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Гриффины"
                                "неверно"
                                "Остров сокровищ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest2Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "Тайна третей планеты"
                                "неверно"
                                "Остров сокровищ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest2Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "Смешарики"    
                                "неверно"
                                "Остров сокровищ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest2Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Остров сокровищ"
                                "верно"
                                $Team2Points += 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest2Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Гриффины"
                                "неверно"
                                "Остров сокровищ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest2Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Тайна третей планеты"
                                "неверно"
                                "Остров сокровищ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest2Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Смешарики"    
                                "неверно"
                                "Остров сокровищ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest2Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Остров сокровищ"
                                "верно"
                                $Team3Points += 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest2Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "Гриффины"
                                "неверно"
                                "Остров сокровищ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest2Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "Тайна третей планеты"
                                "неверно"
                                "Остров сокровищ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest2Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "Смешарики"    
                                "неверно"
                                "Остров сокровищ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest2Status = False
                                jump Round1

                    label R1Cat4Quest3:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 300

                        leader "Вопрос за 300"
                        "За этим послали падчерицу, в мультфильме 12 месяцев"
                        if Turn == 1 :
                            menu: 
                                "Подснежники":
                                    "верно"
                                    $OurTeamPoints += 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest3Status = False
                                    jump Round1 

                                "Ромашки":
                                    "неверно"
                                    "Подснежники"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest3Status = False
                                    jump Round1 

                                "Розы":
                                    "неверно"
                                    "Подснежники"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest3Status = False
                                    jump Round1 

                                "Ель":    
                                    "неверно"
                                    "Подснежники"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest3Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Подснежники"
                                "верно"
                                $Team1Points += 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest3Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Ромашки"
                                "неверно"
                                "Подснежники"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest3Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "Розы"
                                "неверно"
                                "Подснежники"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest3Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "Ель"   
                                "неверно"
                                "Подснежники"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest3Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Подснежники"
                                "верно"
                                $Team2Points += 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest3Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Ромашки"
                                "неверно"
                                "Подснежники"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest3Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Розы"
                                "неверно"
                                "Подснежники"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest3Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Ель"   
                                "неверно"
                                "Подснежники"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest3Status = False
                                jump Round1

                        elif Turn == 4 : 

                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Подснежники"
                                "верно"
                                $Team3Points += 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest3Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "Ромашки"
                                "неверно"
                                "Подснежники"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest3Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "Розы"
                                "неверно"
                                "Подснежники"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest3Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "Ель"   
                                "неверно"
                                "Подснежники"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest3Status = False
                                jump Round1
                    
                    label R1Cat4Quest4:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 400

                        leader "Вопрос за 400"
                        "С этой закуской связан совет кота, мальчику "
                        if Turn == 1 :
                            menu: 
                                "Бутерброд":
                                    "верно"
                                    $OurTeamPoints += 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest4Status = False
                                    jump Round1 

                                "Тарталетки":
                                    "неверно"
                                    "Бутерброд"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest4Status = False
                                    jump Round1 

                                "Огурчик":
                                    "неверно"
                                    "Бутерброд"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest4Status = False
                                    jump Round1 

                                "Чипсы":    
                                    "неверно"
                                    "Бутерброд"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest4Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Бутерброд"
                                "верно"
                                $Team1Points += 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest4Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Тарталетки"
                                "неверно"
                                "Бутерброд"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest4Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "Огурчик"
                                "неверно"
                                "Бутерброд"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest4Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "Чипсы"    
                                "неверно"
                                "Бутерброд"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest4Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Бутерброд"
                                "верно"
                                $Team2Points += 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest4Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Тарталетки"
                                "неверно"
                                "Бутерброд"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest4Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Огурчик"
                                "неверно"
                                "Бутерброд"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest4Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Чипсы"    
                                "неверно"
                                "Бутерброд"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest4Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Бутерброд"
                                "верно"
                                $Team3Points += 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest4Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "Тарталетки"
                                "неверно"
                                "Бутерброд"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest4Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "Огурчик"
                                "неверно"
                                "Бутерброд"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest4Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "Чипсы"    
                                "неверно"
                                "Бутерброд"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest4Status = False
                                jump Round1

                    label R1Cat4Quest5:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 500

                        leader "Вопрос за 500"
                        "Как зовут этого персонажа"
                        hide sexMan
                        show mm
                        if Turn == 1 :
                            $ answer = renpy.input("Кто же это")
                            $ answer = answer.strip() or "Я не знаю"

                            if answer == "Майор френсис монограмм" or answer == "Френсис монограмм" or answer == "Майор монограмм":

                                "Верно"
                                $OurTeamPoints += 500  
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat4Quest5Status = False
                                hide mm
                                show sexMan
                                jump Round1

                            else:
                                
                                "Неверно"
                                $OurTeamPoints -= 500  
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat4Quest5Status = False
                                hide mm
                                show sexMan
                                jump Round1


                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Майор Френсис Монограмм"
                                leader "верно"
                                $Team1Points += 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest5Status = False
                                hide mm
                                jump Round1 
                            if Team1Answer == 2:
                                "Генерал Мальберт Меладзев"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest5Status = False
                                hide mm
                                jump Round1 
                            if Team1Answer == 3:
                                "Майор Олег Монгол"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest5Status = False
                                hide mm
                                jump Round1 
                            if Team1Answer == 4:
                                "Адмирал Михаил Голустян"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest5Status = False
                                hide mm
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Майор Френсис Монограмм"
                                leader "верно"
                                $Team2Points += 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest5Status = False
                                hide mm
                                jump Round1 
                            if Team2Answer == 2:
                                "Генерал Мальберт Меладзев"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest5Status = False
                                hide mm
                                jump Round1 
                            if Team2Answer == 3:
                                "Майор Олег Монгол"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest5Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Адмирал Михаил Голустян"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest5Status = False
                                hide mm
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Майор Френсис Монограмм"
                                leader "верно"
                                $Team3Points += 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest5Status = False
                                hide mm
                                jump Round1 
                            if Team3Answer == 2:
                                "Генерал Мальберт Меладзев"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest5Status = False
                                hide mm
                                jump Round1 
                            if Team3Answer == 3:
                                "Майор Олег Монгол"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest5Status = False
                                hide mm
                                jump Round1 
                            if Team3Answer == 4:
                                "Адмирал Михаил Голустян"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest5Status = False
                                hide mm
                                jump Round1

            label Round2:
                

                $ timez = 300
                $ time_range = 300

                $TeamCat = renpy.random.randint(1,4)
                if R1Cat1Status==1 and TeamCat == 1:
                    $ marker = 'Round2Cat1'

                elif R1Cat2Status==1 and TeamCat == 2:
                    $ marker = 'Round2Cat2'

                elif R1Cat3Status==1 and TeamCat == 3:
                    $ marker = 'Round2Cat3'

                elif R1Cat4Status==1 and TeamCat == 4:
                    $ marker = 'Round2Cat4'
                

                if R2Categories == 1:
                    jump Final

                if R2Cat1Quest1Status == False and R2Cat1Quest2Status == False and R2Cat1Quest3Status == False and R2Cat1Quest4Status == False and R2Cat1Quest5Status == False:
                    $ R1Cat1Status = False
                    $ R1Categories -=1
                
                if R2Cat2Quest1Status == False and R2Cat2Quest2Status == False and R2Cat2Quest3Status == False and R2Cat2Quest4Status == False and R2Cat2Quest5Status == False:
                    $ R1Cat2Status = False
                    $ R1Categories -=1

                if R2Cat3Quest1Status == False and R2Cat3Quest2Status == False and R2Cat3Quest3Status == False and R2Cat3Quest4Status == False and R2Cat3Quest5Status == False:
                    $ R1Cat3Status = False
                    $ R1Categories -=1

                if R2Cat4Quest1Status == False and R2Cat4Quest2Status == False and R2Cat4Quest3Status == False and R2Cat4Quest4Status == False and R2Cat4Quest5Status == False:
                    $ R1Cat4Status = False
                    $ R1Categories -=1

                if Turn == 1:
                    menu:
                        "Языки" if R1Cat1Status == True:
                            jump Round2Cat1
                        "Страны" if R1Cat2Status == True:
                            jump Round2Cat2
                        "Изобретения" if R1Cat2Status == True:
                            jump Round2Cat3
                        "Программирование" if R1Cat2Status == True:
                            jump Round2Cat4

                elif Turn == 2 : 
                        $Team1Qestion = renpy.random.randint(1,4)
                        if R1Cat1Status==1 and Team1Qestion == 1:
                            jump Round2Cat1

                        elif R1Cat2Status==1 and Team1Qestion == 2:
                            jump Round2Cat2

                        elif R1Cat3Status==1 and Team1Qestion == 3:
                            jump Round2Cat3

                        elif R1Cat4Status==1 and Team1Qestion == 4:
                            jump Round2Cat4    

                elif Turn == 3: 
                    $Team1Qestion = renpy.random.randint(1,4)
                    if R1Cat1Status==1 and Team1Qestion == 1:
                        jump Round2Cat1

                    elif R1Cat2Status==1 and Team1Qestion == 2:
                        jump Round2Cat2

                    elif R1Cat3Status==1 and Team1Qestion == 3:
                        jump Round2Cat3

                    elif R1Cat4Status==1 and Team1Qestion == 4:
                        jump Round2Cat4

                elif Turn == 4: 
                    $Team1Qestion = renpy.random.randint(1,4)
                    if R1Cat1Status==1 and Team1Qestion == 1:
                        jump Round2Cat1

                    elif R1Cat2Status==1 and Team1Qestion == 2:
                        jump Round2Cat2

                    elif R1Cat3Status==1 and Team1Qestion == 3:
                        jump Round2Cat3

                    elif R1Cat4Status==1 and Team1Qestion == 4:
                        jump Round2Cat4     
 
                label Round2Cat1:

                    $ timez = 300
                    $ time_range = 300

                    $TeamCat = renpy.random.randint(1,5)
                    if R1Cat1Status==1 and TeamCat == 1:
                        $ marker = 'R2Cat1Quest1'

                    elif R1Cat2Status==1 and TeamCat == 2:
                        $ marker = 'R2Cat1Quest2'

                    elif R1Cat3Status==1 and TeamCat == 3:
                        $ marker = 'R2Cat1Quest3'

                    elif R1Cat4Status==1 and TeamCat == 4:
                        $ marker = 'R2Cat1Quest4'
                    
                    elif R1Cat4Status==1 and TeamCat == 5:
                        $ marker = 'R2Cat1Quest5'

                    if Turn == 1: 
                        gg "Языки"
                        menu: 
                            "100" if R2Cat1Quest1Status == True:
                                jump R2Cat1Quest1

                            "200" if R2Cat1Quest2Status==1:
                                jump R2Cat1Quest2

                            "300" if R2Cat1Quest3Status==1:
                                jump R2Cat1Quest3

                            "400" if R2Cat1Quest4Status==1:
                                jump R2Cat1Quest4

                            "500" if R2Cat1Quest5Status==1:
                                jump R2Cat1Quest5

                    elif Turn == 2 : 
                        team1 "Языки"
                        $Team1Qestion = renpy.random.randint(1,5)
                        if R2Cat1Quest1Status==1 and Team1Qestion == 1:
                            team1 "Вопрос за 100"
                            jump R2Cat1Quest1

                        elif R2Cat1Quest2Status==1 and Team1Qestion == 2:
                            team1 "Вопрос за 200"
                            jump R2Cat1Quest2

                        elif R2Cat1Quest3Status==1 and Team1Qestion == 3:
                            team1 "Вопрос за 300"
                            jump R2Cat1Quest3

                        elif R2Cat1Quest4Status==1 and Team1Qestion == 4:
                            team1 "Вопрос за 400"
                            jump R2Cat1Quest4

                        elif R2Cat1Quest5Status==1 and Team1Qestion == 5:
                            team1 "Вопрос за 500"
                            jump R2Cat1Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round2Cat1    

                    elif Turn == 3: 
                        team2 "Языки"
                        $Team1Qestion = renpy.random.randint(1,5)
                        if R2Cat1Quest1Status==1 and Team1Qestion == 1:
                            team2 "Вопрос за 100"
                            jump R2Cat1Quest1

                        elif R2Cat1Quest2Status==1 and Team1Qestion == 2:
                            team2 "Вопрос за 200"
                            jump R2Cat1Quest2

                        elif R2Cat1Quest3Status==1 and Team1Qestion == 3:
                            team2 "Вопрос за 300"
                            jump R2Cat1Quest3

                        elif R2Cat1Quest4Status==1 and Team1Qestion == 4:
                            team2 "Вопрос за 400"
                            jump R2Cat1Quest4

                        elif R2Cat1Quest5Status==1 and Team1Qestion == 5:
                            team2 "Вопрос за 500"
                            jump R2Cat1Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round2Cat1 

                    elif Turn == 4: 
                        team3 "Языки"
                        $Team1Qestion = renpy.random.randint(1,5)
                        if R2Cat1Quest1Status==1 and Team1Qestion == 1:
                            team3 "Вопрос за 100"
                            jump R2Cat1Quest1

                        elif R2Cat1Quest2Status==1 and Team1Qestion == 2:
                            team3 "Вопрос за 200"
                            jump R2Cat1Quest2

                        elif R2Cat1Quest3Status==1 and Team1Qestion == 3:
                            team3 "Вопрос за 300"
                            jump R2Cat1Quest3

                        elif R2Cat1Quest4Status==1 and Team1Qestion == 4:
                            team3 "Вопрос за 400"
                            jump R2Cat1Quest4

                        elif R2Cat1Quest5Status==1 and Team1Qestion == 5:
                            team3 "Вопрос за 500"
                            jump R2Cat1Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round2Cat1 
                    
                    label R2Cat1Quest1:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 100

                        leader "Вопрос за 100"
                        "Этот язык долго был языком международной дипломатии, однако со временем был замещён Английским "
                        if Turn == 1 :
                            menu: 
                                "Французкий":
                                    leader "верно"
                                    $OurTeamPoints += 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest1Status = False
                                    jump Round1 

                                "Китайский":
                                    "неверно"
                                    "Французкий"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest1Status = False
                                    jump Round1 

                                "Русский":
                                    "неверно"
                                    "Французкий"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest1Status = False
                                    jump Round1 

                                "Немецкий":    
                                    "неверно"
                                    "Французкий"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest1Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "Французкий"
                                "верно"
                                $Team1Points += 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R2Cat1Quest1Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Китайский"
                                "неверно"
                                "Французкий"
                                $OurTeamPoints -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R2Cat1Quest1Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "Русский"
                                "неверно"
                                "Французкий"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R2Cat1Quest1Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "Немецкий"   
                                "неверно"
                                "Французкий"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R2Cat1Quest1Status = False
                                jump Round1 

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "Французкий"
                                "верно"
                                $Team2Points += 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest1Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Китайский"
                                "неверно"
                                "Французкий"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest1Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Русский"
                                "неверно"
                                "Французкий"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest1Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Немецкий"   
                                "неверно"
                                "Французкий"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest1Status = False
                                jump Round1 

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "Французкий"
                                "верно"
                                $Team3Points += 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest1Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Китайский"
                                "неверно"
                                "Французкий"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest1Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Русский"
                                "неверно"
                                "Французкий"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest1Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Немецкий"   
                                "неверно"
                                "Французкий"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest1Status = False
                                jump Round1

                    label R2Cat1Quest2:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 200

                        leader "Вопрос за 200"
                        "Данный язык является самым распространённым в Африке "
                        if Turn == 1 :
                            menu: 
                                "Арабский":
                                    "верно"
                                    $OurTeamPoints += 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest2Status = False
                                    jump Round1 

                                "Афркианский":
                                    "неверно"
                                    "Арабский"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest2Status = False
                                    jump Round1 

                                "Английский":
                                    "неверно"
                                    "Арабский"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest2Status = False
                                    jump Round1 

                                "Итальянский":    
                                    "неверно"
                                    "Арабский"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest2Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "Арабский"
                                "верно"
                                $Team1Points += 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest2Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Афркианский"
                                "неверно"
                                "Арабский"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest2Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "Английский"
                                "неверно"
                                "Арабский"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest2Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "Итальянский"    
                                "неверно"
                                "Арабский"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest2Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "Арабский"
                                "верно"
                                $Team2Points += 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest2Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Афркианский"
                                "неверно"
                                "Арабский"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest2Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Английский"
                                "неверно"
                                "Арабский"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest2Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Итальянский"    
                                "неверно"
                                "Арабский"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest2Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "Арабский"
                                "верно"
                                $Team3Points += 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest2Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "Афркианский"
                                "неверно"
                                "Арабский"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest2Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "Английский"
                                "неверно"
                                "Арабский"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest2Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "Итальянский"    
                                "неверно"
                                "Арабский"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest2Status = False
                                jump Round1

                    label R2Cat1Quest3:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 300

                        leader "Вопрос за 300"
                        "Этот язык программирования является простейшим для создания сайта"
                        if Turn == 1 :
                            menu: 
                                "PHP":
                                    "верно"
                                    $OurTeamPoints += 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest3Status = False
                                    jump Round2 

                                "C#":
                                    "неверно"
                                    "PHP"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest3Status = False
                                    jump Round2 

                                "HTML":
                                    "неверно"
                                    "PHP"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest3Status = False
                                    jump Round2 

                                "Pyhton":    
                                    "неверно"
                                    "PHP"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest3Status = False
                                    jump Round2 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "PHP"
                                "верно"
                                $Team1Points += 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest3Status = False
                                jump Round2 
                            if Team1Answer == 2:
                                "C#"
                                "неверно"
                                "PHP"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest3Status = False
                                jump Round2 
                            if Team1Answer == 3:
                                "HTML"
                                "неверно"
                                "PHP"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest3Status = False
                                jump Round2 
                            if Team1Answer == 4:
                                "Pyhton"    
                                "неверно"
                                "PHP"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest3Status = False
                                jump Round2

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "PHP"
                                "верно"
                                $Team2Points += 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest3Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "C#"
                                "неверно"
                                "PHP"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest3Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "HTML"
                                "неверно"
                                "PHP"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest3Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "Pyhton"    
                                "неверно"
                                "PHP"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest3Status = False
                                jump Round2

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "PHP"
                                "верно"
                                $Team3Points += 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest3Status = False
                                jump Round2 
                            if Team3Answer == 2:
                                "C#"
                                "неверно"
                                "PHP"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest3Status = False
                                jump Round2 
                            if Team3Answer == 3:
                                "HTML"
                                "неверно"
                                "PHP"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest3Status = False
                                jump Round2 
                            if Team3Answer == 4:
                                "Pyhton"    
                                "неверно"
                                "PHP"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest3Status = False
                                jump Round2
                    
                    label R2Cat1Quest4:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 400

                        leader "Вопрос за 400"
                        "Язык, созданный польским лингвистом для международного общения"
                        if Turn == 1 :
                            menu: 
                                "Эсперанто":
                                    "верно"
                                    $OurTeamPoints += 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest4Status = False
                                    jump Round2 

                                "Польский":
                                    "неверно"
                                    "Эсперанто"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest4Status = False
                                    jump Round2 

                                "Межславянский":
                                    "неверно"
                                    "Эсперанто"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest4Status = False
                                    jump Round2 

                                "Скандинавский":    
                                    "неверно"
                                    "Эсперанто"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest4Status = False
                                    jump Round2 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "Эсперанто"
                                "верно"
                                $Team1Points += 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest4Status = False
                                jump Round2 
                            if Team1Answer == 2:
                                "Польский"
                                "неверно"
                                "Эсперанто"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest4Status = False
                                jump Round2 
                            if Team1Answer == 3:
                                "Межславянский"
                                "неверно"
                                "Эсперанто"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest4Status = False
                                jump Round2 
                            if Team1Answer == 4:
                                "Скандинавский"  
                                "неверно"
                                "Эсперанто"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest4Status = False
                                jump Round2

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "Эсперанто"
                                "верно"
                                $Team2Points += 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest4Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "Польский"
                                "неверно"
                                "Эсперанто"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest4Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "Межславянский"
                                "неверно"
                                "Эсперанто"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest4Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "Скандинавский"  
                                "неверно"
                                "Эсперанто"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest4Status = False
                                jump Round2

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "Эсперанто"
                                "верно"
                                $Team3Points += 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest4Status = False
                                jump Round2 
                            if Team3Answer == 2:
                                "Польский"
                                "неверно"
                                "Эсперанто"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest4Status = False
                                jump Round2 
                            if Team3Answer == 3:
                                "Межславянский"
                                "неверно"
                                "Эсперанто"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest4Status = False
                                jump Round2 
                            if Team3Answer == 4:
                                "Скандинавский"  
                                "неверно"
                                "Эсперанто"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest4Status = False
                                jump Round2

                    label R2Cat1Quest5:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 500

                        leader "Вопрос за 500"
                        "Сколько языков у улитки? "
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest5Status = False
                                    jump Round2 

                                "2":
                                    "неверно"
                                    "1"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest5Status = False
                                    jump Round2 

                                "3":
                                    "неверно"
                                    "1"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest5Status = False
                                    jump Round2 

                                "4":    
                                    "неверно"
                                    "1"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest5Status = False
                                    jump Round2 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest5Status = False
                                jump Round2 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "1"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest5Status = False
                                jump Round2 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "1"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest5Status = False
                                jump Round2 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "1"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest5Status = False
                                jump Round2

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest5Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "1"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest5Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "1"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ Cat1Quest5Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "1"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest5Status = False
                                jump Round2

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest5Status = False
                                jump Round2 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "1"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest5Status = False
                                jump Round2 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "1"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest5Status = False
                                jump Round2 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "1"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest5Status = False
                                jump Round2

                label Round2Cat2:
                    
                    $ timez = 300
                    $ time_range = 300

                    $TeamCat = renpy.random.randint(1,5)
                    if R1Cat1Status==1 and TeamCat == 1:
                        $ marker = 'R2Cat2Quest1'

                    elif R1Cat2Status==1 and TeamCat == 2:
                        $ marker = 'R2Cat2Quest2'

                    elif R1Cat3Status==1 and TeamCat == 3:
                        $ marker = 'R2Cat2Quest3'

                    elif R1Cat4Status==1 and TeamCat == 4:
                        $ marker = 'R2Cat2Quest4'
                    
                    elif R1Cat4Status==1 and TeamCat == 5:
                        $ marker = 'R2Cat2Quest5'

                    if Turn == 1: 
                        gg "Страны"
                        menu: 
                            "100" if R2Cat2Quest1Status == True:
                                jump R2Cat2Quest1

                            "200" if R2Cat2Quest2Status==1:
                                jump R2Cat2Quest2

                            "300" if R2Cat2Quest3Status==1:
                                jump R2Cat2Quest3

                            "400" if R2Cat2Quest4Status==1:
                                jump R2Cat2Quest4

                            "500" if R2Cat2Quest5Status==1:
                                jump R2Cat2Quest5

                    elif Turn == 2 : 
                        team1 "Страны"
                        $Team1Qestion = renpy.random.randint(1,5)
                        if R2Cat2Quest1Status==1 and Team1Qestion == 1:
                            team1 "Вопрос за 100"
                            jump R2Cat2Quest1

                        elif R2Cat2Quest2Status==1 and Team1Qestion == 2:
                            team1 "Вопрос за 200"
                            jump R2Cat2Quest2

                        elif R2Cat2Quest3Status==1 and Team1Qestion == 3:
                            team1 "Вопрос за 300"
                            jump R2Cat2Quest3

                        elif R2Cat2Quest4Status==1 and Team1Qestion == 4:
                            team1 "Вопрос за 400"
                            jump R2Cat2Quest4

                        elif R2Cat2Quest5Status==1 and Team1Qestion == 5:
                            team1 "Вопрос за 500"
                            jump R2Cat2Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round2Cat2    

                    elif Turn == 3: 
                        team2 "Страны"
                        $Team2Qestion = renpy.random.randint(1,5)
                        if R2Cat2Quest1Status==1 and Team2Qestion == 1:
                            team2 "Вопрос за 100"
                            jump R2Cat2Quest1

                        elif R2Cat2Quest2Status==1 and Team2Qestion == 2:
                            team2 "Вопрос за 200"
                            jump R2Cat2Quest2

                        elif R2Cat2Quest3Status==1 and Team2Qestion == 3:
                            team2 "Вопрос за 300"
                            jump R2Cat2Quest3

                        elif R2Cat2Quest4Status==1 and Team2Qestion == 4:
                            team2 "Вопрос за 400"
                            jump R2Cat2Quest4

                        elif R2Cat2Quest5Status==1 and Team2Qestion == 5:
                            team2 "Вопрос за 500"
                            jump R2Cat2Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round2Cat2

                    elif Turn == 4: 
                        team3 "Страны"
                        $Team3Qestion = renpy.random.randint(1,5)
                        if R2Cat2Quest1Status==1 and Team3Qestion == 1:
                            team3 "Вопрос за 100"
                            jump R2Cat2Quest1

                        elif R2Cat2Quest2Status==1 and Team3Qestion == 2:
                            team3 "Вопрос за 200"
                            jump R2Cat2Quest2

                        elif R2Cat2Quest3Status==1 and Team3Qestion == 3:
                            team3 "Вопрос за 300"
                            jump R2Cat2Quest3

                        elif R2Cat2Quest4Status==1 and Team3Qestion == 4:
                            team3 "Вопрос за 400"
                            jump R2Cat2Quest4

                        elif R2Cat2Quest5Status==1 and Team3Qestion == 5:
                            team3 "Вопрос за 500"
                            jump R2Cat2Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round2Cat2
                    
                    label R2Cat2Quest1:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 100

                        leader "Вопрос за 100"
                        "Это государство когда-то было самым большим в мире"
                        if Turn == 1 :
                            menu: 
                                "Монголия":
                                    "верно"
                                    $OurTeamPoints += 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest1Status = False
                                    jump Round2 

                                "Китай":
                                    "неверно"
                                    "Монголия"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest1Status = False
                                    jump Round2 

                                "Франция":
                                    "неверно"
                                    "Монголия"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest1Status = False
                                    jump Round2 

                                "Российская Империя":    
                                    "неверно"
                                    "Монголия"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest1Status = False
                                    jump Round2 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Монголия"
                                "верно"
                                $Team1Points += 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R2Cat2Quest1Status = False
                                jump Round2 
                            if Team1Answer == 2:
                                "Китай"
                                "неверно"
                                "Монголия"
                                $OurTeamPoints -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R2Cat2Quest1Status = False
                                jump Round2 
                            if Team1Answer == 3:
                                "Франция"
                                "неверно"
                                "Монголия"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R2Cat2Quest1Status = False
                                jump Round2 
                            if Team1Answer == 4:
                                "Российская Империя"   
                                "неверно"
                                "Монголия"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R2Cat2Quest1Status = False
                                jump Round2 

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Монголия"
                                "верно"
                                $Team2Points += 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest1Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "Китай"
                                "неверно"
                                "Монголия"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest1Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "Франция"
                                "неверно"
                                "Монголия"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest1Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "Российская Империя"   
                                "неверно"
                                "Монголия"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest1Status = False
                                jump Round2 

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Монголия"
                                "верно"
                                $Team3Points += 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest1Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "Китай"
                                "неверно"
                                "Монголия"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest1Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "Франция"
                                "неверно"
                                "Монголия"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest1Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "Российская Империя"   
                                "неверно"
                                "Монголия"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest1Status = False
                                jump Round2

                    label R2Cat2Quest2:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 200

                        leader "Вопрос за 200"
                        "Пятая республика"
                        if Turn == 1 :
                            menu: 
                                "Франция":
                                    "верно"
                                    $OurTeamPoints += 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest2Status = False
                                    jump Round2 

                                "КНР":
                                    "неверно"
                                    "Франция"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest2Status = False
                                    jump Round2 

                                "Англия":
                                    "неверно"
                                    "Франция"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest2Status = False
                                    jump Round2 

                                "Италия":    
                                    "неверно"
                                    "Франция"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest2Status = False
                                    jump Round2 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Франция"
                                "верно"
                                $Team1Points += 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest2Status = False
                                jump Round2 
                            if Team1Answer == 2:
                                "КНР"
                                "неверно"
                                "Франция"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest2Status = False
                                jump Round2 
                            if Team1Answer == 3:
                                "Англия"
                                "неверно"
                                "Франция"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest2Status = False
                                jump Round2 
                            if Team1Answer == 4:
                                "Италия"    
                                "неверно"
                                "Франция"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest2Status = False
                                jump Round2

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Франция"
                                "верно"
                                $Team2Points += 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest2Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "КНР"
                                "неверно"
                                "Франция"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest2Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "Англия"
                                "неверно"
                                "Франция"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest2Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "Италия"    
                                "неверно"
                                "Франция"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest2Status = False
                                jump Round2

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Франция"
                                "верно"
                                $Team3Points += 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest2Status = False
                                jump Round2 
                            if Team3Answer == 2:
                                "КНР"
                                "неверно"
                                "Франция"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest2Status = False
                                jump Round2 
                            if Team3Answer == 3:
                                "Англия"
                                "неверно"
                                "Франция"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest2Status = False
                                jump Round2 
                            if Team3Answer == 4:
                                "Италия"    
                                "неверно"
                                "Франция"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest2Status = False
                                jump Round2

                    label R2Cat2Quest3:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 300

                        leader "Вопрос за 300"
                        "Родина кантри-музыки "
                        if Turn == 1 :
                            menu: 
                                "США":
                                    "верно"
                                    $OurTeamPoints += 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest3Status = False
                                    jump Round2 

                                "Мексика":
                                    "неверно"
                                    "США"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest3Status = False
                                    jump Round2 

                                "Канада":
                                    "неверно"
                                    "США"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest3Status = False
                                    jump Round2 

                                "Куба":    
                                    "неверно"
                                    "США"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest3Status = False
                                    jump Round2 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "США"
                                "верно"
                                $Team1Points += 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest3Status = False
                                jump Round2 
                            if Team1Answer == 2:
                                "Мексика"
                                "неверно"
                                "США"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest3Status = False
                                jump Round2 
                            if Team1Answer == 3:
                                "Канада"
                                "неверно"
                                "США"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest3Status = False
                                jump Round2 
                            if Team1Answer == 4:
                                "Куба" 
                                "неверно"
                                "США"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest3Status = False
                                jump Round2

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "США"
                                "верно"
                                $Team2Points += 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest3Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "Мексика"
                                "неверно"
                                "США"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest3Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "Канада"
                                "неверно"
                                "США"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest3Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "Куба" 
                                "неверно"
                                "США"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest3Status = False
                                jump Round2

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "США"
                                "верно"
                                $Team3Points += 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest3Status = False
                                jump Round2 
                            if Team3Answer == 2:
                                "Мексика"
                                "неверно"
                                "США"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest3Status = False
                                jump Round2 
                            if Team3Answer == 3:
                                "Канада"
                                "неверно"
                                "США"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest3Status = False
                                jump Round2 
                            if Team3Answer == 4:
                                "Куба" 
                                "неверно"
                                "США"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest3Status = False
                                jump Round2
                    
                    label R2Cat2Quest4:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 400

                        leader "Вопрос за 400"
                        "Данное государство было прозвано Балканской Пруссией "
                        if Turn == 1 :
                            menu: 
                                "Болгария":
                                    "верно"
                                    $OurTeamPoints += 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest4Status = False
                                    jump Round2 

                                "Сербия":
                                    "неверно"
                                    "Болгария"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest4Status = False
                                    jump Round2 

                                "Румыния":
                                    "неверно"
                                    "Болгария"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest4Status = False
                                    jump Round2 

                                "Черногория":    
                                    "неверно"
                                    "Болгария"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest4Status = False
                                    jump Round2 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Болгария"
                                "верно"
                                $Team1Points += 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest4Status = False
                                jump Round2 
                            if Team1Answer == 2:
                                "Сербия"
                                "неверно"
                                "Болгария"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest4Status = False
                                jump Round2 
                            if Team1Answer == 3:
                                "Румыния"
                                "неверно"
                                "Болгария"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest4Status = False
                                jump Round2 
                            if Team1Answer == 4:
                                "Черногория"    
                                "неверно"
                                "Болгария"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest4Status = False
                                jump Round2

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Болгария"
                                "верно"
                                $Team2Points += 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest4Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "Сербия"
                                "неверно"
                                "Болгария"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest4Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "Румыния"
                                "неверно"
                                "Болгария"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest4Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "Черногория"    
                                "неверно"
                                "Болгария"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest4Status = False
                                jump Round2

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Болгария"
                                "верно"
                                $Team3Points += 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest4Status = False
                                jump Round2 
                            if Team3Answer == 2:
                                "Сербия"
                                "неверно"
                                "Болгария"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest4Status = False
                                jump Round2 
                            if Team3Answer == 3:
                                "Румыния"
                                "неверно"
                                "Болгария"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest4Status = False
                                jump Round2 
                            if Team3Answer == 4:
                                "Черногория"    
                                "неверно"
                                "Болгария"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest4Status = False
                                jump Round2

                    label R2Cat2Quest5:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 500

                        leader "Вопрос за 500"
                        "Назовите государство"
                        show av
                        if Turn == 1 :
                            $ answer = renpy.input()

                            if anwer == "Австро-Венгрия":

                                $OurTeamPoints += 500  
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest5Status = False
                                hide av
                                jump Round2

                            else:
                                
                                $OurTeamPoints -= 500  
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest5Status = False
                                hide av
                                jump Round2

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Австро-Венгрия"
                                "верно"
                                $Team1Points += 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest5Status = False
                                jump Round2 
                            if Team1Answer == 2:
                                "Монголия"
                                "неверно"
                                "Австро-Венгрия"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ Cat2Quest5Status = False
                                jump Round2 
                            if Team1Answer == 3:
                                "Франция"
                                "неверно"
                                "Австро-Венгрия"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest5Status = False
                                jump Round2 
                            if Team1Answer == 4:
                                "Китай"
                                "неверно"
                                "Австро-Венгрия"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest5Status = False
                                jump Round2

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Австро-Венгрия"
                                "верно"
                                $Team2Points += 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest5Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "Монголия"
                                "неверно"
                                "Австро-Венгрия"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest5Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "Франция"
                                "неверно"
                                "Австро-Венгрия"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest5Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "Китай"
                                "неверно"
                                "Австро-Венгрия"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest5Status = False
                                jump Round2

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest5Status = False
                                jump Round2 
                            if Team3Answer == 2:
                                "Монголия"
                                "неверно"
                                "Австро-Венгрия"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest5Status = False
                                jump Round2 
                            if Team3Answer == 3:
                                "Франция"
                                "неверно"
                                "Австро-Венгрия"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest5Status = False
                                jump Round2 
                            if Team3Answer == 4:
                                "Китай"
                                "неверно"
                                "Австро-Венгрия"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest5Status = False
                                jump Round2

                label Round2Cat3:

                    $ timez = 300
                    $ time_range = 300

                    $TeamCat = renpy.random.randint(1,5)
                    if R1Cat1Status==1 and TeamCat == 1:
                        $ marker = 'R2Cat3Quest1'

                    elif R1Cat2Status==1 and TeamCat == 2:
                        $ marker = 'R2Cat3Quest2'

                    elif R1Cat3Status==1 and TeamCat == 3:
                        $ marker = 'R2Cat3Quest3'

                    elif R1Cat4Status==1 and TeamCat == 4:
                        $ marker = 'R2Cat3Quest4'
                    
                    elif R1Cat4Status==1 and TeamCat == 5:
                        $ marker = 'R2Cat3Quest5'

                    if Turn == 1: 
                        gg "Изобретения"
                        menu: 
                            "100" if R1Cat3Quest1Status == True:
                                jump R1Cat3Quest1

                            "200" if R1Cat3Quest2Status==1:
                                jump R1Cat3Quest2

                            "300" if R1Cat3Quest3Status==1:
                                jump R1Cat3Quest3

                            "400" if R1Cat3Quest4Status==1:
                                jump R1Cat3Quest4

                            "500" if R1Cat3Quest5Status==1:
                                jump R1Cat3Quest5

                    elif Turn == 2 : 
                        team1 "Изобретения"
                        $Team1Qestion = renpy.random.randint(1,5)
                        if R1Cat3Quest1Status==1 and Team1Qestion == 1:
                            team1 "Вопрос за 100"
                            jump R1Cat3Quest1

                        elif R1Cat3Quest2Status==1 and Team1Qestion == 2:
                            team1 "Вопрос за 200"
                            jump R1Cat3Quest2

                        elif R1Cat3Quest3Status==1 and Team1Qestion == 3:
                            team1 "Вопрос за 300"
                            jump R1Cat3Quest3

                        elif R1Cat3Quest4Status==1 and Team1Qestion == 4:
                            team1 "Вопрос за 400"
                            jump R1Cat3Quest4

                        elif R1Cat3Quest5Status==1 and Team1Qestion == 5:
                            team1 "Вопрос за 500"
                            jump R1Cat3Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat3    

                    elif Turn == 3: 
                        team2 "Изобретения"
                        $Team2Qestion = renpy.random.randint(1,5)
                        if R1Cat3Quest1Status==1 and Team1Qestion == 1:
                            team2 "Вопрос за 100"
                            jump R1Cat3Quest1

                        elif R1Cat3Quest2Status==1 and Team1Qestion == 2:
                            team2 "Вопрос за 200"
                            jump R1Cat3Quest2

                        elif R1Cat3Quest3Status==1 and Team1Qestion == 3:
                            team2 "Вопрос за 300"
                            jump R1Cat3Quest3

                        elif R1Cat3Quest4Status==1 and Team1Qestion == 4:
                            team2 "Вопрос за 400"
                            jump R1Cat3Quest4

                        elif R1Cat3Quest5Status==1 and Team1Qestion == 5:
                            team2 "Вопрос за 500"
                            jump R1Cat3Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat3

                    elif Turn == 4: 
                        team3 "Изобретения"
                        $Team3Qestion = renpy.random.randint(1,5)
                        if R1Cat3Quest1Status==1 and Team1Qestion == 1:
                            team3 "Вопрос за 100"
                            jump R1Cat3Quest1

                        elif R1Cat3Quest2Status==1 and Team1Qestion == 2:
                            team3 "Вопрос за 200"
                            jump R1Cat3Quest2

                        elif R1Cat3Quest3Status==1 and Team1Qestion == 3:
                            team3 "Вопрос за 300"
                            jump R1Cat3Quest3

                        elif R1Cat3Quest4Status==1 and Team1Qestion == 4:
                            team3 "Вопрос за 400"
                            jump R1Cat3Quest4

                        elif R1Cat3Quest5Status==1 and Team1Qestion == 5:
                            team3 "Вопрос за 500"
                            jump R1Cat3Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat3
                    
                    label R2Cat3Quest1:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 100

                        leader "Вопрос за 100"
                        "Назовите фамилию братьев, которых считают изобретателями кинематографа."
                        if Turn == 1 :
                            menu: 
                                "Люмьер":
                                    "верно"
                                    $OurTeamPoints += 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest1Status = False
                                    jump Round1 

                                "Клименко":
                                    "неверно"
                                    "Люмьер"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest1Status = False
                                    jump Round1 

                                "Люмен":
                                    "неверно"
                                    "Люмьер"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest1Status = False
                                    jump Round1 

                                "Томпсон":    
                                    "неверно"
                                    "Люмьер"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest1Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Люмьер"
                                "верно"
                                $Team1Points += 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Клименко"
                                "неверно"
                                "Люмьер"
                                $OurTeamPoints -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "Люмен"
                                "неверно"
                                "Люмьер"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "Томпсон"    
                                "неверно"
                                "Люмьер"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat3Quest1Status = False
                                jump Round1 

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Люмьер"
                                "верно"
                                $Team2Points += 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Клименко"
                                "неверно"
                                "Люмьер"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Люмен"
                                "неверно"
                                "Люмьер"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Томпсон"    
                                "неверно"
                                "Люмьер"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest1Status = False
                                jump Round1 

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Люмьер"
                                "верно"
                                $Team3Points += 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Клименко"
                                "неверно"
                                "Люмьер"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Люмен"
                                "неверно"
                                "Люмьер"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Томпсон"    
                                "неверно"
                                "Люмьер"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest1Status = False
                                jump Round1

                    label R2Cat3Quest2:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 200

                        leader "Вопрос за 200"
                        "кто в 1901 году получил патент как изобретатель обычной бритвы?"
                        if Turn == 1 :
                            menu: 
                                "Жиллетт":
                                    "верно"
                                    $OurTeamPoints += 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest2Status = False
                                    jump Round1 

                                "Роберт Кох":
                                    "неверно"
                                    "Жиллетт"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest2Status = False
                                    jump Round1 

                                "Пипин Короткий":
                                    "неверно"
                                    "Жиллетт"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest2Status = False
                                    jump Round1 

                                "Олежик":    
                                    "неверно"
                                    "Жиллетт"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest2Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Жиллетт"
                                "верно"
                                $Team1Points += 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Роберт Кох"
                                "неверно"
                                "Жиллетт"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "Пипин Короткий"
                                "неверно"
                                "Жиллетт"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "Олежик"    
                                "неверно"
                                "Жиллетт"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest2Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Жиллетт"
                                "верно"
                                $Team2Points += 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Роберт Кох"
                                "неверно"
                                "Жиллетт"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Пипин Короткий"
                                "неверно"
                                "Жиллетт"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Олежик"    
                                "неверно"
                                "Жиллетт"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest2Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Жиллетт"
                                "верно"
                                $Team3Points += 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "Роберт Кох"
                                "неверно"
                                "Жиллетт"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "Пипин Короткий"
                                "неверно"
                                "Жиллетт"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "Олежик"    
                                "неверно"
                                "Жиллетт"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest2Status = False
                                jump Round1

                    label R2Cat3Quest3:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 300

                        leader "Вопрос за 300"
                        "Кто изобрёл создал универсальную техническую схему?"
                        if Turn == 1 :
                            menu: 
                                "Алан Тьюринг":
                                    "верно"
                                    $OurTeamPoints += 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest3Status = False
                                    jump Round1 

                                "Конрад Цузе":
                                    "неверно"
                                    "Алан Тьюринг"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest3Status = False
                                    jump Round1 

                                "Джон Атанасов":
                                    "неверно"
                                    "Алан Тьюринг"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest3Status = False
                                    jump Round1 

                                "Джон Мокли":    
                                    "неверно"
                                    "Алан Тьюринг"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest3Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Алан Тьюринг"
                                "верно"
                                $Team1Points += 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Конрад Цузе"
                                "неверно"
                                "Алан Тьюринг"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "Джон Атанасов"
                                "неверно"
                                "Алан Тьюринг"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "Джон Мокли"  
                                "неверно"
                                "Алан Тьюринг"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest3Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Алан Тьюринг"
                                "верно"
                                $Team2Points += 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Конрад Цузе"
                                "неверно"
                                "Алан Тьюринг"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Джон Атанасов"
                                "неверно"
                                "Алан Тьюринг"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Джон Мокли"  
                                "неверно"
                                "Алан Тьюринг"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest3Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Алан Тьюринг"
                                "верно"
                                $Team3Points += 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "Конрад Цузе"
                                "неверно"
                                "Алан Тьюринг"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "Джон Атанасов"
                                "неверно"
                                "Алан Тьюринг"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "Джон Мокли"  
                                "неверно"
                                "Алан Тьюринг"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest3Status = False
                                jump Round1
                    
                    label R2Cat3Quest4:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 400

                        leader "Вопрос за 400"
                        "Какой шведский фабрикант изобрел в 1896 году взрывчатое вещество динамит?"
                        if Turn == 1 :
                            menu: 
                                "Альфред Нобель":
                                    "верно"
                                    $OurTeamPoints += 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest4Status = False
                                    jump Round1 

                                "Роберт Оппенгеймер":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest4Status = False
                                    jump Round1 

                                "Эйнштейн":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest4Status = False
                                    jump Round1 

                                "Николла Тесла":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest4Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Альфред Нобель"
                                "верно"
                                $Team1Points += 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Роберт Оппенгеймер"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "Эйнштейн"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "Николла Тесла" 
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest4Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Альфред Нобель"
                                "верно"
                                $Team2Points += 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Роберт Оппенгеймер"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Эйнштейн"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Николла Тесла" 
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest4Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Альфред Нобель"
                                "верно"
                                $Team3Points += 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "Роберт Оппенгеймер"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "Эйнштейн"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "Николла Тесла" 
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest4Status = False
                                jump Round1

                    label R2Cat3Quest5:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 500

                        leader "Вопрос за 500"
                        "Отец атомной бомбы"
                        if Turn == 1 :
                            menu: 
                                "Роберт Оппенгеймер":
                                    "верно"
                                    $OurTeamPoints += 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest5Status = False
                                    jump Round1 

                                "Манфред фон Арденне":
                                    "неверно"
                                    "Роберт Оппенгеймер"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest5Status = False
                                    jump Round1 

                                "Тимофеев-Ресовский ":
                                    "неверно"
                                    "Роберт Оппенгеймер"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest5Status = False
                                    jump Round1 

                                "Отто Ган":    
                                    "неверно"
                                    "Роберт Оппенгеймер"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest5Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Роберт Оппенгеймер"
                                "верно"
                                $Team1Points += 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "Манфред фон Арденне"
                                "неверно"
                                "Роберт Оппенгеймер"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "Тимофеев-Ресовский "
                                "неверно"
                                "Роберт Оппенгеймер"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "Отто Ган"
                                "неверно"
                                "Роберт Оппенгеймер"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest5Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Роберт Оппенгеймер"
                                "верно"
                                $Team2Points += 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "Манфред фон Арденне"
                                "неверно"
                                "Роберт Оппенгеймер"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "Тимофеев-Ресовский "
                                "неверно"
                                "Роберт Оппенгеймер"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "Отто Ган"
                                "неверно"
                                "Роберт Оппенгеймер"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest5Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Роберт Оппенгеймер"
                                "верно"
                                $Team3Points += 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "Манфред фон Арденне"
                                "неверно"
                                "Роберт Оппенгеймер"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "Тимофеев-Ресовский "
                                "неверно"
                                "Роберт Оппенгеймер"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "Отто Ган"
                                "неверно"
                                "Роберт Оппенгеймер"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest5Status = False
                                jump Round1

                label Round2Cat4:

                    $ timez = 300
                    $ time_range = 300

                    $TeamCat = renpy.random.randint(1,5)
                    if R1Cat1Status==1 and TeamCat == 1:
                        $ marker = 'R2Cat4Quest1'

                    elif R1Cat2Status==1 and TeamCat == 2:
                        $ marker = 'R2Cat4Quest2'

                    elif R1Cat3Status==1 and TeamCat == 3:
                        $ marker = 'R2Cat4Quest3'

                    elif R1Cat4Status==1 and TeamCat == 4:
                        $ marker = 'R2Cat4Quest4'
                    
                    elif R1Cat4Status==1 and TeamCat == 5:
                        $ marker = 'R2Cat4Quest5'

                    if Turn == 1: 
                        gg "Программирование"
                        menu: 
                            "100" if R2Cat4Quest1Status == True:
                                jump R2Cat4Quest1

                            "200" if R2Cat4Quest2Status==1:
                                jump R2Cat4Quest2

                            "300" if R2Cat4Quest3Status==1:
                                jump R2Cat4Quest3

                            "400" if R2Cat4Quest4Status==1:
                                jump R2Cat4Quest4

                            "500" if R2Cat4Quest5Status==1:
                                jump R2Cat4Quest5

                    elif Turn == 2 : 
                        team1 "Программирование"
                        $Team1Qestion = renpy.random.randint(1,5)
                        if R2Cat4Quest1Status==1 and Team1Qestion == 1:
                            team1 "Вопрос за 100"
                            jump R2Cat4Quest1

                        elif R2Cat4Quest2Status==1 and Team1Qestion == 2:
                            team1 "Вопрос за 200"
                            jump R2Cat4Quest2

                        elif R2Cat4Quest3Status==1 and Team1Qestion == 3:
                            team1 "Вопрос за 300"
                            jump R2Cat4Quest3

                        elif R2Cat4Quest4Status==1 and Team1Qestion == 4:
                            team1 "Вопрос за 400"
                            jump R2Cat4Quest4

                        elif R2Cat4Quest5Status==1 and Team1Qestion == 5:
                            team1 "Вопрос за 500"
                            jump R2Cat4Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat4    

                    elif Turn == 3: 
                        team2 "Программирование"
                        $Team2Qestion = renpy.random.randint(1,5)
                        if R2Cat4Quest1Status==1 and Team1Qestion == 1:
                            team2 "Вопрос за 100"
                            jump R2Cat4Quest1

                        elif R2Cat4Quest2Status==1 and Team1Qestion == 2:
                            team2 "Вопрос за 200"
                            jump R2Cat4Quest2

                        elif R2Cat4Quest3Status==1 and Team1Qestion == 3:
                            team2 "Вопрос за 300"
                            jump R2Cat4Quest3

                        elif R2Cat4Quest4Status==1 and Team1Qestion == 4:
                            team2 "Вопрос за 400"
                            jump R2Cat4Quest4

                        elif R2Cat4Quest5Status==1 and Team1Qestion == 5:
                            team2 "Вопрос за 500"
                            jump R2Cat4Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat4

                    elif Turn == 4: 
                        team3 "Программирование"
                        $Team3Qestion = renpy.random.randint(1,5)
                        if R2Cat4Quest1Status==1 and Team1Qestion == 1:
                            team3 "Вопрос за 100"
                            jump R2Cat4Quest1

                        elif R2Cat4Quest2Status==1 and Team1Qestion == 2:
                            team3 "Вопрос за 200"
                            jump R2Cat4Quest2

                        elif R2Cat4Quest3Status==1 and Team1Qestion == 3:
                            team3 "Вопрос за 300"
                            jump R2Cat4Quest3

                        elif R2Cat4Quest4Status==1 and Team1Qestion == 4:
                            team3 "Вопрос за 400"
                            jump R2Cat4Quest4

                        elif R2Cat4Quest5Status==1 and Team1Qestion == 5:
                            team3 "Вопрос за 500"
                            jump R2Cat4Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round2Cat4
                    
                    label R2Cat4Quest1:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 100

                        leader "Вопрос за 100"
                        "Какая единица измерения не относится к измерению информации"
                        if Turn == 1 :
                            menu: 
                                "Герц":
                                    "верно"
                                    $OurTeamPoints += 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest1Status = False
                                    jump Round2 

                                "Килобит":
                                    "неверно"
                                    "Герц"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest1Status = False
                                    jump Round2 

                                "Петабайт":
                                    "неверно"
                                    "Герц"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest1Status = False
                                    jump Round2 

                                "Гигабайт":    
                                    "неверно"
                                    "Герц"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest1Status = False
                                    jump Round2 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Герц"
                                "верно"
                                $Team1Points += 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R2Cat4Quest1Status = False
                                jump Round2 
                            if Team1Answer == 2:
                                "Килобит"
                                "неверно"
                                "Герц"
                                $OurTeamPoints -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R2Cat4Quest1Status = False
                                jump Round2 
                            if Team1Answer == 3:
                                "Петабайт"
                                "неверно"
                                "Герц"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R2Cat4Quest1Status = False
                                jump Round2 
                            if Team1Answer == 4:
                                "Гигабайт"  
                                "неверно"
                                "Герц"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R2Cat4Quest1Status = False
                                jump Round2 

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Герц"
                                "верно"
                                $Team2Points += 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest1Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "Килобит"
                                "неверно"
                                "Герц"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest1Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "Петабайт"
                                "неверно"
                                "Герц"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest1Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "Гигабайт"  
                                "неверно"
                                "Герц"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest1Status = False
                                jump Round2 

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Герц"
                                "верно"
                                $Team3Points += 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest1Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "Килобит"
                                "неверно"
                                "Герц"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest1Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "Петабайт"
                                "неверно"
                                "Герц"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest1Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "Гигабайт"  
                                "неверно"
                                "Герц"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest1Status = False
                                jump Round2

                    label R2Cat4Quest2:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 200

                        leader "Вопрос за 200"
                        "Для чего был использован самый первый язык программирования "
                        if Turn == 1 :
                            menu: 
                                "Ткацкого станка":
                                    "верно"
                                    $OurTeamPoints += 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest2Status = False
                                    jump Round2 

                                "ЭВМ":
                                    "неверно"
                                    "Ткацкого станка"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest2Status = False
                                    jump Round2 

                                "Шифровальная машина":
                                    "неверно"
                                    "Ткацкого станка"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest2Status = False
                                    jump Round2 

                                "Радио приёмник":    
                                    "неверно"
                                    "Ткацкого станка"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest2Status = False
                                    jump Round2 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Ткацкого станка"
                                "верно"
                                $Team1Points += 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest2Status = False
                                jump Round2 
                            if Team1Answer == 2:
                                "ЭВМ"
                                "неверно"
                                "Ткацкого станка"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest2Status = False
                                jump Round2 
                            if Team1Answer == 3:
                                "Шифровальная машина"
                                "неверно"
                                "Ткацкого станка"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest2Status = False
                                jump Round2 
                            if Team1Answer == 4:
                                "Радио приёмник"  
                                "неверно"
                                "Ткацкого станка"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest2Status = False
                                jump Round2

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Ткацкого станка"
                                "верно"
                                $Team2Points += 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest2Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "ЭВМ"
                                "неверно"
                                "Ткацкого станка"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest2Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "Шифровальная машина"
                                "неверно"
                                "Ткацкого станка"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest2Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "Радио приёмник"  
                                "неверно"
                                "Ткацкого станка"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest2Status = False
                                jump Round2

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Ткацкого станка"
                                "верно"
                                $Team3Points += 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest2Status = False
                                jump Round2 
                            if Team3Answer == 2:
                                "ЭВМ"
                                "неверно"
                                "Ткацкого станка"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest2Status = False
                                jump Round2 
                            if Team3Answer == 3:
                                "Шифровальная машина"
                                "неверно"
                                "Ткацкого станка"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest2Status = False
                                jump Round2 
                            if Team3Answer == 4:
                                "Радио приёмник"  
                                "неверно"
                                "Ткацкого станка"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest2Status = False
                                jump Round2

                    label R2Cat4Quest3:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 300

                        leader "Вопрос за 300"
                        "C# является языком программирования"
                        if Turn == 1 :
                            menu: 
                                "1 поколения":
                                    "неверно"
                                    "3 поколения"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest3Status = False
                                    jump Round2 

                                "2 поколения":
                                    "неверно"
                                    "3 поколения"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest3Status = False
                                    jump Round2 

                                "3 поколения":
                                    "верно"
                                    $OurTeamPoints += 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest3Status = False
                                    jump Round2

                                "4 поколения":    
                                    "неверно"
                                    "3 поколения"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest3Status = False
                                    jump Round2 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "1 поколения"
                                "неверно"
                                "3 поколения"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest3Status = False
                                jump Round2 
                            if Team1Answer == 2:
                                "2 поколения"
                                "неверно"
                                "3 поколения"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest3Status = False
                                jump Round2 
                            if Team1Answer == 3:
                                "3 поколения"
                                "верно"
                                $Team1Points += 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest3Status = False
                                jump Round2 
                            if Team1Answer == 4:
                                "4 поколения"   
                                "неверно"
                                "3 поколения"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest3Status = False
                                jump Round2

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "1 поколения"
                                "неверно"
                                "3 поколения"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest3Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "2 поколения"
                                "неверно"
                                "3 поколения"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest3Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "3 поколения"
                                "верно"
                                $Team2Points += 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest3Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "4 поколения"   
                                "неверно"
                                "3 поколения"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest3Status = False
                                jump Round2

                        elif Turn == 4 : 

                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "1 поколения"
                                "неверно"
                                "3 поколения"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest3Status = False
                                jump Round2 
                            if Team3Answer == 2:
                                "2 поколения"
                                "неверно"
                                "3 поколения"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest3Status = False
                                jump Round2 
                            if Team3Answer == 3:
                                "3 поколения"
                                "верно"
                                $Team3Points += 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest3Status = False
                                jump Round2 
                            if Team3Answer == 4:
                                "4 поколения"   
                                "неверно"
                                "3 поколения"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest3Status = False
                                jump Round2
                    
                    label R2Cat4Quest4:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 400

                        leader "Вопрос за 400"
                        "Язык с решёткой"
                        if Turn == 1 :
                            $ answer = renpy.input()

                            if anwer == "C#":

                                $OurTeamPoints += 500  
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest5Status = False
                                jump Round2

                            else:
                                
                                $OurTeamPoints -= 500  
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest5Status = False
                                jump Round2 

                        elif Turn == 2 : 
                            "C#"
                            "верно"
                            $Team1Points += 400
                            if Turn == 2 :
                                $ Turn = 3
                            $ R2Cat4Quest4Status = False
                            jump Round2 

                        elif Turn == 3 : 
                            "C#"
                            "верно"
                            $Team2Points += 400
                            if Turn == 3 :
                                $ Turn = 4
                            $ R2Cat4Quest4Status = False
                            jump Round2 

                        elif Turn == 4 : 
                            "C#"
                            "верно"
                            $Team2Points += 400
                            if Turn == 3 :
                                $ Turn = 4
                            $ R2Cat4Quest4Status = False
                            jump Round2 

                    label R2Cat4Quest5:

                        $ timez = 300
                        $ time_range = 300
                        $ marker = 'costing'

                        $ cost = 500

                        leader "Вопрос за 500"
                        "Как добавить в массив новое число"
                        if Turn == 1 :
                            menu: 
                                "Создать новый массив":
                                    "верно"
                                    $OurTeamPoints += 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest5Status = False
                                    jump Round2 

                                "Просто прибавить число":
                                    "неверно"
                                    "Создать новый массив"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest5Status = False
                                    jump Round2 

                                "Обновить массив":
                                    "неверно"
                                    "Создать новый массив"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest5Status = False
                                    jump Round2 

                                "Создасть список":    
                                    "неверно"
                                    "Создать новый массив"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest5Status = False
                                    jump Round2 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,4)
                            if Team1Answer == 1:
                                "Создать новый массив"
                                "верно"
                                $Team1Points += 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest5Status = False
                                jump Round2 
                            if Team1Answer == 2:
                                "Просто прибавить число"
                                "неверно"
                                "Создать новый массив"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest5Status = False
                                jump Round2 
                            if Team1Answer == 3:
                                "Обновить массив"
                                "неверно"
                                "Создать новый массив"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest5Status = False
                                jump Round2 
                            if Team1Answer == 4:
                                "Создасть список"    
                                "неверно"
                                "Создать новый массив"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest5Status = False
                                jump Round2

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,4)
                            if Team2Answer == 1:
                                "Создать новый массив"
                                "верно"
                                $Team2Points += 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest5Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "Просто прибавить число"
                                "неверно"
                                "Создать новый массив"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest5Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "Обновить массив"
                                "неверно"
                                "Создать новый массив"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest5Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "Создасть список"    
                                "неверно"
                                "Создать новый массив"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest5Status = False
                                jump Round2

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,4)
                            if Team3Answer == 1:
                                "Создать новый массив"
                                "верно"
                                $Team3Points += 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest5Status = False
                                jump Round2 
                            if Team3Answer == 2:
                                "Просто прибавить число"
                                "неверно"
                                "Создать новый массив"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest5Status = False
                                jump Round2 
                            if Team3Answer == 3:
                                "Обновить массив"
                                "неверно"
                                "Создать новый массив"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest5Status = False
                                jump Round2 
                            if Team3Answer == 4:
                                "Создасть список"    
                                "неверно"
                                "Создать новый массив"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest5Status = False
                                jump Round2

            label Final:

                if OurTeamPoints > Team1Points and OurTeamPoints > Team2Points and OurTeamPoints > Team3Points:
                    
                    leader "Поздравляем первую команду с победой! Выходите для получения призов"

                elif Team1Points > OurTeamPoints and Team1Points > Team2Points and Team1Points > Team3Points:

                    if OurTeamPoints > Team2Points and OurTeamPoints > Team3Points:

                        leader "Поздравляем первую команду с вторым местом! Выходите для получения призов"

                    else:
                        
                        gg "Да ладно вам ребят, ну в этот раз не выиграли, зато всегда есть шанс выиграть в следующий раз, а сегодня зато засветились."

                        Member "По факту, но все равно грустно, я мог дома посидеть домашку поделать."

                        gg "Домашку??? Кому ты врешь в доту бы фигачил или кс."

                        Member "Пхех, подловил меня. "

                elif Team2Points > OurTeamPoints and Team2Points > Team1Points and Team2Points > Team3Points:
                    
                    if OurTeamPoints > Team1Points and OurTeamPoints > Team3Points:

                        leader "Поздравляем первую команду с вторым местом! Выходите для получения призов"

                    else:
                        
                        gg "Да ладно вам ребят, ну в этот раз не выиграли, зато всегда есть шанс выиграть в следующий раз, а сегодня зато засветились."

                        Member "По факту, но все равно грустно, я мог дома посидеть домашку поделать."

                        gg "Домашку??? Кому ты врешь в доту бы фигачил или кс."

                        Member "Пхех, подловил меня. "

                elif Team3Points > OurTeamPoints and Team3Points > Team2Points and Team3Points > Team1Points:
                    
                    if OurTeamPoints > Team2Points and OurTeamPoints > Team1Points:

                        leader "Поздравляем первую команду с вторым местом! Выходите для получения призов"

                    else:
                        
                        gg "Да ладно вам ребят, ну в этот раз не выиграли, зато всегда есть шанс выиграть в следующий раз, а сегодня зато засветились."

                        Member "По факту, но все равно грустно, я мог дома посидеть домашку поделать."

                        gg "Домашку??? Кому ты врешь в доту бы фигачил или кс."

                        Member "Пхех, подловил меня. "

        label AfterFinal:

            scene iritenterevening
            with Fade(0.5,0.5,1)

            voice "После мероприятия стоит направиться домой и наш герой с этим согласен"

            scene busstop
            with Fade(1,0.7,1.7)
            scene busonstop
            with Fade(0.5,0.5,1)
            pause(2)

            scene ggroom
            with Fade(0.5,0.5,1)

            gg "Ну что, спокойной мне ночи"

            scene blackscreen
            with Fade(0.5,0.5,1)
