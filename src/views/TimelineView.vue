<script setup lang="ts">
import { ref } from 'vue'

interface TimelineItem {
  id: number
  date: string
  title: string
  description: string
  type: 'article' | 'project' | 'milestone' | 'learning'
}

const timelineItems = ref<TimelineItem[]>([
  {
    id: 1,
    date: '2024-01-15',
    title: '发布 Vue3 性能优化文章',
    description: '总结了在实际项目中遇到的性能问题及解决方案',
    type: 'article',
  },
  {
    id: 2,
    date: '2024-01-10',
    title: '完成编辑器核心模块',
    description: '基于 Canvas 的编辑器架构设计完成',
    type: 'project',
  },
  {
    id: 3,
    date: '2024-01-01',
    title: '2024 新年目标',
    description: '计划学习 WebGL 和 AI 相关知识',
    type: 'milestone',
  },
  {
    id: 4,
    date: '2023-12-20',
    title: '学习 TypeScript 高级类型',
    description: '深入理解了条件类型和映射类型',
    type: 'learning',
  },
  {
    id: 5,
    date: '2023-12-10',
    title: '开源项目发布',
    description: '发布了一个 Vue3 组件库',
    type: 'project',
  },
  {
    id: 6,
    date: '2023-11-28',
    title: '参加前端技术大会',
    description: '分享了 Canvas 编辑器的开发经验',
    type: 'milestone',
  },
])

const getTypeColor = (type: string) => {
  const colors: Record<string, string> = {
    article: '#1890ff',
    project: '#52c41a',
    milestone: '#faad14',
    learning: '#722ed1',
  }
  return colors[type] || '#999'
}

const getTypeLabel = (type: string) => {
  const labels: Record<string, string> = {
    article: '文章',
    project: '项目',
    milestone: '里程碑',
    learning: '学习',
  }
  return labels[type] || type
}
</script>

<template>
  <div class="timeline-page">
    <div class="timeline">
      <div
        v-for="(item, index) in timelineItems"
        :key="item.id"
        class="timeline-item"
        :class="{ 'timeline-item-left': index % 2 === 0, 'timeline-item-right': index % 2 === 1 }"
      >
        <div class="timeline-content">
          <div class="timeline-dot" :style="{ background: getTypeColor(item.type) }"></div>
          <div class="timeline-card">
            <div class="timeline-header">
              <span
                class="timeline-type"
                :style="{ background: getTypeColor(item.type) + '15', color: getTypeColor(item.type) }"
              >
                {{ getTypeLabel(item.type) }}
              </span>
              <span class="timeline-date">{{ item.date }}</span>
            </div>
            <h3 class="timeline-title">{{ item.title }}</h3>
            <p class="timeline-desc">{{ item.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.timeline-page {
  max-width: 800px;
  margin: 0 auto;
}

.timeline {
  position: relative;
  padding: 20px 0;
}

.timeline::before {
  content: '';
  position: absolute;
  left: 50%;
  top: 0;
  bottom: 0;
  width: 2px;
  background: #e8e8e8;
  transform: translateX(-50%);
}

.timeline-item {
  position: relative;
  margin-bottom: 30px;
}

.timeline-content {
  display: flex;
  align-items: flex-start;
  position: relative;
}

.timeline-item-left .timeline-content {
  justify-content: flex-start;
  padding-right: calc(50% + 30px);
}

.timeline-item-right .timeline-content {
  justify-content: flex-end;
  padding-left: calc(50% + 30px);
}

.timeline-dot {
  position: absolute;
  left: 50%;
  top: 20px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  transform: translateX(-50%);
  border: 3px solid #fff;
  box-shadow: 0 0 0 2px #e8e8e8;
}

.timeline-card {
  background: #fff;
  border-radius: 12px;
  padding: 20px;
  border: 1px solid #e8e8e8;
  width: 100%;
  max-width: 340px;
}

.timeline-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.timeline-type {
  padding: 4px 10px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
}

.timeline-date {
  font-size: 12px;
  color: #999;
}

.timeline-title {
  font-size: 15px;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0 0 8px 0;
}

.timeline-desc {
  font-size: 13px;
  color: #666;
  margin: 0;
  line-height: 1.5;
}

@media (max-width: 768px) {
  .timeline::before {
    left: 20px;
  }

  .timeline-item-left .timeline-content,
  .timeline-item-right .timeline-content {
    justify-content: flex-start;
    padding-left: 50px;
    padding-right: 0;
  }

  .timeline-dot {
    left: 20px;
  }

  .timeline-card {
    max-width: 100%;
  }
}
</style>
