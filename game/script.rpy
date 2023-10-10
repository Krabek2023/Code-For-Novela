# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define gg = Character('NoName', color="#b7d436")
define voice = Character('Разказчик', color="#b7d436")
define Kabak = Character('Макс Кабак(Самый сексуальный мужчина)', color='#b14f0e')
define Kris = Character('Матерь Кристина', color = '#b10e44')
define Fahta = Character('Вахтёр', color = '#b80e0e')
define All = Character('Все', color = '#b7d436')
define Prepod = Character('Преподаватель', color = "#ac2d06")

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



    return
