<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { ExternalLink, Pencil, Trash2 } from 'lucide-vue-next'
import { api } from '@/api/request'

interface Friend {
  id: number
  name: string
  avatar: string
  description: string
  url: string
  tags: string[]
}

const friends = ref<Friend[]>([])
const editingId = ref<number | null>(null)
const editForm = ref({
  name: '',
  description: '',
  url: '',
  avatar: '',
  tags: '',
})

const fetchFriends = async () => {
  const data = await api.get<any[]>('/friends')
  friends.value = data.map((item) => ({
    ...item,
    tags: item.tags ? item.tags.split(',').filter(Boolean) : [],
  }))
}

const startEdit = (friend: Friend) => {
  editingId.value = friend.id
  editForm.value = {
    name: friend.name,
    description: friend.description,
    url: friend.url,
    avatar: friend.avatar,
    tags: friend.tags.join(','),
  }
}

const cancelEdit = () => {
  editingId.value = null
}

const saveEdit = async () => {
  if (!editingId.value) return
  await api.put('/friends/' + editingId.value, {
    ...editForm.value,
    tags: editForm.value.tags,
  })
  editingId.value = null
  await fetchFriends()
}

const deleteFriend = async (id: number) => {
  await api.delete('/friends/' + id)
  await fetchFriends()
}

onMounted(fetchFriends)
</script>

<template>
  <div class="friends-page">
    <div class="friends-grid">
      <div
        v-for="friend in friends"
        :key="friend.id"
        class="friend-card"
        :class="{ 'friend-card-editing': editingId === friend.id }"
      >
        <template v-if="editingId === friend.id">
          <div class="edit-form">
            <input v-model="editForm.name" placeholder="名称" class="edit-input" />
            <input v-model="editForm.description" placeholder="描述" class="edit-input" />
            <input v-model="editForm.url" placeholder="链接" class="edit-input" />
            <input v-model="editForm.avatar" placeholder="头像" class="edit-input" />
            <input v-model="editForm.tags" placeholder="标签，逗号分隔" class="edit-input" />
            <div class="edit-actions">
              <button class="edit-btn save" @click="saveEdit">保存</button>
              <button class="edit-btn cancel" @click="cancelEdit">取消</button>
            </div>
          </div>
        </template>
        <template v-else>
          <a :href="friend.url" target="_blank" class="friend-card-link">
            <div class="friend-avatar">{{ friend.avatar }}</div>
            <div class="friend-info">
              <h3 class="friend-name">{{ friend.name }}</h3>
              <p class="friend-desc">{{ friend.description }}</p>
              <div class="friend-tags">
                <span v-for="tag in friend.tags" :key="tag" class="friend-tag">{{ tag }}</span>
              </div>
            </div>
            <ExternalLink :size="16" class="friend-link" />
          </a>
          <div class="friend-actions">
            <button class="action-btn" @click="startEdit(friend)">
              <Pencil :size="16" />
            </button>
            <button class="action-btn" @click="deleteFriend(friend.id)">
              <Trash2 :size="16" />
            </button>
          </div>
        </template>
      </div>
    </div>
  </div>
</template>

<style scoped>
.friends-page {
  max-width: 800px;
  margin: 0 auto;
}

.friends-grid {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.friend-card {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 20px 24px;
  background: #fff;
  border-radius: 12px;
  border: 1px solid #e8e8e8;
  transition: all 0.2s;
}

.friend-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transform: translateX(4px);
}

.friend-card-link {
  display: flex;
  align-items: center;
  gap: 16px;
  flex: 1;
  text-decoration: none;
  color: inherit;
  min-width: 0;
}

.friend-avatar {
  width: 48px;
  height: 48px;
  background: #1a1a1a;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-size: 18px;
  font-weight: 600;
  flex-shrink: 0;
}

.friend-info {
  flex: 1;
  min-width: 0;
}

.friend-name {
  font-size: 15px;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0 0 4px 0;
}

.friend-desc {
  font-size: 13px;
  color: #666;
  margin: 0 0 8px 0;
}

.friend-tags {
  display: flex;
  gap: 6px;
}

.friend-tag {
  padding: 2px 8px;
  border-radius: 4px;
  background: #f5f5f5;
  color: #666;
  font-size: 11px;
}

.friend-link {
  color: #999;
  flex-shrink: 0;
}

.friend-card:hover .friend-link {
  color: #1a1a1a;
}

.friend-actions {
  display: flex;
  gap: 8px;
}

.action-btn {
  background: none;
  border: none;
  padding: 4px;
  cursor: pointer;
  color: #999;
  display: flex;
  align-items: center;
  justify-content: center;
}

.action-btn:hover {
  color: #1a1a1a;
}

.friend-card-editing {
  flex-direction: column;
  align-items: stretch;
}

.edit-form {
  display: flex;
  flex-direction: column;
  gap: 8px;
  width: 100%;
}

.edit-input {
  padding: 8px 12px;
  border: 1px solid #e8e8e8;
  border-radius: 8px;
  font-size: 14px;
  outline: none;
}

.edit-input:focus {
  border-color: #1a1a1a;
}

.edit-actions {
  display: flex;
  gap: 8px;
  margin-top: 4px;
}

.edit-btn {
  padding: 6px 14px;
  border-radius: 6px;
  border: none;
  font-size: 13px;
  cursor: pointer;
}

.edit-btn.save {
  background: #1a1a1a;
  color: #fff;
}

.edit-btn.cancel {
  background: #f5f5f5;
  color: #666;
}

@media (max-width: 768px) {
  .friend-card {
    padding: 16px;
    gap: 12px;
  }

  .friend-avatar {
    width: 40px;
    height: 40px;
    font-size: 14px;
    border-radius: 10px;
  }
}
</style>
