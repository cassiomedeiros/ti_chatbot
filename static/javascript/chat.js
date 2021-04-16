
$(".messages").animate({ scrollTop: $('.messages')[0].scrollHeight - $('.messages')[0].clientHeight}, "fast");

function newMessage(message) {
    if ($.trim(message) == '') {
        return false;
    }
    $('<li class="sent"><img src="http://emilcarlsson.se/assets/mikeross.png" alt="" /><p>' + message + '</p></li>').appendTo($('.messages ul'));
    $('.message-input input').val(null);
    $('.contact.active .preview').html('<span>You: </span>' + message);
    $(".messages").animate({ scrollTop: $('.messages')[0].scrollHeight - $('.messages')[0].clientHeight}, "fast");
    $.ajax({
    url: "/send_message/"+message
}).done(function(e) {
    newReply(e);
});
};

function newReply(message) {
    if ($.trim(message) == '') {
        return false;
    }
    $('<li class="replies"><img src="http://emilcarlsson.se/assets/harveyspecter.png" alt="" /><p>' + message + '</p></li>').appendTo($('.messages ul'));
    $('.message-input input').val(null);
    $('.contact.active .preview').html('<span>You: </span>' + message);
    $(".messages").animate({ scrollTop: $('.messages')[0].scrollHeight - $('.messages')[0].clientHeight}, "fast");
};

$('.submit').click(function () {
    message = $(".message-input input").val();
    newMessage(message);
    newReply();
});

var sendOption =  function(prop) {
    var message = $(prop).text()
    newMessage(message);
    newReply();
}

$(window).on('keydown', function (e) {
    if (e.which == 13) {
        message = $(".message-input input").val();
        newMessage(message);
        newReply();
        return false;
    }
});