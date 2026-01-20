import { pgTable, text, timestamp } from "drizzle-orm/pg-core";

export const crawls = pgTable("crawls", {
    id: text("id").primaryKey(),
    name: text("name").notNull(),
    content: text("content").notNull(),
    createdAt: timestamp("created_at").defaultNow().notNull(),
    updatedAt: timestamp("updated_at")
      .defaultNow()
      .$onUpdate(() => /* @__PURE__ */ new Date())
      .notNull(),
});