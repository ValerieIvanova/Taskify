$(document).ready(function () {
    let sidebarToggleBox = $('#sidebar-toggle-box');
    let sidebar = $('#sidebar');

    let content = $('.content-pos');

    sidebar.hide();
    content.css({left: '1vw'});

    sidebarToggleBox.click(function () {
        sidebar.fadeToggle('slow', function () {
            if (sidebar.is(':visible')) {
                content.animate({left: '8vw'}, 'slow');
            } else {
                content.animate({left: '1vw'}, 'slow');
            }
        });
    });
});