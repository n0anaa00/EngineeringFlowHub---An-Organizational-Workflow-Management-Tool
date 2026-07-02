export interface Integration {
    id: number;
    source_system: string;
    external_id: string;
    sync_status: "SUCCESS" | "FAILED" | "PENDING";
    synced_at?: string;
}