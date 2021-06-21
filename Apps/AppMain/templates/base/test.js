{ % if form.errors % }
var errors = ''; { % for field in form % } { % for error in field.errors % }
errors += '{{ error }}\n'; { % endfor % } { % endfor % }

Swal.fire({
    title: 'Error!',
    text: errors,
    icon: 'error'
}); { % endif % }

$('form').on('submit', function(e) {
    e.preventDefault();

    // var parameters = $(this).serializeArray();
    // Permite una colección de objetos del tipo file (imagenes, documentos, archivos)
    var parameters = new FormData(this);
    submit_with_ajax(window.location.pathname, 'Notificación',
        '¿Estas seguro de realizar la siguiente acción?', parameters,
        function() {
            location.href = '{{ list_url }}';
        });
});