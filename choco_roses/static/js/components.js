const $tableID = $("#table"),
	$BTN = $("#export-btn"),
	$EXPORT = $("#export");


$(".box-add").on("click", "i", () => {
	var box_name = $("#box-name").val();
	let newTr = `\n<tr class="hide">\n  <td class="pt-3-half" contenteditable="true">${box_name}</td><td>\n <span class="table-remove"><button type="button" class="btn iq-bg-danger btn-rounded btn-sm my-0">Remove</button></span>\n  </td>\n</tr>`;

	$tableID.find("tbody tr").length && $("tbody").append(newTr)
}),

$tableID.on("click", ".table-remove", function() {
    $(this).parents("tr").detach()})