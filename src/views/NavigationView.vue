<script setup lang="ts">
import { ref } from 'vue'
import { ExternalLink, Star } from 'lucide-vue-next'

interface NavCategory {
  name: string
  items: {
    name: string
    url: string
    description: string
    icon: string
    isFavorite?: boolean
  }[]
}

const navCategories = ref<NavCategory[]>([
  {
    name: '开发工具',
    items: [
      { name: 'GitHub', url: 'https://github.com', description: '代码托管平台', icon: 'G' },
      { name: 'Vercel', url: 'https://vercel.com', description: '前端部署平台', icon: 'V' },
      { name: 'CodePen', url: 'https://codepen.io', description: '在线代码编辑器', icon: 'C' },
      { name: 'StackBlitz', url: 'https://stackblitz.com', description: '云端 IDE', icon: 'S' },
    ],
  },
  {
    name: '学习资源',
    items: [
      { name: 'MDN', url: 'https://developer.mozilla.org', description: 'Web 技术文档', icon: 'M' },
      { name: '掘金', url: 'https://juejin.cn', description: '技术社区', icon: 'J' },
      { name: '知乎', url: 'https://zhihu.com', description: '问答社区', icon: 'Z' },
      { name: 'Bilibili', url: 'https://bilibili.com', description: '视频学习', icon: 'B' },
    ],
  },
  {
    name: '设计资源',
    items: [
      { name: 'Figma', url: 'https://figma.com', description: '协作设计工具', icon: 'F' },
      { name: 'Dribbble', url: 'https://dribbble.com', description: '设计灵感', icon: 'D' },
      { name: 'Iconify', url: 'https://iconify.design', description: '图标库', icon: 'I' },
      { name: 'Unsplash', url: 'https://unsplash.com', description: '免费图片', icon: 'U' },
    ],
  },
])
</script>

<template>
  <div class="navigation-page">
    <div class="nav-grid">
      <div
        v-for="category in navCategories"
        :key="category.name"
        class="nav-category"
      >
        <h3 class="category-title">{{ category.name }}</h3>
        <div class="nav-items">
          <a
            v-for="item in category.items"
            :key="item.name"
            :href="item.url"
            target="_blank"
            class="nav-item"
          >
            <div class="nav-item-icon">{{ item.icon }}</div>
            <div class="nav-item-info">
              <div class="nav-item-header">
                <span class="nav-item-name">{{ item.name }}</span>
                <ExternalLink :size="12" class="nav-item-link" />
              </div>
              <span class="nav-item-desc">{{ item.description }}</span>
            </div>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.navigation-page {
  max-width: 1000px;
  margin: 0 auto;
}

.nav-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.nav-category {
  background: #fff;
  border-radius: 12px;
  padding: 24px;
  border: 1px solid #e8e8e8;
}

.category-title {
  font-size: 16px;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0 0 16px 0;
  padding-bottom: 12px;
  border-bottom: 1px solid #f5f5f5;
}

.nav-items {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  border-radius: 8px;
  transition: all 0.2s;
}

.nav-item:hover {
  background: #f5f5f5;
}

.nav-item-icon {
  width: 40px;
  height: 40px;
  background: #f5f5f5;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  font-weight: 600;
  color: #1a1a1a;
  flex-shrink: 0;
}

.nav-item-info {
  flex: 1;
  min-width: 0;
}

.nav-item-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 2px;
}

.nav-item-name {
  font-size: 14px;
  font-weight: 500;
  color: #1a1a1a;
}

.nav-item-link {
  color: #999;
}

.nav-item-desc {
  font-size: 12px;
  color: #999;
}

@media (max-width: 768px) {
  .nav-grid {
    grid-template-columns: 1fr;
  }
}
</style>
