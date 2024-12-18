<script lang="ts">
  import * as config from "../config"

  export let title: string
  export let description = ""
</script>

<svelte:head>
  <title>{title} | {config.siteTitle}</title>
  <meta name="description" content={description} />
  <meta property="og:title" content={`${title} | ${config.siteTitle}`} />
  <meta property="og:description" content={description} />
</svelte:head>
