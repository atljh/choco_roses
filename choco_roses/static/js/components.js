const $tableID = $("#table"),
	$BTN = $("#export-btn"),
	$EXPORT = $("#export");


$(".box-add").on("click", "i", () => {
	var box_name = $(".box-add-input").val();
	var csrftoken = $( "input[name='csrfmiddlewaretoken']" ).val();

    $.ajax({
        data: {
            'box_name': box_name,
            'csrfmiddlewaretoken': csrftoken,
        },
        type: "POST",
        url: "/crm/add_box/",

        success: function (response) {
                console.log(response.box_id)
                let newTr = `\n<tr class="boxes" onfocusout="change()">\n  <td class="box-name-label" id=${response.box_id} contenteditable="true">${box_name}</td><td><i class="ri-delete-bin-5-line text-danger box-remove"></i></td>\n</tr>`;
                $tableID.find("table").find("tbody").append(newTr);
                },
        error: function (response) {
            alert("Error");
        }
    });
}),




$tableID.on("click", ".box-invalid", function () {
    var box_id = $(this).parents("tr").find('.box-name-label').attr('id');
    var td = $(this).parents("td");
    var tr = $(this).parents("tr");
    var button = td.find(".box-invalid");
    let newTd = '<td><i class="las la-check text-success box-valid"></i><i class="las la-trash text-danger box-remove"></i></td>'
    var csrftoken = $( "input[name='csrfmiddlewaretoken']" ).val();

    $.ajax({
        data: {
            'box_id': box_id,
            'box_status': 'True',
            'csrfmiddlewaretoken': csrftoken,
            },
            type: "POST",
            url: "/crm/box_status/",

            success: function (response) {
                 if (response.response === 'good') {
                    td.detach()
                    tr.append(newTd)
                 }
                 else {
                    alert(response.error);
                 }
            },
            error: function(){
                alert("Error");
        }
        });

    });


$tableID.on("click", ".box-valid", function () {
    var box_id = $(this).parents("tr").find('.box-name-label').attr('id');
    var td = $(this).parents("td");
    var tr = $(this).parents("tr");
    var button = tr.find(".box-valid");
    let newTr = '<td><i class="las la-times text-danger box-invalid"></i><i class="las la-trash text-danger box-remove"></i></td>'
    var csrftoken = $( "input[name='csrfmiddlewaretoken']" ).val();

    $.ajax({
        data: {
            'box_id': box_id,
            'box_status': 'False',
            'csrfmiddlewaretoken': csrftoken,
            },
            type: "POST",
            url: "/crm/box_status/",

            success: function (response) {
                 if (response.response === 'good') {
                    td.detach()
                    tr.append(newTr)
                 }
                 else {
                    alert(response.error);
                 }
            },
            error: function(){
                alert("Error");
        }
        });

    });


$tableID.on("click", ".box-remove", function () {
    var box_id = $(this).parents("tr").find('.box-name-label').attr('id');
    var tr = $(this).parents("tr");
    var csrftoken = $( "input[name='csrfmiddlewaretoken']" ).val();

    $.ajax({
        data: {
            'box_id': box_id,
            'csrfmiddlewaretoken': csrftoken,
            },
            type: "POST",
            url: "/crm/delete_box/",

            success: function (response) {
                 if (response.response === 'good') {
                    tr.detach()
                 }
                 else {
                    alert(response.error);
                 }
            },
            error: function(){
                alert("Error");
        }
        });

    });


$('.boxes').on('blur', 'td[contenteditable]', function() {
    var box_name = $(this).parents("tr").find('.box-name-label').text()
    var box_id = $(this).attr('id');
    var csrftoken = $( "input[name='csrfmiddlewaretoken']" ).val();

    $.ajax({
        data: {
            'box_id': box_id,
            'box_name': box_name,
            'csrfmiddlewaretoken': csrftoken,
            },
        type: "POST",
        url: "/crm/update_box/",

        success: function (response) {
            if (response.response) {
                console.log('Ok')
            }
            else {
                alert(response.error);
            }
        },
        error: function(){
            alert("Error");
        }
    })
});



