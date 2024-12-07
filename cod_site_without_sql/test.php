<?php
// $host = ;
// $user = 'root';
// $password = 'root';
// $db_new = 'news';

$conn = new mysqli('localhost', 'root', 'root', 'news');

 $news = mysqli_query($conn, "SELECT * FROM `new_inf`");

 $result = mysqli_fetch_assoc($news);

 print_r($result);

if ($conn->connect_error) {
    die("Ошибка подключения: " . $conn->connect_error);
}
echo "Успешное подключение к базе данных.";
?>


