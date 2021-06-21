$(function () {
    $('#data').DataTable({
        responsive: true, //Ajuste de datos dependiendo del ancho del dispositivo
        autoWidth: false, //Respeta los anchos seteados en la tabla
        destroy: true, 
        deferRender: true, //Se usa cuando los datos superan los 50mil registros
        ajax: {
            url: window.location.pathname, //trabajamos dentro de la misma url
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [ //Nombre de mis atributos/campos del modelo
            {"data": "id"},
            {"data": "name"},
            {"data": "desc"},
            {"data": "opciones"},
        ],
        columnDefs: [ //Defino la caracteristica de las columnas
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/sis/category/update/' + row.id + '/" type="button" class="btn btn-outline-success btn-sm"><i class="fas fa-pencil-alt"></i></a> ';
                    buttons += '<a href="/sis/category/delete/' + row.id + '/" type="button" class="btn btn-outline-danger btn-sm"><i class="fas fa-eraser"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {
        }
    });
});