//ROSE PACKING

$(".packing-add").on("click", "i", () => {
	var packing_name = $(".packing-add-input").val();
	var packing_id = $(this).attr('id');
	var csrftoken = $( "input[name='csrfmiddlewaretoken']" ).val();


    $.ajax({
        data: {
            'packing_name': packing_name,
            'csrfmiddlewaretoken': csrftoken,
        },
        type: "POST",
        url: "/crm/add_packing/",

        success: function (response) {
            if (response.response === 'good') {
                let newTr = `\n<tr class="packings" onfocusout="change()">\n  <td class="packing-name-label" id=${response.packing_id} contenteditable="true">${packing_name}</td><td><i class="ri-delete-bin-5-line text-danger packing-remove"></i></td>\n</tr>`;
                $tableID.find("table").find("tbody").append(newTr)
            }
            else {
                alert(response.error);
            }
        },
        error: function (response) {
            alert("Error");
        }
    });
});




$tableID.on("click", ".packing-invalid", function () {
    var packing_id = $(this).parents("tr").find('.packing-name-label').attr('id');
    var td = $(this).parents("td");
    var tr = $(this).parents("tr");
    var button = td.find(".packing-invalid");
    let newTd = '<td><i class="las la-check text-success packing-valid"></i><i class="las la-trash text-danger packing-remove"></i></td>'
    var csrftoken = $( "input[name='csrfmiddlewaretoken']" ).val();

    $.ajax({
        data: {
            'packing_id': packing_id,
            'packing_status': 'True',
            'csrfmiddlewaretoken': csrftoken,
            },
            type: "POST",
            url: "/crm/packing_status/",

            success: function (response) {
                 if (response.response === 'good') {
                    td.detach()
                    tr.append(newTd)
                 }
                 else {
                    alert(response.error);
                 }
            },
            error: function(){
                alert("Error");
        }
        });

    });


$tableID.on("click", ".packing-valid", function () {
    var packing_id = $(this).parents("tr").find('.packing-name-label').attr('id');
    var td = $(this).parents("td");
    var tr = $(this).parents("tr");
    var button = tr.find(".packing-valid");
    let newTr = '<td><i class="las la-times text-danger packing-invalid"></i><i class="las la-trash text-danger packing-remove"></i></td>'
    var csrftoken = $( "input[name='csrfmiddlewaretoken']" ).val();

    $.ajax({
        data: {
            'packing_id': packing_id,
            'packing_status': 'False',
            'csrfmiddlewaretoken': csrftoken,
            },
            type: "POST",
            url: "/crm/packing_status/",

            success: function (response) {
                 if (response.response === 'good') {
                    td.detach()
                    tr.append(newTr)
                 }
                 else {
                    alert(response.error);
                 }
            },
            error: function(){
                alert("Error");
        }
        });

    });



$tableID.on("click", ".packing-remove", function() {
    var packing_id = $(this).parents("tr").find('.packing-name-label').attr('id');
    var tr = $(this).parents("tr");
    var csrftoken = $( "input[name='csrfmiddlewaretoken']" ).val();

    $.ajax({
        data: {
            'packing_id': packing_id,
            'csrfmiddlewaretoken': csrftoken,
            },
            type: "POST",
            url: "/crm/delete_packing/",

            success: function (response) {
                 if (response.response == 'good') {
                    tr.detach()
                 }
                 else {
                    alert(response.error);
                 }
            },
            error: function (response) {
                alert("Error");
            }
        });
    });



$('.packings').on('blur', 'td[contenteditable]', function() {
    var packing_name = $(this).parents("tr").find('.packing-name-label').text()
    var packing_id = $(this).attr('id');
    var csrftoken = $( "input[name='csrfmiddlewaretoken']" ).val();

    $.ajax({
        data: {
            'packing_id': packing_id,
            'packing_name': packing_name,
            'csrfmiddlewaretoken': csrftoken,
            },
        type: "POST",
        url: "/crm/update_packing/",

        success: function (response){
            },
        error: function(response){
            alert("failure");
            }
    })
});
