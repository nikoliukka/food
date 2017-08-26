$(function() {
    $('#getDinner').click(function() {
        $.ajax({
            url: '/getDinner',
            type: 'GET',
            success: function(response) {
                var jsonResponse = JSON.parse(response);
                $('#dinnerSuggestion').text(jsonResponse.data.item);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

    $('#newDinnerForm').submit(function() {
        event.preventDefault();

        $.post({
            url: '/addDinner',
            data: $('#newDinnerForm').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
