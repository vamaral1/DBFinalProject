$(document).ready(function() {
	var table = $('.mentionFollowers').DataTable()
	table.destroy()
	$.ajax({
		url: '/mentionFollowers',
		data: $('form').serialize(),
		type: 'POST',
		dataType: 'json',
		success: function(data){
			$('.mentionFollowers').remove()
			$("<table class='mentionFollowers' class='display' cellspacing='0' width='100%'>"
		    +"<thead>"
		    +"<tr>"
		    +"<th>ScreenName</th>"
		    +"</tr>"
		    +"</thead>"
		    +"<tbody>").appendTo('#mentionFollowersTable');		
		    table = $('.mentionFollowers').DataTable({
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
