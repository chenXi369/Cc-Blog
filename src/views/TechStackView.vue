<script setup lang="ts">
import { ref } from 'vue'

interface TechItem {
  name: string
  icon: string
  category: string
  proficiency: number
  description: string
}

const techCategories = ref([
  {
    name: '前端框架',
    items: [
      { name: 'Vue.js', icon: 'V', proficiency: 95, description: '熟练掌握 Vue3 Composition API' },
      { name: 'React', icon: 'R', proficiency: 90, description: 'Hooks、Next.js 生态' },
      { name: 'TypeScript', icon: 'TS', proficiency: 92, description: '类型系统、泛型编程' },
    ],
  },
  {
    name: '构建工具',
    items: [
      { name: 'Vite', icon: 'V', proficiency: 88, description: '快速构建、HMR' },
      { name: 'Webpack', icon: 'W', proficiency: 85, description: '配置优化、Loader 开发' },
      { name: 'pnpm', icon: 'P', proficiency: 90, description: 'Monorepo 管理' },
    ],
  },
  {
    name: '图形 & 编辑器',
    items: [
      { name: 'Canvas', icon: 'C', proficiency: 88, description: '2D 绘图、动画' },
      { name: 'WebGL', icon: 'W', proficiency: 75, description: 'Three.js、着色器' },
      { name: 'Skia', icon: 'S', proficiency: 70, description: 'CanvasKit、图形渲染' },
    ],
  },
  {
    name: 'AI & 工具',
    items: [
      { name: 'OpenAI', icon: 'AI', proficiency: 82, description: 'API 集成、Prompt 工程' },
      { name: 'LangChain', icon: 'L', proficiency: 75, description: 'AI 应用开发' },
      { name: 'Cursor', icon: 'C', proficiency: 95, description: 'AI 辅助编程' },
    ],
  },
])
</script>

<template>
  <div class="tech-stack-page">
    <div class="tech-grid">
      <div
        v-for="category in techCategories"
        :key="category.name"
        class="category-card"
      >
        <h3 class="category-title">{{ category.name }}</h3>
        <div class="tech-list">
          <div
            v-for="tech in category.items"
            :key="tech.name"
            class="tech-item"
          >
            <div class="tech-header">
              <div class="tech-icon">{{ tech.icon }}</div>
              <div class="tech-info">
                <span class="tech-name">{{ tech.name }}</span>
                <span class="tech-desc">{{ tech.description }}</span>
              </div>
            </div>
            <div class="proficiency-bar">
              <div
                class="proficiency-fill"
                :style="{ width: tech.proficiency + '%' }"
              ></div>
            </div>
            <span class="proficiency-text">{{ tech.proficiency }}%</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.tech-stack-page {
  max-width: 1000px;
  margin: 0 auto;
}

.tech-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}

.category-card {
  background: #fff;
  border-radius: 12px;
  padding: 24px;
  border: 1px solid #e8e8e8;
}

.category-title {
  font-size: 16px;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0 0 20px 0;
  padding-bottom: 12px;
  border-bottom: 1px solid #f5f5f5;
}

.tech-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.tech-item {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.tech-header {
  display: flex;
  align-items: center;
  gap: 12px;
}

.tech-icon {
  width: 40px;
  height: 40px;
  background: #f5f5f5;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  font-weight: 600;
  color: #1a1a1a;
}

.tech-info {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.tech-name {
  font-size: 14px;
  font-weight: 600;
  color: #1a1a1a;
}

.tech-desc {
  font-size: 12px;
  color: #999;
}

.proficiency-bar {
  height: 6px;
  background: #f0f0f0;
  border-radius: 3px;
  overflow: hidden;
}

.proficiency-fill {
  height: 100%;
  background: #1a1a1a;
  border-radius: 3px;
  transition: width 0.6s ease;
}

.proficiency-text {
  font-size: 12px;
  color: #999;
  text-align: right;
}

@media (max-width: 768px) {
  .tech-grid {
    grid-template-columns: 1fr;
  }
}
</style>
