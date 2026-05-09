<script setup lang="ts">
import { ref } from 'vue'
import { Folder, FileText, Clock, MoreVertical } from 'lucide-vue-next'

interface WorkspaceItem {
  id: number
  name: string
  type: 'folder' | 'file'
  updatedAt: string
  size?: string
}

const workspaceItems = ref<WorkspaceItem[]>([
  { id: 1, name: '项目文档', type: 'folder', updatedAt: '2024-01-15' },
  { id: 2, name: '设计稿', type: 'folder', updatedAt: '2024-01-14' },
  { id: 3, name: '需求分析.md', type: 'file', updatedAt: '2024-01-13', size: '24KB' },
  { id: 4, name: '技术方案.md', type: 'file', updatedAt: '2024-01-12', size: '18KB' },
  { id: 5, name: '会议纪要', type: 'folder', updatedAt: '2024-01-10' },
  { id: 6, name: 'API 文档.md', type: 'file', updatedAt: '2024-01-09', size: '45KB' },
])
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
          <div class="item-info">
            <span class="item-name">{{ item.name }}</span>
            <div class="item-meta">
              <span class="item-date">
                <Clock :size="12" />
                {{ item.updatedAt }}
              </span>
              <span v-if="item.size" class="item-size">{{ item.size }}</span>
            </div>
          </div>
          <button class="item-more">
            <MoreVertical :size="16" />
          </button>
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
