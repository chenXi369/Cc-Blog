<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { Github, ExternalLink, Star, GitFork, Pencil, Trash2 } from 'lucide-vue-next'
import { api } from '@/api/request'

interface Project {
  id: number
  name: string
  description: string
  techStack: string[]
  stars: number
  forks: number
  url: string
  demoUrl?: string
  status: 'active' | 'archived' | 'completed'
}

const projects = ref<Project[]>([])
const editingId = ref<number | null>(null)
const editForm = ref({
  name: '',
  description: '',
  url: '',
  demoUrl: '',
  status: 'active' as 'active' | 'archived' | 'completed',
  techStack: '',
})

const fetchProjects = async () => {
  const data = await api.get<any[]>('/projects')
  projects.value = data.map((item) => ({
    ...item,
    techStack: item.tech_stack ? item.tech_stack.split(',').filter(Boolean) : [],
    demoUrl: item.demo_url,
  }))
}

onMounted(fetchProjects)

const getStatusColor = (status: string) => {
  const colors: Record<string, string> = {
    active: '#52c41a',
    archived: '#999',
    completed: '#1890ff',
  }
  return colors[status] || '#999'
}

const getStatusLabel = (status: string) => {
  const labels: Record<string, string> = {
    active: '进行中',
    archived: '已归档',
    completed: '已完成',
  }
  return labels[status] || status
}

const startEdit = (project: Project) => {
  editingId.value = project.id
  editForm.value = {
    name: project.name,
    description: project.description,
    url: project.url,
    demoUrl: project.demoUrl || '',
    status: project.status,
    techStack: project.techStack.join(','),
  }
}

const cancelEdit = () => {
  editingId.value = null
}

const saveEdit = async () => {
  if (editingId.value === null) return
  await api.put('/projects/' + editingId.value, {
    ...editForm.value,
    tech_stack: editForm.value.techStack,
  })
  editingId.value = null
  await fetchProjects()
}

const deleteProject = async (id: number) => {
  if (!confirm('确定要删除这个项目吗？')) return
  await api.delete('/projects/' + id)
  await fetchProjects()
}
</script>

<template>
  <div class="projects-page">
    <div class="projects-grid">
      <div
        v-for="project in projects"
        :key="project.id"
        class="project-card"
      >
        <div class="project-header">
          <div class="project-icon">
            <Github :size="24" />
          </div>
          <div class="project-header-right">
            <div class="project-status" :style="{ color: getStatusColor(project.status) }">
              {{ getStatusLabel(project.status) }}
            </div>
            <button class="icon-btn" @click="startEdit(project)">
              <Pencil :size="14" />
            </button>
            <button class="icon-btn delete-btn" @click="deleteProject(project.id)">
              <Trash2 :size="14" />
            </button>
          </div>
        </div>

        <template v-if="editingId === project.id">
          <div class="edit-form">
            <input v-model="editForm.name" class="edit-input" placeholder="项目名称" />
            <textarea v-model="editForm.description" class="edit-textarea" placeholder="描述" rows="3"></textarea>
            <input v-model="editForm.url" class="edit-input" placeholder="仓库地址" />
            <input v-model="editForm.demoUrl" class="edit-input" placeholder="演示地址" />
            <select v-model="editForm.status" class="edit-select">
              <option value="active">进行中</option>
              <option value="archived">已归档</option>
              <option value="completed">已完成</option>
            </select>
            <input v-model="editForm.techStack" class="edit-input" placeholder="技术栈，逗号分隔" />
            <div class="edit-actions">
              <button class="edit-btn save" @click="saveEdit">保存</button>
              <button class="edit-btn cancel" @click="cancelEdit">取消</button>
            </div>
          </div>
        </template>

        <template v-else>
          <h3 class="project-name">{{ project.name }}</h3>
          <p class="project-desc">{{ project.description }}</p>

          <div class="project-tech">
            <span v-for="tech in project.techStack" :key="tech" class="tech-tag">
              {{ tech }}
            </span>
          </div>

          <div class="project-footer">
            <div class="project-stats">
              <span class="stat">
                <Star :size="14" />
                {{ project.stars }}
              </span>
              <span class="stat">
                <GitFork :size="14" />
                {{ project.forks }}
              </span>
            </div>
            <div class="project-links">
              <a :href="project.url" target="_blank" class="link-btn">
                <Github :size="14" />
              </a>
              <a v-if="project.demoUrl" :href="project.demoUrl" target="_blank" class="link-btn">
                <ExternalLink :size="14" />
              </a>
            </div>
          </div>
        </template>
      </div>
    </div>
  </div>
</template>

<style scoped>
.projects-page {
  max-width: 1000px;
  margin: 0 auto;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}

.project-card {
  background: #fff;
  border-radius: 12px;
  padding: 24px;
  border: 1px solid #e8e8e8;
  transition: all 0.2s;
}

.project-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transform: translateY(-2px);
}

.project-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.project-header-right {
  display: flex;
  align-items: center;
  gap: 8px;
}

.icon-btn {
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  background: #f5f5f5;
  color: #666;
  border: none;
  cursor: pointer;
  transition: all 0.2s;
}

.icon-btn:hover {
  background: #1a1a1a;
  color: #fff;
}

.delete-btn:hover {
  background: #ff4d4f;
  color: #fff;
}

.project-icon {
  width: 40px;
  height: 40px;
  background: #f5f5f5;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #1a1a1a;
}

.project-status {
  font-size: 12px;
  font-weight: 500;
}

.project-name {
  font-size: 16px;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0 0 8px 0;
}

.project-desc {
  font-size: 13px;
  color: #666;
  margin: 0 0 16px 0;
  line-height: 1.5;
}

.project-tech {
  display: flex;
  gap: 6px;
  margin-bottom: 16px;
  flex-wrap: wrap;
}

.tech-tag {
  padding: 4px 10px;
  border-radius: 4px;
  background: #f5f5f5;
  color: #666;
  font-size: 12px;
}

.project-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 16px;
  border-top: 1px solid #f5f5f5;
}

.project-stats {
  display: flex;
  gap: 16px;
}

.stat {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 13px;
  color: #666;
}

.project-links {
  display: flex;
  gap: 8px;
}

.link-btn {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  background: #f5f5f5;
  color: #666;
  transition: all 0.2s;
}

.link-btn:hover {
  background: #1a1a1a;
  color: #fff;
}

.edit-form {
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
  font-size: 13px;
  color: #1a1a1a;
  background: #fff;
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
  padding: 6px 14px;
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
  .projects-grid {
    grid-template-columns: 1fr;
  }
}
</style>
