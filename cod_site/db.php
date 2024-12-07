<?php
$host = 'localhost';
$user = 'root';
$password = 'root';
$db = 'users_regist';

$conn = new mysqli($host, $user, $password, $db);

if ($conn->connect_error) {
    die("Ошибка подключения: " . $conn->connect_error);
}
echo "Успешное подключение к базе данных.";
?>
