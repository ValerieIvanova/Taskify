document.addEventListener("DOMContentLoaded", function () {
    const checkboxes = document.querySelectorAll(".completed-checkbox");

    checkboxes.forEach((checkbox) => {
        checkbox.addEventListener("change", async function () {
            const taskId = this.id.split("-")[1];
            const taskContainer = this.closest(".task-item")
            const checkboxLabel = taskContainer.querySelector(".checkbox-label");
            const checkboxInput = taskContainer.querySelector(".completed-checkbox");

            if (this.checked) {
                if (checkboxLabel.classList.contains("expired")) {
                    checkboxLabel.classList.remove("expired");
                }
                await markTaskAsCompleted(taskId);
                checkboxLabel.classList.add("completed");
            }
        });
    });

    async function markTaskAsCompleted(taskId) {
        try {
            const response = await fetch(`/tasks/mark_task_completed/${taskId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),  // Replace with your CSRF token retrieval method
                },
            });
            const data = await response.json();
            if (data.success) {
                console.log(`Task ${taskId} marked as completed.`);
            } else {
                console.error(`Failed to mark task ${taskId} as completed: ${data.error}`);
            }
        } catch (error) {
            console.log(`An error occurred: ${error}`);
        }
    }

    function getCookie(name) {
        var value = "; " + document.cookie;
        var parts = value.split("; " + name + "=");
        if (parts.length === 2) return parts.pop().split(";").shift();
    }
});