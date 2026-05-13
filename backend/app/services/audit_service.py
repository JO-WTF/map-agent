class AuditService:
    def log_tool_call(self, tool_name: str, input_json: dict, output_json: dict) -> dict:
        return {"tool_name": tool_name, "input": input_json, "output": output_json, "status": "success"}
