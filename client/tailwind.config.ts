import type { Config } from "tailwindcss"
import typographyPlugin from "@tailwindcss/typography"

const fonts = ["system-ui", "sans-serif"]

export default {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  theme: {
    extend: {
      fontFamily: {
        heading: ["Inter", ...fonts],
        body: ["Open Sans", ...fonts],
      },
    },
  },
  plugins: [typographyPlugin],
} satisfies Config
