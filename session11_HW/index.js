const getRandomHexaColor = () => {
  const hexa = '0123456789abcdef';
  let color = '#';
  for (let i=0; i<6; i++) {
      color += hexa[Math.floor(Math.random()*16)];
      // console.log(color);
  }
  return color;
};

setInterval(() => {
  document.querySelector("body").style.backgroundColor = getRandomHexaColor();

},300);

const clockContent = document.querySelector('.time');

const getCurrentTime = () => {
  const date = new Date();
  const year = date.getFullYear();
  const month = date.getMonth() +1;
  const day = date.getDate();
  const hours = date.getHours();
  const minutes = date.getMinutes();
  const seconds = date.getSeconds();
  text = `${year}년 ${month < 10 ? `0${month}` : month}월 ${day < 10 ? `0${day}` : day}일` + 
  ` ${hours < 10 ? `0${hours}` : hours}시 ${minutes < 10 ? `0${minutes}` : minutes}분 ${seconds < 10 ? `0${seconds}` : seconds}초`;
  clockContent.innerText = text;
  console.log(text);
};

const initClock = () => {
  getCurrentTime();
  setInterval(getCurrentTime,1000);

};

initClock();