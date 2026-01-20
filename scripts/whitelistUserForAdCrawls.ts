// script to permit the user object attached to the user identifier to create and manage advertising crawls by granting them the permissions associated with the user role value "1"
import { eq } from "drizzle-orm";
import { db } from "~/lib/db";
import { user as userTable } from "~/lib/db/schema";

async function whitelistUserForAdCrawls(userIdentifier: string) {
  // Find the user by their identifier (e.g., email)
  const user = await db.query.user.findFirst({
    where: eq(userTable.email, userIdentifier),
  });

  if (!user) {
    console.error(`User with identifier "${userIdentifier}" not found.`);
    return;
  }

  // Update the user's role to allow advertising crawls (role "1")
  await db
    .update(userTable)
    .set({ role: 1 })
    .where(eq(userTable.id, user.id));

  console.log(`User with identifier "${userIdentifier}" has been whitelisted for ad crawls. They should be able to see these changes immediately.`);
}

// read the user identifier from command line arguments
const args = process.argv.slice(2);
if (args.length !== 1) {
  console.error("Usage: pnpm run wlcrawl <user-identifier>");
  process.exit(1);
}

const userIdentifier = args[0];

// Execute the function
whitelistUserForAdCrawls(userIdentifier)
  .then(() => {
    console.log("Operation completed.");
    process.exit(0);
  })
  .catch((error) => {
    console.error("An error occurred:", error);
    process.exit(1);
  });