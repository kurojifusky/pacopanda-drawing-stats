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
        "connect-src": ["self"],
      },
    },
  },
  compilerOptions: {
    customElement: true,
  },
}

export default config
