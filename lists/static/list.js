/*global $, test, equal */

$(document).ready(function () {
    $('input').on('keypress', function() {
        $('.has-error').hide();
    });
});

$(document).ready(function () {
    $('input').on('click', function() {
        $('.has-error').hide();
    });
});

