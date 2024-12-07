<?php
include('db.php');
session_start();

if (isset($_POST['submit']) && !empty($_POST['login']) && !empty($_POST['password'])) {
    $login = trim($_POST['login']);
    $pass = trim($_POST['password']);

    if (strlen($login) < 3 || strlen($login) > 255) {
        die("Логин должен содержать от 3 до 255 символов.");
    }

    if (strlen($pass) < 6) {
        die("Пароль должен содержать минимум 6 символов.");
    }

    // Проверка уникальности логина
    $sql_check = "SELECT id FROM `users` WHERE `login` = ?";
    $stmt_check = $conn->prepare($sql_check);
    $stmt_check->bind_param("s", $login);
    $stmt_check->execute();
    $stmt_check->store_result();

    if ($stmt_check->num_rows > 0) {
        die("Этот логин уже используется.");
    }
    $stmt_check->close();

    // Хэширование пароля
    $hashed_pass = password_hash($pass, PASSWORD_DEFAULT);

    // Вставка данных в таблицу
    $sql_insert = "INSERT INTO `users` (`login`, `password`) VALUES (?, ?)";
    $stmt_insert = $conn->prepare($sql_insert);

    if ($stmt_insert) {
        $stmt_insert->bind_param("ss", $login, $hashed_pass);

        if ($stmt_insert->execute()) {
            echo "Данные успешно добавлены!";
            $_SESSION['user_id'] = $stmt_insert->insert_id;
            header("Location: monit_index.php");
            exit();
        } else {
            die("Ошибка выполнения запроса: " . $stmt_insert->error);
        }

        $stmt_insert->close();
    } else {
        die("Ошибка подготовки запроса: " . $conn->error);
    }
} else {
    die("Пожалуйста, заполните все поля формы.");
}

$conn->close();
?>
