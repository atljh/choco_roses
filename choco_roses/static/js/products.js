$(document).ready(function () {
    $(".save-product").on("click", function () {
        var product = $('.product').find('.iq-card-body').find('.form-group').find('.form-control');
        var product_values = {};
        product.each(function(){
            var field = $(this);
            var field_name = field.attr('name');
            var colours_list = [];
            if (field_name == 'colours'){
                colours_list.push(field.val())
                product_values[field_name] = colours_list;
            }
            else {
                product_values[field_name] = field.val();
            }
        });
        var image = $('.product').find('.form-group').find('.product-img-edit').find('.p-image').find('.file-upload').prop('files')[0];
        var csrftoken = $( "input[name='csrfmiddlewaretoken']" ).val();
        var formData = new FormData();

        formData.append('product', JSON.stringify(product_values));
        formData.append('image', image);
        formData.append('csrfmiddlewaretoken', csrftoken);
    
        $.ajax({
            data: formData,
            type: "POST",
            url: "/crm/save_product/",
            cache: false,
            processData: false,
            contentType: false,

            success: function (response) {
                        console.log('All done ok');
//                        location.href = "/crm/products/"
                    },

            error: function (response) {
                console.log("Error");
            }
        });
        return false;
    });
})