// script to make the user object attached to the user identifier an administrator by granting them the administrative permissions associated with the user role value "2"
import "dotenv/config";

import { eq } from "drizzle-orm";
import { db } from "~/lib/db";
import { user as userTable } from "~/lib/db/schema";

async function promoteUser(email: string) {
  // Find the user by their identifier (e.g., email)
  const user = await db.query.user.findFirst({
    where: eq(userTable.email, email),
  });

  if (!user) {
    console.error(`User with email "${email}" not found.`);
    return;
  }

  // Update the user's role to administrator (assuming role "2" is admin)
  await db
    .update(userTable)
    .set({ role: 2 })
    .where(eq(userTable.id, user.id));

  console.log(`User with email "${email}" has been made an administrator.`);
}

// read the user email from command line arguments
const args = process.argv.slice(2);
if (args.length !== 1) {
  console.error("Usage: pnpm user:promote <email>");
  process.exit(1);
}

const email = args[0];

// Execute the function
promoteUser(email)
  .then(() => {
    console.log("Operation completed.");
    process.exit(0);
  })
  .catch((error) => {
    console.error("An error occurred:", error);
    process.exit(1);
  });
