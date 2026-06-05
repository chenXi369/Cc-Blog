<script setup lang="ts">
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAppStore } from '@/stores/app'
import type { FunctionalComponent } from 'vue'
import type { LucideProps } from 'lucide-vue-next'
import {
  Home,
  Cpu,
  FileText,
  Image,
  Briefcase,
  Clock,
  Folder,
  CheckSquare,
  ListTodo,
  Link,
  ChevronLeft,
  ChevronRight,
  X,
} from 'lucide-vue-next'

const route = useRoute()
const router = useRouter()
const appStore = useAppStore()

type IconComponent = FunctionalComponent<LucideProps>

const iconMap: Record<string, IconComponent> = {
  Home,
  Cpu,
  FileText,
  Image,
  Briefcase,
  Clock,
  Folder,
  CheckSquare,
  ListTodo,
  Link,
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

const handleNavClick = (path: string): void => {
  navigateTo(path)
  appStore.closeMobileMenu()
}
</script>

<template>
  <Teleport to="body">
    <div
      v-if="appStore.mobileMenuOpen"
      class="sidebar-overlay"
      @click="appStore.closeMobileMenu"
    />
  </Teleport>
  <aside
    class="sidebar"
    :class="{ collapsed: appStore.collapsed, 'mobile-open': appStore.mobileMenuOpen }"
  >
    <div class="sidebar-header">
      <div class="logo">
        <div class="logo-icon">O</div>
        <div class="logo-text">
          <div class="logo-title">CC</div>
          <div class="logo-desc">不知名程序员</div>
        </div>
      </div>
      <button
        class="collapse-btn desktop-only"
        :aria-label="appStore.collapsed ? '展开侧边栏' : '收起侧边栏'"
        @click="appStore.toggleCollapsed"
      >
        <ChevronLeft v-if="!appStore.collapsed" :size="16" />
        <ChevronRight v-else :size="16" />
      </button>
      <button
        class="mobile-close-btn"
        aria-label="关闭菜单"
        @click="appStore.closeMobileMenu"
      >
        <X :size="20" />
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
          @click="handleNavClick(item.path)"
          @keydown.enter="handleNavClick(item.path)"
        >
          <component
            :is="getMenuIcon(item.icon)"
            v-if="getMenuIcon(item.icon)"
            :size="18"
            class="nav-icon"
            aria-hidden="true"
          />
          <span class="nav-text">{{ item.name }}</span>
          <span v-if="item.badge" class="nav-badge">{{ item.badge }}</span>
        </li>
      </ul>
    </nav>
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

.sidebar.collapsed .logo-text {
  opacity: 0;
  max-width: 0;
  transition: opacity 0.12s ease, max-width 0.2s ease;
}

.sidebar.collapsed .nav-text {
  opacity: 0;
  max-width: 0;
  transition: opacity 0.12s ease, max-width 0.2s ease;
}

.sidebar.collapsed .nav-badge {
  opacity: 0;
  max-width: 0;
  transition: opacity 0.12s ease, max-width 0.2s ease;
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

.logo-text {
  white-space: nowrap;
  overflow: hidden;
  opacity: 1;
  max-width: 200px;
  transition: opacity 0.2s ease 0.15s, max-width 0.3s ease;
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
  white-space: nowrap;
  overflow: hidden;
  opacity: 1;
  max-width: 200px;
  transition: opacity 0.2s ease 0.15s, max-width 0.3s ease;
}

.nav-badge {
  background: #ff4d4f;
  color: #fff;
  font-size: 11px;
  padding: 2px 6px;
  border-radius: 10px;
  min-width: 18px;
  text-align: center;
  white-space: nowrap;
  overflow: hidden;
  opacity: 1;
  max-width: 100px;
  transition: opacity 0.2s ease 0.15s, max-width 0.3s ease;
}

.mobile-close-btn {
  display: none;
  width: 32px;
  height: 32px;
  border: none;
  background: none;
  border-radius: 4px;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: #666;
}

.sidebar-overlay {
  display: none;
}

@media (max-width: 768px) {
  .sidebar {
    position: fixed;
    left: 0;
    top: 0;
    transform: translateX(-100%);
    z-index: 200;
    width: 280px;
    box-shadow: 2px 0 8px rgba(0, 0, 0, 0.15);
  }

  .sidebar.mobile-open {
    transform: translateX(0);
  }

  .sidebar.collapsed {
    width: 280px;
  }

  .desktop-only {
    display: none !important;
  }

  .mobile-close-btn {
    display: flex;
  }

  .logo-text,
  .nav-text,
  .nav-badge {
    opacity: 1 !important;
    max-width: 200px !important;
  }

  .sidebar-overlay {
    display: block;
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.5);
    z-index: 199;
  }
}
</style>
