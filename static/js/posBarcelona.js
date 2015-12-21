$(document).ready(function() {
	var table = $('.posBarcelona').DataTable()
	table.destroy()
	$.ajax({
		url: '/posBarcelona',
		data: $('form').serialize(),
		type: 'POST',
		dataType: 'json',
		success: function(data){
			$('.posBarcelona').remove()
			$("<table class='posBarcelona' class='display' cellspacing='0' width='100%'>"
		    +"<thead>"
		    +"<tr>"
		    +"<th>Content</th>"
		    +"</tr>"
		    +"</thead>"
		    +"<tbody>").appendTo('#posBarcelonaTable');		
		    table = $('.posBarcelona').DataTable({
		    	"data": data.success,
	    		"columns": [
			        { "data": "Content" }
	    		]
			});
			console.log(data);
		},
		error: function(error){
			console.log(error);
		}
	});
});
