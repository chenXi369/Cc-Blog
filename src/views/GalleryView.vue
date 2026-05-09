<script setup lang="ts">
import { ref } from 'vue'
import { Heart, MessageCircle } from 'lucide-vue-next'

interface Photo {
  id: number
  url: string
  title: string
  description: string
  likes: number
  comments: number
  date: string
}

const photos = ref<Photo[]>([
  {
    id: 1,
    url: 'https://picsum.photos/400/300?random=1',
    title: '山间晨雾',
    description: '清晨的山间，云雾缭绕',
    likes: 128,
    comments: 12,
    date: '2024-01-15',
  },
  {
    id: 2,
    url: 'https://picsum.photos/400/500?random=2',
    title: '城市夜景',
    description: '繁华都市的璀璨灯火',
    likes: 256,
    comments: 24,
    date: '2024-01-10',
  },
  {
    id: 3,
    url: 'https://picsum.photos/400/300?random=3',
    title: '海边日落',
    description: '金色的夕阳洒在海面上',
    likes: 189,
    comments: 18,
    date: '2024-01-05',
  },
  {
    id: 4,
    url: 'https://picsum.photos/400/400?random=4',
    title: '樱花盛开',
    description: '春天的粉色浪漫',
    likes: 312,
    comments: 32,
    date: '2023-12-28',
  },
  {
    id: 5,
    url: 'https://picsum.photos/400/300?random=5',
    title: '雪山之巅',
    description: '壮丽的雪山风光',
    likes: 167,
    comments: 15,
    date: '2023-12-20',
  },
  {
    id: 6,
    url: 'https://picsum.photos/400/500?random=6',
    title: '古镇小巷',
    description: '青石板路的古朴韵味',
    likes: 234,
    comments: 21,
    date: '2023-12-15',
  },
])
</script>

<template>
  <div class="gallery-page">
    <div class="gallery-grid">
      <div
        v-for="photo in photos"
        :key="photo.id"
        class="photo-card"
      >
        <div class="photo-wrapper">
          <img :src="photo.url" :alt="photo.title" class="photo-image" />
          <div class="photo-overlay">
            <div class="photo-actions">
              <button class="action-btn">
                <Heart :size="18" />
                <span>{{ photo.likes }}</span>
              </button>
              <button class="action-btn">
                <MessageCircle :size="18" />
                <span>{{ photo.comments }}</span>
              </button>
            </div>
          </div>
        </div>
        <div class="photo-info">
          <h3 class="photo-title">{{ photo.title }}</h3>
          <p class="photo-desc">{{ photo.description }}</p>
          <span class="photo-date">{{ photo.date }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.gallery-page {
  max-width: 1000px;
  margin: 0 auto;
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.photo-card {
  background: #fff;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid #e8e8e8;
  transition: all 0.2s;
}

.photo-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transform: translateY(-2px);
}

.photo-wrapper {
  position: relative;
  overflow: hidden;
}

.photo-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
  display: block;
  transition: transform 0.3s;
}

.photo-card:hover .photo-image {
  transform: scale(1.05);
}

.photo-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.2s;
}

.photo-card:hover .photo-overlay {
  opacity: 1;
}

.photo-actions {
  display: flex;
  gap: 16px;
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  color: #fff;
  font-size: 14px;
  background: none;
  border: none;
  cursor: pointer;
}

.photo-info {
  padding: 16px;
}

.photo-title {
  font-size: 15px;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0 0 6px 0;
}

.photo-desc {
  font-size: 13px;
  color: #666;
  margin: 0 0 8px 0;
}

.photo-date {
  font-size: 12px;
  color: #999;
}

@media (max-width: 768px) {
  .gallery-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .gallery-grid {
    grid-template-columns: 1fr;
  }
}
</style>
