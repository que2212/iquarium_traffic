
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ЦОДД КРД</title>
    <link rel="stylesheet" href="styless.css">
    <link rel="shortcut icon" href="./image/group.png" type="image/x-icon">
    <script src="https://api-maps.yandex.ru/2.1/?lang=ru_RU"></script>
    <script src="https://mapgl.2gis.com/api/js/v1"></script>
</head>
<body>
<div class="menu-btn"><img src="./image/menu.png"></div>
    <div class="menu">
        <ul class="menu-list">
            <ol><a href="./main_index.php">Главная</a></ol>
            <ol><a href="./news_index.php">Новости</a></ol>
            <ol><a href="./cont_index.php">Контакты</a></ol>
            <ol><a href="./analit_traffic_index.php">Аналитика</a></ol>
        </ul>
        <div class="doc">
            <a href="./instruct.docx" download>Инструкция к Использованию карты</a>
        </div>
        <div class="main_logo_menu">
            <img src="./image/biglogo.png" width='100%'>
        </div>
    </div>
    <main class="map_mainn">
        <div class="mapm">
            <div id="map"  style="width:80%; height:100vh"></div>
            <div class="main_buttns">
            <div class="map_switch">
            <span>2GIS</span>
            <label class="switch">
                <input type="checkbox" id="mapToggle">
                <span class="slider round"></span>
            </label>
            <span>Yandex</span>
        </div>

                <div class="panel">
                    <span>Панель Управления</span>
                    <div class="pan"><div class="panel_buttns">
                        <div class="main_panel_buttn">
                            <img src="./camera.png" id="camImage">
                            <a href="./cam.php">Камеры</a>
                        </div>
                        <div class="main_panel_buttn">
                            <img src="./traffic.png" id="trafficImage">
                            <a href="">Светофоры</a>
                        </div>
                        <div class="main_panel_buttn">
                            <img src="./event.png"  id="eventImage">
                            <a href="">Мероприятия</a>  
                        </div></div>
                        <div class="call_buttn">
                            <span>Вызов служб</span>
                            <div class="call"> 
                            <div class="radio">
                                <input class="custom-radio" type="radio" id="color-1" name="color" value="indigo">
                                <label for="color-1">Машина ЦОДД</label>
                            </div>
                            <div class="radio">
                                <input class="custom-radio" type="radio" id="color-2" name="color" value="red">
                                <label for="color-2">Полиция</label>
                            </div>
                            <div class="radio">
                                <input class="custom-radio" type="radio" id="color-4" name="color" value="yellow">
                                <label for="color-4">Пожарные</label>
                            </div>
                            <div class="radio">
                                <input class="custom-radio" type="radio" id="color-5" name="color" value="green">
                                <label for="color-5">Скорая</label>
                            </div>

                        </div>
                    </div>
                </div></div>
                <div class="weather">
                <div class="weather-container">
                    <div class="icon-container">
                    <img id="icon" src="" alt="Иконка погоды">
                    </div>
                    <div class="info-container">
                    <div class="temp" id="temperature">--°C</div>
                    <div class="condition" id="condition">Загрузка...</div>
                    <div class="location" id="location">Краснодар</div>
                    </div>
                 </div>
                </div>
                <div class="panel_notif">
                    <span>Панель Уведомлений</span>
                    <div class="notific">
                        <div class="notif_mess">
                            <span>На улице Северной образовалась <b>ДТП</b></span>
                        </div>
                        <div class="notif_mess">
                            <span>На улице Мачуги образовалась <b>Пробка</b></span>
                        </div>
                        <div class="notif_mess">
                            <span>На улице Северной образовалась <b></b></span>
                        </div>
                        <div class="notif_mess">
                            <span>На улице Северной образовалась <b>Пробка</b></span>
                        </div>
                        <div class="notif_mess">
                            <span>На улице Северной образовалась <b>Пробка</b></span>
                        </div>
                    </div>
                </div>
            </div>
           
</label>
                </div>
            </div>
        </div>
    </main>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="script.js"></script>
</body>
</html>