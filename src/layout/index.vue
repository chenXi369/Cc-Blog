<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import Sidebar from './components/Sidebar.vue'
import { useAppStore } from '@/stores/app'

const route = useRoute()
const appStore = useAppStore()

const pageTitle = computed(() => {
  const titles: Record<string, string> = {
    '/': '首页&简介',
    '/tech-stack': '技术栈',
    '/inspiration': '灵感笔记',
    '/articles': '技术文章',
    '/gallery': '生活相册',
    '/workspace': '工作空间',
    '/navigation': '导航站',
    '/timeline': '时间笔记',
    '/projects': '项目',
    '/todos': '待办事项',
    '/requirements': '项目需求',
    '/demo': 'Demo',
    '/friends': '友链',
  }
  return titles[route.path] || '首页'
})

const pageSubtitle = computed(() => {
  const subtitles: Record<string, string> = {
    '/': '欢迎来到我的博客',
    '/requirements': '管理您的项目需求和开发计划',
  }
  return subtitles[route.path] || ''
})
</script>

<template>
  <div class="layout">
    <Sidebar />
    <main class="main-content" :class="{ collapsed: appStore.collapsed }">
      <header class="page-header">
        <div class="header-left">
          <h1 class="page-title">{{ pageTitle }}</h1>
          <p v-if="pageSubtitle" class="page-subtitle">{{ pageSubtitle }}</p>
        </div>
        <div class="header-right">
          <slot name="header-actions" />
        </div>
      </header>
      <div class="page-content">
        <RouterView />
      </div>
    </main>
  </div>
</template>

<style scoped>
.layout {
  display: flex;
  min-height: 100vh;
  background-color: #f5f5f5;
}

.main-content {
  flex: 1;
  margin-left: 260px;
  transition: margin-left 0.3s ease;
  display: flex;
  flex-direction: column;
}

.main-content.collapsed {
  margin-left: 64px;
}

.page-header {
  background: #fff;
  padding: 20px 24px;
  border-bottom: 1px solid #e8e8e8;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.page-title {
  font-size: 20px;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0;
}

.page-subtitle {
  font-size: 13px;
  color: #999;
  margin: 4px 0 0 0;
}

.page-content {
  flex: 1;
  padding: 24px;
  overflow-y: auto;
}
</style>
