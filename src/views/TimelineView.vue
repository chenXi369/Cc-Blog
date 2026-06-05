<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { api } from '@/api/request'
import { Pencil, Trash2 } from 'lucide-vue-next'

interface TimelineItem {
  id: number
  date: string
  title: string
  description: string
  type: 'article' | 'project' | 'milestone' | 'learning'
}

const timelineItems = ref<TimelineItem[]>([])

const fetchTimeline = async () => {
  timelineItems.value = await api.get<TimelineItem[]>('/timeline')
}

onMounted(fetchTimeline)

const editingId = ref<number | null>(null)
const editForm = ref({
  title: '',
  description: '',
  date: '',
  type: 'article' as 'article' | 'project' | 'milestone' | 'learning',
})

const startEdit = (event: TimelineItem) => {
  editingId.value = event.id
  editForm.value = {
    title: event.title,
    description: event.description,
    date: event.date,
    type: event.type,
  }
}

const cancelEdit = () => {
  editingId.value = null
}

const saveEdit = async () => {
  if (!editingId.value) return
  await api.put('/timeline/' + editingId.value, editForm.value)
  await fetchTimeline()
  editingId.value = null
}

const deleteEvent = async (id: number) => {
  await api.delete('/timeline/' + id)
  await fetchTimeline()
}

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
              <div class="timeline-header-right">
                <span class="timeline-date">{{ item.date }}</span>
                <button class="icon-btn" @click="startEdit(item)">
                  <Pencil :size="14" />
                </button>
                <button class="icon-btn delete" @click="deleteEvent(item.id)">
                  <Trash2 :size="14" />
                </button>
              </div>
            </div>
            <template v-if="editingId === item.id">
              <div class="edit-form">
                <input v-model="editForm.title" class="edit-input" placeholder="标题" />
                <textarea v-model="editForm.description" class="edit-textarea" placeholder="描述" rows="3"></textarea>
                <input v-model="editForm.date" type="date" class="edit-input" />
                <select v-model="editForm.type" class="edit-select">
                  <option value="article">文章</option>
                  <option value="project">项目</option>
                  <option value="milestone">里程碑</option>
                  <option value="learning">学习</option>
                </select>
                <div class="edit-actions">
                  <button class="edit-btn save" @click="saveEdit">保存</button>
                  <button class="edit-btn cancel" @click="cancelEdit">取消</button>
                </div>
              </div>
            </template>
            <template v-else>
              <h3 class="timeline-title">{{ item.title }}</h3>
              <p class="timeline-desc">{{ item.description }}</p>
            </template>
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

.timeline-header-right {
  display: flex;
  align-items: center;
  gap: 8px;
}

.icon-btn {
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
  color: #999;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  transition: all 0.2s;
}

.icon-btn:hover {
  color: #333;
  background: #f0f0f0;
}

.icon-btn.delete:hover {
  color: #ff4d4f;
  background: #fff1f0;
}

.edit-form {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-top: 8px;
}

.edit-input,
.edit-textarea,
.edit-select {
  padding: 6px 10px;
  border: 1px solid #d9d9d9;
  border-radius: 6px;
  font-size: 13px;
  outline: none;
  transition: border-color 0.2s;
}

.edit-input:focus,
.edit-textarea:focus,
.edit-select:focus {
  border-color: #1890ff;
}

.edit-textarea {
  resize: vertical;
}

.edit-actions {
  display: flex;
  gap: 8px;
  margin-top: 4px;
}

.edit-btn {
  padding: 5px 14px;
  border-radius: 6px;
  font-size: 13px;
  border: none;
  cursor: pointer;
  transition: all 0.2s;
}

.edit-btn.save {
  background: #1890ff;
  color: #fff;
}

.edit-btn.save:hover {
  background: #40a9ff;
}

.edit-btn.cancel {
  background: #f5f5f5;
  color: #666;
}

.edit-btn.cancel:hover {
  background: #e0e0e0;
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
