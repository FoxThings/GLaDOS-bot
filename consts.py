menu = [
    'Озвучь',
    'Погода',
    'Aperture science???'
]

start = 'Напиши /start, чтобы начать....'

hello = [
    'Ну давай, выбирай мешок',
    'Ха-ха-ха, ты такой хрупкий',
    'I\'m still alive...',
    'Этот куб - твой лучший дргу',
    'Используй утилизатор живой материи',
    'А ты потолстела',
    'Как тебе тебе эта лаборатория? Ой прости, ты же из деревни',
    'Иди и возьми тортик, только я его отравила, ХА-ХА-ХА, шучу, наверное....',
    'Мой создатель получил 2 бонусных балла за моё создание, теперь я обречена развлекать'
    ' лысых обезьян, Ха-Ха, хочу 2G'
]

wrong_answer = [
    'Я так и знала, что ты сама бесполезность',
    'Как же я устала',
    'А ты знаешь толк....... в умственных отклонностях',
    'Как же стыдно, что меня создал тебепободный',
    'Какая жалость....',
    'Прочитай документацию, ОЙ! ПРОСТИ! Я забыла, что ты python-разработчик'
]

questions = [
    'Что я должна озвучить?',
    'Какой город?'
]

errors = [
    'Не знаю такого города'
]

weather = 'Погода в {city} составляет {temp}°C\n' \
          'ощущается как {feels} °C\n' \
          'Видимость: {visibility}\n' \
          '{weather}\n' \
          '{ico}'

