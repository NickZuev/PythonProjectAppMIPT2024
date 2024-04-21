# PythonProjectAppMIPT2024
My Python project as a part of respective MIPT course. It's an app for language studing.  

## О приложении простыми словами:  
Ради чего создано это приложение? Оно создано, чтобы помогать людям учить слова из иностранных языков. Чтобы учить слова было интересней это приложение поддерживает различные кастомизации(чтобы было комфортнее учить слова), разные способы учить слова(выбирай свой), таблицу результатов(чтобы пользователь знал свои слабые места).  

## Функционал
Меню с выбором способа учить слова, настройками, help-окном, таблицей результатов.  
Сами способы учить слова с некой адаптацией под пользователя.  

## Архитектура:
1. class App
2. class WindowsFactory - паттерн проектирования "Фабрика" для создания окон
###### Дочерние классы:
- AchievementsWindow  
- CardsCreationsWindow 
- CardsWindow 
- ExtractorFromFileWindow 
- HelpWindow  
- InputWindow 
- MenuWindow
- SettingsWindow
- SetupColorWindow


3. CardsWindow:
###### Методы:
- get_next_card(state) - получить следующую карточку нужной(в зависимости от state) стороной вверх
- flip() - перевернуть карточку
- increment() - понизить частоту встречаемости
- decrement() - повысить частоту встречаемости 

4. ExtractorFromFileWindow:
###### Методы:
- extract_from_file(file_path) - получить набор карточек из файла с путём filepath в формате word : translation

5. InputWindow:
###### Методы:
- add_new_card(word, translation) - создаёт новую карточку из аргументов

6. SetupColorWindow
###### Методы:
- change_color(background_colour, text_colour) - меняет цветовую гамму всего приложения

7. class Card  
###### Методы:  
- increment() - уменьшает относительную частоту встречаемости данной карточки  
- decrement() - увеличивает относительную частоту встречаемости данной карточки
- get(state) - позволяет получить слово или перевод в зависимости от аргумента 
- get_weight() - позволяет получить вес карточки
