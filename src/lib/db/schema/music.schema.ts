import { pgTable, text, timestamp } from "drizzle-orm/pg-core";

export const music = pgTable("music", {
    id: text("id").primaryKey(),
    name: text("name").notNull(),
    url: text("url").notNull(),
    createdAt: timestamp("created_at").defaultNow().notNull(),
    updatedAt: timestamp("updated_at")
      .defaultNow()
      .$onUpdate(() => /* @__PURE__ */ new Date())
      .notNull(),
});

export const musicrequests = pgTable("music_requests", {
    id: text("id").primaryKey(),
    userId: text("user_id").notNull(),
    musicId: text("music_id")
    .notNull()
    .references(() => music.id, { onDelete: "cascade" }),
    status: text("status").default("pending").notNull(),
    createdAt: timestamp("created_at").defaultNow().notNull(),
    updatedAt: timestamp("updated_at")
      .defaultNow()
      .$onUpdate(() => /* @__PURE__ */ new Date())
      .notNull(),
});