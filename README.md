# "Windev" AMRSystem

TanStack Start-based ad crawl and music request manager.

Built originally for [KWSF-IP](https://live.mistwx.com/player?channel=kwsf01) but can be easily adapted for any STAR/OBS-based system!

## STACC
- [React 19](https://react.dev) + [React Compiler](https://react.dev/learn/react-compiler)
- TanStack [Start](https://tanstack.com/start/latest) + [Router](https://tanstack.com/router/latest) + [Query](https://tanstack.com/query/latest)
- [Tailwind CSS](https://tailwindcss.com/) + [shadcn/ui](https://ui.shadcn.com/) + [Base UI](https://base-ui.com/)
- [Vite 8](https://vite.dev/blog/announcing-vite8-beta) (beta) + [Nitro v3](https://v3.nitro.build/) (nightly)
- [Drizzle ORM](https://orm.drizzle.team/) + PostgreSQL
- [Better Auth](https://www.better-auth.com/)

## Getting Started

1. Install dependencies:

   ```bash
   pnpm install
   ```

2. Create a `.env` file based on [`.env.example`](./.env.example).

3. Don't be a moron, and push the schema to your database with drizzle-kit:

   ```bash
   pnpm db push
   ```

   https://orm.drizzle.team/docs/migrations

   While it will run without this, it will crash, burn, detonate, and explode, all at once, when you sign in.

4. Run the development server:

   ```bash
   pnpm dev
   ```

   The development server should now be running at [http://localhost:3000](http://localhost:3000).

## Deploying to production

Refer to the [TanStack Start hosting docs](https://tanstack.com/start/latest/docs/framework/react/guide/hosting) for deploying to other platforms.

## Issue watchlist

- [Router/Start issues](https://github.com/TanStack/router/issues) - TanStack Start is in RC.
- [Devtools releases](https://github.com/TanStack/devtools/releases) - TanStack Devtools is in alpha and may still have breaking changes.
- [Vite 8 beta](https://vite.dev/blog/announcing-vite8-beta) - We're using Vite 8 beta which is powered by Rolldown.
- [Nitro v3 nightly](https://v3.nitro.build/docs/nightly) - The template is configured with Nitro v3 nightly by default.

## Goodies

#### Scripts

We use **pnpm**.

- **`auth:generate`** - Regenerate the [auth db schema](./src/lib/db/schema/auth.schema.ts) if you've made changes to your Better Auth [config](./src/lib/auth/auth.ts).
- **`db`** - Run [drizzle-kit](https://orm.drizzle.team/docs/kit-overview) commands. (e.g. `pnpm db generate`, `pnpm db studio`)
- **`ui`** - The shadcn/ui CLI. (e.g. `pnpm ui add button`)
- **`format`**, **`lint`**, **`check-types`** - Run Prettier, ESLint, and check TypeScript types respectively.
  - **`check`** - Run all three above. (e.g. `pnpm check`)
- **`deps`** - Selectively upgrade dependencies via taze.
- **`user:promote`** - Make a user admin via their email. (e.g. `pnpm makeadmin advertising.employee@dimwitnetworks.org`)
- **`user:whitelist`** - Whitelist a user for the `/dashboard/crawls` routes via their email. (e.g. `pnpm whitelist marketing.client@notdimwitnetworks.org`)
- **`user:demote`** - Remove admin AND whitelist status from a user via their email. (e.g. `pnpm demote fired.employee@dimwitnetworks.org`)

**Note: Use user:whitelist if you'd like to strip a user's admin but retain their crawl access.**
#### Utilities

- [`auth/middleware.ts`](./src/lib/auth/middleware.ts) - Sample middleware for forcing authentication on server functions. (see [#5](https://github.com/dotnize/react-tanstarter/issues/5#issuecomment-2615905686) and [#17](https://github.com/dotnize/react-tanstarter/issues/17#issuecomment-2853482062))
- [`theme-toggle.tsx`](./src/components/theme-toggle.tsx), [`theme-provider.tsx`](./src/components/theme-provider.tsx) - A theme toggle and provider for toggling between light and dark mode. ([#7](https://github.com/dotnize/react-tanstarter/issues/7#issuecomment-3141530412))

## License

AMRSystem, an ad crawl and music request manager for OBS/i2-based systems.
Copyright (C) 2026 Hayden Walker.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
