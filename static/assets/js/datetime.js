function getCurrentDateTime() {
    let currentDate = new Date();

    // Format
    let options = {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: 'numeric',
        minute: 'numeric',
        hour12: false
    };
    return currentDate.toLocaleDateString('en-US', options);
}

// Update the date and time element periodically
function updateDateTime() {
    let datetimeElement = document.getElementById('datetime');

    datetimeElement.textContent = getCurrentDateTime();

    // Schedule the next update after 1 second
    setTimeout(updateDateTime, 1000);
}

updateDateTime();