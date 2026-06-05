<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import {
  Search,
  Plus,
  Filter,
  MoreHorizontal,
  CheckCircle2,
  Circle,
  Calendar,
  GitBranch,
  AlertCircle,
  Layers,
  Pencil,
  Trash2,
} from 'lucide-vue-next'
import { api } from '@/api/request'

interface Requirement {
  id: number
  title: string
  status: 'completed' | 'pending' | 'in-progress'
  priority: 'high' | 'medium' | 'low'
  category: string
  date: string
  techStack: string[]
  difficulty: string
  description: string
  tags: string[]
}

interface Stats {
  total: number
  completed: number
  in_progress: number
  completion_rate: number
}

const searchQuery = ref('')
const activeFilter = ref('all')
const requirements = ref<Requirement[]>([])
const statsData = ref<Stats>({ total: 0, completed: 0, in_progress: 0, completion_rate: 0 })

const editingId = ref<number | null>(null)
const editForm = ref({
  title: '',
  description: '',
  category: '',
  priority: 'medium' as 'high' | 'medium' | 'low',
  status: 'pending' as 'completed' | 'pending' | 'in-progress',
  date: '',
  difficulty: '',
  techStack: '',
  tags: '',
})

const filters = [
  { key: 'all', label: '全部需求' },
  { key: 'completed', label: '已完成' },
  { key: 'pending', label: '进行中' },
]

const fetchRequirements = async () => {
  const data = await api.get<any[]>('/requirements')
  requirements.value = data.map((item) => ({
    ...item,
    techStack: item.tech_stack ? item.tech_stack.split(',').filter(Boolean) : [],
    tags: item.tags ? item.tags.split(',').filter(Boolean) : [],
  }))
}

const fetchStats = async () => {
  statsData.value = await api.get<Stats>('/requirements/stats')
}

onMounted(() => {
  fetchRequirements()
  fetchStats()
})

const filteredRequirements = computed(() => {
  let result = requirements.value

  if (activeFilter.value !== 'all') {
    result = result.filter((r) => r.status === activeFilter.value)
  }

  if (searchQuery.value) {
    result = result.filter((r) =>
      r.title.toLowerCase().includes(searchQuery.value.toLowerCase()),
    )
  }

  return result
})

const stats = computed(() => ({
  total: statsData.value.total,
  completed: statsData.value.completed,
  inProgress: statsData.value.in_progress,
  completionRate: statsData.value.completion_rate,
}))

const getPriorityColor = (priority: string) => {
  const colors: Record<string, string> = {
    high: '#ff4d4f',
    medium: '#faad14',
    low: '#52c41a',
  }
  return colors[priority] || '#999'
}

const getStatusColor = (status: string) => {
  return status === 'completed' ? '#52c41a' : '#bfbfbf'
}

const startEdit = (req: Requirement) => {
  editingId.value = req.id
  editForm.value = {
    title: req.title,
    description: req.description,
    category: req.category,
    priority: req.priority,
    status: req.status,
    date: req.date,
    difficulty: req.difficulty,
    techStack: req.techStack.join(','),
    tags: req.tags.join(','),
  }
}

const cancelEdit = () => {
  editingId.value = null
}

const saveEdit = async () => {
  if (!editingId.value) return
  await api.put('/requirements/' + editingId.value, {
    ...editForm.value,
    tech_stack: editForm.value.techStack,
    tags: editForm.value.tags,
  })
  editingId.value = null
  await fetchRequirements()
}

const deleteReq = async (id: number) => {
  if (!confirm('确定要删除该需求吗？')) return
  await api.delete('/requirements/' + id)
  await fetchRequirements()
}
</script>

