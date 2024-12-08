<?php
$apiKey = "ВАШ_API_КЛЮЧ"; // Укажите ваш API-ключ
$lat = "45.035470";       // Широта Краснодара
$lon = "38.975313";       // Долгота Краснодара
$url = "https://api.weather.yandex.ru/v2/forecast?lat=$lat&lon=$lon&lang=ru_RU";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_HTTPHEADER, ["X-Yandex-API-Key: $apiKey"]);

$response = curl_exec($ch);

// Проверяем ошибки CURL
if (curl_errno($ch)) {
    http_response_code(500);
    echo json_encode(["error" => "Ошибка CURL: " . curl_error($ch)]);
    curl_close($ch);
    exit;
}

// Проверяем HTTP-код ответа
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

if ($httpCode !== 200) {
    http_response_code($httpCode);
    echo json_encode(["error" => "Ошибка API. HTTP-код: $httpCode"]);
    exit;
}

// Если всё успешно, возвращаем ответ
header('Content-Type: application/json');
echo $response;
?>
