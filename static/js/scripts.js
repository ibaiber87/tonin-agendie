$(document).ready(function () {

    // Función para generar tarjetas en el bloque 2
    function generar_cards(eventos) {
        const $bloque2 = $('#bloque2');
        $bloque2.empty(); // Vacía el bloque antes de agregar nuevas tarjetas        
        eventos.forEach(function (evento) {
            const $card = $(`
                <a href="${evento.link ? evento.link : '#'}" target="_blank" class="text-decoration-none">
                    <div class="card">
                        <div class="card-body">                            
                            <div class="card-image">
                                <img id="img_card" src=${evento.imagen} class="img-fluid">                                    
                            </div>
                            
                            <h5 class="card-title"><strong>${evento.artistas ? evento.artistas : "-"}</strong></h5>
                            <!-- Contenedor flex para alinear el texto y la imagen en la misma línea -->
                            <div class="d-flex justify-content-between align-items-center">
                                <p class="card-text mb-0">
                                    <strong>Lekua:</strong> ${evento.lugar}<br>
                                    <strong>Data:</strong> ${evento.fecha} - ${evento.hora ? evento.hora.substring(0, 5) : ""}<br>
                                    <strong>Herria:</strong> ${evento.poblacion ? evento.poblacion : "-"} ${evento.provincia ? '(' + evento.provincia + ')' : ""}<br>
                                    <strong>Info:</strong> ${evento.web ? evento.web : "-"}<br>
                                </p>                                
                            </div>
                        </div>
                    </div>
                </a>
            `);
            
            



            // Añadir la tarjeta al bloque 2
            $bloque2.append($card);
        });
    }

    // Función para generar la tabla en el bloque 1
    function devolver_datos() {
        // Realiza una solicitud a la ruta /descargar para obtener los datos
        $.ajax({
            url: '/descargar',
            method: 'GET',
            success: function (response) {
                // Vacía la tabla actual
                const $eventosBody = $('#eventos-body');
                $eventosBody.empty();

                // Generar filas en la tabla (bloque 1)
                response.forEach(function (evento) {
                    const $row = $(`
                        <tr class="row-clickable">
                            <td class="oculto">${evento.id}</td>
                            <td>${evento.fecha}</td>
                            <td>${evento.hora ? evento.hora.substring(0, 5) : "-"}</td>                            
                            <td>${evento.artistas ? evento.artistas : "-"}</td>
                            <td>${evento.lugar ? evento.lugar : "-"}</td>
                            <td>${evento.poblacion ? evento.poblacion : "-"}</td>
                            <td>${evento.provincia ? evento.provincia : "-"}</td>
                            <td>${evento.tipo ? evento.tipo : "-"}</td>                            
                            <td>${evento.precio ? evento.precio : "-"}</td>                            
                            <td>${evento.web ? evento.web : "-"}</td>                            
                        </tr>
                    `);

                    // Agrega un evento 'click' a la fila completa
                    $row.on('click', function () {
                        const link = evento.link ? evento.link : "#";
                        window.open(link, '_blank');
                    });

                    $eventosBody.append($row);
                });

                // Generar tarjetas en el bloque 2 (para pantallas pequeñas)
                generar_cards(response);
            },
            error: function (xhr, status, error) {
                // Maneja errores en la solicitud
                alert('Error al cargar los datos: ' + error);
            }
        });
    }

    function actualizar_bd() {
        //mjuestra la etiqueta actualizando        
        $('#actualizando').removeClass('oculto');

        // Realiza una solicitud a la ruta /actualizar
        $.ajax({
            url: '/actualizar',
            method: 'GET',
            success: function (response) {
                alert('Base de datos actualizada con éxito.');
                $('#actualizando').addClass('oculto');
                location.reload();
            },
            error: function (xhr, status, error) {
                alert('Error al actualizar la base de datos: ' + error);
                $('#actualizando').addClass('oculto');
            }
        });
    }

    // Función para eliminar todos los registros
    function eliminar_datos() {
        // Preguntar al usuario si está seguro
        if (confirm('¿Estás seguro de que deseas eliminar todos los registros? Esta acción no se puede deshacer.')) {
            // Si el usuario confirma, realiza la solicitud DELETE a la ruta /eliminar_todo
            $.ajax({
                url: '/eliminar_todo',
                method: 'DELETE',
                success: function (response) {
                    alert('Todos los registros han sido eliminados con éxito.');
                    location.reload();
                },
                error: function (xhr, status, error) {
                    alert('Error al eliminar los registros: ' + error);
                }
            });
        }
    }

    // Función para borrar filtros y recargar la tabla completa
    function borrar_filtros() {
        $("#datepicker").datepicker("setDate", null);
        $('#filtroTexto').val('');
        devolver_datos();
    }

    // Función para filtrar los datos en la tabla, y los cards en dispositivos pequeños
    function filtrar_datos(filtro) {
        if (filtro) {
            $('#eventos-body tr').filter(function () {
                $(this).toggle($(this).text().toLowerCase().indexOf(filtro) > -1);
            });

            // Filtrar las tarjetas
            $('#bloque2 .card').filter(function () {
                $(this).toggle($(this).text().toLowerCase().indexOf(filtro) > -1);
            });
        }
    }

    // Función para obtener el ancho de la pantalla y mostrar el bloque adecuado
    function obtener_pantalla() {
        const anchoPantalla = window.innerWidth;

        if (anchoPantalla < 992) {  // Pantallas medianas y pequeñas
            $('#bloque1').addClass('oculto');
            $('#bloque2').removeClass('oculto');            
            $('.barra-lateral').addClass('oculto');
            $('#div_filtros_btn').removeClass('oculto');            
        } else {  // Pantallas grandes
            $('#bloque1').removeClass('oculto');
            $('#bloque2').addClass('oculto');
            $('.barra-lateral').removeClass('oculto');
            $('#div_filtros_btn').addClass('oculto');            
        }
    }

    function toggle_botones() {
        $('#divBotones').toggleClass('oculto');
    }

    function toggle_filtros() {
        //mostrar-ocultar controles de filtro
        $('.barra-lateral').toggleClass('oculto');
        
        //cambiamos el texto del boton        
        if ($('.barra-lateral').hasClass('oculto')) {
            $('#filtros_btn').text('Mostrar filtros');
        } else {
            $('#filtros_btn').text('Ocultar filtros');
        }
        console.log($('#filtros_btn').attr('class'));
        console.log("qqqq");
    }

    // Asociar eventos de botones
    $('#logo').dblclick(toggle_botones);
    $('#filtros_btn').click(toggle_filtros);
    $('#actualizar-btn').click(actualizar_bd);
    $('#refrescar-btn').click(devolver_datos);
    $('#eliminar-btn').click(eliminar_datos);
    $('#borrar-filtros-btn').click(borrar_filtros);
    $('#filtrar-btn').click(function () {
        const filtro = $('#filtroTexto').val().toLowerCase();
        filtrar_datos(filtro);
    });

    // Configuración del datepicker
    $("#datepicker").datepicker({
        dateFormat: "dd/mm/yy",
        inline: true, // Esto hace que el calendario sea siempre visible
        firstDay: 1,  // 1 es para lunes
        onSelect: function (dateText) {
            const [dd, mm, yyyy] = dateText.split('/');
            fecha_formateada = `${yyyy}-${mm}-${dd}`;
            filtrar_datos(fecha_formateada);
        }
    });

    // Asociar eventos de redimensionamiento para decidir qué bloque mostrar
    $(window).resize(function () {
        obtener_pantalla();
    });

    // Cargar los datos y establecer el modo (tabla o tarjetas) al iniciar
    obtener_pantalla();
    devolver_datos();
    borrar_filtros();

});
