$(document).ready(function() {
	var table = $('.userLongest').DataTable()
	$('#userLongestSubmit').click(function(){
		table.destroy()
		$.ajax({
			url: '/userLongest',
			data: $('form').serialize(),
			type: 'POST',
			dataType: 'json',
			success: function(data){
				$('.userLongest').remove()
				$("<table class='userLongest' class='display' cellspacing='0' width='100%'>"
			    +"<thead>"
			    +"<tr>"
			    +"<th>ScreenName</th>"
			    +"<th>Content</th>"
			    +"</tr>"
			    +"</thead>"
			    +"<tbody>").appendTo('#userLongestTable');		
			    table = $('.userLongest').DataTable({
			    	"data": data.success,
		    		"columns": [
				        { "data": "ScreenName" },
				        { "data": "Content" },
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
