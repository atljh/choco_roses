
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


$(document).ready(function () {
    $("#saveorder").on("click", function () {
        $.ajax({
            data: $("#order_form").serialize(), // get the form data
            type: $(this).attr('method'), // GET or POST
            url: "/crm/add_bucket/",
            // url: "{% url 'add-bucket' %}",

            // on success
            success: function (response) {
                        alert("S " + response.price);
                    },

            // on error
            error: function (response) {
                alert(response.responseJSON.errors);
                console.log(response.responseJSON.errors)
            }
        });
        return false;
    });
})



// Validate
$(document).ready(function () {
    $("#number").change(function () {
      var username = $(this).val();
      $.ajax({
            url: '/crm/validate_number/',
            data: {
                'number': number
            },
            dataType: 'json',
            success: function (data) {
                 if (data.result) {
                 alert("Username already taken");

                 }
            }
      });
    });
})
