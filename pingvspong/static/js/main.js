/*global window app_config _ jQuery setTimeout*/

;(function($, _, undefined) {
    var ping_template = _.template('<div class="ping">Ping!</div>');
    var pong_template = _.template('<div class="pong">Pong!<div class="time">Czas: ' +
                                   '<span class="sec"><%- sec %></span> sekund i ' +
                                   '<span class="msec"><%- msec %></span> mikrosekund</div>' +
                                   '</div>');

    var $ping_pong = $('#ping-pong');
    var $average_pong = $('#average-pong');
    var pause_time = app_config.pause_time;

    function add(parent, element) {
        element.hide();
        parent.append(element);
        element.show('slow', scroll_down);
    };

    function add_ping(parent) {
        var $ping = $(ping_template({}));
        add(parent, $ping);
    };

    function add_pong(parent, time) {
        if (time) {
            var $pong = $(pong_template({
                sec: time[0],
                msec: time[1]
            }));
            add(parent, $pong);
        }
    };

    function scroll_down() {
        $("html, body").animate({ scrollTop: $(document).height()});
    }

    function update_average_pong(parent, time) {
        if (time) {
            parent.find('.sec').text(time[0]);
            parent.find('.msec').text(time[1]);
        }
    };
    
    function run_contest() {
        add_ping($ping_pong);
        $.ajax({
            type : "POST",
            url : app_config.url,
            data: {
                'token': app_config.token
            },
            success: function(result) {
                add_pong($ping_pong, result.last_time);
                update_average_pong($average_pong, result.average_time);
                if (!result.is_end) {
                    setTimeout(function() {
                        run_contest();
                    }, pause_time);
                } 
            }
        });
    }

    $(document).ready(function() {
        setTimeout(function() {
            run_contest();
        }, pause_time);
    });
}(jQuery, _));
