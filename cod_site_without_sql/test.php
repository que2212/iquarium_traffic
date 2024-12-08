<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Контейнер с прокруткой</title>
    <style>
        .scroll-container {
            width: 300px;        /* Ширина контейнера */
            height: 200px;       /* Высота контейнера */
            overflow: auto;      /* Включаем прокрутку */
            border: 1px solid #000; /* Граница для визуализации */
        }

        .content {
            height: 500px; /* Высота контента больше высоты контейнера */
            background: linear-gradient(to bottom, #f06, yellow);
        }
    </style>
</head>
<body>
    <div class="scroll-container">
        <div class="content">
            Здесь много контента, который не помещается в контейнер.
        </div>
    </div>
</body>
</html>

