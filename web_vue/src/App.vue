<template>
  <header>
    <div>
      <nav>
        <RouterLink to="/">home_view</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>
<script setup lang="ts"></script>

<style scoped></style>
