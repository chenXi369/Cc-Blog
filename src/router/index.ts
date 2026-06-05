import { createRouter, createWebHistory } from 'vue-router'
import Layout from '@/layout/index.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: Layout,
      children: [
        {
          path: '',
          name: 'home',
          component: () => import('@/views/HomeView.vue'),
        },
        {
          path: '/tech-stack',
          name: 'tech-stack',
          component: () => import('@/views/TechStackView.vue'),
        },
        {
          path: '/articles',
          name: 'articles',
          component: () => import('@/views/ArticlesView.vue'),
        },
        {
          path: '/gallery',
          name: 'gallery',
          component: () => import('@/views/GalleryView.vue'),
        },
        {
          path: '/workspace',
          name: 'workspace',
          component: () => import('@/views/WorkspaceView.vue'),
        },
        {
          path: '/timeline',
          name: 'timeline',
          component: () => import('@/views/TimelineView.vue'),
        },
        {
          path: '/projects',
          name: 'projects',
          component: () => import('@/views/ProjectsView.vue'),
        },
        {
          path: '/todos',
          name: 'todos',
          component: () => import('@/views/TodosView.vue'),
        },
        {
          path: '/requirements',
          name: 'requirements',
          component: () => import('@/views/RequirementsView.vue'),
        },
        {
          path: '/friends',
          name: 'friends',
          component: () => import('@/views/FriendsView.vue'),
        },
      ],
    },
  ],
})

export default router
