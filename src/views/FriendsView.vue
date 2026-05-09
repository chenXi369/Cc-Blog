<script setup lang="ts">
import { ref } from 'vue'
import { ExternalLink, Globe } from 'lucide-vue-next'

interface Friend {
  id: number
  name: string
  avatar: string
  description: string
  url: string
  tags: string[]
}

const friends = ref<Friend[]>([
  {
    id: 1,
    name: '张三的博客',
    avatar: 'Z',
    description: '全栈开发者，专注于 Node.js 和 Vue 生态',
    url: 'https://example.com',
    tags: ['全栈', 'Node.js'],
  },
  {
    id: 2,
    name: '李四的技术笔记',
    avatar: 'L',
    description: '前端架构师，分享 React 和工程化实践',
    url: 'https://example.com',
    tags: ['React', '架构'],
  },
  {
    id: 3,
    name: '王五的编程随想',
    avatar: 'W',
    description: '独立开发者，探索 AI 与前端结合',
    url: 'https://example.com',
    tags: ['AI', '独立开发'],
  },
  {
    id: 4,
    name: '赵六的设计工坊',
    avatar: 'Z',
    description: 'UI/UX 设计师，关注用户体验',
    url: 'https://example.com',
    tags: ['设计', 'UX'],
  },
])
</script>

<template>
  <div class="friends-page">
    <div class="friends-grid">
      <a
        v-for="friend in friends"
        :key="friend.id"
        :href="friend.url"
        target="_blank"
        class="friend-card"
      >
        <div class="friend-avatar">{{ friend.avatar }}</div>
        <div class="friend-info">
          <h3 class="friend-name">{{ friend.name }}</h3>
          <p class="friend-desc">{{ friend.description }}</p>
          <div class="friend-tags">
            <span v-for="tag in friend.tags" :key="tag" class="friend-tag">{{ tag }}</span>
          </div>
        </div>
        <ExternalLink :size="16" class="friend-link" />
      </a>
    </div>
  </div>
</template>

<style scoped>
.friends-page {
  max-width: 800px;
  margin: 0 auto;
}

.friends-grid {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.friend-card {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 20px 24px;
  background: #fff;
  border-radius: 12px;
  border: 1px solid #e8e8e8;
  transition: all 0.2s;
}

.friend-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transform: translateX(4px);
}

.friend-avatar {
  width: 48px;
  height: 48px;
  background: #1a1a1a;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-size: 18px;
  font-weight: 600;
  flex-shrink: 0;
}

.friend-info {
  flex: 1;
  min-width: 0;
}

.friend-name {
  font-size: 15px;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0 0 4px 0;
}

.friend-desc {
  font-size: 13px;
  color: #666;
  margin: 0 0 8px 0;
}

.friend-tags {
  display: flex;
  gap: 6px;
}

.friend-tag {
  padding: 2px 8px;
  border-radius: 4px;
  background: #f5f5f5;
  color: #666;
  font-size: 11px;
}

.friend-link {
  color: #999;
  flex-shrink: 0;
}

.friend-card:hover .friend-link {
  color: #1a1a1a;
}
</style>
