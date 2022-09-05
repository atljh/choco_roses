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




const $tableID = $("#table"),
	$BTN = $("#export-btn"),
	$EXPORT = $("#export");


$(".box-add").on("click", "i", () => {
	var box_name = $(".box-add-input").val();
    //0 === $tableID.find("tbody tr").length &&

    $.ajax({
        data: {
            'box_name': box_name,
            'csrfmiddlewaretoken': csrftoken,
        },
        type: "POST",
        url: "/crm/add_box/",

        success: function (response) {
                console.log(response.box_id)
                let newTr = `\n<tr class="boxes">\n  <td class="box-name-label" id=${response.box_id} contenteditable="true">${box_name}</td><td><i class="ri-delete-bin-5-line text-danger box-remove"></i></td>\n</tr>`;
                $tableID.find("table").append(newTr)
                },
        error: function (response) {
            alert("Error");
        }
    });
}),



$tableID.on("click", ".box-remove", function() {
    var box_id = $(this).parents("tr").find('.box-name-label').attr('id');
    var tr = $(this).parents("tr")

    $.ajax({
        data: {
            'box_id': box_id,
            'csrfmiddlewaretoken': csrftoken,
            },
            type: "POST",
            url: "/crm/delete_box/",

            success: function (data) {
                 if (data.status === 'good') {
                    tr.detach()
                 }
                 else {
                    alert(data.status);
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
    $.ajax({
        data: {
            'box_id': box_id,
            'box_name': box_name,
            'csrfmiddlewaretoken': csrftoken,
            },
        type: "POST",
        url: "/crm/update_box/",

        success: function (data) {
             if (data.result) {
             console.log('Ok')
             }
        },
        error: function(){
            alert("failure");
            }
    })
});



//ROSE PACKING

$(".packing-add").on("click", "i", () => {
	var packing_name = $(".packing-add-input").val();
	var packing_id = $(this).attr('id');


    $.ajax({
        data: {
            'packing_name': packing_name,
            'csrfmiddlewaretoken': csrftoken,
        },
        type: "POST",
        url: "/crm/add_packing/",

        success: function (response) {
            let newTr = `\n<tr class="packings">\n  <td class="packing-name-label" id=${response.packing_id} contenteditable="true">${packing_name}</td><td><i class="ri-delete-bin-5-line text-danger packing-remove"></i></td>\n</tr>`;
            $tableID.find("table").append(newTr)
            },
        error: function (response) {
            alert("Error");
        }
    });
});



$tableID.on("click", ".packing-remove", function() {
    var packing_id = $(this).parents("tr").find('.packing-name-label').attr('id');
    var tr = $(this).parents("tr");

    $.ajax({
        data: {
            'packing_id': packing_id,
            'csrfmiddlewaretoken': csrftoken,
            },
            type: "POST",
            url: "/crm/delete_packing/",

            success: function (response) {
                 if (response.status == 'good') {
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