<template>
  <div class="requirements-page">
    <div class="requirements-layout">
      <aside class="requirements-sidebar">
        <div class="search-box">
          <Search :size="16" class="search-icon" />
          <input
            v-model="searchQuery"
            type="text"
            placeholder="搜索需求..."
            class="search-input"
          />
        </div>

        <nav class="filter-nav">
          <button
            v-for="filter in filters"
            :key="filter.key"
            class="filter-btn"
            :class="{ active: activeFilter === filter.key }"
            @click="activeFilter = filter.key"
          >
            <Filter :size="14" />
            <span>{{ filter.label }}</span>
          </button>
        </nav>

        <div class="stats-section">
          <div class="stats-header">
            <Layers :size="14" />
            <span>统计信息</span>
          </div>
          <div class="stats-list">
            <div class="stat-item">
              <span class="stat-label">总需求</span>
              <span class="stat-value">{{ stats.total }}</span>
            </div>
            <div class="stat-item">
              <span class="stat-label">已完成</span>
              <span class="stat-value success">{{ stats.completed }}</span>
            </div>
            <div class="stat-item">
              <span class="stat-label">进行中</span>
              <span class="stat-value warning">{{ stats.inProgress }}</span>
            </div>
            <div class="stat-item">
              <span class="stat-label">完成率</span>
              <span class="stat-value">{{ stats.completionRate }}%</span>
            </div>
          </div>
        </div>
      </aside>

      <div class="requirements-content">
        <div class="content-header">
          <div class="header-filters">
            <button class="header-filter-btn active">
              <Filter :size="14" />
              <span>全部需求</span>
            </button>
          </div>
          <button class="new-requirement-btn">
            <Plus :size="16" />
            <span>新建需求</span>
          </button>
        </div>

        <div class="requirements-list">
          <div
            v-for="req in filteredRequirements"
            :key="req.id"
            class="requirement-card"
          >
            <div class="card-header">
              <div class="card-status">
                <component
                  :is="req.status === 'completed' ? CheckCircle2 : Circle"
                  :size="18"
                  :style="{ color: getStatusColor(req.status) }"
                />
              </div>
              <h3 class="card-title">{{ req.title }}</h3>
              <div class="card-actions">
                <button class="action-btn" @click="startEdit(req)">
                  <Pencil :size="16" />
                </button>
                <button class="action-btn" @click="deleteReq(req.id)">
                  <Trash2 :size="16" />
                </button>
                <button class="action-btn">
                  <MoreHorizontal :size="16" />
                </button>
                <span
                  v-if="req.status === 'completed'"
                  class="status-badge completed"
                >
                  已完成
                </span>
              </div>
            </div>

            <div v-if="editingId === req.id" class="card-body edit-form">
              <div class="edit-fields">
                <input v-model="editForm.title" class="edit-input" placeholder="标题" />
                <textarea v-model="editForm.description" class="edit-textarea" placeholder="描述" rows="3"></textarea>
                <input v-model="editForm.category" class="edit-input" placeholder="分类" />
                <div class="edit-row">
                  <select v-model="editForm.priority" class="edit-select">
                    <option value="high">高优</option>
                    <option value="medium">中优</option>
                    <option value="low">低优</option>
                  </select>
                  <select v-model="editForm.status" class="edit-select">
                    <option value="completed">已完成</option>
                    <option value="pending">待处理</option>
                    <option value="in-progress">进行中</option>
                  </select>
                </div>
                <input v-model="editForm.date" type="date" class="edit-input" />
                <input v-model="editForm.difficulty" class="edit-input" placeholder="难度" />
                <input v-model="editForm.techStack" class="edit-input" placeholder="技术栈（逗号分隔）" />
                <input v-model="editForm.tags" class="edit-input" placeholder="标签（逗号分隔）" />
              </div>
              <div class="edit-actions">
                <button class="edit-save-btn" @click="saveEdit">保存</button>
                <button class="edit-cancel-btn" @click="cancelEdit">取消</button>
              </div>
            </div>
            <div v-else class="card-body">
              <div class="card-meta">
                <span class="meta-tag category">{{ req.category }}</span>
                <span
                  class="meta-tag priority"
                  :style="{ background: getPriorityColor(req.priority) + '15', color: getPriorityColor(req.priority) }"
                >
                  {{ req.priority === 'high' ? '高优' : req.priority === 'medium' ? '中优' : '低优' }}
                </span>
                <span class="meta-item">
                  <Calendar :size="12" />
                  {{ req.date }}
                </span>
                <span class="meta-item">
                  <GitBranch :size="12" />
                  {{ req.techStack.length }}技术栈
                </span>
                <span class="meta-item">
                  <AlertCircle :size="12" />
                  {{ req.difficulty }}
                </span>
              </div>

              <p class="card-description">{{ req.description }}</p>

              <div class="card-tags">
                <span v-for="tag in req.tags" :key="tag" class="tag">
                  {{ tag }}
                </span>
              </div>

              <div class="card-tech-stack">
                <span class="tech-label">相关技术栈</span>
                <div class="tech-list">
                  <span v-for="tech in req.techStack" :key="tech" class="tech-item">
                    <span class="tech-dot"></span>
                    {{ tech }}
                  </span>
                </div>
              </div>

              <div class="card-footer">
                <span class="footer-label">技术难点</span>
                <p class="footer-text">{{ req.description }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.requirements-page {
  max-width: 1200px;
  margin: 0 auto;
}

.requirements-layout {
  display: flex;
  gap: 24px;
}

.requirements-sidebar {
  width: 240px;
  flex-shrink: 0;
}

.search-box {
  position: relative;
  margin-bottom: 16px;
}

.search-icon {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: #999;
}

.search-input {
  width: 100%;
  padding: 10px 12px 10px 36px;
  border: 1px solid #e8e8e8;
  border-radius: 8px;
  font-size: 14px;
  outline: none;
  transition: border-color 0.2s;
}

.search-input:focus {
  border-color: #1a1a1a;
}

.filter-nav {
  display: flex;
  flex-direction: column;
  gap: 4px;
  margin-bottom: 24px;
}

.filter-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 12px;
  border-radius: 6px;
  font-size: 14px;
  color: #666;
  cursor: pointer;
  transition: all 0.2s;
  border: none;
  background: none;
}

.filter-btn:hover {
  background: #f5f5f5;
}

