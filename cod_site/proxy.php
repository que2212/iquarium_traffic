<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json');

$apiKey = '5f4462d5-1c6e-4cb3-a122-1c4f2ae10732'; // Вставьте ваш API-ключ
$url = "https://api.2gis.ru/traffic?key=$apiKey&lat=55.7522&lon=37.6156";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_FAILONERROR, true);
curl_setopt($ch, CURLOPT_TIMEOUT, 10);

$response = curl_exec($ch);

if ($response === false) {
    $error = curl_error($ch);
    http_response_code(500);
    echo json_encode([
        "error" => "Ошибка запроса к API",
        "details" => $error
    ]);
    curl_close($ch);
    exit;
}

curl_close($ch);
echo $response;
?>




