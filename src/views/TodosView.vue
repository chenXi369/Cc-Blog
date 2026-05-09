<script setup lang="ts">
import { ref, computed } from 'vue'
import { CheckCircle2, Circle, Plus, Trash2, Calendar } from 'lucide-vue-next'

interface Todo {
  id: number
  title: string
  completed: boolean
  priority: 'high' | 'medium' | 'low'
  dueDate?: string
  category: string
}

const todos = ref<Todo[]>([
  { id: 1, title: '完成 Vue3 博客项目', completed: false, priority: 'high', dueDate: '2024-01-20', category: '项目' },
  { id: 2, title: '学习 WebGL 基础', completed: false, priority: 'medium', dueDate: '2024-01-25', category: '学习' },
  { id: 3, title: '优化编辑器性能', completed: true, priority: 'high', dueDate: '2024-01-15', category: '项目' },
  { id: 4, title: '整理技术笔记', completed: false, priority: 'low', dueDate: '2024-01-30', category: '文档' },
  { id: 5, title: '阅读 AI 相关论文', completed: false, priority: 'medium', dueDate: '2024-02-01', category: '学习' },
])

const newTodoTitle = ref('')
const filter = ref<'all' | 'active' | 'completed'>('all')

const filteredTodos = computed(() => {
  if (filter.value === 'active') return todos.value.filter((t) => !t.completed)
  if (filter.value === 'completed') return todos.value.filter((t) => t.completed)
  return todos.value
})

const toggleTodo = (todo: Todo) => {
  todo.completed = !todo.completed
}

const deleteTodo = (id: number) => {
  todos.value = todos.value.filter((t) => t.id !== id)
}

const addTodo = () => {
  if (!newTodoTitle.value.trim()) return
  todos.value.push({
    id: Date.now(),
    title: newTodoTitle.value,
    completed: false,
    priority: 'medium',
    category: '其他',
  })
  newTodoTitle.value = ''
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

          <div class="todo-content">
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

          <button class="todo-delete" @click="deleteTodo(todo.id)">
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

.todo-item:hover .todo-delete {
  opacity: 1;
}

.todo-delete:hover {
  color: #ff4d4f;
}
</style>
