<script lang="ts">
  const navItems = ["Browse", "About"]
</script>

<nav class="sticky top-0 px-8 py-3.5 flex items-center justify-between">
  <div>
    <a href="/">
      <img src="./max-icon.png" alt="" class="size-10 rounded-md" />
    </a>
  </div>
  <ul class="flex gap-x-0.5">
    {#each navItems as item}
      <li>
        <a class="px-3 h-full block" href={`/${item.toLowerCase()}`}>
          {item}
        </a>
      </li>
    {/each}
  </ul>
</nav>
