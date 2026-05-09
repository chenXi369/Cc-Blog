<script setup lang="ts">
import { RouterView } from 'vue-router'
</script>

<template>
  <RouterView />
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #1a1a1a;
  background: #f5f5f5;
}

ul, ol {
  list-style: none;
}

a {
  text-decoration: none;
  color: inherit;
}

button {
  border: none;
  background: none;
  cursor: pointer;
  font-family: inherit;
}
</style>
