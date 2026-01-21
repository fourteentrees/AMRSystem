import { createFileRoute } from "@tanstack/react-router";
import { Button } from "~/components/ui/button";

export const Route = createFileRoute("/_auth/dashboard/crawls/")({
  component: AdCrawlsIndex,
});

function AdCrawlsIndex() {
  const { user } = Route.useRouteContext();

  // Check if user role is eq or above 1. If not, return 401 page with return link to dashboard
  // @ts-expect-error -- It very much exists
  if (user.role < 1) {
    return (
      <div className="flex flex-col items-center gap-1">
        No.
        <Button onClick={() => window.location.href = '/dashboard'}>Return to Dashboard</Button>
      </div>
    );
  } else {
    return (
      <div className="flex flex-col items-center gap-1">
        Ad Crawls index page (Protected, role &gt;= 1)
        <pre className="bg-card text-card-foreground rounded-md border p-1 text-xs">
          routes/_auth/dashboard/crawls/index.tsx
        </pre>
        <div className="mt-2 text-center text-xs sm:text-sm">
          User data from route context:
          <pre className="max-w-screen overflow-x-auto px-2 text-start">
            {JSON.stringify(user, null, 2)}
          </pre>
        </div>
      </div>
    )
  }
}
