$(document).ready(function() {
	var table = $('.posClinton').DataTable()
	table.destroy()
	$.ajax({
		url: '/posClinton',
		data: $('form').serialize(),
		type: 'POST',
		dataType: 'json',
		success: function(data){
			$('.posClinton').remove()
			$("<table class='posClinton' class='display' cellspacing='0' width='100%'>"
		    +"<thead>"
		    +"<tr>"
		    +"<th>Total</th>"
		    +"<th>Positive</th>"
		    +"<th>PercentPositive</th>"
		    +"</tr>"
		    +"</thead>"
		    +"<tbody>").appendTo('#posClintonTable');		
		    table = $('.posClinton').DataTable({
		    	"data": data.success,
	    		"columns": [
			        { "data": "Total" },
			        { "data": "Positive"},
			        { "data": "PercentPositive"}
	    		]
			});
			console.log(data);
		},
		error: function(error){
			console.log(error);
		}
	});
});
