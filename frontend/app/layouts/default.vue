<template>
  <div class="w-full h-screen flex flex-col">
    <div class="h-[100px]">
      <NavbarMain />
    </div>
    <div class="w-full grow">
      <slot />
    </div>
  </div>
</template>
