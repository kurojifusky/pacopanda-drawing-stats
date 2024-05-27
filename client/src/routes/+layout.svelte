<script>
  import "../app.css"
  import "@fontsource/inter"
  import "@fontsource/open-sans"
  import "@fontsource/jetbrains-mono"

  import Footer from "$lib/components/Footer.svelte"
  import Navbar from "$lib/components/Navbar.svelte"
</script>

<Navbar />

<main>
  <slot />
</main>

<Footer />
