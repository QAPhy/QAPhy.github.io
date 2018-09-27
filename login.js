function validate(){
var username = document.getElementById("username").value;
var password = document.getElementById("password").value;
if ( username == "root" && password == "root"){
   location="index/Medical_Physics_Education.html";
  }
  else{
    alert("Invalid username or password");
    }
  return false;
  }
