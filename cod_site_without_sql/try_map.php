<?php
$apiKey = 'df305867-e7a6-4a41-8a21-af99d469613d'; // Замените на свой API-ключ
$bbox = '37.36,55.56~37.9,55.92'; // Координаты для области (например, Москва)
$url = "https://api-maps.yandex.ru/services/traffic-info/2.0/?bbox=$bbox&lang=ru_RU&apikey=$apiKey";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    "Accept: application/json"  // Указываем, что ожидаем JSON в ответе
));
$response = curl_exec($ch);
curl_close($ch);

// Проверка на успешность выполнения запроса
if ($response === false) {
    echo "Ошибка при выполнении запроса: " . curl_error($ch);
} else {
    // Декодируем JSON-ответ
    $data = json_decode($response, true);
    echo '<pre>';
    print_r($data);  // Выводим данные для проверки
    echo '</pre>';
}

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch);
$info = curl_getinfo($ch); // Получаем информацию о запросе
curl_close($ch);

echo "Ответ сервера: " . $info['http_code']; // Код ответа сервера

// Если код 200, значит запрос успешный
if ($info['http_code'] == 200) {
    $data = json_decode($response, true);
    echo '<pre>';
    print_r($data);  // Выводим данные для проверки
    echo '</pre>';
} else {
    echo "Ошибка при запросе. Статус: " . $info['http_code'];
    echo "<pre>";
    print_r($response); // Выводим весь ответ
    echo "</pre>";
}





?>


<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Баллы пробок</title>
</head>
<body>
    <h1>Баллы пробок в Москве</h1>
    <div id="traffic">Загрузка...</div>

    <script>
        async function fetchTraffic() {
            try {
                const response = await fetch('monit_index.php'); // Запрос к PHP-скрипту
                const data = await response.json();

                // Предположим, что баллы пробок находятся в "data.jams.level"
                const trafficLevel = data?.jams?.level || 'Нет данных';
                document.getElementById('traffic').innerText = `Баллы пробок: ${trafficLevel}`;
            } catch (error) {
                console.error('Ошибка:', error);
                document.getElementById('traffic').innerText = 'Ошибка загрузки данных.';
            }
        }

        fetchTraffic();
        setInterval(fetchTraffic, 60000); // Обновление каждые 60 секунд
    </script>
</body>
</html>
