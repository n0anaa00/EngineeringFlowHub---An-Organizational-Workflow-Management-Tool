import { syncJira }
from "../api/integrationAPI";

export default function Integrations() {

    const runSync = async () => {

        const result =
            await syncJira();

        console.log(result);
    };

    return (

        <div>

            <h1>
                Integrations
            </h1>

            <button
                onClick={runSync}
            >
                Sync Jira
            </button>

        </div>
    );
}