<script setup lang="ts">
import { ref } from 'vue'
import { Eye, Heart, MessageCircle, Calendar } from 'lucide-vue-next'

interface Article {
  id: number
  title: string
  summary: string
  cover?: string
  tags: string[]
  views: number
  likes: number
  comments: number
  date: string
  readTime: string
}

const articles = ref<Article[]>([
  {
    id: 1,
    title: 'Vue3 性能优化实践指南',
    summary: '从实际项目出发，深入探讨 Vue3 应用的性能优化策略，包括编译优化、渲染优化、状态管理优化等方面。',
    tags: ['Vue.js', '性能优化', '前端'],
    views: 2340,
    likes: 156,
    comments: 32,
    date: '2024-01-15',
    readTime: '12分钟',
  },
  {
    id: 2,
    title: '基于 Canvas 的编辑器架构设计',
    summary: '探讨如何构建高性能的 Canvas 编辑器，包括渲染管线、事件系统、状态管理等核心模块的设计思路。',
    tags: ['Canvas', '编辑器', '架构'],
    views: 1890,
    likes: 128,
    comments: 24,
    date: '2024-01-10',
    readTime: '15分钟',
  },
  {
    id: 3,
    title: 'TypeScript 高级类型编程',
    summary: '深入 TypeScript 类型系统，掌握条件类型、映射类型、模板字面量类型等高级特性的使用技巧。',
    tags: ['TypeScript', '类型系统'],
    views: 3200,
    likes: 210,
    comments: 45,
    date: '2024-01-05',
    readTime: '18分钟',
  },
  {
    id: 4,
    title: 'AI 辅助编程工具对比评测',
    summary: '对比 Cursor、GitHub Copilot、Codeium 等主流 AI 编程助手，分析各自的优势和适用场景。',
    tags: ['AI', '工具', '效率'],
    views: 4560,
    likes: 312,
    comments: 67,
    date: '2023-12-28',
    readTime: '10分钟',
  },
])

const formatNumber = (num: number): string => {
  if (num >= 1000) {
    return (num / 1000).toFixed(1) + 'k'
  }
  return num.toString()
}
</script>

<template>
  <div class="articles-page">
    <div class="articles-list">
      <article
        v-for="article in articles"
        :key="article.id"
        class="article-card"
      >
        <div class="article-content">
          <div class="article-meta-top">
            <span v-for="tag in article.tags" :key="tag" class="article-tag">
              {{ tag }}
            </span>
          </div>
          <h2 class="article-title">{{ article.title }}</h2>
          <p class="article-summary">{{ article.summary }}</p>
          <div class="article-meta-bottom">
            <div class="meta-item">
              <Calendar :size="14" />
              <span>{{ article.date }}</span>
            </div>
            <div class="meta-item">
              <Eye :size="14" />
              <span>{{ formatNumber(article.views) }}</span>
            </div>
            <div class="meta-item">
              <Heart :size="14" />
              <span>{{ article.likes }}</span>
            </div>
            <div class="meta-item">
              <MessageCircle :size="14" />
              <span>{{ article.comments }}</span>
            </div>
            <span class="read-time">{{ article.readTime }}阅读</span>
          </div>
        </div>
      </article>
    </div>
  </div>
</template>

<style scoped>
.articles-page {
  max-width: 800px;
  margin: 0 auto;
}

.articles-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.article-card {
  background: #fff;
  border-radius: 12px;
  padding: 24px;
  border: 1px solid #e8e8e8;
  transition: all 0.2s;
  cursor: pointer;
}

.article-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transform: translateY(-2px);
}

.article-meta-top {
  display: flex;
  gap: 8px;
  margin-bottom: 12px;
}

.article-tag {
  padding: 4px 10px;
  border-radius: 4px;
  background: #f5f5f5;
  color: #666;
  font-size: 12px;
}

.article-title {
  font-size: 18px;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0 0 10px 0;
  line-height: 1.4;
}

.article-summary {
  font-size: 14px;
  color: #666;
  line-height: 1.6;
  margin: 0 0 16px 0;
}

.article-meta-bottom {
  display: flex;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 13px;
  color: #999;
}

.read-time {
  margin-left: auto;
  font-size: 12px;
  color: #999;
}
</style>
