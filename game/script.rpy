# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define gg = Character('NoName', color="#b7d436")
define voice = Character('Разказчик', color="#b7d436")
define Kabak = Character('Макс Кабак(Самый сексуальный мужчина)', color='#b14f0e')
define Kris = Character('Матерь Кристина', color = '#b10e44')
define Fahta = Character('Вахтёр', color = '#b80e0e')
define All = Character('Все', color = '#b7d436')
define Prepod = Character('Преподаватель', color = "#ac2d06")
define leader = Character('Ведущий', color = "#ac2d06")
define Member = Character('Наш чел', color = "#ac2d06")
define team1 = Character('Стрелки', color = "#ac2d06")
define team2 = Character('Прилагательные', color = "#ac2d06")
define team3 = Character('Бикини Ботом', color = "#ac2d06")

# Игра начинается здесь:
label start:

    $Money = 500 #Кол-во денег в рублях
    $Grade = 0 #Успеваемость в процентах 50 = 100%  0 = 50% -50 = 0% при -10 и ниже блок выборов
    $GradeMod = 1 #Множитель успеваемости. Единождый бонус
    $Reputation = 0 #Репутация
    $KabakReputation = 0 #Репутация с максом
    $KrisReputation = 0 #Репутация с кристиной
    label Day0:
        label WAKE_UP_SAMURAI:
            scene blackScreen

            voice "Давайте знакомиться. Я ваш путеводитель по мыслям этого...."

            voice "Абалдуя....."

            voice "Да, так подойдёт. Это наш ГГ(имя будет или не будет позже), и он почти проспал свой первый день в институте"

            scene ggRoomBed
            with Fade(0.5,0.5,1)

            gg "Да *****, почему я не завел несколько будильников? Нужно спешить в Урфу, не слишком-то хочется вылететь в первый день"

        label Waiting_Bus:
            scene busStop
            with Fade(1,0.7,1.7)

            voice "ГГ приходит на остановку. Как бы то странно не было, но на ней было немноголюдно, несмотря на час пик."

            voice "Наш герой принимается ждать автобус."

            gg "Надеюсь я успею"

            scene busOnStop
            with Fade(0.5,0.5,1)
            pause(2)

        label Forward_UrFU:

            scene UrFUenter
            with Fade(0.5,0.5,1)

            gg "*Так, и где мои одногрупники*"

            scene Goslingtable
            with Fade(0.5,0.5,1)

            pause(2)

            scene Tolpa
            with Fade(0.5,0.5,1)

            show kabak1

            Kabak "ГГ, ты чуть не опоздал на первое сентября"

            gg "Извините пожалуйста, будильник не сработал"

            Kabak "Я надеюсь такого не повториться"

            Kabak "верно ведь говорю?"

            gg "Да, конечно, этого больше не повториться, мамой клянусь"

            Kabak "Вот и отлично"

            voice "После разагавора со своим наставником, наш герой начал искать новые знакомства"

            voice "Спустя энное количество времени их всех отправляют во внутрь. ГГ нашёл себе новых друзей"

            voice "И самим собой 'Запомнил' имена своих одногрупников. Благо он запомнил своих наставников, а то его бы армяне уграли"

        label Studik_for_everyone:
            scene RadAud
            with Fade(1,1,2)

            voice "После провёденного инструктажа, всем пекусам выдали их студики"

            scene SdutFoto
            with Fade(0.5,0.5,1)

            gg "Не. Всё-таки красивые у нас студики"

        label Profsoyz:
            scene blackScreen
            with Fade(1,1,2)

            voice "Сейчас наш главный герой направляеться в коворкинг"

            voice "Зачем? Ему не сказали"

            scene coworking
            with Fade(0.5,0.5,1)

            show Kris1

            Kris "Внимание все, Сечас будет информация про проф союз."

            voice "Дальше была долгая реклама проф союза"
            voice "Но мы это опустим, заметив что это действительно полезно для ГГ и что даёт щикарный мерч"

            hide Kris1

            menu:
                voice"Так что, вступаем?"
                "Да":
                    jump  Profsoyz_choise_yes
                "Нет":
                    jump Prof_chos_NO
        label Profsoyz_choise_yes:
        
            gg "Думаю от этого не убудет"
            $Reputation += 15
            jump scene1

        label Prof_chos_NO:
            menu:
                #play music "Enter.mp4"
                "Всё-таки вступаем?":
                    jump Profsoyz_choise_yes
                "Ну его":
                    jump Prof_chos_NO_NO

        label Prof_chos_NO_NO:
            gg "Да ну его. Какой мне от этого смысл"
            voice "Как ни странно, но наш Абалдуй почуствовал как его окутали злые взгляды"
            $Reputation -= 15 
            jump scene1  

        label scene1:
        
            show kabak1 at right

            show Kris1 at left

            Kabak "Ну мы всё вам всё в приципе рассказали"

            Kris "А теперь идём на ВАШ первый в уральском федеральном"

            hide Kris1
            hide kabak1

            voice "Наш герой отправился на ярмарку. Чтож не будем ему мешать"

            scene Guk
            with Fade(1,1,2)

            scene GukVejer
            with Fade(1,1,2)

            gg "Ого уже вечер. Ладно поцаны я поду. До встречи"

            scene ObhagaVejer
            with Fade(1,1,2)

            scene ggRoom
            with Fade(1,2,3)

            gg "Мда...."

            gg "Чую будет весело"

            gg "Ладно. Учёба учёбой, а дота по расписанию"

            scene ggRoomComp
            with Fade(0.5,0.5,1)

            scene blackScreen
            with Fade(0.5,0.5,1)

            "Спустя одну слитую катку"

            scene ggRoomComp
            with Fade(0.5,0.5,1)

            gg "Ладно я щас злой. Лучше на боковую"

            scene ggRoomBed
            with Fade(0.5,0.5,1)
  
    label Day1:

        $ModeusHelp = 0

        scene Day1
        with Fade(1,1,2)

        pause(2)

        label modeusHelp:

            scene ggRoomComp
            with Fade(0.5,0.5,1)

            gg "Черт, сегодня выбор в каком-то модеусе"

            gg "Хммммммммммммммммммммммммммммммммммммм"

            gg "Стоит ли мне к ниму подготовиться?"

            menu:
                "Написать самому сексуальному мужику":
                    jump Sex
                "Дота ван лав":
                    jump noSex

            label Sex:

                gg "Думаю стоит написать Максу"

                gg "Надуюсь он сможет мне помочь"

                voice "Неужто наш Абалдуй решил взяться за ум........................................ брух"

                scene ggRoomCompVK
                with Fade(0.5,0.5,1)

                "Текс в переписке"

                gg "Дарова Макс, посабишь с модеусом заморским"

                Kabak "Привет, да помогу, не проблема"

                scene Modeus
                with Fade(0.2,0.2,0.4)  
        
                Kabak "На главной странице ты сможешь выбрать себе расписание, и конечно смотреть свое расписание "

                scene ModeusChoose
                with Fade(0.2,0.2,0.4)  

                Kabak "Во время выбора тебе будет предоставлена возможность выбрать преподавателя и время, для комфортной учебы."

                scene ggRoomCompVK
                with Fade(0.2,0.2,0.4)

                Kabak "Также, щас я скину тебе плюшку, чтоб ты понимал, какие учителя могут задушить, а какие нет."

                $ModeusHelp = 1

                "Тебе пришёл ворд документ от Кабака, радуйся"

                gg "Ахринеть, спасибо Максимка"

                Kabak "Удачи на голодных играх)))"

                scene ggRoomComp
                with Fade(0.2,0.2,0.4)

                gg "Думаю надо заранее составить расписание"  

                jump ModeusChoosing

            label noSex:

                voice "Как я и думал, для нашего героя амереканская дота важнее диплома" 

                scene ggRoomCompDs
                with Fade(0.2,0.2,0.4)

                gg "Ну что поцаны, время турбо войнов"

                play sound "audio/one-eternity-later.mp3"
                scene 1:
                    yalign 0.5
                    xalign 0.5
                with Fade(0.2,0.2,0.4)

                pause(1)

                scene ggRoomCompDs
                with Fade(0.2,0.2,0.4)

                gg "Ладно ребятки, у меня щас какой-то там модеус. Скоро вернусь"

                $ModeusHelp = 0

                jump ModeusChoosing

        $ModeusChoose = 0
        label ModeusChoosing:

            scene ModeusChoose
            with Fade(0.2,0.2,0.4)

            voice "Открыв модеус и точное время Екатиринбурга, наш герой ждёт старта"

            "На часах 23:55"

            gg "Осталась всего 5 минут"

            "Спустя 4 минуты и 57 секунд"

            gg "23:59:57.....58.....59......00:00:00"

            gg "Пора"
            menu:
                "Использовать заранее сделаное расписание" if ModeusHelp == 1:
                    $ModeusChoose = 1
                "ДУмать на ходу":
                    $ModeusChoose = 0
            
            pause(1.5)

            voice "Наш безимянный впал в ступор. Не будем ему мешать пусть отдохнёт, ведь завтра надинаеться учёба"

    label Day2:

        $Ending = 0

        scene Day2
        with Fade(1,1,2)

        pause(2)

        label Turn:
            
            scene IritEnter
            with Fade(0.5,0.5,1)

            gg "Чёртовы пробки, не успеваю"

            show fahta1

            Fahta "А ну стоять. Студ билет показал!"

            menu: 
                gg "Блин, где этот студик"
                "Показать":
                    jump TurnGood
                "Нафиг надо":
                    jump TurnBad
            
            label TurnGood:

                gg "Вот"

                show fahta2

                Fahta "А, первокурсник, ну хорошо, проходи."

                Fahta "В следующий раз доставай студенческий заранее, чтобы других не задерживать"

                gg "Хорошо, учту"

                hide fahta2

                voice "Когда наш Абалдуй нашёл нужную аудиторию, он заметил что препода ещё нет и садиться как ни в чём не бывало"

                $Grade += 10

                $Ending = 1

                jump Dinner

            label TurnBad:

                gg "*Нахер надо, щас в толпе затеряюсь и всё ок будет*"

                voice "Уфффф, турнекетом прямо по ногам. Наверно больно"

                show fahta1

                Fahta "КУДА ПОЛЕЗ, А НУС ИДИ СЮДА"

                Fahta "Всё идём в деканат"

                hide fahta1

                scene dekonat
                with Fade(0.2,0.2,0.4)

                gg "Может не нада, я первый день. Я на пару опаздываю"

                Fahta "Первый, не первый, мне все-равно, пошли"

                scene blackScreen
                with Fade(0.2,0.2,0.4)

                voice "После ВЕСЬМА поучительной беседы гг отпускают"

                voice "Из-за данного инцедента по шапке прилетоло не только ему но его наставникам"

                voice "Да ещё и пару пропустил"

                $Reputation -=5
                $Grade -=10

                $Ending = 0

                jump Dinner

            label Dinner:

                scene IritSiteEnter
                with Fade(0.5,0.5,1)

                gg "*Щас большак, время есть. Может сходить пообедать?*"

                voice "Наш герой направился в столовую"

                scene KIchen
                with Fade(0.5,0.5,1)

                menu:
                    gg "*Чтобы выбрать*"
                    "Перекус":
                        jump Butter
                    "Полноценный обед" if Money >= 200:
                        jump Obid
            
                label Butter:

                    gg "Ладно бутеры с чайком подут"

                    jump Audit
                
                label Obid:

                    gg "Раз время есть, стоит плотненько пообедать"

                    $Money -= 200

                    $GradeMod = 1.25

                    jump Audit

        label Audit:

            scene ProgAudit
            with Fade(1,1,2)

            show prepod1

            Prepod "Здравствуйте, первокурсники, добро пожаловать в лучший институт нашего ВУЗа."

            Prepod "Отсюда начнется ваша дорога во взрослую и осмысленную жизнь..."

            hide prepod1

            voice "Тут нужен материал"

            gg "*Яре яре. Не думал что программирование такое интересное! Теперь это будет мой любимый предмет*"

            $Grade += 10 * GradeMod

            $GradeMod = 1
            
            show prepod1
            
            Prepod "На этом закончим, можете быть свободны"

            All "Спасибо, до свидания"

        label AfterStuding1:
            
            scene IritEnterevening
            with Fade(1,1,2)

            gg "*Ну вот и закончился мой первый учебный день в Уральском Федеральном. Надеюсь, здесь я исполню все свои желания*"

            scene busStop
            with Fade(1,0.7,1.7)
            scene busOnStop
            with Fade(0.5,0.5,1)
            pause(2)

    label Day3:
        
        scene Day3
        with Fade(1,1,2)

        pause(2)

        label Raspisanie:
            
            scene ggRoomBed
            with Fade(0.5,0.5,1)

            gg "Да уж, ну и ну, столько всего по программированию позадавали."

            gg "Думал, не успею все вовремя сделать, в следующий раз не буду домашку откладывать, не очень хочется такое повторять"

            scene ggRoomComp
            with Fade(0.5,0.5,1)

            gg "Так, какие у меня сегодня занятия? Посмотрим"

            scene ggRoomCompRsp
            with Fade(0.5,0.5,1)

            gg "Так, история, прога и математика значит. Ну, не так все плохо, могло быть и больше пар."

            gg "Ладно. Пора идти"

        label Fhod:

            scene IritEnter
            with Fade(0.5,0.5,1)

            if Ending == 1:

                voice "Наш Абалдуй оказался сообразительным раз решил не выёжываться"

            elif Ending == 0:

                Fahta "Предъяви студенческий."    

                "Вы показываете свой студенческий билет" 

                Fahta "А, так это ты! А где твой электронный пропуск?"  

                gg "Какой пропуск?" 

                Fahta "Электронный пропуск для турникетов где? Нет, значит свободен"

                gg "Да подождите! Нам их не выдавали еще"

                Fahta "Уверен?"

                gg "Да, посмотрите, я только 1 курс"

                voice "Вау как напряжно"

                Fahta "Хммммммммм.... Ну проходи, не задерживай очередь!"

        label History:

            scene RadAud
            with Fade(0.5,0.5,1)

            show prepod2

            voice "Как можно заметить для нашего Абалдуя истроия весьма скучна. Ему точно НЕ понадобяться эти “никому не нужные” даты"

            gg "Ну какая история! Я пришел в ВУЗ, чтобы выучиться на программиста, причем тут история, ладно математика, физ-ра для поддержания образа жизни, но история..."

            Prepod "А теперь будьте добры ответить на мои вопросы, вы же внимательно меня слушали?"

            gg "а...."

            Prepod "Итак, первый вопрос..."

            gg "Что же мне делать?"

            play sound "audio/MirAnimals.mp3"

            voice "Вы можете видеть как один из студентов пытаеться спрятаться от Преподавателя. Он выглядит напуганным и стараеться сидеть тихо"
            
            voice "Тут один из его одногруппников поднимает руку. "

            voice "И наш герой понимает, что это его спасёт. Студент отвечает, а заним второй, третий и так далее"

            stop sound

            hide prepod2

            gg "Фух, вроде бы прокатило. Все-таки придется учить историю, если захочу хорошую оценку"


        label ProgaDay3:
            
            scene Audit
            with Fade(0.5,0.5,1)

            show prepod1

            Prepod "Уважаемые студенты, сегодня помимо обычной лекции мы напишем небольшой тест, чтобы закрепить ваши знания."

            Prepod "Не волнуйтесь, он не будет сложным, если вы, конечно, учились на моих занятиях, а не валяли дурака."

            $Result = 0

            "Ставьте тест сюда"

            #if Resutl >=8:
            #    
            #   gg "Боже, этот тест просто малыш"
            #
            #    $Grade += 10 *1.25

            #elif Result >=6:
                
            #    gg "Тест был нормальным, хорошо, что я все это учил"

            #    $Grade += 10

            #elif Result <6:
                
            #    gg "Да уж, как я мог так плохо написать этот чертов тест?"

            #    $Grade -=10

            hide prepod1

            voice "После теста наш герой отправился на математику"

            voice "И бла бла бла"

            voice "Это скучно. Давайте лучше пойдём в магаз"

        label Producti24:

            scene Shop
            with Fade(0.5,0.5,1)

            voice "Так то лучше"

            gg "Столько всего. Так, чего бы мне взять?"

            menu:
                "Выбрать богато" if Money >=150:
                    jump RichBitch
                "Выбрать много" if Money >=450:
                    jump ManyMany
                "Идти домой и плакать":
                    jump SadBoi

            label RichBitch:

                gg "Ладно возмём что-нибуть повкуснее. Может фильмец посмотрю"

                $Money -= 150
                

            label ManyMany:

                gg "Ладно возмём еды на недельку"

                $Money -= 450   

            label SadBoi:

                gg "Эхххх, до стипы ещё долеко. Пойду фотосинтезировать"

            gg "Ладно, несмотря на всё, пора домой"   

            voice "После этого наш Абалдуй направился домой. Пожелаем ему спокойной ночи" 

            scene blackScreen
            with Fade(0.5,0.5,1)
            
            "[Reputation] [Money] [Grade]"

    label Day4:
        
        scene Day4
        with Fade(1,1,2)

        pause(2)

        label SvoiaIgra:
   
            $ Turn = 1

            $ OurTeamPoints = 0
            $ Team1Points = 0
            $ Team2Points = 0
            $ Team3Points = 0

            $ R1Categories = 4
            $ R2Categories = 4
            $ R3Categories = 4
                
                
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

            $ R1Cat1Status = True
            $ R1Cat1Quest1Status = True
            $ R1Cat1Quest2Status = True
            $ R1Cat1Quest3Status = True
            $ R1Cat1Quest4Status = True             
            $ R1Cat1Quest5Status = True

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

            $ R3Cat1Status = True
            $ R3Cat1Quest1Status = True
            $ R3Cat1Quest2Status = True
            $ R3Cat1Quest3Status = True
            $ R3Cat1Quest4Status = True             
            $ R3Cat1Quest5Status = True

            $ R3Cat2Status = True
            $ R3Cat2Quest1Status = True
            $ R3Cat2Quest2Status = True
            $ R3Cat2Quest3Status = True
            $ R3Cat2Quest4Status = True             
            $ R3Cat2Quest5Status = True

            $ R3Cat3Status = True
            $ R3Cat3Quest1Status = True
            $ R3Cat3Quest2Status = True
            $ R3Cat3Quest3Status = True
            $ R3Cat3Quest4Status = True             
            $ R3Cat3Quest5Status = True

            $ R3Cat4Status = True
            $ R3Cat4Quest1Status = True
            $ R3Cat4Quest2Status = True
            $ R3Cat4Quest3Status = True
            $ R3Cat4Quest4Status = True             
            $ R3Cat4Quest5Status = True

            

            label Round1:
                

                if R1Categories == 1:
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
                        "Категория 1" if R1Cat1Status == True:
                            jump Round1Cat1
                        "Категория 2" if R1Cat2Status == True:
                            jump Round1Cat2
                        "Категория 3" if R1Cat2Status == True:
                            jump Round1Cat3
                        "Категория 4" if R1Cat2Status == True:
                            jump Round1Cat4
                    
 
                label Round1Cat1:
                    
                    if Turn == 1: 
                        gg "Категория 1"
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
                        team1 "Категория 1"
                        $Team1Qestion = renpy.random.randint(1,6)
                        if R1Cat1Quest1Status==1 and Team1Qestion == 1:
                            team1 "Quest1"
                            jump R1Cat1Quest1

                        elif R1Cat1Quest2Status==1 and Team1Qestion == 2:
                            team1 "Quest2"
                            jump R1Cat1Quest2

                        elif R1Cat1Quest3Status==1 and Team1Qestion == 3:
                            team1 "Quest3"
                            jump R1Cat1Quest3

                        elif R1Cat1Quest4Status==1 and Team1Qestion == 4:
                            team1 "Quest4"
                            jump R1Cat1Quest4

                        elif R1Cat1Quest5Status==1 and Team1Qestion == 5:
                            team1 "Quest5"
                            jump R1Cat1Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat1    

                    elif Turn == 3: 
                        team2 "Категория 1"
                        $Team1Qestion = renpy.random.randint(1,6)
                        if R1Cat1Quest1Status==1 and Team1Qestion == 1:
                            team2 "Quest1"
                            jump R1Cat1Quest1

                        elif R1Cat1Quest2Status==1 and Team1Qestion == 2:
                            team2 "Quest2"
                            jump R1Cat1Quest2

                        elif R1Cat1Quest3Status==1 and Team1Qestion == 3:
                            team2 "Quest3"
                            jump R1Cat1Quest3

                        elif R1Cat1Quest4Status==1 and Team1Qestion == 4:
                            team2 "Quest4"
                            jump R1Cat1Quest4

                        elif R1Cat1Quest5Status==1 and Team1Qestion == 5:
                            team2 "Quest5"
                            jump R1Cat1Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat1 

                    elif Turn == 4: 
                        team3 "Категория 1"
                        $Team1Qestion = renpy.random.randint(1,6)
                        if R1Cat1Quest1Status==1 and Team1Qestion == 1:
                            team3 "Quest1"
                            jump R1Cat1Quest1

                        elif R1Cat1Quest2Status==1 and Team1Qestion == 2:
                            team3 "Quest2"
                            jump R1Cat1Quest2

                        elif R1Cat1Quest3Status==1 and Team1Qestion == 3:
                            team3 "Quest3"
                            jump R1Cat1Quest3

                        elif R1Cat1Quest4Status==1 and Team1Qestion == 4:
                            team3 "Quest4"
                            jump R1Cat1Quest4

                        elif R1Cat1Quest5Status==1 and Team1Qestion == 5:
                            team3 "Quest5"
                            jump R1Cat1Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat1 
                    
                    label R1Cat1Quest1:

                        leader "Вопрос за 100"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest1Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest1Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest1Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest1Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat1Quest1Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $OurTeamPoints -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat1Quest1Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat1Quest1Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat1Quest1Status = False
                                jump Round1 

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest1Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest1Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest1Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest1Status = False
                                jump Round1 

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest1Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest1Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest1Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest1Status = False
                                jump Round1

                    label R1Cat1Quest2:

                        leader "Вопрос за 200"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest2Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest2Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest2Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest2Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest2Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest2Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest2Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest2Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest2Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest2Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest2Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest2Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest2Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest2Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest2Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest2Status = False
                                jump Round1

                    label R1Cat1Quest3:

                        leader "Вопрос за 300"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest3Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest3Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest3Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest3Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest3Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest3Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest3Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest3Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest3Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest3Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest3Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest3Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest3Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest3Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest3Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest3Status = False
                                jump Round1
                    
                    label R1Cat1Quest4:

                        leader "Вопрос за 400"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest4Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest4Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest4Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat1Quest4Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest4Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest4Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest4Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat1Quest4Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                "ответ"
                                $Team2Points += 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest4Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest4Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest4Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat1Quest4Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest4Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest4Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest4Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat1Quest4Status = False
                                jump Round1

                    label R1Cat1Quest5:

                        leader "Вопрос за 500"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ Cat1Quest5Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ Cat1Quest5Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ Cat1Quest5Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ Cat1Quest5Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ Cat1Quest5Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ Cat1Quest5Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ Cat1Quest5Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ Cat1Quest5Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ Cat1Quest5Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ Cat1Quest5Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ Cat1Quest5Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ Cat1Quest5Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ Cat1Quest5Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ Cat1Quest5Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ Cat1Quest5Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ Cat1Quest5Status = False
                                jump Round1

                label Round1Cat2:
                    
                    if Turn == 1: 
                        gg "Категория 2"
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
                        team1 "Категория 2"
                        $Team1Qestion = renpy.random.randint(1,6)
                        if R1Cat2Quest1Status==1 and Team1Qestion == 1:
                            team1 "Quest1"
                            jump R1Cat2Quest1

                        elif R1Cat2Quest2Status==1 and Team1Qestion == 2:
                            team1 "Quest2"
                            jump R1Cat2Quest2

                        elif R1Cat2Quest3Status==1 and Team1Qestion == 3:
                            team1 "Quest3"
                            jump R1Cat2Quest3

                        elif R1Cat2Quest4Status==1 and Team1Qestion == 4:
                            team1 "Quest4"
                            jump R1Cat2Quest4

                        elif R1Cat2Quest5Status==1 and Team1Qestion == 5:
                            team1 "Quest5"
                            jump R1Cat2Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat2    

                    elif Turn == 3: 
                        team2 "Категория 2"
                        $Team2Qestion = renpy.random.randint(1,6)
                        if R1Cat2Quest1Status==1 and Team1Qestion == 1:
                            team2 "Quest1"
                            jump R1Cat2Quest1

                        elif R1Cat2Quest2Status==1 and Team1Qestion == 2:
                            team2 "Quest2"
                            jump R1Cat2Quest2

                        elif R1Cat2Quest3Status==1 and Team1Qestion == 3:
                            team2 "Quest3"
                            jump R1Cat2Quest3

                        elif R1Cat2Quest4Status==1 and Team1Qestion == 4:
                            team2 "Quest4"
                            jump R1Cat2Quest4

                        elif R1Cat2Quest5Status==1 and Team1Qestion == 5:
                            team2 "Quest5"
                            jump R1Cat2Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat2

                    elif Turn == 4: 
                        team3 "Категория 2"
                        $Team1Qestion = renpy.random.randint(1,6)
                        if R1Cat2Quest1Status==1 and Team1Qestion == 1:
                            team3 "Quest1"
                            jump R1Cat2Quest1

                        elif R1Cat2Quest2Status==1 and Team1Qestion == 2:
                            team3 "Quest2"
                            jump R1Cat2Quest2

                        elif R1Cat2Quest3Status==1 and Team1Qestion == 3:
                            team3 "Quest3"
                            jump R1Cat2Quest3

                        elif R1Cat2Quest4Status==1 and Team1Qestion == 4:
                            team3 "Quest4"
                            jump R1Cat2Quest4

                        elif R1Cat2Quest5Status==1 and Team1Qestion == 5:
                            team3 "Quest5"
                            jump R1Cat2Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat2
                    
                    label R1Cat2Quest1:

                        leader "Вопрос за 100"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest1Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest1Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest1Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest1Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat2Quest1Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $OurTeamPoints -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat2Quest1Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat2Quest1Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat2Quest1Status = False
                                jump Round1 

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat2Quest1Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat2Quest1Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat2Quest1Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat2Quest1Status = False
                                jump Round1 

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat2Quest1Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat2Quest1Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat2Quest1Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat2Quest1Status = False
                                jump Round1

                    label R1Cat2Quest2:

                        leader "Вопрос за 200"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest2Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest2Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest2Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest2Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ Cat2Quest2Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ Cat2Quest2Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ Cat2Quest2Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ Cat2Quest2Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ Cat2Quest2Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ Cat2Quest2Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ Cat2Quest2Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ Cat2Quest2Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ Cat2Quest2Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ Cat2Quest2Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ Cat2Quest2Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ Cat2Quest2Status = False
                                jump Round1

                    label R1Cat2Quest3:

                        leader "Вопрос за 300"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest3Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest3Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest3Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest3Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat2Quest3Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat2Quest3Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat2Quest3Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat2Quest3Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat2Quest3Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat2Quest3Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat2Quest3Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat2Quest3Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat2Quest3Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat2Quest3Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat2Quest3Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat2Quest3Status = False
                                jump Round1
                    
                    label R1Cat2Quest4:

                        leader "Вопрос за 400"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest4Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest4Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest4Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest4Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat2Quest4Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat2Quest4Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat2Quest4Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat2Quest4Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat2Quest4Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat2Quest4Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat2Quest4Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat2Quest4Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat2Quest4Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat2Quest4Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat2Quest4Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat2Quest4Status = False
                                jump Round1

                    label R1Cat2Quest5:

                        leader "Вопрос за 500"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest5Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest5Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest5Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat2Quest5Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ Cat2Quest5Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ Cat2Quest5Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ Cat2Quest5Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ Cat2Quest5Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ Cat2Quest5Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ Cat2Quest5Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ Cat2Quest5Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ Cat2Quest5Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ Cat2Quest5Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ Cat2Quest5Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ Cat2Quest5Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ Cat2Quest5Status = False
                                jump Round1

                label Round1Cat3:
                    
                    if Turn == 1: 
                        gg "Категория 3"
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
                        team1 "Категория 3"
                        $Team1Qestion = renpy.random.randint(1,6)
                        if R1Cat3Quest1Status==1 and Team1Qestion == 1:
                            team1 "Quest1"
                            jump R1Cat3Quest1

                        elif R1Cat3Quest2Status==1 and Team1Qestion == 2:
                            team1 "Quest2"
                            jump R1Cat3Quest2

                        elif R1Cat3Quest3Status==1 and Team1Qestion == 3:
                            team1 "Quest3"
                            jump R1Cat3Quest3

                        elif R1Cat3Quest4Status==1 and Team1Qestion == 4:
                            team1 "Quest4"
                            jump R1Cat3Quest4

                        elif R1Cat3Quest5Status==1 and Team1Qestion == 5:
                            team1 "Quest5"
                            jump R1Cat3Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat3    

                    elif Turn == 3: 
                        team2 "Категория 3"
                        $Team2Qestion = renpy.random.randint(1,6)
                        if R1Cat3Quest1Status==1 and Team1Qestion == 1:
                            team2 "Quest1"
                            jump R1Cat3Quest1

                        elif R1Cat3Quest2Status==1 and Team1Qestion == 2:
                            team2 "Quest2"
                            jump R1Cat3Quest2

                        elif R1Cat3Quest3Status==1 and Team1Qestion == 3:
                            team2 "Quest3"
                            jump R1Cat3Quest3

                        elif R1Cat3Quest4Status==1 and Team1Qestion == 4:
                            team2 "Quest4"
                            jump R1Cat3Quest4

                        elif R1Cat3Quest5Status==1 and Team1Qestion == 5:
                            team2 "Quest5"
                            jump R1Cat3Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat3

                    elif Turn == 4: 
                        team3 "Категория 3"
                        $Team3Qestion = renpy.random.randint(1,6)
                        if R1Cat3Quest1Status==1 and Team1Qestion == 1:
                            team3 "Quest1"
                            jump R1Cat3Quest1

                        elif R1Cat3Quest2Status==1 and Team1Qestion == 2:
                            team3 "Quest2"
                            jump R1Cat3Quest2

                        elif R1Cat3Quest3Status==1 and Team1Qestion == 3:
                            team3 "Quest3"
                            jump R1Cat3Quest3

                        elif R1Cat3Quest4Status==1 and Team1Qestion == 4:
                            team3 "Quest4"
                            jump R1Cat3Quest4

                        elif R1Cat3Quest5Status==1 and Team1Qestion == 5:
                            team3 "Quest5"
                            jump R1Cat3Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat3
                    
                    label R1Cat3Quest1:

                        leader "Вопрос за 100"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest1Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest1Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest1Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest1Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $OurTeamPoints -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat3Quest1Status = False
                                jump Round1 

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest1Status = False
                                jump Round1 

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest1Status = False
                                jump Round1

                    label R1Cat3Quest2:

                        leader "Вопрос за 200"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest2Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest2Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest2Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest2Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest2Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest2Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest2Status = False
                                jump Round1

                    label R1Cat3Quest3:

                        leader "Вопрос за 300"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest3Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest3Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest3Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest3Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest3Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest3Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest3Status = False
                                jump Round1
                    
                    label R1Cat3Quest4:

                        leader "Вопрос за 400"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest4Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest4Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest4Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest4Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest4Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest4Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest4Status = False
                                jump Round1

                    label R1Cat3Quest5:

                        leader "Вопрос за 500"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest5Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest5Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest5Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest5Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest5Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest5Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest5Status = False
                                jump Round1

                label Round1Cat4:
                    
                    if Turn == 1: 
                        gg "Категория 4"
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
                        team1 "Категория 4"
                        $Team1Qestion = renpy.random.randint(1,6)
                        if R1Cat4Quest1Status==1 and Team1Qestion == 1:
                            team1 "Quest1"
                            jump R1Cat4Quest1

                        elif R1Cat4Quest2Status==1 and Team1Qestion == 2:
                            team1 "Quest2"
                            jump R1Cat4Quest2

                        elif R1Cat4Quest3Status==1 and Team1Qestion == 3:
                            team1 "Quest3"
                            jump R1Cat4Quest3

                        elif R1Cat4Quest4Status==1 and Team1Qestion == 4:
                            team1 "Quest4"
                            jump R1Cat4Quest4

                        elif R1Cat4Quest5Status==1 and Team1Qestion == 5:
                            team1 "Quest5"
                            jump R1Cat4Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat4    

                    elif Turn == 3: 
                        team2 "Категория 3"
                        $Team2Qestion = renpy.random.randint(1,6)
                        if R1Cat4Quest1Status==1 and Team1Qestion == 1:
                            team2 "Quest1"
                            jump R1Cat4Quest1

                        elif R1Cat4Quest2Status==1 and Team1Qestion == 2:
                            team2 "Quest2"
                            jump R1Cat4Quest2

                        elif R1Cat4Quest3Status==1 and Team1Qestion == 3:
                            team2 "Quest3"
                            jump R1Cat4Quest3

                        elif R1Cat4Quest4Status==1 and Team1Qestion == 4:
                            team2 "Quest4"
                            jump R1Cat4Quest4

                        elif R1Cat4Quest5Status==1 and Team1Qestion == 5:
                            team2 "Quest5"
                            jump R1Cat4Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat4

                    elif Turn == 4: 
                        team3 "Категория 3"
                        $Team3Qestion = renpy.random.randint(1,6)
                        if R1Cat4Quest1Status==1 and Team1Qestion == 1:
                            team3 "Quest1"
                            jump R1Cat4Quest1

                        elif R1Cat4Quest2Status==1 and Team1Qestion == 2:
                            team3 "Quest2"
                            jump R1Cat4Quest2

                        elif R1Cat4Quest3Status==1 and Team1Qestion == 3:
                            team3 "Quest3"
                            jump R1Cat4Quest3

                        elif R1Cat4Quest4Status==1 and Team1Qestion == 4:
                            team3 "Quest4"
                            jump R1Cat4Quest4

                        elif R1Cat4Quest5Status==1 and Team1Qestion == 5:
                            team3 "Quest5"
                            jump R1Cat4Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat4
                    
                    label R1Cat4Quest1:

                        leader "Вопрос за 100"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest1Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest1Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest1Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest1Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat4Quest1Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $OurTeamPoints -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat4Quest1Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat4Quest1Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat4Quest1Status = False
                                jump Round1 

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest1Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest1Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest1Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest1Status = False
                                jump Round1 

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest1Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest1Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest1Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest1Status = False
                                jump Round1

                    label R1Cat4Quest2:

                        leader "Вопрос за 200"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest2Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest2Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest2Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest2Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest2Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest2Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest2Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest2Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest2Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest2Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest2Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest2Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest2Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest2Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest2Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest2Status = False
                                jump Round1

                    label R1Cat4Quest3:

                        leader "Вопрос за 300"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest3Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest3Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest3Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest3Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest3Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest3Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest3Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest3Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest3Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest3Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest3Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest3Status = False
                                jump Round1

                        elif Turn == 4 : 

                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest3Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest3Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest3Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest3Status = False
                                jump Round1
                    
                    label R1Cat4Quest4:

                        leader "Вопрос за 400"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest4Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest4Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest4Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest4Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest4Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest4Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest4Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest4Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest4Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest4Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest4Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest4Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest4Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest4Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest4Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest4Status = False
                                jump Round1

                    label R1Cat4Quest5:

                        leader "Вопрос за 500"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest5Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest5Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest5Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat4Quest5Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest5Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest5Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest5Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat4Quest5Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest5Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest5Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest5Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat4Quest5Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest5Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest5Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest5Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat4Quest5Status = False
                                jump Round1

            label Round2:

                if R1Categories == 1:
                    jump Round3

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
                        "Категория 1" if R1Cat1Status == True:
                            jump Round2Cat1
                        "Категория 2" if R1Cat2Status == True:
                            jump Round2Cat2
                        "Категория 3" if R1Cat2Status == True:
                            jump Round2Cat3
                        "Категория 4" if R1Cat2Status == True:
                            jump Round2Cat4
                    
 
                label Round2Cat1:
                    
                    if Turn == 1: 
                        gg "Категория 1"
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
                        team1 "Категория 1"
                        $Team1Qestion = renpy.random.randint(1,6)
                        if R2Cat1Quest1Status==1 and Team1Qestion == 1:
                            team1 "Quest1"
                            jump R2Cat1Quest1

                        elif R2Cat1Quest2Status==1 and Team1Qestion == 2:
                            team1 "Quest2"
                            jump R2Cat1Quest2

                        elif R2Cat1Quest3Status==1 and Team1Qestion == 3:
                            team1 "Quest3"
                            jump R2Cat1Quest3

                        elif R2Cat1Quest4Status==1 and Team1Qestion == 4:
                            team1 "Quest4"
                            jump R2Cat1Quest4

                        elif R2Cat1Quest5Status==1 and Team1Qestion == 5:
                            team1 "Quest5"
                            jump R2Cat1Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round2Cat1    

                    elif Turn == 3: 
                        team2 "Категория 1"
                        $Team1Qestion = renpy.random.randint(1,6)
                        if R2Cat1Quest1Status==1 and Team1Qestion == 1:
                            team2 "Quest1"
                            jump R2Cat1Quest1

                        elif R2Cat1Quest2Status==1 and Team1Qestion == 2:
                            team2 "Quest2"
                            jump R2Cat1Quest2

                        elif R2Cat1Quest3Status==1 and Team1Qestion == 3:
                            team2 "Quest3"
                            jump R2Cat1Quest3

                        elif R2Cat1Quest4Status==1 and Team1Qestion == 4:
                            team2 "Quest4"
                            jump R2Cat1Quest4

                        elif R2Cat1Quest5Status==1 and Team1Qestion == 5:
                            team2 "Quest5"
                            jump R2Cat1Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round2Cat1 

                    elif Turn == 4: 
                        team3 "Категория 1"
                        $Team1Qestion = renpy.random.randint(1,6)
                        if R2Cat1Quest1Status==1 and Team1Qestion == 1:
                            team3 "Quest1"
                            jump R2Cat1Quest1

                        elif R2Cat1Quest2Status==1 and Team1Qestion == 2:
                            team3 "Quest2"
                            jump R2Cat1Quest2

                        elif R2Cat1Quest3Status==1 and Team1Qestion == 3:
                            team3 "Quest3"
                            jump R2Cat1Quest3

                        elif R2Cat1Quest4Status==1 and Team1Qestion == 4:
                            team3 "Quest4"
                            jump R2Cat1Quest4

                        elif R2Cat1Quest5Status==1 and Team1Qestion == 5:
                            team3 "Quest5"
                            jump R2Cat1Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round2Cat1 
                    
                    label R2Cat1Quest1:

                        leader "Вопрос за 100"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest1Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest1Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest1Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest1Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R2Cat1Quest1Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $OurTeamPoints -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R2Cat1Quest1Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R2Cat1Quest1Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R2Cat1Quest1Status = False
                                jump Round1 

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest1Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest1Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest1Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest1Status = False
                                jump Round1 

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest1Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest1Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest1Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest1Status = False
                                jump Round1

                    label R2Cat1Quest2:

                        leader "Вопрос за 200"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest2Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest2Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest2Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest2Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest2Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest2Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest2Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest2Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest2Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest2Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest2Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest2Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest2Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest2Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest2Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest2Status = False
                                jump Round1

                    label R2Cat1Quest3:

                        leader "Вопрос за 300"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest3Status = False
                                    jump Round2 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest3Status = False
                                    jump Round2 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest3Status = False
                                    jump Round2 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest3Status = False
                                    jump Round2 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest3Status = False
                                jump Round2 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest3Status = False
                                jump Round2 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest3Status = False
                                jump Round2 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest3Status = False
                                jump Round2

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest3Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest3Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest3Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest3Status = False
                                jump Round2

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest3Status = False
                                jump Round2 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest3Status = False
                                jump Round2 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest3Status = False
                                jump Round2 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest3Status = False
                                jump Round2
                    
                    label R2Cat1Quest4:

                        leader "Вопрос за 400"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest4Status = False
                                    jump Round2 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest4Status = False
                                    jump Round2 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest4Status = False
                                    jump Round2 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest4Status = False
                                    jump Round2 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest4Status = False
                                jump Round2 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest4Status = False
                                jump Round2 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest4Status = False
                                jump Round2 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest4Status = False
                                jump Round2

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                "ответ"
                                $Team2Points += 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest4Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest4Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest4Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest4Status = False
                                jump Round2

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest4Status = False
                                jump Round2 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest4Status = False
                                jump Round2 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest4Status = False
                                jump Round2 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest4Status = False
                                jump Round2

                    label R2Cat1Quest5:

                        leader "Вопрос за 500"
                        "Вопрос"
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
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest5Status = False
                                    jump Round2 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat1Quest5Status = False
                                    jump Round2 

                                "4":    
                                    "неверно"
                                    "ответ"
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
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest5Status = False
                                jump Round2 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat1Quest5Status = False
                                jump Round2 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
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
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat1Quest5Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ Cat1Quest5Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
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
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest5Status = False
                                jump Round2 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest5Status = False
                                jump Round2 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat1Quest5Status = False
                                jump Round2

                label Round2Cat2:
                    
                    if Turn == 1: 
                        gg "Категория 2"
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
                        team1 "Категория 2"
                        $Team1Qestion = renpy.random.randint(1,6)
                        if R2Cat2Quest1Status==1 and Team1Qestion == 1:
                            team1 "Quest1"
                            jump R2Cat2Quest1

                        elif R2Cat2Quest2Status==1 and Team1Qestion == 2:
                            team1 "Quest2"
                            jump R2Cat2Quest2

                        elif R2Cat2Quest3Status==1 and Team1Qestion == 3:
                            team1 "Quest3"
                            jump R2Cat2Quest3

                        elif R2Cat2Quest4Status==1 and Team1Qestion == 4:
                            team1 "Quest4"
                            jump R2Cat2Quest4

                        elif R2Cat2Quest5Status==1 and Team1Qestion == 5:
                            team1 "Quest5"
                            jump R2Cat2Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round2Cat2    

                    elif Turn == 3: 
                        team2 "Категория 2"
                        $Team2Qestion = renpy.random.randint(1,6)
                        if R2Cat2Quest1Status==1 and Team2Qestion == 1:
                            team2 "Quest1"
                            jump R2Cat2Quest1

                        elif R2Cat2Quest2Status==1 and Team2Qestion == 2:
                            team2 "Quest2"
                            jump R2Cat2Quest2

                        elif R2Cat2Quest3Status==1 and Team2Qestion == 3:
                            team2 "Quest3"
                            jump R2Cat2Quest3

                        elif R2Cat2Quest4Status==1 and Team2Qestion == 4:
                            team2 "Quest4"
                            jump R2Cat2Quest4

                        elif R2Cat2Quest5Status==1 and Team2Qestion == 5:
                            team2 "Quest5"
                            jump R2Cat2Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round2Cat2

                    elif Turn == 4: 
                        team3 "Категория 2"
                        $Team3Qestion = renpy.random.randint(1,6)
                        if R2Cat2Quest1Status==1 and Team3Qestion == 1:
                            team3 "Quest1"
                            jump R2Cat2Quest1

                        elif R2Cat2Quest2Status==1 and Team3Qestion == 2:
                            team3 "Quest2"
                            jump R2Cat2Quest2

                        elif R2Cat2Quest3Status==1 and Team3Qestion == 3:
                            team3 "Quest3"
                            jump R2Cat2Quest3

                        elif R2Cat2Quest4Status==1 and Team3Qestion == 4:
                            team3 "Quest4"
                            jump R2Cat2Quest4

                        elif R2Cat2Quest5Status==1 and Team3Qestion == 5:
                            team3 "Quest5"
                            jump R2Cat2Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round2Cat2
                    
                    label R2Cat2Quest1:

                        leader "Вопрос за 100"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest1Status = False
                                    jump Round2 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest1Status = False
                                    jump Round2 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest1Status = False
                                    jump Round2 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest1Status = False
                                    jump Round2 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R2Cat2Quest1Status = False
                                jump Round2 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $OurTeamPoints -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R2Cat2Quest1Status = False
                                jump Round2 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R2Cat2Quest1Status = False
                                jump Round2 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R2Cat2Quest1Status = False
                                jump Round2 

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest1Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest1Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest1Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest1Status = False
                                jump Round2 

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest1Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest1Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest1Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest1Status = False
                                jump Round2

                    label R2Cat2Quest2:

                        leader "Вопрос за 200"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest2Status = False
                                    jump Round2 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest2Status = False
                                    jump Round2 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest2Status = False
                                    jump Round2 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest2Status = False
                                    jump Round2 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest2Status = False
                                jump Round2 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest2Status = False
                                jump Round2 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest2Status = False
                                jump Round2 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest2Status = False
                                jump Round2

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest2Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest2Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest2Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest2Status = False
                                jump Round2

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest2Status = False
                                jump Round2 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest2Status = False
                                jump Round2 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest2Status = False
                                jump Round2 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest2Status = False
                                jump Round2

                    label R2Cat2Quest3:

                        leader "Вопрос за 300"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest3Status = False
                                    jump Round2 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest3Status = False
                                    jump Round2 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest3Status = False
                                    jump Round2 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest3Status = False
                                    jump Round2 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest3Status = False
                                jump Round2 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest3Status = False
                                jump Round2 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest3Status = False
                                jump Round2 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest3Status = False
                                jump Round2

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest3Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest3Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest3Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest3Status = False
                                jump Round2

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest3Status = False
                                jump Round2 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest3Status = False
                                jump Round2 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest3Status = False
                                jump Round2 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest3Status = False
                                jump Round2
                    
                    label R2Cat2Quest4:

                        leader "Вопрос за 400"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest4Status = False
                                    jump Round2 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest4Status = False
                                    jump Round2 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest4Status = False
                                    jump Round2 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest4Status = False
                                    jump Round2 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest4Status = False
                                jump Round2 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest4Status = False
                                jump Round2 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest4Status = False
                                jump Round2 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest4Status = False
                                jump Round2

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest4Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest4Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest4Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest4Status = False
                                jump Round2

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest4Status = False
                                jump Round2 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest4Status = False
                                jump Round2 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest4Status = False
                                jump Round2 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest4Status = False
                                jump Round2

                    label R2Cat2Quest5:

                        leader "Вопрос за 500"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest5Status = False
                                    jump Round2 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest5Status = False
                                    jump Round2 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest5Status = False
                                    jump Round2 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat2Quest5Status = False
                                    jump Round2 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest5Status = False
                                jump Round2 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ Cat2Quest5Status = False
                                jump Round2 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest5Status = False
                                jump Round2 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat2Quest5Status = False
                                jump Round2

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest5Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest5Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest5Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat2Quest5Status = False
                                jump Round2

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest5Status = False
                                jump Round2 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest5Status = False
                                jump Round2 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest5Status = False
                                jump Round2 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat2Quest5Status = False
                                jump Round2

                label Round2Cat3:
                    
                    if Turn == 1: 
                        gg "Категория 3"
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
                        team1 "Категория 3"
                        $Team1Qestion = renpy.random.randint(1,6)
                        if R1Cat3Quest1Status==1 and Team1Qestion == 1:
                            team1 "Quest1"
                            jump R1Cat3Quest1

                        elif R1Cat3Quest2Status==1 and Team1Qestion == 2:
                            team1 "Quest2"
                            jump R1Cat3Quest2

                        elif R1Cat3Quest3Status==1 and Team1Qestion == 3:
                            team1 "Quest3"
                            jump R1Cat3Quest3

                        elif R1Cat3Quest4Status==1 and Team1Qestion == 4:
                            team1 "Quest4"
                            jump R1Cat3Quest4

                        elif R1Cat3Quest5Status==1 and Team1Qestion == 5:
                            team1 "Quest5"
                            jump R1Cat3Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat3    

                    elif Turn == 3: 
                        team2 "Категория 3"
                        $Team2Qestion = renpy.random.randint(1,6)
                        if R1Cat3Quest1Status==1 and Team1Qestion == 1:
                            team2 "Quest1"
                            jump R1Cat3Quest1

                        elif R1Cat3Quest2Status==1 and Team1Qestion == 2:
                            team2 "Quest2"
                            jump R1Cat3Quest2

                        elif R1Cat3Quest3Status==1 and Team1Qestion == 3:
                            team2 "Quest3"
                            jump R1Cat3Quest3

                        elif R1Cat3Quest4Status==1 and Team1Qestion == 4:
                            team2 "Quest4"
                            jump R1Cat3Quest4

                        elif R1Cat3Quest5Status==1 and Team1Qestion == 5:
                            team2 "Quest5"
                            jump R1Cat3Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat3

                    elif Turn == 4: 
                        team3 "Категория 3"
                        $Team3Qestion = renpy.random.randint(1,6)
                        if R1Cat3Quest1Status==1 and Team1Qestion == 1:
                            team3 "Quest1"
                            jump R1Cat3Quest1

                        elif R1Cat3Quest2Status==1 and Team1Qestion == 2:
                            team3 "Quest2"
                            jump R1Cat3Quest2

                        elif R1Cat3Quest3Status==1 and Team1Qestion == 3:
                            team3 "Quest3"
                            jump R1Cat3Quest3

                        elif R1Cat3Quest4Status==1 and Team1Qestion == 4:
                            team3 "Quest4"
                            jump R1Cat3Quest4

                        elif R1Cat3Quest5Status==1 and Team1Qestion == 5:
                            team3 "Quest5"
                            jump R1Cat3Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat3
                    
                    label R2Cat3Quest1:

                        leader "Вопрос за 100"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest1Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest1Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest1Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest1Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $OurTeamPoints -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R1Cat3Quest1Status = False
                                jump Round1 

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest1Status = False
                                jump Round1 

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest1Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest1Status = False
                                jump Round1

                    label R2Cat3Quest2:

                        leader "Вопрос за 200"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest2Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest2Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest2Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest2Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest2Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest2Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest2Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest2Status = False
                                jump Round1

                    label R2Cat3Quest3:

                        leader "Вопрос за 300"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest3Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest3Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest3Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest3Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest3Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest3Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest3Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest3Status = False
                                jump Round1
                    
                    label R2Cat3Quest4:

                        leader "Вопрос за 400"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest4Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest4Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest4Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest4Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest4Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest4Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest4Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest4Status = False
                                jump Round1

                    label R2Cat3Quest5:

                        leader "Вопрос за 500"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest5Status = False
                                    jump Round1 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest5Status = False
                                    jump Round1 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest5Status = False
                                    jump Round1 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R1Cat3Quest5Status = False
                                    jump Round1 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R1Cat3Quest5Status = False
                                jump Round1

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R1Cat3Quest5Status = False
                                jump Round1

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest5Status = False
                                jump Round1 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R1Cat3Quest5Status = False
                                jump Round1

                label Round2Cat4:
                    
                    if Turn == 1: 
                        gg "Категория 4"
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
                        team1 "Категория 4"
                        $Team1Qestion = renpy.random.randint(1,6)
                        if R2Cat4Quest1Status==1 and Team1Qestion == 1:
                            team1 "Quest1"
                            jump R2Cat4Quest1

                        elif R2Cat4Quest2Status==1 and Team1Qestion == 2:
                            team1 "Quest2"
                            jump R2Cat4Quest2

                        elif R2Cat4Quest3Status==1 and Team1Qestion == 3:
                            team1 "Quest3"
                            jump R2Cat4Quest3

                        elif R2Cat4Quest4Status==1 and Team1Qestion == 4:
                            team1 "Quest4"
                            jump R2Cat4Quest4

                        elif R2Cat4Quest5Status==1 and Team1Qestion == 5:
                            team1 "Quest5"
                            jump R2Cat4Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat4    

                    elif Turn == 3: 
                        team2 "Категория 3"
                        $Team2Qestion = renpy.random.randint(1,6)
                        if R2Cat4Quest1Status==1 and Team1Qestion == 1:
                            team2 "Quest1"
                            jump R2Cat4Quest1

                        elif R2Cat4Quest2Status==1 and Team1Qestion == 2:
                            team2 "Quest2"
                            jump R2Cat4Quest2

                        elif R2Cat4Quest3Status==1 and Team1Qestion == 3:
                            team2 "Quest3"
                            jump R2Cat4Quest3

                        elif R2Cat4Quest4Status==1 and Team1Qestion == 4:
                            team2 "Quest4"
                            jump R2Cat4Quest4

                        elif R2Cat4Quest5Status==1 and Team1Qestion == 5:
                            team2 "Quest5"
                            jump R2Cat4Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round1Cat4

                    elif Turn == 4: 
                        team3 "Категория 3"
                        $Team3Qestion = renpy.random.randint(1,6)
                        if R2Cat4Quest1Status==1 and Team1Qestion == 1:
                            team3 "Quest1"
                            jump R2Cat4Quest1

                        elif R2Cat4Quest2Status==1 and Team1Qestion == 2:
                            team3 "Quest2"
                            jump R2Cat4Quest2

                        elif R2Cat4Quest3Status==1 and Team1Qestion == 3:
                            team3 "Quest3"
                            jump R2Cat4Quest3

                        elif R2Cat4Quest4Status==1 and Team1Qestion == 4:
                            team3 "Quest4"
                            jump R2Cat4Quest4

                        elif R2Cat4Quest5Status==1 and Team1Qestion == 5:
                            team3 "Quest5"
                            jump R2Cat4Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round2Cat4
                    
                    label R2Cat4Quest1:

                        leader "Вопрос за 100"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest1Status = False
                                    jump Round2 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest1Status = False
                                    jump Round2 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest1Status = False
                                    jump Round2 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest1Status = False
                                    jump Round2 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R2Cat4Quest1Status = False
                                jump Round2 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $OurTeamPoints -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R2Cat4Quest1Status = False
                                jump Round2 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R2Cat4Quest1Status = False
                                jump Round2 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R2Cat4Quest1Status = False
                                jump Round2 

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest1Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest1Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest1Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest1Status = False
                                jump Round2 

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest1Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest1Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest1Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest1Status = False
                                jump Round2

                    label R2Cat4Quest2:

                        leader "Вопрос за 200"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest2Status = False
                                    jump Round2 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest2Status = False
                                    jump Round2 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest2Status = False
                                    jump Round2 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest2Status = False
                                    jump Round2 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest2Status = False
                                jump Round2 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest2Status = False
                                jump Round2 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest2Status = False
                                jump Round2 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest2Status = False
                                jump Round2

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest2Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest2Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest2Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest2Status = False
                                jump Round2

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest2Status = False
                                jump Round2 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest2Status = False
                                jump Round2 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest2Status = False
                                jump Round2 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest2Status = False
                                jump Round2

                    label R2Cat4Quest3:

                        leader "Вопрос за 300"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest3Status = False
                                    jump Round2 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest3Status = False
                                    jump Round2 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest3Status = False
                                    jump Round2 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest3Status = False
                                    jump Round2 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest3Status = False
                                jump Round2 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest3Status = False
                                jump Round2 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest3Status = False
                                jump Round2 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest3Status = False
                                jump Round2

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest3Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest3Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest3Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest3Status = False
                                jump Round2

                        elif Turn == 4 : 

                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest3Status = False
                                jump Round2 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest3Status = False
                                jump Round2 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest3Status = False
                                jump Round2 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest3Status = False
                                jump Round2
                    
                    label R2Cat4Quest4:

                        leader "Вопрос за 400"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest4Status = False
                                    jump Round2 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest4Status = False
                                    jump Round2 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest4Status = False
                                    jump Round2 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest4Status = False
                                    jump Round2 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest4Status = False
                                jump Round2 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest4Status = False
                                jump Round2 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest4Status = False
                                jump Round2 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest4Status = False
                                jump Round2

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest4Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest4Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest4Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest4Status = False
                                jump Round2

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest4Status = False
                                jump Round2 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest4Status = False
                                jump Round2 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest4Status = False
                                jump Round2 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest4Status = False
                                jump Round2

                    label R2Cat4Quest5:

                        leader "Вопрос за 500"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest5Status = False
                                    jump Round2 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest5Status = False
                                    jump Round2 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest5Status = False
                                    jump Round2 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R2Cat4Quest5Status = False
                                    jump Round2 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest5Status = False
                                jump Round2 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest5Status = False
                                jump Round2 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest5Status = False
                                jump Round2 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R2Cat4Quest5Status = False
                                jump Round2

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest5Status = False
                                jump Round2 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest5Status = False
                                jump Round2 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest5Status = False
                                jump Round2 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R2Cat4Quest5Status = False
                                jump Round2

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest5Status = False
                                jump Round2 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest5Status = False
                                jump Round2 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest5Status = False
                                jump Round2 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R2Cat4Quest5Status = False
                                jump Round2

            label Round3:

                if R1Categories == 1:
                    jump Final

                if R3Cat1Quest1Status == False and R3Cat1Quest2Status == False and R3Cat1Quest3Status == False and R3Cat1Quest4Status == False and R3Cat1Quest5Status == False:
                    $ R1Cat1Status = False
                    $ R1Categories -=1
                
                if R3Cat2Quest1Status == False and R3Cat2Quest2Status == False and R3Cat2Quest3Status == False and R3Cat2Quest4Status == False and R3Cat2Quest5Status == False:
                    $ R1Cat2Status = False
                    $ R1Categories -=1

                if R3Cat3Quest1Status == False and R3Cat3Quest2Status == False and R3Cat3Quest3Status == False and R3Cat3Quest4Status == False and R3Cat3Quest5Status == False:
                    $ R1Cat3Status = False
                    $ R1Categories -=1

                if R3Cat4Quest1Status == False and R3Cat4Quest2Status == False and R3Cat4Quest3Status == False and R3Cat4Quest4Status == False and R3Cat4Quest5Status == False:
                    $ R1Cat4Status = False
                    $ R1Categories -=1    
                if Turn == 1:
                    menu:
                        "Категория 1" if R1Cat1Status == True:
                            jump Round3Cat1
                        "Категория 2" if R1Cat2Status == True:
                            jump Round3Cat2
                        "Категория 3" if R1Cat2Status == True:
                            jump Round3Cat3
                        "Категория 4" if R1Cat2Status == True:
                            jump Round3Cat4
                    
 
                label Round3Cat1:
                    
                    if Turn == 1: 
                        gg "Категория 1"
                        menu: 
                            "100" if R3Cat1Quest1Status == True:
                                jump R3Cat1Quest1

                            "200" if R3Cat1Quest2Status==1:
                                jump R3Cat1Quest2

                            "300" if R3Cat1Quest3Status==1:
                                jump R3Cat1Quest3

                            "400" if R3Cat1Quest4Status==1:
                                jump R3Cat1Quest4

                            "500" if R3Cat1Quest5Status==1:
                                jump R3Cat1Quest5

                    elif Turn == 2 : 
                        team1 "Категория 1"
                        $Team1Qestion = renpy.random.randint(1,6)
                        if R3Cat1Quest1Status==1 and Team1Qestion == 1:
                            team1 "Quest1"
                            jump R3Cat1Quest1

                        elif R3Cat1Quest2Status==1 and Team1Qestion == 2:
                            team1 "Quest2"
                            jump R3Cat1Quest2

                        elif R3Cat1Quest3Status==1 and Team1Qestion == 3:
                            team1 "Quest3"
                            jump R3Cat1Quest3

                        elif R3Cat1Quest4Status==1 and Team1Qestion == 4:
                            team1 "Quest4"
                            jump R3Cat1Quest4

                        elif R3Cat1Quest5Status==1 and Team1Qestion == 5:
                            team1 "Quest5"
                            jump R3Cat1Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round3Cat1    

                    elif Turn == 3: 
                        team2 "Категория 1"
                        $Team1Qestion = renpy.random.randint(1,6)
                        if R3Cat1Quest1Status==1 and Team1Qestion == 1:
                            team2 "Quest1"
                            jump R3Cat1Quest1

                        elif R3Cat1Quest2Status==1 and Team1Qestion == 2:
                            team2 "Quest2"
                            jump R3Cat1Quest2

                        elif R3Cat1Quest3Status==1 and Team1Qestion == 3:
                            team2 "Quest3"
                            jump R3Cat1Quest3

                        elif R3Cat1Quest4Status==1 and Team1Qestion == 4:
                            team2 "Quest4"
                            jump R3Cat1Quest4

                        elif R2Cat1Quest5Status==1 and Team1Qestion == 5:
                            team2 "Quest5"
                            jump R2Cat1Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round3Cat1 

                    elif Turn == 4: 
                        team3 "Категория 1"
                        $Team1Qestion = renpy.random.randint(1,6)
                        if R3Cat1Quest1Status==1 and Team1Qestion == 1:
                            team3 "Quest1"
                            jump R3Cat1Quest1

                        elif R3Cat1Quest2Status==1 and Team1Qestion == 2:
                            team3 "Quest2"
                            jump R3Cat1Quest2

                        elif R3Cat1Quest3Status==1 and Team1Qestion == 3:
                            team3 "Quest3"
                            jump R3Cat1Quest3

                        elif R3Cat1Quest4Status==1 and Team1Qestion == 4:
                            team3 "Quest4"
                            jump R3Cat1Quest4

                        elif R3Cat1Quest5Status==1 and Team1Qestion == 5:
                            team3 "Quest5"
                            jump R3Cat1Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round3Cat1 
                    
                    label R3Cat1Quest1:

                        leader "Вопрос за 100"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat1Quest1Status = False
                                    jump Round3 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat1Quest1Status = False
                                    jump Round3 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat1Quest1Status = False
                                    jump Round3 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat1Quest1Status = False
                                    jump Round3 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R3Cat1Quest1Status = False
                                jump Round3 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $OurTeamPoints -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R3Cat1Quest1Status = False
                                jump Round3 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R3Cat1Quest1Status = False
                                jump Round3 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R3Cat1Quest1Status = False
                                jump Round3 

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat1Quest1Status = False
                                jump Round3 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat1Quest1Status = False
                                jump Round3 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat1Quest1Status = False
                                jump Round3 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat1Quest1Status = False
                                jump Round3 

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat1Quest1Status = False
                                jump Round3 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat1Quest1Status = False
                                jump Round3 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat1Quest1Status = False
                                jump Round3 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat1Quest1Status = False
                                jump Round3

                    label R3Cat1Quest2:

                        leader "Вопрос за 200"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat1Quest2Status = False
                                    jump Round3 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat1Quest2Status = False
                                    jump Round3 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat1Quest2Status = False
                                    jump Round3 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat1Quest2Status = False
                                    jump Round3 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat1Quest2Status = False
                                jump Round3 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat1Quest2Status = False
                                jump Round3 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat1Quest2Status = False
                                jump Round3 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat1Quest2Status = False
                                jump Round3

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat1Quest2Status = False
                                jump Round3 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat1Quest2Status = False
                                jump Round3 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat1Quest2Status = False
                                jump Round3 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat1Quest2Status = False
                                jump Round3

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat1Quest2Status = False
                                jump Round3 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat1Quest2Status = False
                                jump Round3 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat1Quest2Status = False
                                jump Round3 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat1Quest2Status = False
                                jump Round3

                    label R3Cat1Quest3:

                        leader "Вопрос за 300"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat1Quest3Status = False
                                    jump Round3 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat1Quest3Status = False
                                    jump Round3 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat1Quest3Status = False
                                    jump Round3 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat1Quest3Status = False
                                    jump Round3 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat1Quest3Status = False
                                jump Round3 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat1Quest3Status = False
                                jump Round3 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat1Quest3Status = False
                                jump Round3 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat1Quest3Status = False
                                jump Round3

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat1Quest3Status = False
                                jump Round3 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat1Quest3Status = False
                                jump Round3 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat1Quest3Status = False
                                jump Round3 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat1Quest3Status = False
                                jump Round3

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat1Quest3Status = False
                                jump Round3 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat1Quest3Status = False
                                jump Round3 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat1Quest3Status = False
                                jump Round3 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat1Quest3Status = False
                                jump Round3
                    
                    label R3Cat1Quest4:

                        leader "Вопрос за 400"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat1Quest4Status = False
                                    jump Round3 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat1Quest4Status = False
                                    jump Round3 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat1Quest4Status = False
                                    jump Round3 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat1Quest4Status = False
                                    jump Round3 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat1Quest4Status = False
                                jump Round3 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat1Quest4Status = False
                                jump Round3 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat1Quest4Status = False
                                jump Round3 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat1Quest4Status = False
                                jump Round3

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                "ответ"
                                $Team2Points += 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat1Quest4Status = False
                                jump Round3 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat1Quest4Status = False
                                jump Round3 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat1Quest4Status = False
                                jump Round3 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat1Quest4Status = False
                                jump Round3

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat1Quest4Status = False
                                jump Round3 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat1Quest4Status = False
                                jump Round3 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat1Quest4Status = False
                                jump Round3 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat1Quest4Status = False
                                jump Round3

                    label R3Cat1Quest5:

                        leader "Вопрос за 500"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat1Quest5Status = False
                                    jump Round3 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat1Quest5Status = False
                                    jump Round3 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat1Quest5Status = False
                                    jump Round3 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat1Quest5Status = False
                                    jump Round3 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat1Quest5Status = False
                                jump Round3 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat1Quest5Status = False
                                jump Round3 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat1Quest5Status = False
                                jump Round3 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat1Quest5Status = False
                                jump Round3

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat1Quest5Status = False
                                jump Round3 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat1Quest5Status = False
                                jump Round3 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat1Quest5Status = False
                                jump Round3 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat1Quest5Status = False
                                jump Round3

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat1Quest5Status = False
                                jump Round3 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat1Quest5Status = False
                                jump Round3 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat1Quest5Status = False
                                jump Round3 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat1Quest5Status = False
                                jump Round3

                label Round3Cat2:
                    
                    if Turn == 1: 
                        gg "Категория 2"
                        menu: 
                            "100" if R3Cat2Quest1Status == True:
                                jump R3Cat2Quest1

                            "200" if R3Cat2Quest2Status==1:
                                jump R3Cat2Quest2

                            "300" if R3Cat2Quest3Status==1:
                                jump R3Cat2Quest3

                            "400" if R3Cat2Quest4Status==1:
                                jump R3Cat2Quest4

                            "500" if R3Cat2Quest5Status==1:
                                jump R3Cat2Quest5

                    elif Turn == 2 : 
                        team1 "Категория 2"
                        $Team1Qestion = renpy.random.randint(1,6)
                        if R3Cat2Quest1Status==1 and Team1Qestion == 1:
                            team1 "Quest1"
                            jump R3Cat2Quest1

                        elif R3Cat2Quest2Status==1 and Team1Qestion == 2:
                            team1 "Quest2"
                            jump R3Cat2Quest2

                        elif R3Cat2Quest3Status==1 and Team1Qestion == 3:
                            team1 "Quest3"
                            jump R3Cat2Quest3

                        elif R3Cat2Quest4Status==1 and Team1Qestion == 4:
                            team1 "Quest4"
                            jump R3Cat2Quest4

                        elif R3Cat2Quest5Status==1 and Team1Qestion == 5:
                            team1 "Quest5"
                            jump R3Cat2Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round3Cat2    

                    elif Turn == 3: 
                        team2 "Категория 2"
                        $Team2Qestion = renpy.random.randint(1,6)
                        if R3Cat2Quest1Status==1 and Team2Qestion == 1:
                            team2 "Quest1"
                            jump R3Cat2Quest1

                        elif R3Cat2Quest2Status==1 and Team2Qestion == 2:
                            team2 "Quest2"
                            jump R3Cat2Quest2

                        elif R3Cat2Quest3Status==1 and Team2Qestion == 3:
                            team2 "Quest3"
                            jump R3Cat2Quest3

                        elif R3Cat2Quest4Status==1 and Team2Qestion == 4:
                            team2 "Quest4"
                            jump R3Cat2Quest4

                        elif R3Cat2Quest5Status==1 and Team2Qestion == 5:
                            team2 "Quest5"
                            jump R3Cat2Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round3Cat2

                    elif Turn == 4: 
                        team3 "Категория 2"
                        $Team3Qestion = renpy.random.randint(1,6)
                        if R3Cat2Quest1Status==1 and Team3Qestion == 1:
                            team3 "Quest1"
                            jump R3Cat2Quest1

                        elif R3Cat2Quest2Status==1 and Team3Qestion == 2:
                            team3 "Quest2"
                            jump R3Cat2Quest2

                        elif R3Cat2Quest3Status==1 and Team3Qestion == 3:
                            team3 "Quest3"
                            jump R3Cat2Quest3

                        elif R3Cat2Quest4Status==1 and Team3Qestion == 4:
                            team3 "Quest4"
                            jump R3Cat2Quest4

                        elif R3Cat2Quest5Status==1 and Team3Qestion == 5:
                            team3 "Quest5"
                            jump R3Cat2Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round3Cat2
                    
                    label R3Cat2Quest1:

                        leader "Вопрос за 100"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat2Quest1Status = False
                                    jump Round3 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat2Quest1Status = False
                                    jump Round3 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat2Quest1Status = False
                                    jump Round3 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat2Quest1Status = False
                                    jump Round3 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R3Cat2Quest1Status = False
                                jump Round3 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $OurTeamPoints -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R3Cat2Quest1Status = False
                                jump Round3 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R3Cat2Quest1Status = False
                                jump Round3 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R3Cat2Quest1Status = False
                                jump Round3 

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat2Quest1Status = False
                                jump Round3 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat2Quest1Status = False
                                jump Round3 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat2Quest1Status = False
                                jump Round3 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat2Quest1Status = False
                                jump Round3 

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat2Quest1Status = False
                                jump Round3 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat2Quest1Status = False
                                jump Round3 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat2Quest1Status = False
                                jump Round3 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat2Quest1Status = False
                                jump Round3

                    label R3Cat2Quest2:

                        leader "Вопрос за 200"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat2Quest2Status = False
                                    jump Round3 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat2Quest2Status = False
                                    jump Round3 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat2Quest2Status = False
                                    jump Round3 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat2Quest2Status = False
                                    jump Round3 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat2Quest2Status = False
                                jump Round3 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat2Quest2Status = False
                                jump Round3 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat2Quest2Status = False
                                jump Round3 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat2Quest2Status = False
                                jump Round3

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat2Quest2Status = False
                                jump Round3 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat2Quest2Status = False
                                jump Round3 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat2Quest2Status = False
                                jump Round3 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat2Quest2Status = False
                                jump Round3

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat2Quest2Status = False
                                jump Round3 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat2Quest2Status = False
                                jump Round3 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat2Quest2Status = False
                                jump Round3 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat2Quest2Status = False
                                jump Round3

                    label R3Cat2Quest3:

                        leader "Вопрос за 300"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat2Quest3Status = False
                                    jump Round3 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat2Quest3Status = False
                                    jump Round3 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat2Quest3Status = False
                                    jump Round3 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat2Quest3Status = False
                                    jump Round3 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat2Quest3Status = False
                                jump Round3 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat2Quest3Status = False
                                jump Round3 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat2Quest3Status = False
                                jump Round3 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat2Quest3Status = False
                                jump Round3

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat2Quest3Status = False
                                jump Round3 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat2Quest3Status = False
                                jump Round3 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat2Quest3Status = False
                                jump Round3 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat2Quest3Status = False
                                jump Round3

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat2Quest3Status = False
                                jump Round3 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat2Quest3Status = False
                                jump Round3 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat2Quest3Status = False
                                jump Round3 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat2Quest3Status = False
                                jump Round3
                    
                    label R3Cat2Quest4:

                        leader "Вопрос за 400"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat2Quest4Status = False
                                    jump Round3 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat2Quest4Status = False
                                    jump Round3 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat2Quest4Status = False
                                    jump Round3 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat2Quest4Status = False
                                    jump Round3 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat2Quest4Status = False
                                jump Round3 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat2Quest4Status = False
                                jump Round3 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat2Quest4Status = False
                                jump Round3 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat2Quest4Status = False
                                jump Round3

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat2Quest4Status = False
                                jump Round3 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat2Quest4Status = False
                                jump Round3 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat2Quest4Status = False
                                jump Round3 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat2Quest4Status = False
                                jump Round3

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat2Quest4Status = False
                                jump Round3 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat2Quest4Status = False
                                jump Round3 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat2Quest4Status = False
                                jump Round3 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat2Quest4Status = False
                                jump Round3

                    label R3Cat2Quest5:

                        leader "Вопрос за 500"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat2Quest5Status = False
                                    jump Round3 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat2Quest5Status = False
                                    jump Round3 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat2Quest5Status = False
                                    jump Round3 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat2Quest5Status = False
                                    jump Round3 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat2Quest5Status = False
                                jump Round3 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat2Quest5Status = False
                                jump Round3 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat2Quest5Status = False
                                jump Round3 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat2Quest5Status = False
                                jump Round3

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat2Quest5Status = False
                                jump Round3 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat2Quest5Status = False
                                jump Round3 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat2Quest5Status = False
                                jump Round3 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat2Quest5Status = False
                                jump Round3

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat2Quest5Status = False
                                jump Round3 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat2Quest5Status = False
                                jump Round3 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat2Quest5Status = False
                                jump Round3 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat2Quest5Status = False
                                jump Round3

                label Round3Cat3:
                    
                    if Turn == 1: 
                        gg "Категория 3"
                        menu: 
                            "100" if R3Cat3Quest1Status == True:
                                jump R3Cat3Quest1

                            "200" if R3Cat3Quest2Status==1:
                                jump R3Cat3Quest2

                            "300" if R3Cat3Quest3Status==1:
                                jump R3Cat3Quest3

                            "400" if R3Cat3Quest4Status==1:
                                jump R3Cat3Quest4

                            "500" if R3Cat3Quest5Status==1:
                                jump R3Cat3Quest5

                    elif Turn == 2 : 
                        team1 "Категория 3"
                        $Team1Qestion = renpy.random.randint(1,6)
                        if R3Cat3Quest1Status==1 and Team1Qestion == 1:
                            team1 "Quest1"
                            jump R3Cat3Quest1

                        elif R3Cat3Quest2Status==1 and Team1Qestion == 2:
                            team1 "Quest2"
                            jump R3Cat3Quest2

                        elif R3Cat3Quest3Status==1 and Team1Qestion == 3:
                            team1 "Quest3"
                            jump R2Cat3Quest3

                        elif R3Cat3Quest4Status==1 and Team1Qestion == 4:
                            team1 "Quest4"
                            jump R3Cat3Quest4

                        elif R3Cat3Quest5Status==1 and Team1Qestion == 5:
                            team1 "Quest5"
                            jump R3Cat3Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round3Cat3    

                    elif Turn == 3: 
                        team2 "Категория 3"
                        $Team2Qestion = renpy.random.randint(1,6)
                        if R3Cat3Quest1Status==1 and Team1Qestion == 1:
                            team2 "Quest1"
                            jump R3Cat3Quest1

                        elif R3Cat3Quest2Status==1 and Team1Qestion == 2:
                            team2 "Quest2"
                            jump R3Cat3Quest2

                        elif R3Cat3Quest3Status==1 and Team1Qestion == 3:
                            team2 "Quest3"
                            jump R3Cat3Quest3

                        elif R3Cat3Quest4Status==1 and Team1Qestion == 4:
                            team2 "Quest4"
                            jump R3Cat3Quest4

                        elif R3Cat3Quest5Status==1 and Team1Qestion == 5:
                            team2 "Quest5"
                            jump R3Cat3Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round3Cat3

                    elif Turn == 4: 
                        team3 "Категория 3"
                        $Team3Qestion = renpy.random.randint(1,6)
                        if R3Cat3Quest1Status==1 and Team1Qestion == 1:
                            team3 "Quest1"
                            jump R3Cat3Quest1

                        elif R3Cat3Quest2Status==1 and Team1Qestion == 2:
                            team3 "Quest2"
                            jump R3Cat3Quest2

                        elif R3Cat3Quest3Status==1 and Team1Qestion == 3:
                            team3 "Quest3"
                            jump R3Cat3Quest3

                        elif R3Cat3Quest4Status==1 and Team1Qestion == 4:
                            team3 "Quest4"
                            jump R3Cat3Quest4

                        elif R3Cat3Quest5Status==1 and Team1Qestion == 5:
                            team3 "Quest5"
                            jump R3Cat3Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round3Cat3
                    
                    label R3Cat3Quest1:

                        leader "Вопрос за 100"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat3Quest1Status = False
                                    jump Round3 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat3Quest1Status = False
                                    jump Round3 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat3Quest1Status = False
                                    jump Round3 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat3Quest1Status = False
                                    jump Round3 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R3Cat3Quest1Status = False
                                jump Round3 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $OurTeamPoints -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R3Cat3Quest1Status = False
                                jump Round3 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R3Cat3Quest1Status = False
                                jump Round3 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R3Cat3Quest1Status = False
                                jump Round3 

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat3Quest1Status = False
                                jump Round3 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat3Quest1Status = False
                                jump Round3 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat3Quest1Status = False
                                jump Round3 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat3Quest1Status = False
                                jump Round3 

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat3Quest1Status = False
                                jump Round3 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat3Quest1Status = False
                                jump Round3 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat3Quest1Status = False
                                jump Round3 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat3Quest1Status = False
                                jump Round3

                    label R3Cat3Quest2:

                        leader "Вопрос за 200"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat3Quest2Status = False
                                    jump Round3 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat3Quest2Status = False
                                    jump Round3 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat3Quest2Status = False
                                    jump Round3 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat3Quest2Status = False
                                    jump Round3 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat3Quest2Status = False
                                jump Round3 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat3Quest2Status = False
                                jump Round3 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat3Quest2Status = False
                                jump Round3 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat3Quest2Status = False
                                jump Round3

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat3Quest2Status = False
                                jump Round3 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat3Quest2Status = False
                                jump Round3 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat3Quest2Status = False
                                jump Round3 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat3Quest2Status = False
                                jump Round3

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat3Quest2Status = False
                                jump Round3 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat3Quest2Status = False
                                jump Round3 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat3Quest2Status = False
                                jump Round3 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat3Quest2Status = False
                                jump Round3

                    label R3Cat3Quest3:

                        leader "Вопрос за 300"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat3Quest3Status = False
                                    jump Round3 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat3Quest3Status = False
                                    jump Round3 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat3Quest3Status = False
                                    jump Round3 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat3Quest3Status = False
                                    jump Round3 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat3Quest3Status = False
                                jump Round3 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat3Quest3Status = False
                                jump Round3 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat3Quest3Status = False
                                jump Round3 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat3Quest3Status = False
                                jump Round3

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat3Quest3Status = False
                                jump Round3 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat3Quest3Status = False
                                jump Round3 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat3Quest3Status = False
                                jump Round3 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat3Quest3Status = False
                                jump Round3

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat3Quest3Status = False
                                jump Round3 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat3Quest3Status = False
                                jump Round3 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat3Quest3Status = False
                                jump Round3 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat3Quest3Status = False
                                jump Round3
                    
                    label R3Cat3Quest4:

                        leader "Вопрос за 400"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat3Quest4Status = False
                                    jump Round3 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat3Quest4Status = False
                                    jump Round3 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat3Quest4Status = False
                                    jump Round3 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat3Quest4Status = False
                                    jump Round3 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat3Quest4Status = False
                                jump Round3 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat3Quest4Status = False
                                jump Round3 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat3Quest4Status = False
                                jump Round3 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat3Quest4Status = False
                                jump Round3

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat3Quest4Status = False
                                jump Round3 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat3Quest4Status = False
                                jump Round3 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat3Quest4Status = False
                                jump Round3 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat3Quest4Status = False
                                jump Round3

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat3Quest4Status = False
                                jump Round3 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat3Quest4Status = False
                                jump Round3 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat3Quest4Status = False
                                jump Round3 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat3Quest4Status = False
                                jump Round3

                    label R3Cat3Quest5:

                        leader "Вопрос за 500"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat3Quest5Status = False
                                    jump Round3 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat3Quest5Status = False
                                    jump Round3 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat3Quest5Status = False
                                    jump Round3 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat3Quest5Status = False
                                    jump Round3 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat3Quest5Status = False
                                jump Round3 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat3Quest5Status = False
                                jump Round3 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat3Quest5Status = False
                                jump Round3 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat3Quest5Status = False
                                jump Round3

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat3Quest5Status = False
                                jump Round3 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat3Quest5Status = False
                                jump Round3 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat3Quest5Status = False
                                jump Round3 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat3Quest5Status = False
                                jump Round3

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat3Quest5Status = False
                                jump Round3 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat3Quest5Status = False
                                jump Round3 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat3Quest5Status = False
                                jump Round3 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat3Quest5Status = False
                                jump Round3

                label Round3Cat4:
                    
                    if Turn == 1: 
                        gg "Категория 4"
                        menu: 
                            "100" if R3Cat4Quest1Status == True:
                                jump R3Cat4Quest1

                            "200" if R3Cat4Quest2Status==1:
                                jump R3Cat4Quest2

                            "300" if R3Cat4Quest3Status==1:
                                jump R3Cat4Quest3

                            "400" if R3Cat4Quest4Status==1:
                                jump R3Cat4Quest4

                            "500" if R3Cat4Quest5Status==1:
                                jump R3Cat4Quest5

                    elif Turn == 2 : 
                        team1 "Категория 4"
                        $Team1Qestion = renpy.random.randint(1,6)
                        if R3Cat4Quest1Status==1 and Team1Qestion == 1:
                            team1 "Quest1"
                            jump R3Cat4Quest1

                        elif R3Cat4Quest2Status==1 and Team1Qestion == 2:
                            team1 "Quest2"
                            jump R3Cat4Quest2

                        elif R3Cat4Quest3Status==1 and Team1Qestion == 3:
                            team1 "Quest3"
                            jump R3Cat4Quest3

                        elif R3Cat4Quest4Status==1 and Team1Qestion == 4:
                            team1 "Quest4"
                            jump R3Cat4Quest4

                        elif R3Cat4Quest5Status==1 and Team1Qestion == 5:
                            team1 "Quest5"
                            jump R3Cat4Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round3Cat4    

                    elif Turn == 3: 
                        team2 "Категория 3"
                        $Team2Qestion = renpy.random.randint(1,6)
                        if R3Cat4Quest1Status==1 and Team1Qestion == 1:
                            team2 "Quest1"
                            jump R3Cat4Quest1

                        elif R3Cat4Quest2Status==1 and Team1Qestion == 2:
                            team2 "Quest2"
                            jump R3Cat4Quest2

                        elif R3Cat4Quest3Status==1 and Team1Qestion == 3:
                            team2 "Quest3"
                            jump R3Cat4Quest3

                        elif R3Cat4Quest4Status==1 and Team1Qestion == 4:
                            team2 "Quest4"
                            jump R3Cat4Quest4

                        elif R3Cat4Quest5Status==1 and Team1Qestion == 5:
                            team2 "Quest5"
                            jump R3Cat4Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round3Cat4

                    elif Turn == 4: 
                        team3 "Категория 3"
                        $Team3Qestion = renpy.random.randint(1,6)
                        if R3Cat4Quest1Status==1 and Team1Qestion == 1:
                            team3 "Quest1"
                            jump R3Cat4Quest1

                        elif R3Cat4Quest2Status==1 and Team1Qestion == 2:
                            team3 "Quest2"
                            jump R3Cat4Quest2

                        elif R3Cat4Quest3Status==1 and Team1Qestion == 3:
                            team3 "Quest3"
                            jump R3Cat4Quest3

                        elif R3Cat4Quest4Status==1 and Team1Qestion == 4:
                            team3 "Quest4"
                            jump R3Cat4Quest4

                        elif R3Cat4Quest5Status==1 and Team1Qestion == 5:
                            team3 "Quest5"
                            jump R3Cat4Quest5
                        else:
                            "Этого вопроса нет"
                            jump Round3Cat4
                    
                    label R3Cat4Quest1:

                        leader "Вопрос за 100"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat4Quest1Status = False
                                    jump Round3 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat4Quest1Status = False
                                    jump Round3 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat4Quest1Status = False
                                    jump Round3 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 100
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat4Quest1Status = False
                                    jump Round3 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R3Cat4Quest1Status = False
                                jump Round3 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $OurTeamPoints -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R3Cat4Quest1Status = False
                                jump Round3 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R3Cat4Quest1Status = False
                                jump Round3 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 100
                                if Turn == 1 :
                                    $ Turn = 2
                                $ R3Cat4Quest1Status = False
                                jump Round3 

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat4Quest1Status = False
                                jump Round3 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat4Quest1Status = False
                                jump Round3 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat4Quest1Status = False
                                jump Round3 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 100
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat4Quest1Status = False
                                jump Round3 

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat4Quest1Status = False
                                jump Round3 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat4Quest1Status = False
                                jump Round3 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat4Quest1Status = False
                                jump Round3 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 100
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat4Quest1Status = False
                                jump Round3

                    label R3Cat4Quest2:

                        leader "Вопрос за 200"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat4Quest2Status = False
                                    jump Round3 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat4Quest2Status = False
                                    jump Round3 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat4Quest2Status = False
                                    jump Round3 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 200
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat4Quest2Status = False
                                    jump Round3 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat4Quest2Status = False
                                jump Round3 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat4Quest2Status = False
                                jump Round3 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat4Quest2Status = False
                                jump Round3 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 200
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat4Quest2Status = False
                                jump Round3

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat4Quest2Status = False
                                jump Round3 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat4Quest2Status = False
                                jump Round3 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat4Quest2Status = False
                                jump Round3 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 200
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat4Quest2Status = False
                                jump Round3

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat4Quest2Status = False
                                jump Round3 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat4Quest2Status = False
                                jump Round3 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat4Quest2Status = False
                                jump Round3 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 200
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat4Quest2Status = False
                                jump Round3

                    label R3Cat4Quest3:

                        leader "Вопрос за 300"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat4Quest3Status = False
                                    jump Round3 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat4Quest3Status = False
                                    jump Round3 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat4Quest3Status = False
                                    jump Round3 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 300
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat4Quest3Status = False
                                    jump Round3 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat4Quest3Status = False
                                jump Round3 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat4Quest3Status = False
                                jump Round3 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat4Quest3Status = False
                                jump Round3 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 300
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat4Quest3Status = False
                                jump Round3

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat4Quest3Status = False
                                jump Round3 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat4Quest3Status = False
                                jump Round3 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat4Quest3Status = False
                                jump Round3 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 300
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat4Quest3Status = False
                                jump Round3

                        elif Turn == 4 : 

                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat4Quest3Status = False
                                jump Round3 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat4Quest3Status = False
                                jump Round3 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat4Quest3Status = False
                                jump Round3 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 300
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat4Quest3Status = False
                                jump Round3
                    
                    label R3Cat4Quest4:

                        leader "Вопрос за 400"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat4Quest4Status = False
                                    jump Round3 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat4Quest4Status = False
                                    jump Round3 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat4Quest4Status = False
                                    jump Round3 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 400
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat4Quest4Status = False
                                    jump Round3 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat4Quest4Status = False
                                jump Round3 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat4Quest4Status = False
                                jump Round3 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat4Quest4Status = False
                                jump Round3 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 400
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat4Quest4Status = False
                                jump Round3

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat4Quest4Status = False
                                jump Round3 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat4Quest4Status = False
                                jump Round3 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat4Quest4Status = False
                                jump Round3 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 400
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat4Quest4Status = False
                                jump Round3

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat4Quest4Status = False
                                jump Round3 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat4Quest4Status = False
                                jump Round3 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat4Quest4Status = False
                                jump Round3 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 400
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat4Quest4Status = False
                                jump Round3

                    label R3Cat4Quest5:

                        leader "Вопрос за 500"
                        "Вопрос"
                        if Turn == 1 :
                            menu: 
                                "1":
                                    "верно"
                                    $OurTeamPoints += 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat4Quest5Status = False
                                    jump Round3 

                                "2":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat4Quest5Status = False
                                    jump Round3 

                                "3":
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat4Quest5Status = False
                                    jump Round3 

                                "4":    
                                    "неверно"
                                    "ответ"
                                    $OurTeamPoints -= 500
                                    if Turn == 1 :
                                        $ Turn = 2
                                    $ R3Cat4Quest5Status = False
                                    jump Round3 

                        elif Turn == 2 : 
                            $Team1Answer = renpy.random.randint(1,5)
                            if Team1Answer == 1:
                                "1"
                                "верно"
                                $Team1Points += 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat4Quest5Status = False
                                jump Round3 
                            if Team1Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat4Quest5Status = False
                                jump Round3 
                            if Team1Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat4Quest5Status = False
                                jump Round3 
                            if Team1Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team1Points -= 500
                                if Turn == 2 :
                                    $ Turn = 3
                                $ R3Cat4Quest5Status = False
                                jump Round3

                        elif Turn == 3 : 
                            $Team2Answer = renpy.random.randint(1,6)
                            if Team2Answer == 1:
                                "1"
                                "верно"
                                $Team2Points += 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat4Quest5Status = False
                                jump Round3 
                            if Team2Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat4Quest5Status = False
                                jump Round3 
                            if Team2Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat4Quest5Status = False
                                jump Round3 
                            if Team2Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team2Points -= 500
                                if Turn == 3 :
                                    $ Turn = 4
                                $ R3Cat4Quest5Status = False
                                jump Round3

                        elif Turn == 4 : 
                            $Team3Answer = renpy.random.randint(1,6)
                            if Team3Answer == 1:
                                "1"
                                "верно"
                                $Team3Points += 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat4Quest5Status = False
                                jump Round3 
                            if Team3Answer == 2:
                                "2"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat4Quest5Status = False
                                jump Round3 
                            if Team3Answer == 3:
                                "3"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat4Quest5Status = False
                                jump Round3 
                            if Team3Answer == 4:
                                "4"
                                "неверно"
                                "ответ"
                                $Team3Points -= 500
                                if Turn == 4 :
                                    $ Turn = 1
                                $ R3Cat4Quest5Status = False
                                jump Round3

            label Final:

                if OurTeamPoints > Team1Points and OurTeamPoints > Team2Points and OurTeamPoints > Team3Points:
                    leader "Final for our team"

                elif Team1Points > OurTeamPoints and Team1Points > Team2Points and Team1Points > Team3Points:

                    if OurTeamPoints > Team2Points and OurTeamPoints > Team3Points:

                        leader "Our team second place"

                    else:
                        
                        gg "we suck"
                
                elif Team2Points > OurTeamPoints and Team2Points > Team1Points and Team2Points > Team3Points:
                    
                    if OurTeamPoints > Team1Points and OurTeamPoints > Team3Points:

                        leader "Our team second place"

                    else:
                        
                        gg "we suck"

                elif Team3Points > OurTeamPoints and Team3Points > Team2Points and Team3Points > Team1Points:
                    
                    if OurTeamPoints > Team2Points and OurTeamPoints > Team1Points:

                        leader "Our team second place"

                    else:
                        
                        gg "we suck"

return

