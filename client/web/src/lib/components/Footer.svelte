<script lang="ts">
  const fullDate = new Date().getFullYear()

  const copyright = `© ${fullDate} Kerby Keith Aquino, licensed under Apache 2.0`
  const githubUrl = "https://github.com/kurojifusky/pacopanda-drawing-stats"
</script>

<footer class="px-8 py-6">
  <p>{copyright}</p>
  <a href={githubUrl} target="_blank" rel="noreferer noopener"> Source code </a>
</footer>
