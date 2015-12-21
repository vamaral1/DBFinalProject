$(document).ready(function() {
	var table = $('.userNBA').DataTable()
	table.destroy()
	$.ajax({
		url: '/userNBA',
		data: $('form').serialize(),
		type: 'POST',
		dataType: 'json',
		success: function(data){
			$('.userNBA').remove()
			$("<table class='userNBA' class='display' cellspacing='0' width='100%'>"
		    +"<thead>"
		    +"<tr>"
		    +"<th>Content</th>"
		    +"</tr>"
		    +"</thead>"
		    +"<tbody>").appendTo('#userNBATable');		
		    table = $('.userNBA').DataTable({
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
