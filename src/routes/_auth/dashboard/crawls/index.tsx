import { createFileRoute } from "@tanstack/react-router";
import { SignOutButton } from "~/components/sign-out-button";

export const Route = createFileRoute("/_auth/dashboard/crawls/")({
  component: AdCrawlsIndex,
});

function AdCrawlsIndex() {
  const { user } = Route.useRouteContext();

  // todo :3
}
