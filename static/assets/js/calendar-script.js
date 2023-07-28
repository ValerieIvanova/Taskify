document.addEventListener('DOMContentLoaded', function () {
    // Get the calendar element
    let calendarEl = document.getElementById('calendar');

    // Initialize the calendar
    let calendar = new FullCalendar.Calendar(calendarEl, {
        headerToolbar: {
            start: 'today prev,next',
            center: 'title',
            end: 'dayGridMonth listWeek timeGridWeek timeGridDay',
        },
        initialView: 'dayGridMonth', // Set the initial view to dayGridMonth (month view)
        selectable: true, // Enable date selection
        dateClick: function (info) {
            let selectedDate = info.dateStr;
            if (selectedDate < today()) {
                return;
            }
            displayAddTaskForm(info.dateStr); // Call the function to display the add task form
        },
        events: '/tasks/calendar/events/', // Specify the URL to fetch events
        eventContent: function (arg) {
            // Custom event content function
            return {
                html: `<div class="calendar-event" style="background-color: ${arg.event.extendedProps.category_color}; color: black">${arg.event.title}</div>`,
                // Use the category color as the background color and set the font color to black
            };
        },
        firstDay: 1, // Set Monday as the first day of the week
        eventClick: function (info) {
            // Handle event click
            showTaskDetails(info.event.id);
        }
    });

    // Function to get today's date
    function today() {
        let now = new Date();
        now.setHours(0, 0, 0, 0);
        let year = now.getFullYear();
        let month = String(now.getMonth() + 1).padStart(2, '0');
        let day = String(now.getDate()).padStart(2, '0');
        return `${year}-${month}-${day}`;
    }

    // Function to display the add task form
    function displayAddTaskForm(selectedDate) {
        let formWrapper = document.getElementById('calendar-form-wrapper');
        let form = document.getElementById('add-task-form');
        let startDate = document.querySelector("#id_start_date");
        let dueDate = document.querySelector("#id_due_date");

        startDate.value = selectedDate;
        dueDate.value = selectedDate;
        formWrapper.classList.remove('hidden-form'); // Remove the hidden-form class to show the form
    }

    // Function to display the details of a task
    function showTaskDetails(taskId) {
        window.location.href = window.location.origin + '/tasks/details/' + taskId + '/';
    }

    // Render the calendar
    calendar.render();
});
