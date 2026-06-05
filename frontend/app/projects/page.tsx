"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import api from "../../services/api";

export default function ProjectsPage() {
  const [projects, setProjects] = useState<any[]>([]);

  useEffect(() => {
    fetchProjects();
  }, []);

  const fetchProjects = async () => {
    try {
      const response = await api.get("/projects/");
      setProjects(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="p-8">
      <div className="mb-4 space-x-4">
  <Link href="/projects">Projects</Link>

  <Link href="/tasks">Tasks</Link>

  <Link href="/create-task">Create Task</Link>

  <button
    onClick={() => {
      localStorage.removeItem("token");
      window.location.href = "/";
    }}
    className="ml-4 bg-red-500 text-white px-3 py-1 rounded"
  >
    Logout
  </button>
</div>

      <h1 className="text-3xl font-bold mb-6">
        Projects
      </h1>

      {projects.map((project) => (
        <div
          key={project.id}
          className="border p-4 mb-4 rounded"
        >
          <h2 className="text-xl font-semibold">
            {project.name}
          </h2>

          <p>{project.description}</p>

          <p className="text-sm text-gray-500">
            Created By: {project.created_by}
          </p>
        </div>
      ))}
    </div>
  );
}