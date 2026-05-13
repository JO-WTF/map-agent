import { AgentChatPanel } from "@/components/workbench/AgentChatPanel";
import { AgentTimeline } from "@/components/workbench/AgentTimeline";
import { ResultTable } from "@/components/workbench/ResultTable";

export default function WorkbenchPage() {
  return (
    <main className="grid grid-cols-3 gap-4 p-4">
      <section><h2>Chat</h2><AgentChatPanel /></section>
      <section><h2>Map/Charts (placeholder)</h2><div className="h-64 border" /></section>
      <section><h2>Timeline</h2><AgentTimeline /></section>
      <section className="col-span-3"><h2>Result Table</h2><ResultTable /></section>
    </main>
  );
}
