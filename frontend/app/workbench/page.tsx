import { AgentChatPanel } from "@/components/workbench/AgentChatPanel";
import { AgentTimeline } from "@/components/workbench/AgentTimeline";
import { ResultTable } from "@/components/workbench/ResultTable";
import { MapPanel } from "@/components/workbench/MapPanel";
import { ChartPanel } from "@/components/workbench/ChartPanel";
import { TaskStatusBar } from "@/components/workbench/TaskStatusBar";

export default function WorkbenchPage() {
  return (
    <main className="p-4">
      <TaskStatusBar />
      <section className="grid grid-cols-3 gap-4">
        <section><h2>Chat</h2><AgentChatPanel /></section>
        <section><MapPanel /></section>
        <section><ChartPanel /></section>
      </section>
      <section className="mt-4 grid grid-cols-2 gap-4">
        <section><h2>Timeline</h2><AgentTimeline /></section>
        <section><h2>Result Table</h2><ResultTable /></section>
      </section>
    </main>
  );
}
