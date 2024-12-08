<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ЦОДД КРД</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="shortcut icon" href="./image/group.png" type="image/x-icon">
    <script src="https://mapgl.2gis.com/api/js/v1"></script>
</head>
<body>
    <header>
    <div class="head_stat">
        <div class="situat">
            <h1>О ситуации на дорогах</h1>
            <div class="trafic"><span class=""id="numb_of_sit">10</span>
            <p>Высокая загруженность дорог</p></div>
        </div>
        <div class="tiem_clock">
            <img src="./image/clock.png">
            <span id="time_clck">13:00</span>
        </div>
    </div>
    <div>
        <div class="head_buttn">
            <a href="./main_index.php" class="main_buttn">Главная</a>
            <a href="./regist_index.php" class="main_buttn">Мониторинг</a>
            <img src="./image/shortlogo.png" width='5%'>
            <a href="./news_index.php" class="main_buttn">Новости</a>
            <a href="./cont_index.php" class="main_buttn">Контакты</a>
        </div>
    </div>
    </header>
    <main class="new_main">
    <div class="news_text_h1"><b>Последние новости</b></div>
    <div class="fixed_menu"><div id="map" class="news_map" style="width:100%; height:40vh"></div>
    <div class="requests">
        <span>Произошло какое-то ДТП?</span>
        <button><a href="./request_form.php">Сообщите Нам!</a></button></div>
    </div>
        <div class="news_box">
            
            <div class="new_box_info">
               <img src="./image/1.png">
                <div class="news_box_text">
                    <h1>Момент ДТП с поездом и легковушкой в Краснодарском крае попал на видео</h1>
                </div>
            </div>
            <div class="new_box_info">
               <img src="./image/2.png">
                <div class="news_box_text">
                    <h1>Поезд протаранил легковушку в Краснодарском крае, три человека пострадали</h1>
                    
                </div>
            </div>
            <div class="new_box_info">
               <img src="./image/3.png">
                <div class="news_box_text">
                    <h1>Ростовчанин погиб в ДТП в Краснодарском крае, влетев в дерево</h1>
                    
                </div>
            </div>
            <div class="new_box_info">
               <img src="./image/4.png">
                <div class="news_box_text">
                    <h1>Водитель ВАЗа погиб в ДТП с двумя автомобилями на Кубани</h1>
                    
                </div>
            </div>
            <div class="new_box_info">
              <img src="./image/5.png">
                <div class="news_box_text">
                    <h1>Под Краснодаром водитель иномарки сбил перебегавшего дорогу подростка</h1>
                    
                </div>
            </div>
            <div class="new_box_info">
               <img src="./image/6.png">
                <div class="news_box_text">
                    <h1>Дело краснодарского экс-судьи о смертельном ДТП рассмотрит Верховный суд РФ</h1>
                    
                </div>
            </div>
            <div class="new_box_info">
               <img src="./image/7.png">
                <div class="news_box_text">
                    <h1>На Кубани парень сбил несостоявшуюся тещу, кидавшую камни в его автомобил</h1>
                    
                </div>
            </div>
            <div class="new_box_info">
               <img src="./image/8.png">
                <div class="news_box_text">
                    <h1>Двое детей и один взрослый пострадали в ДТП с участием такси в Сочи</h1>
                    
                </div>
            </div>
        </div>
        </main>
    <footer>
        <div class="footer_info">
            <div class="logo_info">
                <img src="./image/logo.png" width='100%'>
            </div>
            <div class="info_block">
                <div><img src='./image/Location.png'/><p>350007, Российская Федерация, Краснодарский край, г. Краснодар, ул. Рашпилевская, 157</p></div>
                <div><img src='./image/Phone.png'/><p>+7 (861) 991-28-50</p></div>
                <div><img src='./image/Email.png'/><p>codd@codd.krasnodar.ru</p></div>
            </div>
        </div>
    </footer>
    <script src="scriptt.js"></script>
    
</body>
</html>
