/*global window app_config _ jQuery*/

(function($, _, undefined) {
    function run_contest() {
        $.ajax({
            type : "POST",
            url : app_config.url,
            data: {
                'token': app_config.token
            },
            success: function(result) {
                if (!result.is_end) {
                    run_contest();
                } 
                else {
                    console.log(result);
                }
            }
        });
    }
    console.log('yolo');
    $(document).ready(function() {
        run_contest();
    });
}(jQuery, _));
