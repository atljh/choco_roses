// CLONE BUCKET FORM

$(document).ready(function () {
    var copies=1;
    $("#add").on("click", function () {
        var clone = $( "#bucket" )
        .clone(true, true).attr('id','bucket_'+(copies++)).appendTo(".order-body");
    });
});


// CLONE COLOURS FIELD

$(document).ready(function () {
    var copies=1;
    $("#addcolour").on("click", function () {
        table = $(this).parent().find('.colour_table');
        $("#colour").clone(true, true).attr('name','colours_'+(copies++)).appendTo(table);
    });
});


// GET CSRF TOKEN
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


// GET ORDER

$(document).ready(function () {
    $("#saveorder").on("click", function () {

        // Get orders fields
        var order = $('.order').find('.iq-card-body').find('.form-group').find('.form-control');
        const orders_details = {};
        order.each(function(){
            var order_field = $(this);
            var order_field_name = order_field.attr('name');
            orders_details[order_field_name] = order_field.val();
        });

        // Ger orders checkboxes
        var checkbox = $('.order').find('.iq-card-body').find('.checkbox').find('.check')
        checkbox.each(function(){
            var checkbox_field = $(this).prop("checked");
            var checkbox_name = $(this).attr('name');
            orders_details[checkbox_name] = checkbox_field;
        });


        // Get orders buckets and save to array as dict
        var bucket = $( ".bucket" ).find('.iq-card-body');
        const all_buckets = [];
        bucket.each(function(){
            bucket_fields = $(this).find('.form-group').find('.form-control');
            const bucket_values = {};
            var colours_list = [];
            bucket_fields.each(function(){
                var field = $(this);
                var field_name = field.attr('name');
                if (field_name == 'colours'){
                    colours_list.push(field.val())
                    bucket_values[field_name] = colours_list;
                }
                else {
                    bucket_values[field_name] = field.val();
                }
            });
            all_buckets.push(bucket_values);
        });


        // Send request with order data
        $.ajax({
            data: {
                'order': JSON.stringify(orders_details),
                'buckets': JSON.stringify(all_buckets),
                'csrfmiddlewaretoken': csrftoken,
            },
            type: "POST",
            url: "/crm/save_order/",

            success: function (response) {
                        alert ('All done ok');
                        location.href = "/crm/orders/"

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


$(document).ready(function () {
    $("#delivery_data").change(function () {
      $.ajax({
            url: '/crm/validate_delivery_data/',
            data: $("#delivery_data").serialize(),
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


$(document).ready(function () {
    $("#pickup_data").change(function () {
      $.ajax({
            url: '/crm/validate_pickup_data/',
            data: $("#pickup_data").serialize(),
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


$(document).ready(function () {
    $("#payment").change(function () {
      $.ajax({
            url: '/crm/validate_payment/',
            data: $("#payment").serialize(),
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

$(document).ready(function () {
    $("#from_where").change(function () {
      $.ajax({
            url: '/crm/validate_from_where/',
            data: $("#from_where").serialize(),
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


$(document).ready(function () {
    $("#description").change(function () {
      $.ajax({
            url: '/crm/validate_description/',
            data: $("#description").serialize(),
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

$(document).ready(function () {
    $("#total_price").change(function () {
      $.ajax({
            url: '/crm/validate_total_price/',
            data: $("#total_price").serialize(),
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

$(document).ready(function () {
    $("#price").change(function () {
      $.ajax({
            url: '/crm/validate_price/',
            data: $("#price").serialize(),
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





