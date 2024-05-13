/* eslint-disable import/no-unresolved */
import { defineConfig } from "astro/config"

import tailwind from "@astrojs/tailwind"
import lit from "@astrojs/lit"
import sitemap from "@astrojs/sitemap"
import vercel from "@astrojs/vercel/serverless"

// https://astro.build/config
export default defineConfig({
  integrations: [lit(), tailwind(), sitemap()],
  output: "server",
  adapter: vercel(),
})
