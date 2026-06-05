<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { Heart, MessageCircle, Pencil, Trash2 } from 'lucide-vue-next'
import { api } from '@/api/request'

interface Photo {
  id: number
  url: string
  title: string
  description: string
  likes: number
  comments: number
  date: string
}

const photos = ref<Photo[]>([])
const editingId = ref<number | null>(null)
const editForm = ref({
  title: '',
  description: '',
  url: '',
  date: ''
})

const fetchPhotos = async () => {
  photos.value = await api.get<Photo[]>('/photos')
}

const startEdit = (photo: Photo) => {
  editingId.value = photo.id
  editForm.value = {
    title: photo.title,
    description: photo.description,
    url: photo.url,
    date: photo.date
  }
}

const cancelEdit = () => {
  editingId.value = null
}

const saveEdit = async () => {
  if (editingId.value === null) return
  await api.put('/photos/' + editingId.value, editForm.value)
  editingId.value = null
  await fetchPhotos()
}

const deletePhoto = async (id: number) => {
  await api.delete('/photos/' + id)
  await fetchPhotos()
}

onMounted(fetchPhotos)
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
          <div class="photo-info-header">
            <template v-if="editingId !== photo.id">
              <h3 class="photo-title">{{ photo.title }}</h3>
              <div class="photo-actions-inline">
                <button class="inline-btn" @click="startEdit(photo)">
                  <Pencil :size="14" />
                </button>
                <button class="inline-btn" @click="deletePhoto(photo.id)">
                  <Trash2 :size="14" />
                </button>
              </div>
            </template>
          </div>
          <template v-if="editingId === photo.id">
            <div class="edit-form">
              <input v-model="editForm.title" class="edit-input" placeholder="标题" />
              <input v-model="editForm.description" class="edit-input" placeholder="描述" />
              <input v-model="editForm.url" class="edit-input" placeholder="图片地址" />
              <input v-model="editForm.date" class="edit-input" placeholder="日期" />
              <div class="edit-form-actions">
                <button class="edit-btn save" @click="saveEdit">保存</button>
                <button class="edit-btn cancel" @click="cancelEdit">取消</button>
              </div>
            </div>
          </template>
          <template v-else>
            <p class="photo-desc">{{ photo.description }}</p>
            <span class="photo-date">{{ photo.date }}</span>
          </template>
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

.photo-info-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 6px;
}

.photo-actions-inline {
  display: flex;
  gap: 8px;
}

.inline-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 4px;
  background: none;
  border: none;
  cursor: pointer;
  color: #999;
  transition: color 0.2s;
}

.inline-btn:hover {
  color: #1a1a1a;
}

.edit-form {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.edit-input {
  padding: 6px 8px;
  font-size: 13px;
  border: 1px solid #ddd;
  border-radius: 6px;
  outline: none;
}

.edit-input:focus {
  border-color: #1890ff;
}

.edit-form-actions {
  display: flex;
  gap: 8px;
  margin-top: 4px;
}

.edit-btn {
  flex: 1;
  padding: 6px 0;
  font-size: 13px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: opacity 0.2s;
}

.edit-btn:hover {
  opacity: 0.85;
}

.edit-btn.save {
  background: #1890ff;
  color: #fff;
}

.edit-btn.cancel {
  background: #f0f0f0;
  color: #666;
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
