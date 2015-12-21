$(document).ready(function() {
	var table = $('.hashtagNBA').DataTable()
	table.destroy()
	$.ajax({
		url: '/hashtagNBA',
		data: $('form').serialize(),
		type: 'POST',
		dataType: 'json',
		success: function(data){
			$('.hashtagNBA').remove()
			$("<table class='hashtagNBA' class='display' cellspacing='0' width='100%'>"
		    +"<thead>"
		    +"<tr>"
		    +"<th>ScreenName</th>"
		    +"</tr>"
		    +"</thead>"
		    +"<tbody>").appendTo('#hashtagNBATable');		
		    table = $('.hashtagNBA').DataTable({
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
