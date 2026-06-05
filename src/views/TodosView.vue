<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { CheckCircle2, Circle, Plus, Trash2, Calendar, Pencil } from 'lucide-vue-next'
import { api } from '@/api/request'

interface Todo {
  id: number
  title: string
  completed: boolean
  priority: 'high' | 'medium' | 'low'
  dueDate?: string
  category: string
}

const todos = ref<Todo[]>([])
const newTodoTitle = ref('')
const filter = ref<'all' | 'active' | 'completed'>('all')
const editingId = ref<number | null>(null)
const editForm = ref({
  title: '',
  priority: 'medium' as 'high' | 'medium' | 'low',
  dueDate: '',
  category: '',
})

const fetchTodos = async () => {
  const data = await api.get<any[]>('/todos')
  todos.value = data.map((item) => ({
    ...item,
    dueDate: item.due_date,
  }))
}

onMounted(fetchTodos)

const filteredTodos = computed(() => {
  if (filter.value === 'active') return todos.value.filter((t) => !t.completed)
  if (filter.value === 'completed') return todos.value.filter((t) => t.completed)
  return todos.value
})

const toggleTodo = async (todo: Todo) => {
  const updated = await api.put<any>(`/todos/${todo.id}`, {
    completed: !todo.completed,
  })
  todo.completed = updated.completed
}

const deleteTodo = async (id: number) => {
  await api.delete(`/todos/${id}`)
  todos.value = todos.value.filter((t) => t.id !== id)
}

const addTodo = async () => {
  if (!newTodoTitle.value.trim()) return
  const created = await api.post<any>('/todos', {
    title: newTodoTitle.value,
    completed: false,
    priority: 'medium',
    category: '其他',
  })
  todos.value.unshift({
    ...created,
    dueDate: created.due_date,
  })
  newTodoTitle.value = ''
}

const startEdit = (todo: Todo) => {
  editingId.value = todo.id
  editForm.value = {
    title: todo.title,
    priority: todo.priority,
    dueDate: todo.dueDate || '',
    category: todo.category,
  }
}

const cancelEdit = () => {
  editingId.value = null
}

const saveEdit = async () => {
  if (editingId.value === null) return
  const updated = await api.put<any>(`/todos/${editingId.value}`, {
    title: editForm.value.title,
    priority: editForm.value.priority,
    dueDate: editForm.value.dueDate,
    category: editForm.value.category,
  })
  const todo = todos.value.find((t) => t.id === editingId.value)
  if (todo) {
    todo.title = updated.title
    todo.priority = updated.priority
    todo.dueDate = updated.due_date
    todo.category = updated.category
  }
  editingId.value = null
}

const getPriorityColor = (priority: string) => {
  const colors: Record<string, string> = {
    high: '#ff4d4f',
    medium: '#faad14',
    low: '#52c41a',
  }
  return colors[priority] || '#999'
}
</script>

<template>
  <div class="todos-page">
    <div class="todos-container">
      <div class="todos-input">
        <input
          v-model="newTodoTitle"
          type="text"
          placeholder="添加新的待办事项..."
          class="todo-input"
          @keyup.enter="addTodo"
        />
        <button class="add-btn" @click="addTodo">
          <Plus :size="18" />
        </button>
      </div>

      <div class="todos-filters">
        <button
          class="filter-btn"
          :class="{ active: filter === 'all' }"
          @click="filter = 'all'"
        >
          全部
        </button>
        <button
          class="filter-btn"
          :class="{ active: filter === 'active' }"
          @click="filter = 'active'"
        >
          进行中
        </button>
        <button
          class="filter-btn"
          :class="{ active: filter === 'completed' }"
          @click="filter = 'completed'"
        >
          已完成
        </button>
      </div>

      <div class="todos-list">
        <div
          v-for="todo in filteredTodos"
          :key="todo.id"
          class="todo-item"
          :class="{ completed: todo.completed }"
        >
          <button class="todo-check" @click="toggleTodo(todo)">
            <CheckCircle2 v-if="todo.completed" :size="20" class="check-icon checked" />
            <Circle v-else :size="20" class="check-icon" />
          </button>

          <div v-if="editingId !== todo.id" class="todo-content">
            <span class="todo-title">{{ todo.title }}</span>
            <div class="todo-meta">
              <span
                class="todo-priority"
                :style="{ color: getPriorityColor(todo.priority) }"
              >
                {{ todo.priority === 'high' ? '高' : todo.priority === 'medium' ? '中' : '低' }}优先级
              </span>
              <span v-if="todo.dueDate" class="todo-date">
                <Calendar :size="12" />
                {{ todo.dueDate }}
              </span>
              <span class="todo-category">{{ todo.category }}</span>
            </div>
          </div>

          <div v-else class="todo-content">
            <div class="edit-form">
              <input
                v-model="editForm.title"
                type="text"
                class="edit-input edit-title"
                placeholder="标题"
              />
              <div class="edit-row">
                <select v-model="editForm.priority" class="edit-select">
                  <option value="high">高</option>
                  <option value="medium">中</option>
                  <option value="low">低</option>
                </select>
                <input
                  v-model="editForm.dueDate"
                  type="date"
                  class="edit-input edit-date"
                />
                <input
                  v-model="editForm.category"
                  type="text"
                  class="edit-input edit-category"
                  placeholder="分类"
                />
              </div>
              <div class="edit-actions">
                <button class="edit-btn save" @click="saveEdit">保存</button>
                <button class="edit-btn cancel" @click="cancelEdit">取消</button>
              </div>
            </div>
          </div>

          <button v-if="editingId !== todo.id" class="todo-edit" @click="startEdit(todo)">
            <Pencil :size="16" />
          </button>
          <button v-if="editingId !== todo.id" class="todo-delete" @click="deleteTodo(todo.id)">
            <Trash2 :size="16" />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.todos-page {
  max-width: 700px;
  margin: 0 auto;
}

