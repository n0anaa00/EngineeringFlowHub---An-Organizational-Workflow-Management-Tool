import { useEffect, useState } from "react";

import KPIWidget from
"../components/KPIWidget";

import api from "../api/axios";

export default function Dashboard() {

    const [data, setData] = useState<any>();

    useEffect(() => {

        api
            .get("/reports/dashboard")
            .then(res => setData(res.data));

    }, []);

    if (!data)
        return <p>Loading...</p>;

    return (

        <div>

            <h1>Dashboard</h1>

            <KPIWidget
                title="Projects"
                value={data.projects}
            />

            <KPIWidget
                title="Open Tasks"
                value={data.open_tasks}
            />

            <KPIWidget
                title="Completed Tasks"
                value={data.completed_tasks}
            />

        </div>
    );
}