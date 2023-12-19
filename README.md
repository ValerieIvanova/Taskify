This website is securely hosted on the PythonAnywhere platform, providing a robust and reliable environment for seamless user access.<br>
# -> https://taskify.pythonanywhere.com/
Important Note:
PythonAnywhere does not support running a Redis server. As a result, the reminder functionality that relies on Celery and Redis to send reminders at specified dates and times will not be available on this platform.

Taskify is a simple task manager website designed for personal use. It allows users to register, login, and logout. The website features a delightful login and registration form with an owl that playfully hides its eyes when the user inputs their password. With Taskify, users can efficiently manage their tasks, create, update, and delete them as needed. Each task can be associated with a category for easy organization.
![Screenshot 2023-08-10 at 16 53 44](https://github.com/ValerieIvanova/Taskify/assets/105737781/798b97fc-7c43-4059-ae50-2a68a80dba53)

Key Features:
1. User Registration and Login: Taskify provides a user-friendly registration and login system.
![Screenshot 2023-08-10 at 16 56 02](https://github.com/ValerieIvanova/Taskify/assets/105737781/20522175-432a-4b9d-8c27-8cc806455bab)
![Screenshot 2023-08-10 at 16 56 23](https://github.com/ValerieIvanova/Taskify/assets/105737781/40be3c6a-f2b3-473f-8f34-ffefa861ded3)

2. Task Management: Users can create, update, and delete tasks as needed.
![Screenshot 2023-08-10 at 16 58 13](https://github.com/ValerieIvanova/Taskify/assets/105737781/ccefca9b-a5a7-4319-8576-82556471c4b9)

3. Task Details: Users can view detailed information about each task.
![Screenshot 2023-08-10 at 16 58 53](https://github.com/ValerieIvanova/Taskify/assets/105737781/4b1158d1-3bce-4ada-a4c0-68b7aa30fd49)

4. Categories: Tasks can be assigned to different categories for better organization.
5. Calendar View: Taskify utilizes the FullCalendar library to present tasks in a user-friendly calendar format. The completed tasks which are not deleted apear with green color, while all the other tasks have colors depending on their category.
![Screenshot 2023-08-10 at 17 01 21](https://github.com/ValerieIvanova/Taskify/assets/105737781/18374380-9a89-49a7-99ac-6b13bd6334e4)

6. Add Tasks from Calendar: By clicking on a date, users can conveniently add new tasks directly from the calendar.
11. Email Reminders: Taskify features an advanced reminder system that leverages the power of Celery and Redis to deliver seamless and timely notifications to the users. Through this sophisticated integration, users can set reminders for specific dates and times, ensuring they never miss important tasks or appointments.<br>

<b>How It Works?</b><br>
-Celery Task Queue: Behind the scenes, Celery, a powerful distributed task queue, manages the scheduling and execution of reminder tasks. This ensures efficient handling of reminders without impacting the overall system performance.

-Redis for Efficient Data Handling: Redis, an in-memory data structure store, acts as the message broker for Celery. It efficiently manages task messages, enabling smooth communication between different components of the reminder system.

-Scheduled Delivery: The Celery task scheduler interacts with Redis to execute reminders at the exact date and time set by the user. This results in timely notifications delivered to the user's preferred communication channels.

-Reliable and Scalable: The Celery-Redis combination ensures reliability and scalability. Reminders are delivered even during high traffic periods, and the system can handle a growing number of users and tasks seamlessly.
![Screenshot 2023-08-10 at 17 13 34](https://github.com/ValerieIvanova/Taskify/assets/105737781/0d66817a-748f-4a48-bb27-2be824691108)

13. Responsive Design: Taskify is designed to work seamlessly across various devices, ensuring a smooth user experience.
![IMG_7864](https://github.com/ValerieIvanova/Taskify/assets/105737781/9801de7b-e0eb-4355-afa5-eb5226d4eb0a)
![IMG_7863](https://github.com/ValerieIvanova/Taskify/assets/105737781/ff2942ce-4475-4cac-9aa9-d167e705011c)
![IMG_7866](https://github.com/ValerieIvanova/Taskify/assets/105737781/01bd8ef7-0423-43a8-9f1c-456d981fb0b5)

