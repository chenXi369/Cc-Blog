<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { Folder, FileText, Clock, MoreVertical, Pencil, Trash2 } from 'lucide-vue-next'
import { api } from '@/api/request'

interface WorkspaceItem {
  id: number
  name: string
  type: 'folder' | 'file'
  updatedAt: string
  size?: string
}

const workspaceItems = ref<WorkspaceItem[]>([])
const editingId = ref<number | null>(null)
const editForm = ref<{ name: string; type: 'folder' | 'file'; size: string }>({
  name: '',
  type: 'file',
  size: '',
})

const fetchWorkspace = async () => {
  const data = await api.get<any[]>('/workspace')
  workspaceItems.value = data.map((item) => ({
    ...item,
    updatedAt: item.updated_at,
  }))
}

const startEdit = (item: WorkspaceItem) => {
  editingId.value = item.id
  editForm.value = {
    name: item.name,
    type: item.type,
    size: item.size || '',
  }
}

const cancelEdit = () => {
  editingId.value = null
  editForm.value = { name: '', type: 'file', size: '' }
}

const saveEdit = async () => {
  if (editingId.value === null) return
  await api.put('/workspace/' + editingId.value, {
    ...editForm.value,
    updated_at: new Date().toISOString().slice(0, 10),
  })
  await fetchWorkspace()
  cancelEdit()
}

const deleteItem = async (id: number) => {
  await api.delete('/workspace/' + id)
  await fetchWorkspace()
}

onMounted(fetchWorkspace)
</script>

<template>
  <div class="workspace-page">
    <div class="workspace-toolbar">
      <div class="breadcrumb">
        <span class="breadcrumb-item">工作空间</span>
        <span class="breadcrumb-separator">/</span>
        <span class="breadcrumb-item active">全部文件</span>
      </div>
    </div>

    <div class="workspace-content">
      <div class="items-grid">
        <div
          v-for="item in workspaceItems"
          :key="item.id"
          class="workspace-item"
        >
          <div class="item-icon">
            <Folder v-if="item.type === 'folder'" :size="32" class="folder-icon" />
            <FileText v-else :size="32" class="file-icon" />
          </div>
          <div v-if="editingId === item.id" class="item-edit-form">
            <input v-model="editForm.name" class="edit-input" placeholder="名称" />
            <select v-model="editForm.type" class="edit-select">
              <option value="folder">文件夹</option>
              <option value="file">文件</option>
            </select>
            <input v-model="editForm.size" class="edit-input" placeholder="大小" />
            <div class="edit-actions">
              <button class="edit-btn save" @click.stop="saveEdit">保存</button>
              <button class="edit-btn cancel" @click.stop="cancelEdit">取消</button>
            </div>
          </div>
          <div v-else class="item-info">
            <span class="item-name">{{ item.name }}</span>
            <div class="item-meta">
              <span class="item-date">
                <Clock :size="12" />
                {{ item.updatedAt }}
              </span>
              <span v-if="item.size" class="item-size">{{ item.size }}</span>
            </div>
          </div>
          <div v-if="editingId !== item.id" class="item-actions">
            <button class="item-action-btn" @click.stop="startEdit(item)">
              <Pencil :size="14" />
            </button>
            <button class="item-action-btn" @click.stop="deleteItem(item.id)">
              <Trash2 :size="14" />
            </button>
            <button class="item-more">
              <MoreVertical :size="16" />
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.workspace-page {
  max-width: 1000px;
  margin: 0 auto;
}

.workspace-toolbar {
  margin-bottom: 20px;
}

.breadcrumb {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  color: #666;
}

.breadcrumb-item.active {
  color: #1a1a1a;
  font-weight: 500;
}

.breadcrumb-separator {
  color: #999;
}

.items-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

.workspace-item {
  background: #fff;
  border-radius: 12px;
  padding: 20px;
  border: 1px solid #e8e8e8;
  display: flex;
  align-items: center;
  gap: 16px;
  transition: all 0.2s;
  cursor: pointer;
}

.workspace-item:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.item-icon {
  width: 48px;
  height: 48px;
  background: #f5f5f5;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.folder-icon {
  color: #faad14;
}

.file-icon {
  color: #1890ff;
}

.item-info {
  flex: 1;
  min-width: 0;
}

.item-name {
  font-size: 14px;
  font-weight: 500;
  color: #1a1a1a;
  display: block;
  margin-bottom: 6px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.item-meta {
  display: flex;
  align-items: center;
  gap: 12px;
}

.item-date {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 12px;
  color: #999;
}

.item-size {
  font-size: 12px;
  color: #999;
}

.item-more {
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  color: #999;
  cursor: pointer;
  opacity: 0;
  transition: opacity 0.2s;
}

.workspace-item:hover .item-more {
  opacity: 1;
}

.item-more:hover {
  background: #f5f5f5;
}

.item-actions {
  display: flex;
  align-items: center;
  gap: 4px;
  opacity: 0;
  transition: opacity 0.2s;
}

.workspace-item:hover .item-actions {
  opacity: 1;
}

.item-action-btn {
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  color: #999;
  cursor: pointer;
}

.item-action-btn:hover {
  background: #f5f5f5;
  color: #1a1a1a;
}

.item-edit-form {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.edit-input,
.edit-select {
  padding: 4px 8px;
  border: 1px solid #d9d9d9;
  border-radius: 4px;
  font-size: 13px;
  outline: none;
  width: 100%;
}

.edit-input:focus,
.edit-select:focus {
  border-color: #1890ff;
}

.edit-actions {
  display: flex;
  gap: 8px;
}

.edit-btn {
  padding: 4px 10px;
  border-radius: 4px;
  font-size: 12px;
  cursor: pointer;
  border: none;
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
  background: #e8e8e8;
}

@media (max-width: 768px) {
  .items-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .items-grid {
    grid-template-columns: 1fr;
  }
}
</style>
