//$(document).ready(function(){
//  $("#add").click(function(){
//      var clone = $( "#dubl:first" ).clone();
////      $(clone).attr('colour1','changedId'); //change cloned element id attribute
////      $(clone).find('select').attr('id','changedId1'); //change cloned element children attribute also
//      $(clone).insertAfter( "#dubl:last" );
//  });
//});

//$(document).ready(function(){
//  $("#add").click(function(){
//      var myDiv = document.getElementById("dubl");
//      var divClone = myDiv.cloneNode(true);
//      document.body.appendChild(divClone);
//  });
//});


$(document).ready(function () {
    $("#add").on("click", function () {
        var clone = $( "#dubl:first" ).clone(false, false)
        $(clone).insertAfter( "#dubl:last" );
        console.log($(clone).attr("class"));
    });
});

//$(document).ready(function () {
//    $("#add").on("click", function () {
//        var clone = $( "#dubl:first" )
//        .clone(false, false)[0].outerHTML.replace(/(\d)/g, function(a) {
//          return parseInt(a) + 1
//        });
//        $(clone).insertAfter( "#dubl:last" );
//        console.log($(clone).attr("class"));
//    });
//});

//$(document).ready(function () {
//    $("#addcolour").on("click", function () {
//        var clone = $("#colour:last")
//        .clone(false, false)[0].outerHTML.replace(/(\d)/g, function(a) {
//          return parseInt(a) + 1
//        });
////        $(clone).appendTo("body");
////        $(clone).insertAfter( "[class^=form-group c]:last" );
//        $(clone).insertAfter( "#colour:last" );
//        console.log($(clone).attr("class"));
//    });
//});


