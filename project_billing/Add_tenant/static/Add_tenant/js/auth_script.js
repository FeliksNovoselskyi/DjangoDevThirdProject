$(document).ready(function() {
    $(".auth_submit_button").click(function() {
        // console.log("sos")
        $.ajax({
            url: "/auth_page/",
            type: "POST",
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                name: $(".name").val(),
                password: $(".password").val(),
            },
        }) 
    })
})