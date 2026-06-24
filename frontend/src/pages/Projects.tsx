import { useEffect, useState } from "react";

import { getProjects }
from "../api/projectAPI";

export default function Projects() {

    const [projects,
        setProjects] = useState([]);

    useEffect(() => {

        getProjects()
            .then(setProjects);

    }, []);

    return (

        <div>

            <h1>Projects</h1>

            <table>

                <thead>

                <tr>
                    <th>Name</th>
                    <th>Status</th>
                </tr>

                </thead>

                <tbody>

                {projects.map(
                    (project: any) => (

                    <tr key={project.id}>

                        <td>
                            {project.name}
                        </td>

                        <td>
                            {project.status}
                        </td>

                    </tr>

                ))}

                </tbody>

            </table>

        </div>
    );
}