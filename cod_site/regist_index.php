
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>РЕГИСТРАЦИЯ</title>
    <link rel="stylesheet" href="style.css">
    <link rel="shortcut icon" href="./image/group.png" type="image/x-icon">
    <script src="https://mapgl.2gis.com/api/js/v1"></script>
</head>
<body>
<main class="main_singup">
    <div class="registr_main">
        <img src="./image/mainlogo.png" width="10%">
        <form action="./register.php" method="post">
            <div class="register_form"><label for="login">Ваш Логин</label>
            <input type="text" name="login"  placeholder="Введите ваш логин"></input>
            <label for="email">Ваш email</label>
            <input type="email" name="email"  placeholder="Введите ваш email"></input>
            <label for="pass">Ваш Пароль</label>
            <input type="password" name="pass"  placeholder="Введите ваш пароль"></input>
            <label for="pass">Повторите Пароль</label>
            <input type="password" name="repeatpass"  placeholder="Введите ваш пароль"></input>
        </div>
            <input type="submit" value="Зарегистрироваться">
        </form> 
    </div>
</main>
    <script src="script.js"></script>
    
</body>

</html>