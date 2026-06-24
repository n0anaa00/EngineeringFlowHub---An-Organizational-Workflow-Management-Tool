import {
BrowserRouter,
Routes,
Route
}
from "react-router-dom";

import Dashboard
from "../pages/Dashboard";

import Projects
from "../pages/Projects";

import Tasks
from "../pages/Tasks";

import Integrations
from "../pages/Integrations";

export default function Router() {

    return (

        <BrowserRouter>

            <Routes>

                <Route
                    path="/"
                    element={<Dashboard />}
                />

                <Route
                    path="/projects"
                    element={<Projects />}
                />

                <Route
                    path="/tasks"
                    element={<Tasks />}
                />

                <Route
                    path="/integrations"
                    element={<Integrations />}
                />

            </Routes>

        </BrowserRouter>
    );
}