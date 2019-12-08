var apiUrl = location.protocol + '//' + location.host + "/api/";

$(document).ready(function() {
    
    document.getElementById("form").addEventListener('submit',function(evt){
        console.log("test");
        //get user input data
      evt.preventDefault();
      var username = $("#usernameInput").val();
      var password = $("#passwordInput").val();
      console.log(username);
      console.log(password);
      //check user inputs
      if (username == "") {
        alert("Enter username");
        return;
      } else if (password == "") {
        alert("Enter password");
        return;
      }
    
      //create json data
      var inputData = '{' + '"username" : "' +username + '", ' + '"password" : "' + password + '"}';
    
      //make ajax call to get the desired data
      $.ajax({
        type: 'POST',
        url: apiUrl + 'check_account',
        data: inputData,
        dataType: 'json',
        contentType: 'application/json',
        beforeSend: function() {
          //alert('Fetching....');
        },
        success: function(data) {
          //plot the returned data
          redirect(data);
        },
        error: function(jqXHR, textStatus, errorThrown) {
          //reload on error
          alert("Error: Try again")
          console.log(errorThrown);
          console.log(textStatus);
          console.log(jqXHR);
    
          location.reload();
        },
        complete: function() {
          //alert('Complete')
        }
      });
    
    
    });
});

function redirect(data)
{
    if(data != " ")
    {
        location.replace(location.protocol + '//' + location.host + '/map')
        
    }
    else{
        alert("Invalid username or password")
    }
   
}


