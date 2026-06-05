"use client";

import { useEffect, useState } from "react";
import api from "../../services/api";

export default function TasksPage() {
  const [tasks, setTasks] = useState<any[]>([]);

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      const response = await api.get("/tasks/");
      setTasks(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">
        Tasks
      </h1>

      {tasks.map((task) => (
        <div
          key={task.id}
          className="border p-4 rounded mb-4"
        >
          <h2 className="text-xl font-semibold">
            {task.title}
          </h2>

          <p>{task.description}</p>

          <p>
            <strong>Status:</strong> {task.status}
          </p>

          <p>
            <strong>Project ID:</strong> {task.project_id}
          </p>

          <p>
            <strong>Assigned To:</strong> {task.assigned_to}
          </p>

          <p>
            <strong>Due Date:</strong> {task.due_date}
          </p>
        </div>
      ))}
    </div>
  );
}