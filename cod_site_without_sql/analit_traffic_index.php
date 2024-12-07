
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ЦОДД КРД</title>
    <link rel="stylesheet" href="styless.css">
    <link rel="shortcut icon" href="./image/group.png" type="image/x-icon">
    <script src="https://mapgl.2gis.com/api/js/v1"></script>
</head>
<body>
    <header>
    <div class="head_stat">
        <div class="situat">
            <h1>О ситуации на дорогах</h1>
            <div class="trafic"><span class=""id="numb_of_sit">10</span>
            <p>Высока загруженность дорог</p></div>
        </div>
        <div class="tiem_clock">
            <img src="./image/clock.png">
            <span id="time_clck">13:00</span>
        </div>
    </div>
    <div>
        <div class="head_buttn">
            <a href="./main_index.php" class="main_buttn">Главная</a>
            <a href="./monit_index.php" class="main_buttn">Мониторинг</a>
            <img src="./image/shortlogo.png">
            <a href="./news_index.php" class="main_buttn">Новости</a>
            <a href="./cont_index.php" class="main_buttn">Контакты</a>
        </div>
    </div>
    </header>
    <main>
        <div class="graphics"></div><iframe src='./graph1.html'width="100%" height="800" frameborder="0"></iframe>
        <iframe src='./graph2.html'width="100%" height="800" frameborder="0"></iframe>
        <iframe src='./graph3.html'width="100%" height="800" frameborder="0"></iframe>


    
        </main>
    <footer>
        <div class="footer_info">
            <div class="logo_info">
                <img src="./image/logo.png">
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