
$(document).ready(function () {
    var copies=1;
    $("#add").on("click", function () {
        var clone = $( "#bucket" )
        .clone(true, true).attr('id','bucket_'+(copies++)).appendTo(".order-body");
    });
});


$(document).ready(function () {
    var copies=1;
    $("#addcolour").on("click", function () {
        table = $(this).parent().find('.colour_table');
        $("#colour").clone(true, true).attr('id','colour_'+(copies++)).appendTo(table);
    });
});



//$(document).ready(function () {
//    $("#saveorder").on("click", function () {
//        $.ajax({
//            data: $("#order_form").serialize(),
//            type: $(this).attr('method'),
//            url: "/crm/add_bucket/",
//
//            success: function (response) {
//                        alert("S " + response.price);
//                    },
//
//            error: function (response) {
//                alert("Error");
//            }
//        });
//        return false;
//    });
//})


// GET CSRF TOKEN
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');



$(document).ready(function () {
    $("#saveorder").on("click", function () {
//        var bucket = $( ".bucket" ).find('.iq-card-body').find('.form-group').find('.form-control')
        var bucket = $( ".bucket" ).find('.iq-card-body')
        const items = [];
        bucket.each(function(){
            bucket_items = $(this).find('.form-group').find('.form-control');
            const temp = [];
            bucket_items.each(function(){
                item = $(this).val()
                temp.push(item);
//                if (item != ''){
//                    items.push(item);
//                    }
            });
            items.push(temp);
        });
        console.log(items)

        $.ajax({
            data: {
                  'items': JSON.stringify(items),
//                'items':items,
                csrfmiddlewaretoken: csrftoken,
            },
            type: "POST",
            url: "/crm/add_bucket/",

            success: function (response) {
                        alert ('All done ok');
                    },

            error: function (response) {
                alert("Error");
            }
        });
        return false;
    });
})



// Validate number

$(document).ready(function () {
    $("#number").change(function () {
      $.ajax({
            url: '/crm/validate_number/',
            data: $("#number").serialize(),
            dataType: 'json',
            success: function (data) {
                 if (data.result) {
                 console.log('Ok')
                 }
                 else {
                 alert("No");
                 }
            },
            error: function(){
                alert("failure");
        }
      });
    });
})



// Validate name_surname

$(document).ready(function () {
    $("#name_surname").change(function () {
      $.ajax({
            url: '/crm/validate_name/',
            data: $("#name_surname").serialize(),
            dataType: 'json',
            success: function (data) {
                 if (data.result) {
                 console.log('Ok')
                 }
                 else {
                 alert("No");
                 }
            },
            error: function(){
                alert("failure");
        }
      });
    });
})


//Validate address

$(document).ready(function () {
    $("#address").change(function () {
      $.ajax({
            url: '/crm/validate_address/',
            data: $("#address").serialize(),
            dataType: 'json',
            success: function (data) {
                 if (data.result) {
                 console.log('Ok')
                 }
                 else {
                 alert("No");
                 }
            },
            error: function(){
                alert("failure");
        }
      });
    });
})


//Validate phone

$(document).ready(function () {
    $("#phone").change(function () {
      $.ajax({
            url: '/crm/validate_phone/',
            data: $("#phone").serialize(),
            dataType: 'json',
            success: function (data) {
                 if (data.result) {
                 console.log('Ok')
                 }
                 else {
                 alert("No");
                 }
            },
            error: function(){
                alert("failure");
        }
      });
    });
})


//Validate instagram

$(document).ready(function () {
    $("#instagram").change(function () {
      $.ajax({
            url: '/crm/validate_instagram/',
            data: $("#instagram").serialize(),
            dataType: 'json',
            success: function (data) {
                 if (data.result) {
                 console.log('Ok')
                 }
                 else {
                 alert("No");
                 }
            },
            error: function(){
                alert("failure");
        }
      });
    });
})



//$('#signup-btn').click(function(event){
//    if(validate()){
//        $.ajax({
//            method: "POST",
//            url: '/register',
//            data: {
//                name :$('#id_fullname').val(),
//                email : $('#id_email').val(),
//                country : $('#id_country').val(),
//                password : $('#id_password').val(),
//                csrfmiddlewaretoken:'{{ csrf_token }}',
//
//            },
//            success: function(res) {
//                var response = $.parseJSON(res)
//                $('.signup-data').html(response.msg)
//                      if (response.code == 200) {
//                      $('.signup-data').html(response.msg);
//                      window.location = "http://localhost:8000";
//                }
//             },
//        })
//
//      })
//    }
//
//})

//function validate(){
//
//    var isValid = true;
//    if (!$('#id_fullname').val()){
//        isValid = false
//    }
//    if (!$('#id_email').val()){
//        isValid = false
//    }else{
//       if(!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test($('#id_email').val()))){
//            isValid = false;
//        }
//    }
//    if (!$('#id_country').val()){
//        isValid = false
//    }
//    if (!$('#id_password').val()){
//        isValid = false
//    }
//    return isValid;
//}





