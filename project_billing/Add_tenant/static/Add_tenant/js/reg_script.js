$(document).ready(function() {
    $(".submit_button").click(function() {
        // console.log("sos")
        $.ajax({
            url: "/reg_page/",
            type: "POST",
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                name: $(".name").val(),
                email: $(".email").val(),
                password: $(".password").val(),
                phone: $(".phone").val(),
                // error: $(".error").val()
                
            },
            // success:function() {
            //     console.log(111)
            //     $(".error_div").text(`
            //         <p class="error">Реєстрація успішна</p>
            //     `)
            // },
            // error: function(){
            //     console.log(222)
            //     $(".error_div").text(`
            //         <p class="error">Заповніть усі поля, пароль має бути довше 7 символів</p>
            //     `)
            // }
            
        }) 
    })
})