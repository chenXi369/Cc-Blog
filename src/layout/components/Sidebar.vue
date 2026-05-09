<script setup lang="ts">
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAppStore } from '@/stores/app'
import type { FunctionalComponent } from 'vue'
import type { LucideProps } from 'lucide-vue-next'
import {
  Home,
  Cpu,
  Lightbulb,
  FileText,
  Image,
  Briefcase,
  Compass,
  Clock,
  Folder,
  CheckSquare,
  ListTodo,
  Play,
  Link,
  Github,
  BookOpen,
  Database,
  Video,
  Twitter,
  ChevronLeft,
  ChevronRight,
} from 'lucide-vue-next'

const route = useRoute()
const router = useRouter()
const appStore = useAppStore()

type IconComponent = FunctionalComponent<LucideProps>

const iconMap: Record<string, IconComponent> = {
  Home,
  Cpu,
  Lightbulb,
  FileText,
  Image,
  Briefcase,
  Compass,
  Clock,
  Folder,
  CheckSquare,
  ListTodo,
  Play,
  Link,
}

const onlineIconMap: Record<string, IconComponent> = {
  Github,
  BookOpen,
  Database,
  Video,
  Twitter,
}

const isActive = computed(() => (path: string) => {
  if (path === '/') {
    return route.path === '/'
  }
  return route.path === path
})

const navigateTo = (path: string): void => {
  if (route.path !== path) {
    router.push(path)
  }
}

const getMenuIcon = (iconName: string): IconComponent | undefined => {
  return iconMap[iconName]
}

const getOnlineIcon = (iconName: string): IconComponent | undefined => {
  return onlineIconMap[iconName]
}
</script>

<template>
  <aside class="sidebar" :class="{ collapsed: appStore.collapsed }">
    <div class="sidebar-header">
      <div class="logo">
        <div class="logo-icon">O</div>
        <div v-if="!appStore.collapsed" class="logo-text">
          <div class="logo-title">ObjectX</div>
          <div class="logo-desc">不知名程序员</div>
        </div>
      </div>
      <button
        class="collapse-btn"
        :aria-label="appStore.collapsed ? '展开侧边栏' : '收起侧边栏'"
        @click="appStore.toggleCollapsed"
      >
        <ChevronLeft v-if="!appStore.collapsed" :size="16" />
        <ChevronRight v-else :size="16" />
      </button>
    </div>

    <nav class="sidebar-nav" aria-label="主导航">
      <ul class="nav-list" role="menubar">
        <li
          v-for="item in appStore.menuItems"
          :key="item.id"
          class="nav-item"
          :class="{ active: isActive(item.path) }"
          role="menuitem"
          tabindex="0"
          @click="navigateTo(item.path)"
          @keydown.enter="navigateTo(item.path)"
        >
          <component
            :is="getMenuIcon(item.icon)"
            v-if="getMenuIcon(item.icon)"
            :size="18"
            class="nav-icon"
            aria-hidden="true"
          />
          <span v-if="!appStore.collapsed" class="nav-text">{{ item.name }}</span>
          <span v-if="!appStore.collapsed && item.badge" class="nav-badge">{{ item.badge }}</span>
        </li>
      </ul>
    </nav>

    <div v-if="!appStore.collapsed" class="sidebar-footer">
      <div class="footer-label">Online</div>
      <ul class="online-list" role="list">
        <li v-for="link in appStore.onlineLinks" :key="link.name" class="online-item">
          <component
            :is="getOnlineIcon(link.icon)"
            v-if="getOnlineIcon(link.icon)"
            :size="14"
            class="online-icon"
            aria-hidden="true"
          />
          <span class="online-name">{{ link.name }}</span>
          <a :href="link.url" target="_blank" rel="noopener noreferrer" class="online-arrow" aria-label="打开 {{ link.name }}">
            →
          </a>
        </li>
      </ul>
    </div>
  </aside>
</template>

<style scoped>
.sidebar {
  width: 260px;
  height: 100vh;
  background: #fff;
  border-right: 1px solid #e8e8e8;
  display: flex;
  flex-direction: column;
  position: fixed;
  left: 0;
  top: 0;
  z-index: 100;
  transition: width 0.3s ease;
}

.sidebar.collapsed {
  width: 64px;
}

.sidebar-header {
  padding: 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid #f0f0f0;
}

.logo {
  display: flex;
  align-items: center;
  gap: 10px;
}

.logo-icon {
  width: 36px;
  height: 36px;
  background: #1a1a1a;
  color: #fff;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 16px;
  flex-shrink: 0;
}

.logo-title {
  font-size: 15px;
  font-weight: 600;
  color: #1a1a1a;
  line-height: 1.2;
}

.logo-desc {
  font-size: 11px;
  color: #999;
  line-height: 1.2;
}

.collapse-btn {
  width: 24px;
  height: 24px;
  border: 1px solid #e8e8e8;
  background: #fff;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: #666;
  flex-shrink: 0;
  transition: background-color 0.2s;
}

.collapse-btn:hover {
  background: #f5f5f5;
}

.sidebar-nav {
  flex: 1;
  overflow-y: auto;
  padding: 8px 0;
}

.nav-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 16px;
  margin: 2px 8px;
  border-radius: 6px;
  cursor: pointer;
  color: #666;
  font-size: 14px;
  transition: all 0.2s;
  position: relative;
  outline: none;
}

.nav-item:hover {
  background: #f5f5f5;
  color: #1a1a1a;
}

.nav-item:focus-visible {
  box-shadow: 0 0 0 2px #1a1a1a;
}

.nav-item.active {
  background: #1a1a1a;
  color: #fff;
}

.nav-icon {
  flex-shrink: 0;
}

.nav-text {
  flex: 1;
}

.nav-badge {
  background: #ff4d4f;
  color: #fff;
  font-size: 11px;
  padding: 2px 6px;
  border-radius: 10px;
  min-width: 18px;
  text-align: center;
}

.sidebar-footer {
  padding: 16px;
  border-top: 1px solid #f0f0f0;
}

.footer-label {
  font-size: 11px;
  color: #999;
  text-transform: uppercase;
  margin-bottom: 8px;
  letter-spacing: 1px;
}

.online-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.online-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 6px 0;
  font-size: 13px;
  color: #666;
}

.online-icon {
  color: #999;
}

.online-name {
  flex: 1;
}

.online-arrow {
  color: #999;
  text-decoration: none;
  font-size: 12px;
  transition: color 0.2s;
}

.online-arrow:hover {
  color: #1a1a1a;
}
</style>
