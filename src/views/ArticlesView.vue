<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { Eye, Heart, MessageCircle, Calendar, Pencil, Trash2 } from 'lucide-vue-next'
import { api } from '@/api/request'

interface Article {
  id: number
  title: string
  summary: string
  cover?: string
  tags: string[]
  views: number
  likes: number
  comments: number
  date: string
  readTime: string
}

interface ArticleEditForm {
  title: string
  summary: string
  cover?: string
  tags: string
  views: number
  likes: number
  comments: number
  date: string
  readTime: string
}

const articles = ref<Article[]>([])
const editingId = ref<number | null>(null)
const editForm = ref<Partial<ArticleEditForm>>({})

const fetchArticles = async () => {
  const data = await api.get<any[]>('/articles')
  articles.value = data.map((item) => ({
    ...item,
    tags: item.tags ? item.tags.split(',').filter(Boolean) : [],
    readTime: item.read_time || '',
  }))
}

onMounted(fetchArticles)

const startEdit = (article: Article) => {
  editingId.value = article.id
  editForm.value = {
    ...article,
    tags: article.tags.join(','),
  }
}

const cancelEdit = () => {
  editingId.value = null
  editForm.value = {}
}

const saveEdit = async () => {
  if (!editingId.value) return
  await api.put('/articles/' + editingId.value, {
    ...editForm.value,
    tags: editForm.value.tags,
  })
  await fetchArticles()
  editingId.value = null
}

const deleteArticle = async (id: number) => {
  await api.delete('/articles/' + id)
  await fetchArticles()
}

const formatNumber = (num: number): string => {
  if (num >= 1000) {
    return (num / 1000).toFixed(1) + 'k'
  }
  return num.toString()
}
</script>

<template>
  <div class="articles-page">
    <div class="articles-list">
      <article
        v-for="article in articles"
        :key="article.id"
        class="article-card"
      >
        <div class="article-actions">
          <button
            v-if="editingId !== article.id"
            class="action-btn"
            @click.stop="startEdit(article)"
          >
            <Pencil :size="16" />
          </button>
          <button
            v-if="editingId !== article.id"
            class="action-btn"
            @click.stop="deleteArticle(article.id)"
          >
            <Trash2 :size="16" />
          </button>
        </div>

        <div v-if="editingId === article.id" class="article-edit-form">
          <input v-model="editForm.title" placeholder="标题" />
          <textarea v-model="editForm.summary" placeholder="摘要" rows="3" />
          <input v-model="editForm.tags" placeholder="标签（逗号分隔）" />
          <input v-model="editForm.date" placeholder="日期" />
          <input v-model="editForm.readTime" placeholder="阅读时间" />
          <div class="edit-actions">
            <button class="edit-btn save" @click="saveEdit">保存</button>
            <button class="edit-btn cancel" @click="cancelEdit">取消</button>
          </div>
        </div>

        <div v-else class="article-content">
          <div class="article-meta-top">
            <span v-for="tag in article.tags" :key="tag" class="article-tag">
              {{ tag }}
            </span>
          </div>
          <h2 class="article-title">{{ article.title }}</h2>
          <p class="article-summary">{{ article.summary }}</p>
          <div class="article-meta-bottom">
            <div class="meta-item">
              <Calendar :size="14" />
              <span>{{ article.date }}</span>
            </div>
            <div class="meta-item">
              <Eye :size="14" />
              <span>{{ formatNumber(article.views) }}</span>
            </div>
            <div class="meta-item">
              <Heart :size="14" />
              <span>{{ article.likes }}</span>
            </div>
            <div class="meta-item">
              <MessageCircle :size="14" />
              <span>{{ article.comments }}</span>
            </div>
            <span class="read-time">{{ article.readTime }}阅读</span>
          </div>
        </div>
      </article>
    </div>
  </div>
</template>

<style scoped>
.articles-page {
  max-width: 800px;
  margin: 0 auto;
}

.articles-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.article-card {
  position: relative;
  background: #fff;
  border-radius: 12px;
  padding: 24px;
  border: 1px solid #e8e8e8;
  transition: all 0.2s;
  cursor: pointer;
}

.article-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transform: translateY(-2px);
}

.article-meta-top {
  display: flex;
  gap: 8px;
  margin-bottom: 12px;
}

.article-tag {
  padding: 4px 10px;
  border-radius: 4px;
  background: #f5f5f5;
  color: #666;
  font-size: 12px;
}

.article-title {
  font-size: 18px;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0 0 10px 0;
  line-height: 1.4;
}

.article-summary {
  font-size: 14px;
  color: #666;
  line-height: 1.6;
  margin: 0 0 16px 0;
}

.article-meta-bottom {
  display: flex;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 13px;
  color: #999;
}

.read-time {
  margin-left: auto;
  font-size: 12px;
  color: #999;
}

.article-actions {
  position: absolute;
  top: 16px;
  right: 16px;
  display: flex;
  gap: 8px;
}

.action-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border: none;
  background: transparent;
  color: #999;
  cursor: pointer;
  border-radius: 6px;
  transition: all 0.2s;
}

.action-btn:hover {
  background: #f5f5f5;
  color: #333;
}

.article-edit-form {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.article-edit-form input,
.article-edit-form textarea {
  padding: 8px 12px;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  font-size: 14px;
  outline: none;
  resize: vertical;
}

.article-edit-form input:focus,
.article-edit-form textarea:focus {
  border-color: #409eff;
}

.edit-actions {
  display: flex;
  gap: 12px;
  margin-top: 8px;
}

.edit-btn {
  padding: 8px 16px;
  border: none;
  border-radius: 6px;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s;
}

.edit-btn.save {
  background: #409eff;
  color: #fff;
}

.edit-btn.save:hover {
  background: #66b1ff;
}

.edit-btn.cancel {
  background: #f5f5f5;
  color: #666;
}

.edit-btn.cancel:hover {
  background: #e0e0e0;
}

@media (max-width: 768px) {
  .article-card {
    padding: 16px;
  }

  .article-title {
    font-size: 16px;
  }

  .article-meta-bottom {
    gap: 12px;
  }

  .read-time {
    margin-left: 0;
    width: 100%;
  }
}
</style>
