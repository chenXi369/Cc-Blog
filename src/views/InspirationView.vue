<script setup lang="ts">
import { ref } from 'vue'
import { Lightbulb, Calendar, Tag } from 'lucide-vue-next'

interface Inspiration {
  id: number
  content: string
  source?: string
  tags: string[]
  date: string
  color: string
}

const inspirations = ref<Inspiration[]>([
  {
    id: 1,
    content: '好的代码就像好的笑话，不需要解释。',
    source: '《代码大全》',
    tags: ['编程', '代码质量'],
    date: '2024-01-15',
    color: '#1890ff',
  },
  {
    id: 2,
    content: '简单是可靠的先决条件。',
    source: 'Edsger W. Dijkstra',
    tags: ['设计', '架构'],
    date: '2024-01-10',
    color: '#52c41a',
  },
  {
    id: 3,
    content: '过早优化是万恶之源。',
    source: 'Donald Knuth',
    tags: ['性能', '优化'],
    date: '2024-01-05',
    color: '#faad14',
  },
  {
    id: 4,
    content: 'Talk is cheap. Show me the code.',
    source: 'Linus Torvalds',
    tags: ['开源', '行动'],
    date: '2023-12-28',
    color: '#722ed1',
  },
])
</script>

<template>
  <div class="inspiration-page">
    <div class="inspiration-grid">
      <div
        v-for="item in inspirations"
        :key="item.id"
        class="inspiration-card"
        :style="{ borderTopColor: item.color }"
      >
        <div class="inspiration-icon" :style="{ background: item.color + '15', color: item.color }">
          <Lightbulb :size="20" />
        </div>
        <p class="inspiration-content">{{ item.content }}</p>
        <p v-if="item.source" class="inspiration-source">—— {{ item.source }}</p>
        <div class="inspiration-footer">
          <div class="inspiration-tags">
            <span v-for="tag in item.tags" :key="tag" class="inspiration-tag">
              <Tag :size="10" />
              {{ tag }}
            </span>
          </div>
          <span class="inspiration-date">
            <Calendar :size="12" />
            {{ item.date }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.inspiration-page {
  max-width: 900px;
  margin: 0 auto;
}

.inspiration-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}

.inspiration-card {
  background: #fff;
  border-radius: 12px;
  padding: 24px;
  border: 1px solid #e8e8e8;
  border-top: 3px solid;
  transition: all 0.2s;
}

.inspiration-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transform: translateY(-2px);
}

.inspiration-icon {
  width: 40px;
  height: 40px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 16px;
}

.inspiration-content {
  font-size: 15px;
  color: #1a1a1a;
  line-height: 1.6;
  margin: 0 0 12px 0;
  font-style: italic;
}

.inspiration-source {
  font-size: 13px;
  color: #999;
  margin: 0 0 16px 0;
  text-align: right;
}

.inspiration-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 16px;
  border-top: 1px solid #f5f5f5;
}

.inspiration-tags {
  display: flex;
  gap: 8px;
}

.inspiration-tag {
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 4px 10px;
  border-radius: 4px;
  background: #f5f5f5;
  color: #666;
  font-size: 12px;
}

.inspiration-date {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 12px;
  color: #999;
}

@media (max-width: 768px) {
  .inspiration-grid {
    grid-template-columns: 1fr;
  }
}
</style>
