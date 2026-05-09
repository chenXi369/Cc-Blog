<script setup lang="ts">
import { ref } from 'vue'
import { Play, ExternalLink } from 'lucide-vue-next'

interface Demo {
  id: number
  title: string
  description: string
  thumbnail: string
  url: string
  tags: string[]
}

const demos = ref<Demo[]>([
  {
    id: 1,
    title: 'Canvas 粒子动画',
    description: '基于 Canvas 的交互式粒子动画效果',
    thumbnail: 'https://picsum.photos/400/250?random=10',
    url: '#',
    tags: ['Canvas', '动画'],
  },
  {
    id: 2,
    title: '3D 卡片翻转',
    description: 'CSS3 3D 变换实现的卡片翻转效果',
    thumbnail: 'https://picsum.photos/400/250?random=11',
    url: '#',
    tags: ['CSS3', '3D'],
  },
  {
    id: 3,
    title: '拖拽排序',
    description: '原生拖拽 API 实现的列表排序',
    thumbnail: 'https://picsum.photos/400/250?random=12',
    url: '#',
    tags: ['拖拽', '交互'],
  },
  {
    id: 4,
    title: '虚拟列表',
    description: '高性能大数据列表渲染方案',
    thumbnail: 'https://picsum.photos/400/250?random=13',
    url: '#',
    tags: ['性能', '列表'],
  },
])
</script>

<template>
  <div class="demo-page">
    <div class="demo-grid">
      <div
        v-for="demo in demos"
        :key="demo.id"
        class="demo-card"
      >
        <div class="demo-thumbnail">
          <img :src="demo.thumbnail" :alt="demo.title" />
          <div class="demo-overlay">
            <a :href="demo.url" target="_blank" class="demo-play">
              <Play :size="24" />
            </a>
          </div>
        </div>
        <div class="demo-info">
          <h3 class="demo-title">{{ demo.title }}</h3>
          <p class="demo-desc">{{ demo.description }}</p>
          <div class="demo-tags">
            <span v-for="tag in demo.tags" :key="tag" class="demo-tag">{{ tag }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.demo-page {
  max-width: 1000px;
  margin: 0 auto;
}

.demo-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}

.demo-card {
  background: #fff;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid #e8e8e8;
  transition: all 0.2s;
}

.demo-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transform: translateY(-2px);
}

.demo-thumbnail {
  position: relative;
  overflow: hidden;
}

.demo-thumbnail img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  display: block;
}

.demo-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.2s;
}

.demo-card:hover .demo-overlay {
  opacity: 1;
}

.demo-play {
  width: 56px;
  height: 56px;
  background: #fff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #1a1a1a;
  transition: transform 0.2s;
}

.demo-play:hover {
  transform: scale(1.1);
}

.demo-info {
  padding: 20px;
}

.demo-title {
  font-size: 16px;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0 0 8px 0;
}

.demo-desc {
  font-size: 13px;
  color: #666;
  margin: 0 0 12px 0;
}

.demo-tags {
  display: flex;
  gap: 6px;
}

.demo-tag {
  padding: 4px 10px;
  border-radius: 4px;
  background: #f5f5f5;
  color: #666;
  font-size: 12px;
}

@media (max-width: 768px) {
  .demo-grid {
    grid-template-columns: 1fr;
  }
}
</style>
