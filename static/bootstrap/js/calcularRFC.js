document.getElementById("id_fecha_de_nacimiento").oninput = function() {check_user()};
document.getElementById("id_nombre").oninput = function() {check_user()};
document.getElementById("id_ap_paterno").oninput = function() {check_user()};
document.getElementById("id_ap_materno").oninput = function() {check_user()};

vocales="aeiouAEIOU";  
function sacarvocal(paterno){
    for(a=0;a<paterno.length+1;a++)
    { 
        letra=paterno.trim().charAt(a); 
        if(vocales.indexOf(letra)!=-1)
        { 
            return letra; 
            break; 
        } 
    } 
} 

function check_user(){
    nombre=document.getElementById("id_nombre").value;
    letra_nombre=nombre.trim().charAt(0);
    apellido_materno=document.getElementById("id_ap_materno").value;
    letra_apellido_materno=apellido_materno.trim().charAt(0);
    fecha=document.getElementById("id_fecha_de_nacimiento").value;
    yy_fecha=fecha.trim().substring(2,4);
    mm_fecha=fecha.trim().substring(5,7);
    dd_fecha=fecha.trim().substring(8,10);


    if((document.getElementById("id_ap_paterno").value != "") || (document.getElementById("id_fecha_de_nacimiento").value != "")) 
    {
        apellido_paterno=document.getElementById("id_ap_paterno").value;
        letra_apellido_paterno=apellido_paterno.trim().charAt(0);
        apellido_paterno=apellido_paterno.trim().substr(1);
        var funcion=sacarvocal(apellido_paterno);
        result=letra_apellido_paterno+funcion+letra_apellido_materno+letra_nombre+yy_fecha+mm_fecha+dd_fecha;
        document.getElementById("id_rfc").value = result.toUpperCase();
    }
    else
    {
        result=letra_apellido_materno+letra_nombre;
        document.getElementById("id_rfc").value = result.toUpperCase();
    }
}


/*SOLO SELECCIONAR UN CHECKBOX*/
$('input[name="sexo"]').on('change', function() {
   $('input[name="sexo"]').not(this).prop('checked', false);
});

$('input[name="estado_civil"]').on('change', function() {
   $('input[name="estado_civil"]').not(this).prop('checked', false);
});

$('input[name="primaria"]').on('change', function() {
   $('input[name="primaria"]').not(this).prop('checked', false);
});

$('input[name="secundaria"]').on('change', function() {
   $('input[name="secundaria"]').not(this).prop('checked', false);
});

$('input[name="preparatoria"]').on('change', function() {
   $('input[name="preparatoria"]').not(this).prop('checked', false);
});

$('input[name="licenciatura"]').on('change', function() {
   $('input[name="licenciatura"]').not(this).prop('checked', false);
});

$('input[name="postgrado"]').on('change', function() {
   $('input[name="postgrado"]').not(this).prop('checked', false);
});

$('input[name="practica_deporte"]').on('change', function() {
   $('input[name="practica_deporte"]').not(this).prop('checked', false);
});

$('input[name="lado_dominante"]').on('change', function() {
   $('input[name="lado_dominante"]').not(this).prop('checked', false);
});

$('input[name="nivel"]').on('change', function() {
   $('input[name="nivel"]').not(this).prop('checked', false);
});

$('input[name="esta_embarazada"]').on('change', function() {
   $('input[name="esta_embarazada"]').not(this).prop('checked', false);
});

$('input[name="esta_amamantando"]').on('change', function() {
   $('input[name="esta_amamantando"]').not(this).prop('checked', false);
});