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