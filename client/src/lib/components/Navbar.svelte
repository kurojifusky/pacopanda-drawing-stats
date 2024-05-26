<script lang="ts">
  const navItems = ["Browse", "About"]
</script>

<nav class="sticky top-0 px-6 py-2">
  <div><a href="/">logo</a></div>
  <ul>
    {#each navItems as item}
      <li>
        <a href={`/${item.toLowerCase()}`}>
          {item}
        </a>
      </li>
    {/each}
  </ul>
</nav>
