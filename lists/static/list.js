/*global jQuery */
jQuery(document).ready(function ($) {

    var bindEventListeners = function () {
        $('input[name="text"]').on('keypress', function () {
            $('.has-error').hide();
        });

        $('input[name="text"]').on('click', function() {
            $('.has-error').hide();
        });
    };

    $.extend(window, true, {
        'Superlists': {
            'Lists': {
                'bindEventListeners': bindEventListeners
            }
        }
    });
});

