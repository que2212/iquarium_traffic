let currentMap;

const coordinates = [
    { lat: 45.033915, lon: 38.974063, title: "Перекресток Северная и Красная", Image:"./image/cam_krd.jpg", url: "перейти к камере" },
    { lat: 45.036392, lon: 38.971892, title: "Перекресток Северная и Тургенева", Image:"./image/cam_krd.jpg" },
    { lat: 45.033124, lon: 38.973567, title: "Перекресток Красная и Октябрьская", Image:"./image/cam_krd.jpg" },
    { lat: 45.052776, lon: 38.970568, title: "Перекресток Красных Партизан и Гагарина", Image:"./image/cam_krd.jpg" },
    { lat: 45.035493, lon: 38.979744, title: "Перекресток Дзержинского и Лузана",  }
];

const createBalloonContent = (point) => {
    let content = `<h3>${point.title}</h3>`;
    if (point.Image) {
        content += `<img src="${point.Image}" alt="${point.title}" style="width:200px;height:auto;">`;
    }
    return content;
};

function init2GISMap() {
    if (!mapgl) {
        console.error("mapgl library is not loaded");
        return;
    }

    currentMap = new mapgl.Map('map', {
        key: '5f4462d5-1c6e-4cb3-a122-1c4f2ae10732',
        center: [38.97584111279573, 45.03996344849367],
        zoom: 15,
        trafficControl: 'topRight',
    });

    coordinates.forEach(coord => {
        const marker = new mapgl.Marker(currentMap, {
            coordinates: [coord.lon, coord.lat],
        });
       
    });
}

function initYandexMap() {
    if (!ymaps) {
        console.error("Yandex Maps library is not loaded");
        return;
    }

    ymaps.ready(() => {
        currentMap = new ymaps.Map('map', {
            center: [45.03996344849367, 38.97584111279573],
            zoom: 15,
            controls: ['trafficControl'],
            
        });



        const createBalloonContent = (point, index) => {
            let content = `<div><h3>${point.title}</h3>`;
    
            if (point.Image) {
                content += `<img src="${point.Image}" alt="${point.title}" style="width:200px;height:auto;">`;
            }
    
            // Добавляем input range только для второго и пятого объекта
            if (index === 4) {
                content += `
                    <div style="margin-top: 10px;">
                        <label for="range_${point.lat}_${point.lon}">Изменение Светофора:</label>
                        <input id="range_${point.lat}_${point.lon}" type="range" min="0" max="100" value="50" 
                               oninput="document.getElementById('range_value_${point.lat}_${point.lon}').innerText = this.value">
                        <span id="range_value_${point.lat}_${point.lon}">50сек</span>
                    </div>
                `;
            }
    
            content += `</div>`;
            return content;
        };

        coordinates.forEach((point, index) => {
            try {
                const placemark = new ymaps.Placemark([point.lat, point.lon], {
                    balloonContent: createBalloonContent(point, index)
                }, {
                    balloonCloseButton: true,
                    hideIconOnBalloonOpen: false
                });
                currentMap.geoObjects.add(placemark);
            } catch (error) {
                console.error('Ошибка при добавлении метки:', error, point);
            }
        });
    });
}

function switchMap(useYandex) {
    if (currentMap) {
        if (currentMap.destroy) {
            currentMap.destroy(); 
        } else {
            document.getElementById('map').innerHTML = ''; 
        }
    }

    if (useYandex) {
        initYandexMap();
    } else {
        init2GISMap();
    }
}

// Обработчик переключения карт
document.getElementById('mapToggle').addEventListener('change', (e) => {
    switchMap(e.target.checked);
});

// Инициализация карты по умолчанию (2GIS)
init2GISMap();





$('.menu-btn').on('click', function (e) {
    e.preventDefault();
    $('.menu').toggleClass('menu_active');
    $('.content').toggleClass('content_active');
});


const apiKey = 'b56b9673d6fb4a9bb9595322240712'; 


const url = `https://api.weatherapi.com/v1/current.json?key=${apiKey}&q=Krasnodar&lang=ru`;


function getWeather() {
  fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error('Не удалось получить данные о погоде');
      }
      return response.json();
    })
    .then(data => {
      const temperature = data.current.temp_c;  // Температура
      const condition = data.current.condition.text;  // Условия погоды
      const icon = data.current.condition.icon;  // Иконка погоды
      const location = data.location.name;  // Название города

      document.getElementById('temperature').textContent = `${temperature}°C`;
      document.getElementById('condition').textContent = condition;
      document.getElementById('icon').src = `https:${icon}`;
      document.getElementById('location').textContent = location;
    })
    .catch(error => {
      document.getElementById('condition').textContent = 'Ошибка загрузки';
      console.error('Ошибка:', error);
    });
}


getWeather();


document.addEventListener('DOMContentLoaded', () => {
    const trafficImage = document.getElementById('trafficImage');

    if (trafficImage) {
        trafficImage.addEventListener('click', () => {
            if (trafficImage.src.includes('traffic.png')) {
                trafficImage.src = 'traffic_point.png';
            } else {
                trafficImage.src = 'traffic.png';
            }
        });
    } else {
        console.error('Element with ID "trafficImage" not found.');
    }

    const eventImage = document.getElementById('eventImage');

    if (eventImage) {
        eventImage.addEventListener('click', () => {
            if (eventImage.src.includes('event.png')) {
                eventImage.src = 'event_point.png';
            } else {
                eventImage.src = 'event.png';
            }
        });
    } else {
        console.error('Element with ID "eventImage" not found.');
    }

    const camImage = document.getElementById('camImage');

    if (camImage) {
        camImage.addEventListener('click', () => {
            if (camImage.src.includes('camera.png')) {
                camImage.src = 'camera_point.png';
            } else {
                camImage.src = 'camera.png';
            }
        });
    } else {
        console.error('Element with ID "camImage" not found.');
    }
});





