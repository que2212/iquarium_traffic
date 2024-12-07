
var timeElement = document.getElementById('time_clck');

function updateTime() {
  var currentTime = new Date();
  var hours = currentTime.getHours().toString().padStart(2, '0');
  var minutes = currentTime.getMinutes().toString().padStart(2, '0');
  timeElement.textContent = hours + ':' + minutes;
};


updateTime();

setInterval(updateTime, 1000);


const map = new mapgl.Map('map', {
    key: '5f4462d5-1c6e-4cb3-a122-1c4f2ae10732',
    center: [38.97584111279573, 45.03996344849367],
    zoom: 15,
    trafficControl: 'topRight',
});


// const socket = new WebSocket('wss://ws.2gis.ru/v1/traffic');

// // Соединение установлено
// socket.onopen = function(event) {
//     console.log('WebSocket connection established');
//     socket.send(JSON.stringify({ action: "subscribe", event: "traffic-score-event" }));
// };

// // Обработка входящих сообщений
// socket.onmessage = function(event) {
//     const data = JSON.parse(event.data);
//     console.log("Received data:", data);
// };

// // Обработка ошибок подключения
// socket.onerror = function(error) {
//     console.error('WebSocket Error:', error);
//     alert('Ошибка подключения к WebSocket');
// };

// // Закрытие соединения
// socket.onclose = function(event) {
//     console.log('WebSocket connection closed');
// };


// // Объявляем функцию как async
// async function fetchTraffic() {
//     const apiKey = '5f4462d5-1c6e-4cb3-a122-1c4f2ae10732';
//     const url = 'https://catalog.api.2gis.com/2.0/transport/calculate_route?key=${apiKey}';
  
//     const body = {
//       points: [
//         { type: "start", lon: 38.974556, lat: 45.035470 }, // Точка отправления
//         { type: "end", lon: 39.015057, lat: 45.050444 }    // Точка назначения
//       ],
//       type: "car",
//       traffic: true // Учитываем пробки
//     };
  
//     try {
//       const response = await fetch(url, {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//         },
//         body: JSON.stringify(body),
//       });
  
//       if (!response.ok) throw new Error('Ошибка при загрузке данных');
//       const data = await response.json();
  
//       console.log(data); // Для проверки структуры данных
  
//       if (!data.routes || data.routes.length === 0) {
//         throw new Error('Маршрут не найден');
//       }
  
//       const legs = data.routes[0].legs;
//       if (!legs || legs.length === 0) {
//         throw new Error('Этапы маршрута не найдены');
//       }
  
//       // Извлечение времени в пути с пробками и без
//       const trafficTime = legs[0].time_with_traffic; // Время в пробках
//       const normalTime = legs[0].time;               // Время без пробок
  
//       // Проверка данных
//       if (!trafficTime || !normalTime) {
//         throw new Error('Данные о времени недоступны');
//       }
  
//       // Расчет уровня пробок
//       const trafficLevel = trafficTime / normalTime;
//       const trafficElement = document.getElementById('numb_of_sit');
//       trafficElement.textContent = 'Уровень пробок: ${Math.round(trafficLevel * 10)} баллов';
//     } catch (error) {
//       console.error(error);
//       document.getElementById('numb_of_sit').textContent = 'Ошибка загрузки данных о пробках';
//     }
//   }
  
//   // Вызываем функцию
//   fetchTraffic();