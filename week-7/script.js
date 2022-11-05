const jsonUrl = "http://127.0.0.1:3000/api/member?username="

let jsonData = {};
let username;

function search(){
    fetch(jsonUrl, {method: "get"})
        .then((response) =>{
            return response.json();
        }).then((data) =>{
            jsonData=data.data;
            username = jsonData['name'];
            let myDiv = document.querySelector("#search");
            let newDiv = document.createElement("div");
            newDiv.textContent = username;
            myDiv.appendChild(newDiv);
        })
}