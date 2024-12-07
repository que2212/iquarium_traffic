
// var timeElement = document.getElementById('time_clck');

// function updateTime() {
//   var currentTime = new Date();
//   var hours = currentTime.getHours().toString().padStart(2, '0');
//   var minutes = currentTime.getMinutes().toString().padStart(2, '0');
//   timeElement.textContent = hours + ':' + minutes;
// };


// updateTime();

// setInterval(updateTime, 1000);


let currentMap;

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

        document.getElementById('mapToggle').addEventListener('change', (e) => {
            switchMap(e.target.checked);
        });

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




