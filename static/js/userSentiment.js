$(document).ready(function() {
	var table = $('.userSentiment').DataTable()
	$('#userSentimentSubmit').click(function(){
		table.destroy()
		$.ajax({
			url: '/userSentiment',
			data: $('form').serialize(),
			type: 'POST',
			dataType: 'json',
			success: function(data){
				$('.userSentiment').remove()
				$("<table class='userSentiment' class='display' cellspacing='0' width='100%'>"
			    +"<thead>"
			    +"<tr>"
			    +"<th>Sentiment</th>"
			    +"</tr>"
			    +"</thead>"
			    +"<tbody>").appendTo('#userSentimentTable');		
			    table = $('.userSentiment').DataTable({
			    	"data": data.success,
		    		"columns": [
				        { "data": "Sentiment" }
		    		]
				});
				console.log(data);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
