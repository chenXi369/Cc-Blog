<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { Mail, MapPin, Calendar, Github, BookOpen } from 'lucide-vue-next'
import { api } from '@/api/request'

interface Activity {
  id: number
  content: string
  time_text: string
}

const activities = ref<Activity[]>([])
const articleCount = ref(0)
const projectCount = ref(0)

const fetchActivities = async () => {
  activities.value = await api.get<Activity[]>('/activities?limit=5')
}

const fetchCounts = async () => {
  const articles = await api.get<any[]>('/articles')
  const projects = await api.get<any[]>('/projects')
  articleCount.value = articles.length
  projectCount.value = projects.length
}

onMounted(() => {
  fetchActivities()
  fetchCounts()
})

const skillTags = [
  'Vue.js', 'React', 'TypeScript', 'Node.js', 'Canvas', 'WebGL', 'AI', '编辑器',
]
</script>

<template>
  <div class="home-page">
    <div class="profile-card">
      <div class="profile-header">
        <div class="avatar">
          <span class="avatar-text">O</span>
        </div>
        <div class="profile-info">
          <h2 class="profile-name">CC</h2>
          <p class="profile-title">不知名程序员</p>
          <p class="profile-desc">前端 & AI & 编辑器</p>
        </div>
      </div>

      <div class="profile-stats">
        <div class="stat-box">
          <span class="stat-number">{{ articleCount }}</span>
          <span class="stat-label">文章</span>
        </div>
        <div class="stat-box">
          <span class="stat-number">{{ projectCount }}</span>
          <span class="stat-label">项目</span>
        </div>
        <div class="stat-box">
          <span class="stat-number">2.3k</span>
          <span class="stat-label">访客</span>
        </div>
      </div>

      <div class="profile-details">
        <div class="detail-item">
          <MapPin :size="16" />
          <span>中国 · 南昌</span>
        </div>
        <div class="detail-item">
          <Mail :size="16" />
          <span>CC@example.com</span>
        </div>
        <div class="detail-item">
          <Calendar :size="16" />
          <span>Joined 2020</span>
        </div>
      </div>

      <div class="profile-links">
        <a href="https://github.com" target="_blank" class="profile-link">
          <Github :size="18" />
          <span>Github</span>
        </a>
        <a href="https://juejin.cn" target="_blank" class="profile-link">
          <BookOpen :size="18" />
          <span>掘金</span>
        </a>
      </div>
    </div>

    <div class="content-grid">
      <div class="content-card">
        <h3 class="card-title">最新动态</h3>
        <div class="activity-list">
          <div v-for="activity in activities" :key="activity.id" class="activity-item">
            <div class="activity-dot"></div>
            <div class="activity-content">
              <p class="activity-text">{{ activity.content }}</p>
              <span class="activity-time">{{ activity.time_text }}</span>
            </div>
          </div>
        </div>
      </div>

      <div class="content-card">
        <h3 class="card-title">技能标签</h3>
        <div class="skill-tags">
          <span v-for="tag in skillTags" :key="tag" class="skill-tag">{{ tag }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home-page {
  max-width: 900px;
  margin: 0 auto;
}

.profile-card {
  background: #fff;
  border-radius: 12px;
  padding: 32px;
  border: 1px solid #e8e8e8;
  margin-bottom: 24px;
}

.profile-header {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 24px;
}

.avatar {
  width: 80px;
  height: 80px;
  background: #1a1a1a;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.avatar-text {
  font-size: 32px;
  font-weight: 700;
  color: #fff;
}

.profile-name {
  font-size: 24px;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0 0 4px 0;
}

.profile-title {
  font-size: 15px;
  color: #666;
  margin: 0 0 4px 0;
}

.profile-desc {
  font-size: 13px;
  color: #999;
  margin: 0;
}

.profile-stats {
  display: flex;
  gap: 32px;
  padding: 20px 0;
  border-top: 1px solid #f5f5f5;
  border-bottom: 1px solid #f5f5f5;
  margin-bottom: 20px;
}

.stat-box {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.stat-number {
  font-size: 24px;
  font-weight: 700;
  color: #1a1a1a;
}

.stat-label {
  font-size: 13px;
  color: #999;
}

.profile-details {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 20px;
}

.detail-item {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 14px;
  color: #666;
}

.profile-links {
  display: flex;
  gap: 12px;
}

.profile-link {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  border-radius: 8px;
  background: #f5f5f5;
  color: #1a1a1a;
  font-size: 14px;
  font-weight: 500;
  transition: background 0.2s;
}

.profile-link:hover {
  background: #e8e8e8;
}

.content-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}

.content-card {
  background: #fff;
  border-radius: 12px;
  padding: 24px;
  border: 1px solid #e8e8e8;
}

.content-card .card-title {
  font-size: 16px;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0 0 16px 0;
}

.activity-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.activity-item {
  display: flex;
  gap: 12px;
}

.activity-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #1890ff;
  margin-top: 6px;
  flex-shrink: 0;
}

.activity-content {
  flex: 1;
}

.activity-text {
  font-size: 14px;
  color: #1a1a1a;
  margin: 0 0 4px 0;
}

.activity-time {
  font-size: 12px;
  color: #999;
}

.skill-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.skill-tag {
  padding: 8px 16px;
  border-radius: 20px;
  background: #f5f5f5;
  color: #666;
  font-size: 13px;
  transition: all 0.2s;
}

.skill-tag:hover {
  background: #1a1a1a;
  color: #fff;
}

@media (max-width: 768px) {
  .profile-card {
    padding: 20px;
  }

  .profile-header {
    flex-direction: column;
    text-align: center;
    gap: 16px;
  }

  .profile-stats {
    justify-content: space-around;
    gap: 0;
  }

  .stat-number {
    font-size: 20px;
  }

  .profile-links {
    flex-wrap: wrap;
  }

  .content-grid {
    grid-template-columns: 1fr;
    gap: 16px;
  }

  .content-card {
    padding: 20px;
  }
}
</style>
