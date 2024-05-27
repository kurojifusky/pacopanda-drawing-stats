import type { Config } from "tailwindcss"
import typographyPlugin from "@tailwindcss/typography"
import defaultTheme from "tailwindcss/defaultTheme"

export default {
  darkMode: "class",
  content: ["./src/**/*.{html,svelte,ts}"],
  theme: {
    extend: {
      fontFamily: {
        inter: ["Inter", ...defaultTheme.fontFamily.sans],
        "open-sans": ["Open Sans", ...defaultTheme.fontFamily.sans],
        "jetbrains-mono": ["JetBrains Mono", ...defaultTheme.fontFamily.mono],
      },
    },
  },
  plugins: [typographyPlugin],
} satisfies Config
