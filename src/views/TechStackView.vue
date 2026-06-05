<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { Pencil, Trash2 } from 'lucide-vue-next'
import { api } from '@/api/request'

interface TechItem {
  id: number
  name: string
  icon: string
  proficiency: number
  description: string
}

interface TechCategory {
  id: number
  name: string
  items: TechItem[]
}

const techCategories = ref<TechCategory[]>([])
const editingId = ref<number | null>(null)
const editForm = ref({
  name: '',
  icon: '',
  description: '',
  proficiency: 0,
})

const fetchTechStack = async () => {
  techCategories.value = await api.get<TechCategory[]>('/tech-stack')
}

const startEdit = (item: TechItem) => {
  editingId.value = item.id
  editForm.value = {
    name: item.name,
    icon: item.icon,
    description: item.description,
    proficiency: item.proficiency,
  }
}

const cancelEdit = () => {
  editingId.value = null
}

const saveEdit = async () => {
  if (editingId.value === null) return
  await api.put('/tech-stack/items/' + editingId.value, editForm.value)
  editingId.value = null
  await fetchTechStack()
}

const deleteItem = async (id: number) => {
  await api.delete('/tech-stack/items/' + id)
  await fetchTechStack()
}

const deleteCategory = async (id: number) => {
  await api.delete('/tech-stack/categories/' + id)
  await fetchTechStack()
}

onMounted(fetchTechStack)
</script>

<template>
  <div class="tech-stack-page">
    <div class="tech-grid">
      <div
        v-for="category in techCategories"
        :key="category.id"
        class="category-card"
      >
        <div class="category-title-wrap">
          <h3 class="category-title">{{ category.name }}</h3>
          <button class="icon-btn delete-category-btn" @click="deleteCategory(category.id)">
            <Trash2 :size="14" />
          </button>
        </div>
        <div class="tech-list">
          <div
            v-for="tech in category.items"
            :key="tech.id"
            class="tech-item"
          >
            <div v-if="editingId === tech.id" class="edit-form">
              <input v-model="editForm.name" placeholder="名称" />
              <input v-model="editForm.icon" placeholder="图标" />
              <input v-model="editForm.description" placeholder="描述" />
              <input v-model.number="editForm.proficiency" type="number" min="0" max="100" placeholder="熟练度" />
              <div class="edit-actions">
                <button class="save-btn" @click="saveEdit">保存</button>
                <button class="cancel-btn" @click="cancelEdit">取消</button>
              </div>
            </div>
            <template v-else>
              <div class="item-actions">
                <button class="icon-btn" @click="startEdit(tech)">
                  <Pencil :size="14" />
                </button>
                <button class="icon-btn" @click="deleteItem(tech.id)">
                  <Trash2 :size="14" />
                </button>
              </div>
              <div class="tech-header">
                <div class="tech-icon">{{ tech.icon }}</div>
                <div class="tech-info">
                  <span class="tech-name">{{ tech.name }}</span>
                  <span class="tech-desc">{{ tech.description }}</span>
                </div>
              </div>
              <div class="proficiency-bar">
                <div
                  class="proficiency-fill"
                  :style="{ width: tech.proficiency + '%' }"
                ></div>
              </div>
              <span class="proficiency-text">{{ tech.proficiency }}%</span>
            </template>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.tech-stack-page {
  max-width: 1000px;
  margin: 0 auto;
}

.tech-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}

.category-card {
  background: #fff;
  border-radius: 12px;
  padding: 24px;
  border: 1px solid #e8e8e8;
}

.category-title-wrap {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-bottom: 12px;
  border-bottom: 1px solid #f5f5f5;
  margin-bottom: 20px;
}

.category-title {
  font-size: 16px;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0;
}

.tech-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.tech-item {
  display: flex;
  flex-direction: column;
  gap: 8px;
  position: relative;
}

.item-actions {
  position: absolute;
  top: 0;
  right: 0;
  display: flex;
  gap: 4px;
}

.icon-btn {
  background: none;
  border: none;
  cursor: pointer;
  padding: 2px;
  color: #999;
  line-height: 1;
}

.icon-btn:hover {
  color: #1a1a1a;
}

.tech-header {
  display: flex;
  align-items: center;
  gap: 12px;
}

.tech-icon {
  width: 40px;
  height: 40px;
  background: #f5f5f5;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  font-weight: 600;
  color: #1a1a1a;
}

.tech-info {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.tech-name {
  font-size: 14px;
  font-weight: 600;
  color: #1a1a1a;
}

.tech-desc {
  font-size: 12px;
  color: #999;
}

.proficiency-bar {
  height: 6px;
  background: #f0f0f0;
  border-radius: 3px;
  overflow: hidden;
}

.proficiency-fill {
  height: 100%;
  background: #1a1a1a;
  border-radius: 3px;
  transition: width 0.6s ease;
}

.proficiency-text {
  font-size: 12px;
  color: #999;
  text-align: right;
}

.edit-form {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.edit-form input {
  padding: 6px 10px;
  border: 1px solid #e8e8e8;
  border-radius: 6px;
  font-size: 13px;
  outline: none;
}

.edit-form input:focus {
  border-color: #1a1a1a;
}

.edit-actions {
  display: flex;
  gap: 8px;
}

.save-btn,
.cancel-btn {
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 13px;
  cursor: pointer;
  border: none;
}

.save-btn {
  background: #1a1a1a;
  color: #fff;
}

.cancel-btn {
  background: #f5f5f5;
  color: #1a1a1a;
}

@media (max-width: 768px) {
  .tech-grid {
    grid-template-columns: 1fr;
  }
}
</style>
