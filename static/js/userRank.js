$(document).ready(function() {
	var table = $('.userRank').DataTable()
	table.destroy()
	$.ajax({
		url: '/userRank',
		data: $('form').serialize(),
		type: 'POST',
		dataType: 'json',
		success: function(data){
			$('.userRank').remove()
			$("<table class='userRank' class='display' cellspacing='0' width='100%'>"
		    +"<thead>"
		    +"<tr>"
		    +"<th>UserId</th>"
		    +"<th>ScreenName</th>"
		    +"<th>FollowersToFollowingRatio</th>"
		    +"</tr>"
		    +"</thead>"
		    +"<tbody>").appendTo('#userRankTable');		
		    table = $('.userRank').DataTable({
		    	"data": data.success,
	    		"columns": [
	    			{ "data": "UserId" },
	    			{ "data": "ScreenName" },
			        { "data": "FollowersToFollowingRatio" }
	    		]
			});
			console.log(data);
		},
		error: function(error){
			console.log(error);
		}
	});
});
