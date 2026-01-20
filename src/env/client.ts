import { createEnv } from "@t3-oss/env-core";
import * as z from "zod";

export const env = createEnv({
  clientPrefix: "VITE_",
  client: {
    VITE_BASE_URL: z.url().default("https://expert-dollop-54559rwp69637pw5-3000.app.github.dev/"),
  },
  runtimeEnv: import.meta.env,
});
