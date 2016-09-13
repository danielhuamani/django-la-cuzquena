jQuery(document).ready(function($) {

	if($(".vehiculos").length > 0){

		$(".vehiculos").click(function(event) {
			/* Act on the event */
			var valor_data = $(this).attr('data-vehiculo');
			var class_active = "."+valor_data
			/*$(".pop-active").removeClass('pop-active');*/
			$(class_active).addClass('pop-active');
			$(".vehiculos-pages .overlay").addClass('overlay-block')
		});
		$(".icon-cross").click(function(event) {
			/* Act on the event */
			$(".pop-active").removeClass('pop-active');
			console.log($("vehiculos-pages .overlay"))
			$(".vehiculos-pages .overlay").removeClass('overlay-block')

		});
		$(".vehiculos-pages .overlay").click(function(event) {
			/* Act on the event */
			console.log($(this))
			$(".pop-active").removeClass('pop-active');
			$(".vehiculos-pages .overlay").removeClass('overlay-block')
		});
	}
	$("header .overlay").click(function(event) {

		$(".icon-menu").removeClass('res-menu-des')
		$("header .close").removeClass('res-active')
	    $("header .overlay").removeClass('res-active')
	    $(".nav-principal").removeClass('nav-principal-active')
		/* Act on the event */
	});

	$(".icon-menu").click(function(event) {

	   $("header .close").addClass('res-active')
	   $("header .overlay").addClass('res-active')
	   $(".nav-principal").addClass('nav-principal-active')
	   $("header .close").removeClass('res-menu-des')
	   $(this).addClass('res-menu-des')
	});
	$("header .close").click(function(event) {
		$(this).addClass('res-menu-des')
		$(".icon-menu").removeClass('res-menu-des')
		$("header .close").removeClass('res-active')
	    $("header .overlay").removeClass('res-active')
	    $(".nav-principal").removeClass('nav-principal-active')
		/* Act on the event */
	});
});
