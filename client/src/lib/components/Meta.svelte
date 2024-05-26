<script lang="ts">
  import * as config from "../config"

  export let title: string
  export let description = ""
</script>

<svelte:head>
  <title>{title} | {config.siteTitle}</title>
  <meta property="og:title" content={`${title} | ${config.siteTitle}`} />
  <meta name="twitter:title" content={`${title} | ${config.siteTitle}`} />
</svelte:head>
