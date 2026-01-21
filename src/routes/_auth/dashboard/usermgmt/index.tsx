import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/_auth/dashboard/usermgmt/')({
  component: RouteComponent,
})

function RouteComponent() {
  const { user } = Route.useRouteContext()

  // Check if user role is eq or above 2. If not, return 401 page with return link to dashboard
  // @ts-expect-error -- It very much exists
  if (user.role < 2) {
    return (
      <div className="flex flex-col items-center gap-1">
        Oh HELL no.
        <button onClick={() => (window.location.href = '/dashboard')}>
          Return to Dashboard
        </button>
      </div>
    )
  } else {
    return (
      <div className="flex flex-col items-center gap-1">
        User Management index page (Protected, role &gt;= 2)
        <pre className="bg-card text-card-foreground rounded-md border p-1 text-xs">
          routes/_auth/dashboard/usermgmt/index.tsx
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
