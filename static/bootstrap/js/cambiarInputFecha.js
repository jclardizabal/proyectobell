$( document ).ready(function() {
	$("#id_fecha").focus(function(){
	    $(this).prop('type', 'date');
	});

	$("#id_fecha_de_nacimiento").focus(function(){
	    $(this).prop('type', 'date');
	});
});/* CIERRA LA FUNCION*/