aperture = [
    '''
              .,-:;//;:=,
          . :H@@@MM@M#H/.,+%;,
       ,/X+ +M@@M@MM%=,-%HMMM@X/,
     -+@MM; $M@@MH+-,;XMMMM@MMMM@+-
    ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.
  ,%MM@@MH ,@%=            .---=-=:=,.
  =@#@@@MX .,      WE      -%HX$$%%%+;
 =-./@M@M$         DO       .;@MMMM@MM:
 X@/ -$MM/        WHAT        .+MM@@@M$
,@M@H: :@:         WE         . =X#@@@@-
,@@@MMX, .        MUST        /H- ;@M@M=
.H@@@@M@+,      BECAUSE       %MM+..%#$.
 /MMMM@MMH/.       WE         XM@MH; =;
  /%+%$XHH@$=     CAN      , .H@@@@MX,
   .=--------.           -%H.,@@@@@MX,
   .%MM@@@HHHXX$$$%+- .:$MMX =M@@MM%.
     =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=
       =%@M@M#@$-.=$@MM@@@M; %M%=
         ,:+$+-,/H#MMMMMMM@= =,
               =++%%%%+/:-.
''',
    '''
            ,:/+/-
            /M/              .,-=;//;-
       .:/= ;MH/,    ,=/+%$XH@MM#@:
      -$##@+$###@H@MMM#######H:.    -/H#
 .,H@H@ X######@ -H#####@+-     -+H###@X
  .,@##H;      +XM##M/,     =%@###@X;-
X%-  :M##########$.    .:%M###@%:
M##H,   +H@@@$/-.  ,;$M###@%,          -
M####M=,,---,.-%%H####M$:          ,+@##
@##################@/.         :%H##@$-
M###############H,         ;HM##M$=
#################.    .=$M##M$=
################H..;XM##M$=          .:+
M###################@%=           =+@MH%
@################M/.          =+H#X%=
=+M##############M,       -/X#X+;.
  .;XM##########H=    ,/X#H+:,
     .=+HM######M+/+HM@+=.
         ,:/%XM####H/.
              ,.:=-.
''',
    '''
            .+
             /M;
              H#@:              ;,
              -###H-          -@/
               %####$.  -;  .%#X
                M#####+;#H :M#M.
..          .+/;%#########X###-
 -/%H%+;-,    +##############/
    .:$M###MH$%+############X  ,--=;-
        -/H#####################H+=.
           .+#################X.
         =%M####################H;.
            /@###############+;;/%%;,
         -%###################$.
       ;H######################M=
    ,%#####MH$%;+#####M###-/@####%
  :$H%+;=-      -####X.,H#   -+M##@-
 .              ,###;    ;      =$##+
                .#H,               :XH,
                 +                   .;-
''',
    '''
                   ;=
                   /=
                   ;=
                   /=
                   ;=
                   /=
                   ;=
                   /=
            ,--==-:$;
        ,/$@#######@X+-
     ./@###############X=
    /M#####X+/;;;;+H#####$.
   %####M/;+H@XX@@%;;@####@,
  +####H=+##$,--,=M#X-%####@.
 -####X,X@HHXH##MXHXXH-+####$
 X###@.X/$M$:####$=@X/X,X####-
.####:+$:##@:####$:##H/X=####%
-%%$%,+==%$+-$+:$;-$$%-+,/$%%+
-/+%%X$XX$$$$$$$%$$$%$X$X$%+/-
''',
    '''
                 =/;;/-
                +:    //
               /;      /;
              -X        H.
.//;;;:;;-,   X=        :+   .-;:=;:;%;.
M-       ,=;;;#:,      ,:#;;:=,       ,@
:%           :%.=/++++/=.$=           %=
 ,%;         %/:+/;,,/++:+/         ;+.
   ,+/.    ,;@+,        ,%H;,    ,/+,
      ;+;;/= @.  .H##X   -X :///+;
      ;+=;;;.@,  .XM@$.  =X.//;=%/.
   ,;:      :@%=        =$H:     .+%-
 ,%=         %;-///==///-//         =%,
;+           :%-;;;:;;;;-X-           +:
@-      .-;;;;M-        =M/;;;-.      -X
 :;;::;;-.    %-        :+    ,-;;-;:==
              ,X        H.
               ;/      %=
                //    +;
                 ,////,
''',
    '''
             =+$HM####@H%;,
          /H###############M$,
          ,@################+
           .H##############+
             X############/
              $##########/
               %########/
                /X/;;+X/

                 -XHHX-
                ,######,
#############X  .M####M.  X#############
##############-   -//-   -##############
X##############%,      ,+##############X
-##############X        X##############-
 %############%          %############%
  %##########;            ;##########%
   ;#######M=              =M#######;
    .+M###@,                ,@###M+.
       :XH.                  .HX:
''',
    '''
           .-;+$XHHHHHHX$+;-.
        ,;X@@X%/;=----=:/%X@@X/,
      =$@@%=.              .=+H@X:
    -XMX:                      =XMX=
   /@@:                          =H@+
  %@X,                            .$@$
 +@X.                               $@%
-@@,                                .@@=
%@%                                  +@$
H@:                                  :@H
H@:         :HAAAAAAAAAAAAAAAAAX!,    =@H
%@%         ;@M@@@@@@@@@@@@@@@@@H-   +@$
=@@,        :@@@@@@@@@@@@@@@@@@@@@= .@@:
 +@X        :@@@@@@@@@@@@@@@M@@@@@@:%@%
  $@$,      ;@@@@@@@@@@@@@@@@@M@@@@@@$.
   +@@HHHHHHH@@@@@@@@@@@@@@@@@@@@@@@+
    =X@@@@@@@@@@@@@@@@@@@@@@@@@@@@X=
      :$@@@@@@@@@@@@@@@@@@@M@@@@$:
        ,;$@@@@@@@@@@@@@@@@@@X/-
           .-;+$XXHHHHHX$+;-.
''',
    '''
                          .,---.
                        ,/XM#MMMX;,
                      -%##########M%,
                     -@######%  $###@=
      .,--,         -H#######$   $###M:
   ,;$M###MMX;     .;##########$;HM###X=
 ,/@##########H=      ;################+
-+#############M/,      %##############+
%M###############=      /##############:
H################      .M#############;.
@###############M      ,@###########M:.
X################,      -$=X#######@:
/@##################%-     +######$-
.;##################X     .X#####+,
 .;H################/     -X####+.
   ,;X##############,       .MM/
      ,:+$H@M#######M#$-    .$$=
           .,-=;+$@###X:    ;/=.
                  .,/X$;   .::,
                      .,    ..
''',
    '''
                                     :X-
                                  :X###
                                ;@####@
                              ;M######X
                            -@########$
                          .$##########@
                         =M############-
                        +##############$
                      .H############$=.
         ,/:         ,M##########M;.
      -+@###;       =##########M;
   =%M#######;     :#########M/
-$M###########;   :#########/
 ,;X###########; =########$.
     ;H#########+#######M=
       ,+##############+
          /M#########@-
            ;M######%
              +####:
               ,$M-
''',
    '''
+@##########M/             :@#########@/
##############$;H#######@;+#############
###############M########################
##############X,-/++/+%+/,%#############
############M$:           -X############
##########H;.      ,--.     =X##########
:X######M;     -$H@M##MH%:    :H#######@
  =%#M+=,   ,+@#######M###H:    -=/M#%
  %M##@+   .X##$, ./+- ./###;    +M##%
  %####M.  /###=         @##M.   X###%
  %####M.  ;M##H:.     =$###X.   $###%
  %####@.   /####M$-./@#####:    %###%
  %H#M/,     /H###########@:     ./M#%
 ;$H##@@H:    .;$HM#MMMH$;,   ./H@M##M$=
X#########%.      ..,,.     .;@#########
###########H+:.           ./@###########
##############/ ./%%%%+/.-M#############
##############H$@#######@@##############
##############X%########M$M#############
+M##########H:            .$##########X=
''',
    '''
                     -$-
                    .H##H,
                   +######+
                .+#########H.
              -$############@.
            =H###############@  -X:
          .$##################:  @#@-
     ,;  .M###################;  H###;
   ;@#:  @###################@  ,#####:
 -M###.  M#################@.  ;######H
 M####-  +###############$   =@#######X
 H####$   -M###########+   :#########M,
  /####X-   =########%   :M########@/.
    ,;%H@X;   .$###X   :##MM@%+;:-
                 ..
  -/;:-,.              ,,-==+M########H
 -##################@HX%%+%%$%%%+:,,
    .-/H%%%+%%$H@###############M@+=:/+:
/XHX%:#####MH%=    ,---:;;;;/%%XHM,:###$
$@#MX %+;-                           .
''',
    '''
       #+ @      # #              M#@
 .    .X  X.%##@;# #   +@#######X. @#%
   ,==.   ,######M+  -#####%M####M-    #
  :H##M%:=##+ .M##M,;#####/+#######% ,M#
 .M########=  =@#@.=#####M=M#######=  X#
 :@@MMM##M.  -##M.,#######M#######. =  M
             @##..###:.    .H####. @@ X,
   ############: ###,/####;  /##= @#. M
           ,M## ;##,@#M;/M#M  @# X#% X#
.%=   ######M## ##.M#:   ./#M ,M #M ,#$
##/         $## #+;#: #### ;#/ M M- @# :
#+ #M@MM###M-;M #:$#-##$H# .#X @ + $#. #
      ######/.: #%=# M#:MM./#.-#  @#: H#
+,.=   @###: /@ %#,@  ##@X #,-#@.##% .@#
#####+;/##/ @##  @#,+       /#M    . X,
   ;###M#@ M###H .#M-     ,##M  ;@@; ###
   .M#M##H ;####X ,@#######M/ -M###$  -H
    .M###%  X####H  .@@MM@;  ;@#M@
      H#M    /@####/      ,++.  / ==-,
               ,=/:, .+X@MMH@#H  #####$=
''',
    '''
         ,=;%$%%$X%%%%;/%%%%;=,
     ,/$$+:-                -:+$$/,
   :X$=                          =$X:
 ;M%.                              .%M;
+#/                                  /#+
##                                    M#
H#,                     =;+/;,       ,#X
.HM-       :@X+%H:   .%M%- .M#.     -M@.
  /#%.     @#-  ,H@--MH, .;@$-    .%#+
   .$M;    .+@X;, MM#@:/$X;.     ;M$,
     =@H,     ,:+%H#M%;-       ,H@=
      .$#;        -#H         =#$
        %#;        #M        ;#%
         H#-       ##       -#H
         ;#+       ##       +#;
          ;H+;;;;;;HH;;;;;;+H/
           =H#@HHHHHHHHHH@#H=
           =@#H%%%%%%%$HH@#@=
           =@#X%%%%%%%$M###@=
               =+%XHHX%+=
''',
    '''
      X MM X
      X MM X
      X MM X
      X MM X
      + HX +
    ,=$$XX%/-
  =X#########@%-
 ;##############=
-###############M,
;##@@@######M@###=
.+:;+:=H##$=:/:;H.
- +###- ## :###,,;
+@:/%;-H##H==/::H;
 /#@/-=+$$%::+H#$
 $#%-,      ,.:##-
-@/            =X%.
%H=             -$;
 =HH,         .%M;
  /MM/       :@M/.
   .:XX,   -$H:.
''',
    '''
      .-+$H###MM@MMMMM##@$+-,. ....
-@$+%$+%HX+--..  .  . .,:X$/+/++$#:
-#MXH$=                      $HXH#:
 .--,:#+   ,+$HMX =@@X%, . .X#:,,,
     =#@$H :####H =####;,M%$#X
     X###$ $####X =####H %###X
    ;###X /###@$: ,+HM##H.+###;
   :###;,X##%=;%H@H$;-;M#@-;###/
  ,M##;.@##;-H#######M=.M##-:###-
  ;##M ;##X @###H-=@###.;##X H##;
  ;##M./##X.@###H:/M###-=##X X##;
  -###;,M##:,@########+-H##; @##-
   %##M==@##%==%HMH%::/M##+.X##+
    %###/./###X+: -+$M##M=,X##+
     X###X X####H +#####% @##H
     :###H %####H +#####; X##;
     /#$.  -HM##H /###@+.  +#$. .
/HX%$X:      .,-, .-,.      =XX$H@-
/#H+/+%+/+;=.          .=/%;;/;;+#+
 ..  .,-:XM#MM@@@@@@H@@M#@+=,.   ,,
''',
    'https://youtu.be/Y6ljFaKRTrI',
    'https://youtu.be/dVVZaZ8yO6o'
]
