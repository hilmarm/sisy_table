var baseUrl = 'https://widget.fahrfahraway.com/';

(function () {
    var jQuery;

    /******** Load jQuery if not present *********/
    if (window.jQuery === undefined) { // || window.jQuery.fn.jquery !== '1.4.2') {
        var script_tag = document.createElement('script');
        script_tag.setAttribute("type", "text/javascript");
        script_tag.setAttribute("src", baseUrl + "lib/widget/vendor/jquery/dist/jquery.min.js");
        if (script_tag.readyState) {
            script_tag.onreadystatechange = function () { // For old versions of IE
                if (this.readyState == 'complete' || this.readyState == 'loaded') {
                    jQueryLoadHandler();
                }
            };
        } else { // Other browsers
            script_tag.onload = jQueryLoadHandler;
        }
        // Try to find the head, otherwise default to the documentElement
        (document.getElementsByTagName("head")[0] || document.documentElement).appendChild(script_tag);
    } else {
        // The jQuery version on the window is the one we want to use
        jQuery = window.jQuery;
        main();
    }

    function jQueryLoadHandler() {
        // Restore $ and window.jQuery to their previous values and store the
        // new jQuery in our local jQuery variable
        jQuery = window.jQuery.noConflict(true);
        // Call our main function
        main();
    }

    /******** Our main function ********/
    function main() {

        (function ($) {
            $.getStylesheet = function (href) {
                var $d = $.Deferred();
                var $link = $('<link/>', {
                    rel: 'stylesheet',
                    type: 'text/css',
                    href: href
                }).appendTo('head');
                $d.resolve($link);
                return $d.promise();
            };
        })(jQuery);

        jQuery(document).ready(function ($) {
            // $.getScript( "ajax/test.js", function( data, textStatus, jqxhr ) {
            //     console.log( data ); // Data returned
            //     console.log( textStatus ); // Success
            //     console.log( jqxhr.status ); // 200
            //     console.log( "Load was performed." );
            // });
            var languageId = $('#ffa-root').data('language');
						if (languageId == null || languageId == undefined || languageId.length == 0) {
							var languageId = 'de';
						}
            window.jQuery = $;						
            $.when(
                $.getStylesheet(baseUrl + 'lib/widget/main.css?rand=52'),						
                $.getScript(baseUrl + 'lib/widget/vendor/bootstrap/dist/js/bootstrap.min.js'),
                $.getScript(baseUrl + 'lib/widget/vendor/handlebars/handlebars.min.js'),
                $.getScript(baseUrl + 'lib/widget/vendor/typeahead.js/dist/typeahead.bundle.min.js'),
                $.getScript(baseUrl + 'lib/widget/vendor/bootstrap-validator/js/validator.js'),
                $.getScript(baseUrl + 'lib/widget/vendor/moment/min/moment.min.js'),
                $.getScript(baseUrl + 'lib/widget/vendor/bootstrap-datetimepicker/js/bootstrap-datetimepicker.min.js'),
                //$.getScript(baseUrl + 'lib/widget/vendor/bootstrap-datetimepicker/js/locales/bootstrap-datetimepicker.'+ languageId + '.js'),
                // $.getScript(baseUrl + 'lib/widget/widget.js'),
                //$.getStylesheet(baseUrl + 'lib/widget/vendor/bootstrap/dist/css/bootstrap.min.css'),
                $.getStylesheet(baseUrl + 'lib/widget/vendor/bootstrap-datetimepicker/css/bootstrap-datetimepicker.min.css'),
                //$.getStylesheet(baseUrl + 'lib/widget/vendor/fontawesome/css/font-awesome.min.css'),
                $.Deferred(function (deferred) {
                    $(deferred.resolve);
                })
            ).done(function () {
                var eventId = $('#ffa-root').data('id');
                $('#ffa-root').load(baseUrl + 'embed/?event=' + eventId + '&language='+ languageId, function () {
                    $.getScript(baseUrl + 'lib/widget/widget.js');
                });
            });

        });
    }


})();
