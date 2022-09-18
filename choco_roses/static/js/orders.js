// CLONE BUCKET FORM
$(document).ready(function () {
    var copies=1;
    $("#add").on("click", function () {
        var clone = $( ".bucket" )
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


// GET ORDER

$(document).ready(function () {
    $("#saveorder").on("click", function () {

        var order = $('.order').find('.iq-card-body').find('.form-group').find('.form-control');
        var orders_details = {};
        order.each(function(){
            var order_field = $(this);
            var order_field_name = order_field.attr('name');
            orders_details[order_field_name] = order_field.val();
        });

        var checkbox = $('.order').find('.iq-card-body').find('.checkbox').find('.check');
        checkbox.each(function(){
            var checkbox_field = $(this).prop("checked");
            var checkbox_name = $(this).attr('name');
            orders_details[checkbox_name] = checkbox_field;
        });

        var bucket = $( ".bucket" ).find('.iq-card-body');
        var all_buckets = [];
        var images_list = [];

        var csrftoken = $( "input[name='csrfmiddlewaretoken']" ).val();
        var formData = new FormData();

        var bucket_id = 0;
        bucket.each(function(){
            bucket_id++;
            var bucket_fields = $(this).find('.form-group').find('.form-control');
            var bucket_values = {};
            bucket_values['id'] = bucket_id;
            var colours_list = [];
            var image = $(this).find('.form-group').find('.custom-file').find('.custom-file-input').prop('files')[0];
            formData.append(`${bucket_id}`, image);
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

//        for (i = 0; i < images_list.length; i++) {
//                        formData.append('file' + i, images_list[i]);
//                    }
//
        formData.append('order', JSON.stringify(orders_details));
        formData.append('buckets', JSON.stringify(all_buckets));
        formData.append('csrfmiddlewaretoken', csrftoken);

        $.ajax({
//            data: {
//                'order': JSON.stringify(orders_details),
//                'buckets': JSON.stringify(all_buckets),
//                'image': formData.append('images', JSON.stringify(images_list)),
//                'csrfmiddlewaretoken': formData.append('csrfmiddlewaretoken', csrftoken);,
//            },
            data: formData,
            type: "POST",
            url: "/crm/save_order/",
            cache: false,
            processData: false,
            contentType: false,

            success: function (response) {
                        alert ('All done ok');
//                        location.href = "/crm/orders/"
                    },

            error: function (response) {
                alert("Error");
            }
        });
        return false;
    });
})

// Delete order

$(document).ready(function () {
    $(".deleteorder").on("click", function () {
        var order_number = $(this).attr("order_number");
        var csrftoken = $( "input[name='csrfmiddlewaretoken']" ).val();
        var tr = $(this).parents("tr");

        $.ajax({
            data: {
                'order_number': order_number,
                'csrfmiddlewaretoken': csrftoken,
                },
            type: "POST",
            url: "/crm/delete_order/",

            success: function (response) {
                    tr.detach()
            },

            error: function (response) {
                alert("Error");
            }
        });
    });
    })


$(document).ready(()=>{
      $('.custom-file-input').change(function(){
        const file = this.files[0];
        var image = $(this).parent('.custom-file').find('.output_image');
        if (file){
          let reader = new FileReader();
          reader.onload = function(event){
            image.attr('src', event.target.result);
          }
          reader.readAsDataURL(file);
        }
      });
    });


// Validate number

//$(document).ready(function () {
//    $("#number").change(function () {
//      $.ajax({
//            url: '/crm/validate_number/',
//            data: $("#number").serialize(),
//            dataType: 'json',
//            success: function (data) {
//                 if (data.result) {
//                 console.log('Ok')
//                 }
//                 else {
//                 alert("No");
//                 }
//            },
//            error: function(){
//                alert("failure");
//        }
//      });
//    });
//})
//
//
//
//// Validate name_surname
//
//$(document).ready(function () {
//    $("#name_surname").change(function () {
//      $.ajax({
//            url: '/crm/validate_name/',
//            data: $("#name_surname").serialize(),
//            dataType: 'json',
//            success: function (data) {
//                 if (data.result) {
//                 console.log('Ok')
//                 }
//                 else {
//                 alert("No");
//                 }
//            },
//            error: function(){
//                alert("failure");
//        }
//      });
//    });
//})
//
//
////Validate address
//
//$(document).ready(function () {
//    $("#address").change(function () {
//      $.ajax({
//            url: '/crm/validate_address/',
//            data: $("#address").serialize(),
//            dataType: 'json',
//            success: function (data) {
//                 if (data.result) {
//                 console.log('Ok')
//                 }
//                 else {
//                 alert("No");
//                 }
//            },
//            error: function(){
//                alert("failure");
//        }
//      });
//    });
//})
//
//
////Validate phone
//
//$(document).ready(function () {
//    $("#phone").change(function () {
//      $.ajax({
//            url: '/crm/validate_phone/',
//            data: $("#phone").serialize(),
//            dataType: 'json',
//            success: function (data) {
//                 if (data.result) {
//                 console.log('Ok')
//                 }
//                 else {
//                 alert("No");
//                 }
//            },
//            error: function(){
//                alert("failure");
//        }
//      });
//    });
//})
//
//
////Validate instagram
//
//$(document).ready(function () {
//    $("#instagram").change(function () {
//      $.ajax({
//            url: '/crm/validate_instagram/',
//            data: $("#instagram").serialize(),
//            dataType: 'json',
//            success: function (data) {
//                 if (data.result) {
//                 console.log('Ok')
//                 }
//                 else {
//                 alert("No");
//                 }
//            },
//            error: function(){
//                alert("failure");
//        }
//      });
//    });
//})
//
//
//$(document).ready(function () {
//    $("#delivery_data").change(function () {
//      $.ajax({
//            url: '/crm/validate_delivery_data/',
//            data: $("#delivery_data").serialize(),
//            dataType: 'json',
//            success: function (data) {
//                 if (data.result) {
//                 console.log('Ok')
//                 }
//                 else {
//                 alert("No");
//                 }
//            },
//            error: function(){
//                alert("failure");
//        }
//      });
//    });
//})
//
//
//$(document).ready(function () {
//    $("#pickup_data").change(function () {
//      $.ajax({
//            url: '/crm/validate_pickup_data/',
//            data: $("#pickup_data").serialize(),
//            dataType: 'json',
//            success: function (data) {
//                 if (data.result) {
//                 console.log('Ok')
//                 }
//                 else {
//                 alert("No");
//                 }
//            },
//            error: function(){
//                alert("failure");
//        }
//      });
//    });
//})
//
//
//$(document).ready(function () {
//    $("#payment").change(function () {
//      $.ajax({
//            url: '/crm/validate_payment/',
//            data: $("#payment").serialize(),
//            dataType: 'json',
//            success: function (data) {
//                 if (data.result) {
//                 console.log('Ok')
//                 }
//                 else {
//                 alert("No");
//                 }
//            },
//            error: function(){
//                alert("failure");
//        }
//      });
//    });
//})
//
//$(document).ready(function () {
//    $("#from_where").change(function () {
//      $.ajax({
//            url: '/crm/validate_from_where/',
//            data: $("#from_where").serialize(),
//            dataType: 'json',
//            success: function (data) {
//                 if (data.result) {
//                 console.log('Ok')
//                 }
//                 else {
//                 alert("No");
//                 }
//            },
//            error: function(){
//                alert("failure");
//        }
//      });
//    });
//})
//
//
//$(document).ready(function () {
//    $("#description").change(function () {
//      $.ajax({
//            url: '/crm/validate_description/',
//            data: $("#description").serialize(),
//            dataType: 'json',
//            success: function (data) {
//                 if (data.result) {
//                 console.log('Ok')
//                 }
//                 else {
//                 alert("No");
//                 }
//            },
//            error: function(){
//                alert("failure");
//        }
//      });
//    });
//})
//
//$(document).ready(function () {
//    $("#total_price").change(function () {
//      $.ajax({
//            url: '/crm/validate_total_price/',
//            data: $("#total_price").serialize(),
//            dataType: 'json',
//            success: function (data) {
//                 if (data.result) {
//                 console.log('Ok')
//                 }
//                 else {
//                 alert("No");
//                 }
//            },
//            error: function(){
//                alert("failure");
//        }
//      });
//    });
//})
//
//$(document).ready(function () {
//    $("#price").change(function () {
//      $.ajax({
//            url: '/crm/validate_price/',
//            data: $("#price").serialize(),
//            dataType: 'json',
//            success: function (data) {
//                 if (data.result) {
//                 console.log('Ok')
//                 }
//                 else {
//                 alert("No");
//                 }
//            },
//            error: function(){
//                alert("failure");
//        }
//      });
//    });
//})






