import adapter from "@sveltejs/adapter-auto"
import { vitePreprocess } from "@sveltejs/vite-plugin-svelte"
import { mdsvex } from "mdsvex"

/** @type {import('@sveltejs/kit').Config} */
const config = {
  extensions: [".svelte", ".md"],
  preprocess: [
    vitePreprocess(),
    mdsvex(
      /** @type {import('mdsvex').MdsvexOptions} */ ({
        extensions: [".md"],
      }),
    ),
  ],
  kit: {
    adapter: adapter(),
    csp: {
      mode: "nonce",
      directives: {
        "default-src": ["self", "localhost:*"],
        "connect-src": [
          "self",
          "localhost:*",
          "https://cloudflareinsights.com",
          "https://*.clarity.ms",
        ],
        "script-src": [
          "self",
          "unsafe-eval",
          "localhost:*",
          "https://static.cloudflareinsights.com",
          "https://www.clarity.ms",
        ],
        "style-src": ["self", "localhost:*", "unsafe-inline"],
        "upgrade-insecure-requests": true,
      },
    },
  },
  compilerOptions: {
    customElement: true,
  },
}

export default config
