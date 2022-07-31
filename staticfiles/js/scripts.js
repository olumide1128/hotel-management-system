/*!
* Start Bootstrap - Simple Sidebar v6.0.5 (https://startbootstrap.com/template/simple-sidebar)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-simple-sidebar/blob/master/LICENSE)
*/
// 
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }


});


//Search Validation for Empty Input
function searchValidate(){
    var search = document.getElementById('form1').value;
    if(search == "" || search == null){
        document.getElementById('searchErr').style.display = 'block';
        console.log("Input is empty!");
        return false;
    }else{
        return true;
    }
}


$('#roomType').change(function(){
    var optionSelected = $(this).find("option:selected");
    var valueSelected  = optionSelected.val();

    var csrftoken = getCookie('csrftoken');

    $.ajax({
        type: 'POST',
        headers:{'X-CSRFToken':csrftoken},
        url: "/process_select/",
        data: {
            "valueSelected":valueSelected 
        },
        success: function(data){
            console.log(data.rooms);

            $('#room').html("<option  selected disabled=''>Select Room</option>");

            $.each(data.rooms, function (i, room) {
                $('#room').append($('<option>', { 
                    value: room,
                    text : room
                }));
            });
        }
    });
});


$(document).ready(function(){
    $('#guest_detail').change(function(){
        var optionSelected = $(this).find("option:selected");
        var valueSelected  = optionSelected.val();
    
        var csrftoken = getCookie('csrftoken');
    
        $.ajax({
            type: 'POST',
            headers:{'X-CSRFToken':csrftoken},
            url: "/process_guest_detail/",
            data: {
                "valueSelected":valueSelected 
            },
            success: function(data){
                console.log(data);
                
                console.log(data.first_name);
    
                $('#firstName').val(data.first_name);
                $('#lastName').val(data.last_name);
                $('#phone').val(data.phone);
                $('#Address').val(data.Address);
                $('#card_num').val(data.card_num);
                $('#card_cvv').val(data.card_cvv);
                $('#card_expiry').val(data.card_expiry);
                
            }
        });
    });
});



function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;

}


//FormValidation (Checkin and Reservation Form)
function validateCheckinReserveForm(){

    var firstName = document.getElementById('firstName').value;
    var lastName = document.getElementById('lastName').value;
    var phone = document.getElementById('phone').value;
    var Address = document.getElementById('Address').value;
    var roomType = document.getElementById('roomType').value;
    var room = document.getElementById('room').value;
    var no_of_persons = document.getElementById('no_of_persons').value;
    var card_num = document.getElementById('card_num').value;
    var card_cvv = document.getElementById('card_cvv').value;
    var card_expiry = document.getElementById('card_expiry').value;
    var Checkin = document.getElementById('Checkin').value;
    var Checkout = document.getElementById('Checkout').value;

    if(firstName == "" || lastName == "" || phone == "" || Address == "" || roomType == "Select Room Type" || 
    room == "Select Room" || no_of_persons == "Select No of Persons" || card_num == "" || card_cvv == "" ||
    card_expiry == "" || Checkin == "" || Checkout == ""){
        displayError("Error: All Fields must be Filled!");
        return false;
    }else if(!/^[a-zA-Z]+$/.test(firstName) || !/^[a-zA-Z]+$/.test(lastName) ){
        displayError("Error: Name must contain only letters!");
        return false;
    }else if(!/^\d+$/.test(phone)){
        displayError("Error: Phone Number must contain only Numbers!");
        return false;
    }else if(!/^\d{16}$/.test(card_num)){
        displayError("Error: Card Number must be 16 digits and contain only Numbers!");
        return false;
    }else if(!/^\d{3}$/.test(card_cvv)){
        displayError("Error: Card CVV must be 3 digits and contain only Numbers!");
        return false;
    }else if(!/^\d{2}\/\d{4}$/.test(card_expiry)){
        displayError("Error: Card Expiry must be in the format 'mm/yyyy'!");
        return false;
    }else{
        hideError();
        return true;
    }
}


function validateRoomForm(){

    var roomNum = document.getElementById('roomNum').value;
    var roomPrice = document.getElementById('roomPrice').value;
    var roomType = document.getElementById('roomType').value;

    if(roomNum == "" || roomPrice == "" || roomType == "Select Room Type"){
        displayError("Error: All Fields must be Filled!");
        return false;
    }else if(!/^\d+$/.test(roomNum)){
        displayError("Error: Room Number must contain only Numbers!");
        return false;
    }else if(!/^\d+\.?\d*$/.test(roomPrice)){
        displayError("Error: Price must be Numeric!");
        return false;
    }else{
        hideError();
        return true;
    }

}



function validateStaffForm(){
    

    var firstName = document.getElementById('firstname').value;
    var lastName = document.getElementById('lastname').value;
    var email = document.getElementById('email').value;
    var address = document.getElementById('address').value;
    var dob = document.getElementById('dob').value;
    var department = document.getElementById('department').value;
    

    if(firstName == "" || lastName == "" || email == "" || address == "" || dob == "" || department == "Select Department"){
        displayError("Error: All Fields must be Filled!");
        return false;
    }else if(!/^[a-zA-Z]+$/.test(firstName) || !/^[a-zA-Z]+$/.test(lastName)){
        displayError("Error: Name must contain only letters!")
        return false;
    }else if(!/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)){
        displayError("Error: Incorrect Email Format!");
        return false;
    }else{
        hideError();
        return true;
    }

}



function displayError(msg){

    document.getElementById("errMsg").innerHTML = msg;
    document.getElementById("errBox").style.display = "block";

}

function hideError(){
    document.getElementById("errBox").style.display = "none";
}