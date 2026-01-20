import { createServerFn } from "@tanstack/react-start";
import { getRequest, setResponseHeader } from "@tanstack/react-start/server";
import { eq } from "drizzle-orm";
import { auth } from "~/lib/auth/auth";
import { db } from "~/lib/db";
import { user as userTable } from "~/lib/db/schema";

export const $getUser = createServerFn({ method: "GET" }).handler(async () => {
  const session = await auth.api.getSession({
    headers: getRequest().headers,
    returnHeaders: true,
  });

  const cookies = session.headers?.getSetCookie();
  if (cookies?.length) setResponseHeader("Set-Cookie", cookies);

  const sessionUser = session.response?.user;
  if (!sessionUser) return null;

  const dbUser = await db.query.user.findFirst({
    where: eq(userTable.id, sessionUser.id),
  });

  return dbUser ? { ...sessionUser, role: dbUser.role } : sessionUser;
});