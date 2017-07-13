

function getContent() {
    $.get('/review/content' ,function(data){
        $.each(data, function(index, review) {
            singleContent = '' +
				'<li class="list-group-item">' +
                        '<div>' + review.content + '</div>' +
                '</li>';
			$("#review-content-ul").append(singleContent);
       });
    });
}

$(document).ready(function() {
    getContent();

    $('#put-data-submit').click(
        function putContent() {
            var csrftoken = $("[name=csrfmiddlewaretoken]").val();
            content = $('#data-input').val();
            var requestData = {
                'csrfmiddlewaretoken':csrftoken,
                'content':content,
            };

            $.post('/review/content', requestData,function(data){

                if ('1' == data)
                    $('#put-data-status-label').text('Done!');
                else
                    $('#put-data-status-label').text('Failed!');
                $('#put-data-status').css("color","red")

                setTimeout(function () {
                    $('#put-data-status-label').text('TODY');
                $('#put-data-status').css("color","#000000")
                },2000);
            });
        }
    )
});

