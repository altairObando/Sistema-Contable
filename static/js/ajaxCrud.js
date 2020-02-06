'use strict';
/**
$(function () {
    var loading = $("#loading").hide();
    $(document).ajaxStart(function () {
        $("#modal-default-body").hide();
        loading.show();
    }).ajaxStop(function () {
        loading.hide();
        $("#parcialCreateUpdate").show();
    });
});
**/

function loadForm(uri, title){
    $("#modal-default-body").html("");
    $(".modal-title").text(title.replace(new RegExp('&nbsp', 'g'), ' '));
    $("#modal-default").modal();
    $.ajax({
        type: "GET",
        url : uri,
        success: function(result){
            $("#modal-default-body").html(result);
        }
    }).fail(function(xhr){
        $("#modal-default-body").html(xhr);
    });
}

function submitForm(form){
    $.validator.unobtrusive.parse(form);
    if($(form).valid()){
        $.ajax({
           type: 'POST',
           url: form.action,
            data: $(form).serialize(),
            success: function(result){
                let icono = result.guardado ? 'success' : 'error';
                swal.fire({
                   title: "Operación finalizada",
                   text: result.mensaje,
                   icon: icono
               });
                dataTable.ajax.reload();
                $("#modal-default").modal("hide");
                $('[data-toggle="tooltip"]').tooltip();
            }
        });
    }else{
        return false;
    }
    return false;
}

function deleteForm(url){
    Swal.fire({
        title: "¿Esta seguro de eliminar esto?",
        message: "Confirme la eliminación de este elemento",
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, eliminar!'
    }).then((result) =>{
       if(result.value){
           $.ajax({
               url: url,
               method: "POST",
               dataType: "JSON",
               success: function(response){
                   let icono = response.guardado ? 'success' : 'error';
                    swal.fire({
                       title: "Operación finalizada",
                       text: response.mensaje,
                       icon: icono
                   });
                    dataTable.ajax.reload();
                    $('[data-toggle="tooltip"]').tooltip();
               }
           });
       }else{
           swal.fire({
                   title: "Operación cancelada",
                   text: "No se ha eliminado el elemento",
                   icon: "success"
               });
       }
    });
}

