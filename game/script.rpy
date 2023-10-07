# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define gg = Character('NoName', color="#b7d436")
define voice = Character('Разказчик', color="#b7d436")
define Kabak = Character('Макс Кабак(Самый сексуальный мужчина)', color='#b14f0e')
define Kris = Character('Матерь Кристина', color = '#b10e44')

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    $Reputation = 0

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

    label Studik_for_everyone:
        scene RadAud
        with Fade(1,1,2)

        voice "Часть в аудитории не готова"

        scene audStud
        with Fade(0.5,0.2,0.7)

    label Profsoyz:
        scene blackScreen

        voice "Сейчас наш главный герой направляеться в коворкинг"

        voice "Зачем, ему не сказали"

        scene coworking
        with Fade(0.5,0.5,1)

        Kris "Внимание все, Сечас будет информация про проф союз."

        voice "Дальше была долгая реклама проф союза"
        voice "Но мы это опустим, заметив что это действительно полезно для ГГ и что дайт щикарный мерч"

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
            "Вступить?":
                jump Profsoyz_choise_yes
            "Ну его?":
                jump Prof_chos_NO_NO

    label Prof_chos_NO_NO:
        gg "Да ну его. Какой мне от этого смысл"
        voice "Как ни странно, но наш Абалдуй почуствовал как его окутали злые взгляды"
        $Reputation -= 15 
        jump scene1  

    label scene1:   
        voice "Твоя репутация: [Reputation]"










        

    
    

    return
