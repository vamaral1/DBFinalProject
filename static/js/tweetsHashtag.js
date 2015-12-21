$(document).ready(function() {
	var table = $('.tweetsHashtag').DataTable()
	$('#tweetsHashtagSubmit').click(function(){
		table.destroy()
		$.ajax({
			url: '/tweetsHashtag',
			data: $('form').serialize(),
			type: 'POST',
			dataType: 'json',
			success: function(data){
				$('.tweetsHashtag').remove()
				$("<table class='tweetsHashtag' class='display' cellspacing='0' width='100%'>"
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
			    +"<tbody>").appendTo('#tweetsHashtagTable');		
			    table = $('.tweetsHashtag').DataTable({
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
