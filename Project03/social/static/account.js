function delIntResponse(data,status) {
    if (status == 'success') {
    	location.reload();
    }
    else {
    	alert('failed to delete interest' + status);
    }
}

function deleteInterest(event) {
    let interest = event.target.id;
    let json_data = { "interest" : interest };
    let url_path = interest_delete_url;
    $.post(url_path, json_data, delIntResponse);
}

$(document).ready(function() {
    $('.inter-tag').click(deleteInterest);
});