.filter-btn.active {
  background: #1a1a1a;
  color: #fff;
}

.stats-section {
  background: #fff;
  border-radius: 8px;
  padding: 16px;
  border: 1px solid #e8e8e8;
}

.stats-header {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  font-weight: 600;
  color: #1a1a1a;
  margin-bottom: 12px;
  padding-bottom: 12px;
  border-bottom: 1px solid #f0f0f0;
}

.stats-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.stat-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 13px;
}

.stat-label {
  color: #666;
}

.stat-value {
  font-weight: 600;
  color: #1a1a1a;
}

.stat-value.success {
  color: #52c41a;
}

.stat-value.warning {
  color: #faad14;
}

.requirements-content {
  flex: 1;
}

.content-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.header-filters {
  display: flex;
  gap: 8px;
}

.header-filter-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  border-radius: 6px;
  font-size: 14px;
  color: #666;
  background: #fff;
  border: 1px solid #e8e8e8;
  cursor: pointer;
}

.header-filter-btn.active {
  background: #1a1a1a;
  color: #fff;
  border-color: #1a1a1a;
}

.new-requirement-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  border-radius: 6px;
  font-size: 14px;
  color: #fff;
  background: #1a1a1a;
  border: none;
  cursor: pointer;
  transition: opacity 0.2s;
}

.new-requirement-btn:hover {
  opacity: 0.9;
}

.requirements-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.requirement-card {
  background: #fff;
  border-radius: 12px;
  border: 1px solid #e8e8e8;
  overflow: hidden;
}

.card-header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px 20px;
  border-bottom: 1px solid #f5f5f5;
}

.card-status {
  display: flex;
  align-items: center;
}

.card-title {
  flex: 1;
  font-size: 15px;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0;
}

.card-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.action-btn {
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  color: #999;
  cursor: pointer;
}

.action-btn:hover {
  background: #f5f5f5;
}

.status-badge {
  padding: 4px 10px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
}

.status-badge.completed {
  background: #f6ffed;
  color: #52c41a;
  border: 1px solid #b7eb8f;
}

.card-body {
  padding: 16px 20px;
}

.card-meta {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 12px;
  flex-wrap: wrap;
}

.meta-tag {
  padding: 4px 10px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
}

.meta-tag.category {
  background: #f5f5f5;
  color: #666;
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 12px;
  color: #999;
}

.card-description {
  font-size: 14px;
  color: #666;
  margin-bottom: 12px;
  line-height: 1.5;
}

.card-tags {
  display: flex;
  gap: 6px;
  margin-bottom: 16px;
}

.tag {
  padding: 4px 10px;
  border-radius: 4px;
  font-size: 12px;
  color: #666;
  background: #f5f5f5;
  cursor: pointer;
  transition: all 0.2s;
}

.tag:hover {
  background: #e8e8e8;
}

.card-tech-stack {
  background: #fafafa;
  border-radius: 8px;
  padding: 12px 16px;
  margin-bottom: 12px;
}

.tech-label {
  font-size: 12px;
  color: #999;
  margin-bottom: 8px;
  display: block;
}

.tech-list {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.tech-item {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  color: #666;
}

.tech-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #1890ff;
}

.card-footer {
  border-top: 1px solid #f5f5f5;
  padding-top: 12px;
}

.footer-label {
  font-size: 12px;
  color: #999;
  margin-bottom: 4px;
  display: block;
}

.footer-text {
  font-size: 13px;
  color: #666;
  margin: 0;
}

.edit-fields {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.edit-input,
.edit-textarea,
.edit-select {
  padding: 8px 12px;
  border: 1px solid #e8e8e8;
  border-radius: 6px;
  font-size: 14px;
  outline: none;
  transition: border-color 0.2s;
  background: #fff;
}

.edit-input:focus,
.edit-textarea:focus,
.edit-select:focus {
  border-color: #1a1a1a;
}

.edit-row {
  display: flex;
  gap: 10px;
}

.edit-row .edit-select {
  flex: 1;
}

.edit-actions {
  display: flex;
  gap: 10px;
  margin-top: 12px;
}

.edit-save-btn,
.edit-cancel-btn {
  padding: 8px 16px;
  border-radius: 6px;
  font-size: 14px;
  cursor: pointer;
  border: none;
  transition: opacity 0.2s;
}

.edit-save-btn {
  background: #1a1a1a;
  color: #fff;
}

.edit-cancel-btn {
  background: #f5f5f5;
  color: #666;
}

.edit-save-btn:hover,
.edit-cancel-btn:hover {
  opacity: 0.9;
}

@media (max-width: 768px) {
  .requirements-layout {
    flex-direction: column;
    gap: 16px;
  }

  .requirements-sidebar {
    width: 100%;
  }

  .filter-nav {
    flex-direction: row;
    flex-wrap: wrap;
  }

  .stats-section {
    display: none;
  }

  .content-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
  }

  .card-header {
    padding: 12px 16px;
  }

  .card-body {
    padding: 12px 16px;
  }

  .card-meta {
    gap: 6px;
  }
}
</style>
