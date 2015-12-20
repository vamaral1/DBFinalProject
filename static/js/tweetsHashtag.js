$(function(){
	$('#submit').click(function(){
		
		$.ajax({
			url: '/tweetsHashtag',
			data: $('form').serialize(),
			type: 'POST',
			dataType: 'json',
			success: function(data){
				$('#tweetsHashtagTable').dataTable({
					data: data,
		    		columns: [
				        { "mDataProp": "TweetId" },
				        { "mDataProp": "UserId" },
				        { "mDataProp": "Time" },
				        { "mDataProp": "Content" },
				        { "mDataProp": "Sentiment" },
				        { "mDataProp": "Lat" },
				        { "mDataProp": "Lon" }
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
