$(document).ready(function() {
	var table = $('.userLiked').DataTable()
	table.destroy()
	$.ajax({
		url: '/userLiked',
		data: $('form').serialize(),
		type: 'POST',
		dataType: 'json',
		success: function(data){
			$('.userLiked').remove()
			$("<table class='userLiked' class='display' cellspacing='0' width='100%'>"
		    +"<thead>"
		    +"<tr>"
		    +"<th>Hashtag</th>"
		    +"</tr>"
		    +"</thead>"
		    +"<tbody>").appendTo('#userLikedTable');		
		    table = $('.userLiked').DataTable({
		    	"data": data.success,
	    		"columns": [
			        { "data": "Hashtag" }
	    		]
			});
			console.log(data);
		},
		error: function(error){
			console.log(error);
		}
	});
});
