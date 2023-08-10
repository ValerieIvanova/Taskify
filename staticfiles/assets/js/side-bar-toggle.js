$(document).ready(function () {
    // Select the sidebar toggle box
    let sidebarToggleBox = $('#sidebar-toggle-box');

    // Select the sidebar
    let sidebar = $('#sidebar');

    let content = $('.content-pos');

    sidebar.hide();
    content.css({left: '1vw'});

    // Attach a click event handler to the sidebar toggle box
    sidebarToggleBox.click(function () {
        // Toggle the visibility of the sidebar using slideToggle animation
        sidebar.fadeToggle('slow', function () {
            if (sidebar.is(':visible')) {
                content.animate({left: '8vw'}, 'slow');
            } else {
                content.animate({left: '1vw'}, 'slow');
            }
        });
    });
});