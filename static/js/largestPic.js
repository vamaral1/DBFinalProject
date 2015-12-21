$(document).ready(function() {
	var table = $('.largestPic').DataTable()
	table.destroy()
	$.ajax({
		url: '/largestPic',
		data: $('form').serialize(),
		type: 'POST',
		dataType: 'json',
		success: function(data){
			$('.largestPic').remove()
			$("<table class='largestPic' class='display' cellspacing='0' width='100%'>"
		    +"<thead>"
		    +"<tr>"
		    +"<th>LargestMediaLink</th>"
		    +"</tr>"
		    +"</thead>"
		    +"<tbody>").appendTo('#largestPicTable');		
		    table = $('.largestPic').DataTable({
		    	"data": data.success,
	    		"columns": [
			        {
                        'data': 'LargestPictureLink',
                        'sortable': false,
                        'searchable': false,
                        'render': function (webSite) {
                            if (!webSite) {
                                return 'N/A';
                            }
                            else {
                                return '<a href=' + webSite + '>'
                                    + webSite.substr(0, 30) + '...' + '</a>';
                            }
                        }
                    }
	    		]

			});
			console.log(data);
		},
		error: function(error){
			console.log(error);
		}
	});
});
