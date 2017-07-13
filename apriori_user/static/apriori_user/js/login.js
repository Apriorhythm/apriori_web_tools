
$(document).ready(function(){
	$(".form-template-error-div").attr("class", "col-sm-offset-2 col-sm-10");
	$(".form-template-error-span").attr("class", "text-danger small");
	$(".form-template-field-label").attr("class", "control-label col-sm-3");
	$(".form-template-field").attr("class", "col-sm-9 form-box");


	$('#loginButton').click(function(){

		var username = $("#id_username").val();
		var password = $("#id_password").val();
		var secretCode = $("#id_secret_code").val();

        var requestData = {
            'username': username,
            'password': password,
            'secret_code': secret_code
        }
		alert(username + " " + password);

		$.post('user/login', requestData, function(data){
			alert(data)
			if ("OK" == data)
				window.location.href = "/";
		});
	});


});
