<script setup lang="ts">
import { ref } from 'vue'
import { Github, ExternalLink, Star, GitFork } from 'lucide-vue-next'

interface Project {
  id: number
  name: string
  description: string
  techStack: string[]
  stars: number
  forks: number
  url: string
  demoUrl?: string
  status: 'active' | 'archived' | 'completed'
}

const projects = ref<Project[]>([
  {
    id: 1,
    name: 'Vue3 Blog',
    description: '基于 Vue3 的个人博客系统，支持文章管理、项目展示等功能',
    techStack: ['Vue3', 'TypeScript', 'Vite'],
    stars: 128,
    forks: 32,
    url: 'https://github.com',
    demoUrl: '#',
    status: 'active',
  },
  {
    id: 2,
    name: 'Canvas Editor',
    description: '基于 Canvas 的图形编辑器，支持多种图形绘制和编辑',
    techStack: ['Canvas', 'TypeScript', 'Webpack'],
    stars: 256,
    forks: 48,
    url: 'https://github.com',
    status: 'active',
  },
  {
    id: 3,
    name: 'AI Chat Tool',
    description: '集成 OpenAI API 的智能聊天工具，支持多种模型',
    techStack: ['React', 'Node.js', 'OpenAI'],
    stars: 89,
    forks: 15,
    url: 'https://github.com',
    status: 'completed',
  },
  {
    id: 4,
    name: 'Component Library',
    description: 'Vue3 组件库，包含常用 UI 组件',
    techStack: ['Vue3', 'Vite', 'Sass'],
    stars: 167,
    forks: 28,
    url: 'https://github.com',
    status: 'active',
  },
])

const getStatusColor = (status: string) => {
  const colors: Record<string, string> = {
    active: '#52c41a',
    archived: '#999',
    completed: '#1890ff',
  }
  return colors[status] || '#999'
}

const getStatusLabel = (status: string) => {
  const labels: Record<string, string> = {
    active: '进行中',
    archived: '已归档',
    completed: '已完成',
  }
  return labels[status] || status
}
</script>

<template>
  <div class="projects-page">
    <div class="projects-grid">
      <div
        v-for="project in projects"
        :key="project.id"
        class="project-card"
      >
        <div class="project-header">
          <div class="project-icon">
            <Github :size="24" />
          </div>
          <div class="project-status" :style="{ color: getStatusColor(project.status) }">
            {{ getStatusLabel(project.status) }}
          </div>
        </div>

        <h3 class="project-name">{{ project.name }}</h3>
        <p class="project-desc">{{ project.description }}</p>

        <div class="project-tech">
          <span v-for="tech in project.techStack" :key="tech" class="tech-tag">
            {{ tech }}
          </span>
        </div>

        <div class="project-footer">
          <div class="project-stats">
            <span class="stat">
              <Star :size="14" />
              {{ project.stars }}
            </span>
            <span class="stat">
              <GitFork :size="14" />
              {{ project.forks }}
            </span>
          </div>
          <div class="project-links">
            <a :href="project.url" target="_blank" class="link-btn">
              <Github :size="14" />
            </a>
            <a v-if="project.demoUrl" :href="project.demoUrl" target="_blank" class="link-btn">
              <ExternalLink :size="14" />
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.projects-page {
  max-width: 1000px;
  margin: 0 auto;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}

.project-card {
  background: #fff;
  border-radius: 12px;
  padding: 24px;
  border: 1px solid #e8e8e8;
  transition: all 0.2s;
}

.project-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transform: translateY(-2px);
}

.project-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.project-icon {
  width: 40px;
  height: 40px;
  background: #f5f5f5;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #1a1a1a;
}

.project-status {
  font-size: 12px;
  font-weight: 500;
}

.project-name {
  font-size: 16px;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0 0 8px 0;
}

.project-desc {
  font-size: 13px;
  color: #666;
  margin: 0 0 16px 0;
  line-height: 1.5;
}

.project-tech {
  display: flex;
  gap: 6px;
  margin-bottom: 16px;
  flex-wrap: wrap;
}

.tech-tag {
  padding: 4px 10px;
  border-radius: 4px;
  background: #f5f5f5;
  color: #666;
  font-size: 12px;
}

.project-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 16px;
  border-top: 1px solid #f5f5f5;
}

.project-stats {
  display: flex;
  gap: 16px;
}

.stat {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 13px;
  color: #666;
}

.project-links {
  display: flex;
  gap: 8px;
}

.link-btn {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  background: #f5f5f5;
  color: #666;
  transition: all 0.2s;
}

.link-btn:hover {
  background: #1a1a1a;
  color: #fff;
}

@media (max-width: 768px) {
  .projects-grid {
    grid-template-columns: 1fr;
  }
}
</style>
