import { useEffect, useState } from "react";

import { getTasks }
from "../api/taskAPI";

export default function Tasks() {

    const [tasks,
        setTasks] = useState([]);

    useEffect(() => {

        getTasks()
            .then(setTasks);

    }, []);

    return (

        <div>

            <h1>Tasks</h1>

            {tasks.map(
                (task: any) => (

                <div key={task.id}>

                    {task.title}

                </div>

            ))}

        </div>
    );
}