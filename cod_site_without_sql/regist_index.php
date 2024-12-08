<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ЦОДД КРД</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="shortcut icon" href="./image/group.png" type="image/x-icon">
    <script src="https://mapgl.2gis.com/api/js/v1"></script>
</head>
<body class="regist_body">
<form class="register_form" action="./auth.php" method="POST">

        <img src="./image/mainlogo.png" width="20%">
        <h2>Регистрация</h2>
        <div class="regist_inputs"><label>Введите ваш Логин</label>
        <input type="text" name="login" placeholder="Введите логин" required>
        <label>Введите ваш Пароль</label>
        <input type="text" name="password" placeholder="Введите пароль" required></div>
        <button type="submit" name="submit">Зарегистрироваться</button>
        <p>Уже есть аккаунт? <a href="./auth.php">Войти</a></p>

    </form>
</body>
</html>
