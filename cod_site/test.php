


<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Уровень пробок</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        #trafficScore {
            font-size: 1.5em;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>Уровень пробок в вашем городе</h1>
    <div id="trafficScore">Загрузка данных...</div>


    <script>
    async function fetchTrafficData() {
        const proxyUrl = './proxy.php'; // Путь к вашему прокси
        try {
            const response = await fetch(proxyUrl);
            if (!response.ok) {
                throw new Error('Ошибка сети: ' + response.statusText);
            }
            const data = await response.json();

            // Извлекаем уровень пробок
            const trafficLevel = data?.traffic?.level || 'нет данных';
            document.getElementById('trafficScore').textContent = `Уровень пробок: ${trafficLevel}`;
        } catch (error) {
            console.error('Ошибка при получении данных о пробках:', error);
            document.getElementById('trafficScore').textContent = 'Ошибка загрузки данных.';
        }
    }

    fetchTrafficData();
</script>

</script>

</body>
</html>
