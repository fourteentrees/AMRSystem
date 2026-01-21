// script to permit the user object attached to the user identifier to create and manage advertising crawls by granting them the permissions associated with the user role value "1"
import "dotenv/config";

import { eq } from "drizzle-orm";
import { db } from "~/lib/db";
import { user as userTable } from "~/lib/db/schema";

async function whitelistUser(email: string) {
  const user = await db.query.user.findFirst({
    where: eq(userTable.email, email),
  });

  if (!user) {
    console.error(`User with email "${email}" not found.`);
    return;
  }

  await db
    .update(userTable)
    .set({ role: 1 })
    .where(eq(userTable.id, user.id));

  console.log(
    `User with email "${email}" has been whitelisted for ad crawls. They should be able to see these changes immediately.`,
  );
}

// read the user email from command line arguments
const args = process.argv.slice(2);
if (args.length !== 1) {
  console.error("Usage: pnpm user:whitelist <email>");
  process.exit(1);
}

const email = args[0];

// Execute the function
whitelistUser(email)
  .then(() => {
    console.log("Operation completed.");
    process.exit(0);
  })
  .catch((error) => {
    console.error("An error occurred:", error);
    process.exit(1);
  });
