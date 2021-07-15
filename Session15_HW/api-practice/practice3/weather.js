const input = document.querySelector('#city')
const button = document.querySelector('#submit')
const weatherBox = document.querySelector('#weatherBox')
const cities = ['New york', 'London', 'Paris', 'Dubai']

const API_KEY = "ec54d362c42f1e731fbdefab436f5dd5"

button.addEventListener('click', async()=>{

  // input에 입력된 도시명을 사용하여 적절한 uri로 날씨정보 요청
  // response받아서 weatherBox에 적절하게 넣어준다.
  // innerHTML활용!
  // weatherBox html template 예시
  /*
    `<div class="name">${name}</div>
     <img class="icon" src="http://openweathermap.org/img/w/${icon}.png">
     <div class="main">${main}</div>
     <div class="description">${description}</div>
     <div class="temp">${temp}°C</div>`
  */

  /*

  
  --직접 작성해보세요--
  api.openweathermap.org/data/2.5/weather?q={city name}&appid={API_KEY}

  */

  try {
    var res = await axios.get(
      `https://api.openweathermap.org/data/2.5/weather?q=${input.value}&appid=${API_KEY}`
    );
  

  var { main, description, icon} = res.data.weather[0];
  var temp = Math.round(res.data.main.temp - 273.15);
  var name = res.data.name;

  console.log(res.data.weather[0]);

  weatherBox.innerHTML += `
  <div id="myWeather">
  <div class="name" style="font-weight:bold; font-size:25px">${name}</div>
  <p>Now</p>
  <img class="icon" src="./icon/${icon}.png">
  <div class="temp">${temp}°C</div>
  <div class="main">${main}</div>
  <div class="description">${description}</div></div>
  `;
  
  for (let i = 0; i<cities.length; i++){
    var res = await axios.get(
      `https://api.openweathermap.org/data/2.5/weather?q=${cities[i]}&appid=${API_KEY}`
    );
  

    var { main, description, icon} = res.data.weather[0];
    var temp = Math.round(res.data.main.temp - 273.15);
    var name = res.data.name;

    console.log(res.data.weather[0]);

    weatherBox.innerHTML += `
    <div id="weather">
    <div class="name" style="font-weight:bold; font-size:25px">${name}</div>
    <p>Now</p>
    <img class="icon" src="./icon/${icon}.png">
    <div class="temp">${temp}°C</div>
    <div class="main">${main}</div>
    <div class="description">${description}</div></div>
    `;

  }
} catch (error) {
  console.log(error);
}

})