<script lang="ts">
  export let img: string = ""
  export let heading: string = ""
  export let suffixItem: string = ""
  export let suffixGraph: object[] = []
</script>

<div class="flex items-center px-3 py-2 rounded-md">
  <!-- Heading and stuff -->
  <div class="flex gap-x-2">
    <img src={img} alt="" />
    <div class="flex flex-col">
      <span>{heading}</span>
    </div>
  </div>
  <!-- suffix -->
  <div>{suffixItem}</div>
</div>
