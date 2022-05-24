$(document).ready(function(){
    verCarro();
});

function verCarro(){
    if($('#carro_compra').val() > 0){
        $('.dropdown-menu-right').addClass('show');
        $('li.dropdown').addClass('show');
        $('.navbar-collapse').addClass('show');
    }
};