import type { Config } from "tailwindcss"
import typographyPlugin from "@tailwindcss/typography"

export default {
  darkMode: "class",
  content: ["./src/**/*.{html,svelte,ts}"],
  theme: {
    extend: {
    },
  },
  plugins: [typographyPlugin],
} satisfies Config
