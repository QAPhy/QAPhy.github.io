function validate(){
var username = document.getElementById("username").value;
var password = document.getElementById("password").value;
if ( username == "username1" && password == "password1"){
   location="index/Medical_Physics_Education.html";
  }
  else{
    alert("Invalid username or password");
    }
  return false;
  }
