$(document).ready(function () {
    // When the password field is clicked
    $(".password-field").on("click", function () {
        // Add the "password" class to the relevant elements
        $(".hand").addClass("password");
        $(".hand-r").addClass("password");
        $(".arm").addClass("password");
        $(".arm-r").addClass("password");
    });

    // When a click occurs anywhere in the document
    $(document).on("click", function (event) {
        // Check if the click target is not the password input or any of its parent elements
        if (!$(event.target).closest(".password-field").length) {
            // Remove the "password" class from the relevant elements
            $(".hand").removeClass("password");
            $(".hand-r").removeClass("password");
            $(".arm").removeClass("password");
            $(".arm-r").removeClass("password");
        }
    });
});