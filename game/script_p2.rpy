label Day5:

    scene Day5
    with Fade(1,1,2)

    pause(2)

    label tests1:

        scene progaudit
        with Fade(1,1,2)

        Prepod "Уважаемые студенты, сегодня мы пройдем с вами **ТЕМА**, просьба не отвлекаться, так как тема очень важна для последующих занятий."

        "place test here!!!!!"

    label Razeb:

        scene iritenter
        with Fade(1,1,2)

        $ chanse = renpy.random.randint(1,11)

        if chanse == 6:
                
            call down
        else:
            jump godpnigstyle

    label down:

        "Егор, сюда надо написать момент с подскальзывание на 'говне'"

    label godpnigstyle:

        $ timez = 80
        $ time_range = 80

        menu:
            "съебаться":
                jump run
            "быть пуськой":
                jump pussyboi
            "переч в лицо":
                jump illfuckyou

        label run:

            noname "Эээ, куда?! А ну стой, с**а!"

            voice "Нужно было ходить на физ-ру, чтобы быстрее бегать в такие критические моменты."

            gg "Ааа, ну за что мне это все, что я сделал?"

            voice "Он начинает отрываться от преследователей и скрывается за поворотом"

            gg "Куда бежать?"

            gg ""
return