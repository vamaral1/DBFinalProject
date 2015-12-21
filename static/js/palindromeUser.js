$(document).ready(function() {
	var table = $('.palindromeUser').DataTable()
	table.destroy()
	$.ajax({
		url: '/palindromeUser',
		data: $('form').serialize(),
		type: 'POST',
		dataType: 'json',
		success: function(data){
			$('.palindromeUser').remove()
			$("<table class='palindromeUser' class='display' cellspacing='0' width='100%'>"
		    +"<thead>"
		    +"<tr>"
		    +"<th>TweetId</th>"
		    +"<th>ScreenName</th>"
		    +"<th>NumPosts</th>"
		    +"</tr>"
		    +"</thead>"
		    +"<tbody>").appendTo('#palindromeUserTable');		
		    table = $('.palindromeUser').DataTable({
		    	"data": data.success,
	    		"columns": [
			        { "data": "TweetId" },
			        { "data": "ScreenName" },
			        { "data": "NumPosts" }
	    		]
			});
			console.log(data);
		},
		error: function(error){
			console.log(error);
		}
	});
});
