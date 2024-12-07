<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Toggle Image</title>
    <style>
        img {
            cursor: pointer;
        }
        body{
            background-color:grey;
        }
    </style>
</head>
<body>
    <img id="trafficImage" src="traffic.png" alt="Traffic Image" width="200">
    <script >// Находим элемент изображения по ID
const trafficImage = document.getElementById('trafficImage');

// Добавляем обработчик события "click"
trafficImage.addEventListener('click', () => {
    // Проверяем текущий src и меняем его
    if (trafficImage.src.includes('traffic.png')) {
        trafficImage.src = 'traffic_point.png';
    } else {
        trafficImage.src = 'traffic.png';
    }
});
</script>
</body>
</html>
