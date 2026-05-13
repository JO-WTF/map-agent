export type TaskResult = {
  summary: Record<string, any>;
  map_data: Record<string, any>;
  charts: Record<string, any>;
  tables: Record<string, any>;
  files: Record<string, any>;
  logs: Array<Record<string, any>>;
};
