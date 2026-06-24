import api from "./axios";

export const syncJira = async () => {
    const response = await api.post(
        "/integrations/jira/sync"
    );

    return response.data;
};