import { createFileRoute, Link, Outlet } from "@tanstack/react-router";
import { Button } from "~/components/ui/button";
export const Route = createFileRoute("/_auth/dashboard")({
  component: DashboardLayout,
});

function DashboardLayout() {
  const { user } = Route.useRouteContext();

  // @ts-expect-error -- It very much exists
  const showCrawlsButton = user.role >= 1;

  return (
    <div className="flex min-h-svh flex-col items-center justify-center gap-10 p-2">
      <div className="flex flex-col items-center gap-2">
        <h1 className="text-3xl font-bold sm:text-4xl">DimwitNetworks Requestr</h1>

        <div className="text-foreground/80 mb-4 flex flex-col items-center gap-2 text-sm">
          Buttons for what you can do:
        </div>

        {showCrawlsButton && (
          <Button render={<Link to="/dashboard/crawls" />} className="w-fit" size="lg">
            Ad Crawls
          </Button>
        )}
        <Button render={<Link to="/dashboard" />} className="w-fit" size="lg" nativeButton={false}>
          Back to Dashboard
        </Button>
      </div>

      <Outlet />
    </div>
  );
}
