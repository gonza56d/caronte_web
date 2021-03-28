
var prevent = true;
var pass = $('#id_password');
var re_pass = $('#id_re_password');

var oops = $('#oops').text();
var passwords_do_not_match = $('#passwords_do_not_match').text();

$('#signup_form').submit(function(e) {
    if (prevent) {
        e.preventDefault();
    }

    if (pass.val() !== re_pass.val()) {
        prevent = true;
        Swal.fire({
            icon: 'error',
            title: oops+'... :(',
            text: passwords_do_not_match
        });
        pass.val('');
        re_pass.val('');
    } else {
        prevent = false;
        this.submit();
    }

});
