$(document).ready(function() {
	var table = $('.tweetsWord').DataTable()
	$('#tweetsWordSubmit').click(function(){
		table.destroy()
		$.ajax({
			url: '/tweetsWord',
			data: $('form').serialize(),
			type: 'POST',
			dataType: 'json',
			success: function(data){
				$('.tweetsWord').remove()
				$("<table class='tweetsWord' class='display' cellspacing='0' width='100%'>"
			    +"<thead>"
			    +"<tr>"
			    +"<th>TweetId</th>"
			    +"<th>UserId</th>"
			    +"<th>Time</th>"
			    +"<th>Content</th>"
			    +"<th>Sentiment</th>"
			    +"<th>Lat</th>"
			    +"<th>Lon</th>"
			    +"</tr>"
			    +"</thead>"
			    +"<tbody>").appendTo('#tweetsWordTable');		
			    table = $('.tweetsWord').DataTable({
			    	"data": data.success,
		    		"columns": [
				        { "data": "TweetId" },
				        { "data": "UserId" },
				        { "data": "Time" },
				        { "data": "Content" },
				        { "data": "Sentiment" },
				        { "data": "Lat" },
				        { "data": "Lon" }
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
