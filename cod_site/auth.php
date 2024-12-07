<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Авторизация</title>
    <link rel="stylesheet" href="styless.css">
    <link rel="shortcut icon" href="./image/group.png" type="image/x-icon">
    <script src="https://mapgl.2gis.com/api/js/v1"></script>
</head>
<body class="regist_body">
    <form class="register_form" action="./monit_index.php" method="POST">
        <img src="./image/mainlogo.png" width="20%">
        <h2>Регистрация</h2>
        <div class="regist_inputs"><label>Введите ваш Логин</label>
        <input type="text" name="login" placeholder="Введите логин" required>
        <label>Введите ваш Пароль</label>
        <input type="text" name="password" placeholder="Введите пароль" required></div>
        <button type="submit" name="submit">Войти</button>
        <p>Нет аккаунтф? <a href="./regist_index.php">Зарегистрироваться</a></p>

    </form>
</body>
</main>
    <script src="script.js"></script>
    
</body>

</html>

 <?php
session_start();
include 'db.php';

$error = '';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = trim($_POST['login']);
    $password = $_POST['password'];

    if (empty($username) || empty($password)) {
        $error = "Пожалуйста, заполните все поля.";
    } else {
        $sql = "SELECT id, password FROM users WHERE login = ?";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("s", $username);
        $stmt->execute();
        $stmt->store_result();

        if ($stmt->num_rows == 1) {
            $stmt->bind_result($user_id, $hashed_password);
            $stmt->fetch();

            if (password_verify($password, $hashed_password)) {
                $_SESSION['user_id'] = $user_id;
                
            header("Location: monit_index.php");
            exit();

            } else {
                $error = "Неверное имя пользователя или пароль.";
            }
        } else {
            $error = "Неверное имя пользователя или пароль.";
        }
    }
}
?> 
