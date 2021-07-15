const userInfoBox = document.querySelector("#userInfoBox");

const getUser = async () => {
  try {
    // jsonplaceholder의 API에 axios를 사용해서 request
    // GET /users/:id 형식으로 원하는 id의 user정보를 가져온다.
    // javascript 비동기 세션 13 참고
    // axios로 api에 요청하여 response받고, setUserInfo를 사용해 userInfoBox의 text를 바꿔준다.
    /*

    -- 직접 작성해보세요! --


    
    */
    var user = {}

    const res = await axios.get('https://jsonplaceholder.typicode.com/users/1')
    setUserInfo(res.data)
    
  } catch (error) {
    console.log(error);
  }
};

const setUserInfo = ( {name, username, email, phone} ) => {
  // userInfoBox안에 user정보를 보여주도록 하는 함수
  // dom element안의 내용을 어떻게 바꿀수 있을지 고민해보고 작성해보세요!
  // 작성 후 위의 axios response를 가공하는데 사용
  /*
  
  -- 직접 작성해보세요! --

  */
 userInfoBox.innerText = `
 이름 : ${name}
 아이디 : ${username}
 이메일 : ${email}
 전화번호 : ${phone}`
};
