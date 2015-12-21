$(document).ready(function() {
	var table = $('.posSentiment').DataTable()
	table.destroy()
	$.ajax({
		url: '/posSentiment',
		data: $('form').serialize(),
		type: 'POST',
		dataType: 'json',
		success: function(data){
			$('.posSentiment').remove()
			$("<table class='posSentiment' class='display' cellspacing='0' width='100%'>"
		    +"<thead>"
		    +"<tr>"
		    +"<th>ScreenName</th>"
		    +"<th>PositiveTweetCount</th>"
		    +"</tr>"
		    +"</thead>"
		    +"<tbody>").appendTo('#posSentimentTable');		
		    table = $('.posSentiment').DataTable({
		    	"data": data.success,
	    		"columns": [
	    			{ "data": "ScreenName" },
			        { "data": "PositiveTweetCount" }
	    		]
			});
			console.log(data);
		},
		error: function(error){
			console.log(error);
		}
	});
});
