async function loadTasks() {
    try {
        const response = await fetch("/tasks");
        const tasks = await response.json();

        const tasksContainer = document.querySelector(".tasks");

        tasksContainer.innerHTML = "";

        const title = document.createElement("h2");
        title.textContent = "Мои задачи";
        tasksContainer.appendChild(title);

        tasks.forEach(task => {
            const taskElement = document.createElement("div");
            taskElement.className = "task";

            if (task.completed) {
                taskElement.classList.add("completed");
            }

            const checkbox = document.createElement("input");
            checkbox.type = "checkbox";
            checkbox.checked = task.completed;
            checkbox.addEventListener("change", async () => {
    await fetch(`/tasks/${task.id}`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title: task.title,
            completed: checkbox.checked
        })
    });

    loadTasks();
});

            const taskTitle = document.createElement("span");
            taskTitle.textContent = task.title;

            taskElement.appendChild(checkbox);
taskElement.appendChild(taskTitle);

const deleteButton = document.createElement("button");
deleteButton.textContent = "🗑️";
deleteButton.className = "delete-task";

deleteButton.addEventListener("click", async () => {
    await fetch(`/tasks/${task.id}`, {
        method: "DELETE"
    });

    loadTasks();
});

taskElement.appendChild(deleteButton);

tasksContainer.appendChild(taskElement);
        });

    } catch (error) {
        console.error("Ошибка:", error);
    }
}


async function addTask() {
    const title = prompt("Введите название задачи:");

    if (!title || !title.trim()) {
        return;
    }

    await fetch("/tasks", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title: title.trim()
        })
    });

    loadTasks();
}


document
    .getElementById("addTaskButton")
    .addEventListener("click", addTask);


loadTasks();