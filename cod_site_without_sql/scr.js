document.addEventListener('DOMContentLoaded', () => {
    ymaps.ready(init);
});

function init() {
    try {
        const trafficElement = document.getElementById('traffic-score');
        if (!trafficElement) {
            console.error('Элемент для отображения данных о пробках не найден.');
            return;
        }

        const mapContainer = document.createElement('div');
        mapContainer.id = 'map';
        mapContainer.style.display = 'none'; // Скрываем карту
        document.body.appendChild(mapContainer);

        const map = new ymaps.Map('map', {
            center: [45.035470, 38.975313], // Координаты Краснодара
            zoom: 10,
            controls: []
        });

        const trafficControl = new ymaps.control.TrafficControl({ state: { providerKey: 'traffic#actual' } });
        map.controls.add(trafficControl);

        const trafficProvider = trafficControl.getProvider('traffic#actual');
        if (trafficProvider && trafficProvider.state) {
            trafficProvider.state.events.once('change', () => {
                console.log('Провайдер данных о пробках готов.');
                updateTraffic(trafficControl, trafficElement);
            });
        } else {
            console.error('Провайдер данных о пробках не инициализирован.');
        }

        setInterval(() => updateTraffic(trafficControl, trafficElement), 300000); // 5 минут
    } catch (error) {
        console.error('Ошибка при инициализации карты:', error);
    }
}

function updateTraffic(trafficControl, trafficElement) {
    const trafficProvider = trafficControl.getProvider('traffic#actual');
    if (!trafficProvider) {
        console.error('Провайдер данных о пробках не найден.');
        trafficElement.textContent = 'Нет данных о пробках.';
        return;
    }

    if (!trafficProvider.state) {
        console.error('Состояние провайдера недоступно.');
        trafficElement.textContent = 'Нет данных о пробках.';
        return;
    }

    trafficProvider.state.events.once('change', () => {
        const trafficLevel = trafficProvider.state.get('level');
        trafficElement.textContent = trafficLevel !== null && typeof trafficLevel !== 'undefined' 
            ? `Пробки: ${trafficLevel} баллов`
            : 'Нет данных о пробках.';
    });

    try {
        trafficProvider.update();
    } catch (error) {
        console.error('Ошибка при обновлении данных о пробках:', error);
        trafficElement.textContent = 'Ошибка получения данных.';
    }
}