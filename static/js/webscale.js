$(document).ready(function() {
	var table = $('.webscale').DataTable()
	table.destroy()
	$.ajax({
		url: '/webscale',
		data: $('form').serialize(),
		type: 'POST',
		dataType: 'json',
		success: function(data){
			$('.webscale').remove()
			$("<table class='webscale' class='display' cellspacing='0' width='100%'>"
		    +"<thead>"
		    +"<tr>"
		    +"<th>ScreenName</th>"
		    +"</tr>"
		    +"</thead>"
		    +"<tbody>").appendTo('#webscaleTable');		
		    table = $('.webscale').DataTable({
		    	"data": data.success,
	    		"columns": [
			        { "data": "ScreenName" }
	    		]
			});
			console.log(data);
		},
		error: function(error){
			console.log(error);
		}
	});
});
