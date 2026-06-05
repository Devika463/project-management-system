"use client";

import { useState } from "react";
import api from "../../services/api";

export default function CreateTaskPage() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [projectId, setProjectId] = useState("");
  const [assignedTo, setAssignedTo] = useState("");
  const [dueDate, setDueDate] = useState("");

  const handleCreateTask = async () => {
    try {
      await api.post("/tasks/", {
        title,
        description,
        status: "pending",
        project_id: Number(projectId),
        assigned_to: Number(assignedTo),
        due_date: dueDate,
      });

      alert("Task Created Successfully");

      setTitle("");
      setDescription("");
      setProjectId("");
      setAssignedTo("");
      setDueDate("");
    } catch (error) {
      console.error(error);
      alert("Failed to Create Task");
    }
  };

  return (
    <div className="p-8 max-w-lg mx-auto">
      <h1 className="text-3xl font-bold mb-6">
        Create Task
      </h1>

      <input
        className="border p-2 w-full mb-3"
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />

      <input
        className="border p-2 w-full mb-3"
        placeholder="Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />

      <input
        className="border p-2 w-full mb-3"
        placeholder="Project ID"
        value={projectId}
        onChange={(e) => setProjectId(e.target.value)}
      />

      <input
        className="border p-2 w-full mb-3"
        placeholder="Assigned User ID"
        value={assignedTo}
        onChange={(e) => setAssignedTo(e.target.value)}
      />

      <input
        type="date"
        className="border p-2 w-full mb-3"
        value={dueDate}
        onChange={(e) => setDueDate(e.target.value)}
      />

      <button
        className="bg-green-500 text-white px-4 py-2 w-full"
        onClick={handleCreateTask}
      >
        Create Task
      </button>
    </div>
  );
}