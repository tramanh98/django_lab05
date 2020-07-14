function deleteCommand(idpro) {
    $.ajax({
        url: 'http://127.0.0.1:8000/delete/'+ idpro,
        type: "DELETE",
        dataType: "json",
        success: function () {
            $('#' + idpro).remove();
            addMessage("Deleted data successfully");
        },
        error: function () {
            addMessage("Delete failed!");
        }
    });
}




  