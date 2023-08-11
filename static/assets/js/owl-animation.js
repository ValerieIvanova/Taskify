$(document).ready(function () {
    $(".password-field").on("focus", function () {
        $(".hand").addClass("password");
        $(".hand-r").addClass("password");
        $(".arm").addClass("password");
        $(".arm-r").addClass("password");
    });

    $(".password-field").on("blur", function (event) {
            $(".hand").removeClass("password");
            $(".hand-r").removeClass("password");
            $(".arm").removeClass("password");
            $(".arm-r").removeClass("password");
        // }
    });
});