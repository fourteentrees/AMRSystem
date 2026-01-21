import { createFileRoute } from "@tanstack/react-router";
import { Button } from "~/components/ui/button";

// @ts-expect-error This works, dont ask me how
export const Route = createFileRoute("/songrequest")({
  component: SongrequestPage,
});

function SongrequestPage() {
    return (
        <div className="flex flex-col items-center gap-4">
            <h1 className="text-2xl font-bold">Request a song to be played!</h1>
            <p className="text-foreground/80 max-sm:text-xs">
                Below is a table of available songs. Click on a song to request it.
            </p>
            <div className="overflow-x-auto w-full max-w-2xl">
                <table className="table-auto w-full border-collapse border border-gray-300">
                    <thead>
                        <tr>
                            <th className="border border-gray-300 px-4 py-2">Song Name</th>
                            <th className="border border-gray-300 px-4 py-2">URL</th>
                            <th className="border border-gray-300 px-4 py-2">Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        {/* Example song row */}
                        <tr>
                            <td className="border border-gray-300 px-4 py-2">Song A</td>
                            <td className="border border-gray-300 px-4 py-2">
                                <a href="https://example.com/song-a" className="text-blue-500 underline" target="_blank" rel="noreferrer">semistatic:Song.mp3</a>
                            </td>
                            <td className="border border-gray-300 px-4 py-2">
                                <Button>Request</Button>
                            </td>
                        </tr>
                        {/* TODO fetch from music table */}
                    </tbody>
                </table>
            </div>
        </div>
    );
}