.todos-container {
  background: #fff;
  border-radius: 12px;
  padding: 24px;
  border: 1px solid #e8e8e8;
}

.todos-input {
  display: flex;
  gap: 12px;
  margin-bottom: 20px;
}

.todo-input {
  flex: 1;
  padding: 12px 16px;
  border: 1px solid #e8e8e8;
  border-radius: 8px;
  font-size: 14px;
  outline: none;
  transition: border-color 0.2s;
}

.todo-input:focus {
  border-color: #1a1a1a;
}

.add-btn {
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #1a1a1a;
  color: #fff;
  border-radius: 8px;
  cursor: pointer;
  transition: opacity 0.2s;
}

.add-btn:hover {
  opacity: 0.9;
}

.todos-filters {
  display: flex;
  gap: 8px;
  margin-bottom: 20px;
}

.filter-btn {
  padding: 8px 16px;
  border-radius: 6px;
  font-size: 13px;
  color: #666;
  background: #f5f5f5;
  border: none;
  cursor: pointer;
  transition: all 0.2s;
}

.filter-btn:hover {
  background: #e8e8e8;
}

.filter-btn.active {
  background: #1a1a1a;
  color: #fff;
}

.todos-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.todo-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px;
  border-radius: 8px;
  transition: all 0.2s;
}

.todo-item:hover {
  background: #f5f5f5;
}

.todo-item.completed .todo-title {
  text-decoration: line-through;
  color: #999;
}

.todo-check {
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: none;
  border: none;
  cursor: pointer;
  color: #999;
}

.check-icon.checked {
  color: #52c41a;
}

.todo-content {
  flex: 1;
  min-width: 0;
}

.todo-title {
  font-size: 14px;
  color: #1a1a1a;
  display: block;
  margin-bottom: 4px;
}

.todo-meta {
  display: flex;
  gap: 12px;
  align-items: center;
}

.todo-priority {
  font-size: 12px;
  font-weight: 500;
}

.todo-date {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 12px;
  color: #999;
}

.todo-category {
  padding: 2px 8px;
  border-radius: 4px;
  background: #f0f0f0;
  color: #666;
  font-size: 11px;
}

.todo-delete {
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: none;
  border: none;
  cursor: pointer;
  color: #999;
  opacity: 0;
  transition: opacity 0.2s;
}

.todo-item:hover .todo-delete,
.todo-item:hover .todo-edit {
  opacity: 1;
}

.todo-delete:hover {
  color: #ff4d4f;
}

.todo-edit {
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: none;
  border: none;
  cursor: pointer;
  color: #999;
  opacity: 0;
  transition: opacity 0.2s;
}

.todo-edit:hover {
  color: #1a1a1a;
}

@media (max-width: 768px) {
  .todos-container {
    padding: 16px;
  }

  .todo-item {
    padding: 12px;
  }

  .todo-meta {
    flex-wrap: wrap;
    gap: 8px;
  }

  .todo-delete,
  .todo-edit {
    opacity: 1;
  }
}

.edit-form {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.edit-input,
.edit-select {
  padding: 6px 10px;
  border: 1px solid #e8e8e8;
  border-radius: 6px;
  font-size: 13px;
  outline: none;
  transition: border-color 0.2s;
}

.edit-input:focus,
.edit-select:focus {
  border-color: #1a1a1a;
}

.edit-row {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.edit-row .edit-select {
  min-width: 80px;
}

.edit-row .edit-date {
  min-width: 130px;
}

.edit-row .edit-category {
  min-width: 80px;
  flex: 1;
}

.edit-actions {
  display: flex;
  gap: 8px;
}

.edit-btn {
  padding: 6px 14px;
  border-radius: 6px;
  font-size: 13px;
  border: none;
  cursor: pointer;
  transition: opacity 0.2s;
}

.edit-btn.save {
  background: #1a1a1a;
  color: #fff;
}

.edit-btn.cancel {
  background: #f5f5f5;
  color: #666;
}

.edit-btn:hover {
  opacity: 0.9;
}

@media (max-width: 768px) {
  .edit-row {
    flex-direction: column;
  }

  .edit-row .edit-category {
    width: 100%;
  }
}
</style>
