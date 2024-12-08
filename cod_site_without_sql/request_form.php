<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="styles.css">
    <link rel="shortcut icon" href="./image/group.png" type="image/x-icon">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Форма заявки ЦОДД</title>
    <style>
       
        
    </style>
</head>
<body class="req_bod">

    <div class="container">
        <h2>Форма заявки</h2>
        <form action="/submit" method="post" enctype="multipart/form-data">
            
            <div class="form-group">
                <label for="fullName">ФИО заявителя</label>
                <input type="text" id="fullName" name="fullName" required>
            </div>

            <div class="form-group">
                <label for="email">Электронная почта</label>
                <input type="email" id="email" name="email" required>
            </div>

            <div class="form-group">
                <label for="phone">Телефон</label>
                <input type="tel" id="phone" name="phone" required>
            </div>

            <div class="form-group">
                <label for="location">Местоположение проблемы</label>
                <input type="text" id="location" name="location" required>
            </div>

            <div class="form-group">
                <label for="description">Описание проблемы</label>
                <textarea id="description" name="description" required></textarea>
            </div>

            <div class="form-group">
                <label for="image">Прикрепить изображение (опционально)</label>
                <input type="file" id="image" name="image" accept="image/*">
                <span class="file-label">Выберите изображение для прикрепления (jpg, png, gif и т.д.)</span>
                <div class="file-info" id="file-info"></div>
            </div>

            <div class="form-actions">
                <button type="submit">Отправить заявку</button>
            </div>

        </form>
        <div class="back-button">
            <a href="news_index.php">Назад к новостям</a>
        </div>
    </div>

    <script src="scriptt.js"></script>

</body>
</html>
