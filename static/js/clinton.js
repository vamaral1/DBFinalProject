$(document).ready(function() {
	var table = $('.clinton').DataTable()
	table.destroy()
	$.ajax({
		url: '/clinton',
		data: $('form').serialize(),
		type: 'POST',
		dataType: 'json',
		success: function(data){
			$('.clinton').remove()
			$("<table class='clinton' class='display' cellspacing='0' width='100%'>"
		    +"<thead>"
		    +"<tr>"
		    +"<th>Total</th>"
		    +"<th>Positive</th>"
		    +"<th>PercentPositive</th>"
		    +"</tr>"
		    +"</thead>"
		    +"<tbody>").appendTo('#clintonTable');		
		    table = $('.clinton').DataTable({
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
