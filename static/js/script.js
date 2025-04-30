function toggleTaskStatus(checkbox) {
    const taskId = checkbox.id;
    const isCompleted = checkbox.checked;

    console.log(`Task ID: ${taskId}, Completed: ${isCompleted}`); // Debugging log

    fetch(`/update_status/${taskId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ completed: isCompleted })
    })

    const todoElement = checkbox.closest('.todo');
    todoElement.style.textDecoration = isCompleted ? 'line-through' : 'none';



}
