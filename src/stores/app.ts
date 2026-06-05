import { defineStore } from 'pinia'
import { ref } from 'vue'

export interface MenuItem {
  id: number
  name: string
  icon: string
  path: string
  badge?: number
}

export interface OnlineLink {
  name: string
  icon: string
  url: string
}

export const useAppStore = defineStore('app', () => {
  const collapsed = ref(false)
  const mobileMenuOpen = ref(false)

  const menuItems = ref<MenuItem[]>([
    { id: 1, name: '首页&简介', icon: 'Home', path: '/' },
    { id: 2, name: '技术栈', icon: 'Cpu', path: '/tech-stack' },
    { id: 3, name: '技术文章', icon: 'FileText', path: '/articles' },
    { id: 4, name: '生活相册', icon: 'Image', path: '/gallery' },
    { id: 5, name: '工作空间', icon: 'Briefcase', path: '/workspace' },
    { id: 6, name: '时间笔记', icon: 'Clock', path: '/timeline' },
    { id: 7, name: '项目', icon: 'Folder', path: '/projects' },
    { id: 8, name: '待办事项', icon: 'CheckSquare', path: '/todos' },
    { id: 9, name: '项目需求', icon: 'ListTodo', path: '/requirements', badge: 11 },
    { id: 10, name: '友链', icon: 'Link', path: '/friends' },
  ])

  const onlineLinks = ref<OnlineLink[]>([
    { name: 'Github', icon: 'Github', url: 'https://github.com' },
    { name: '掘金', icon: 'BookOpen', url: 'https://juejin.cn' },
    { name: '知识库', icon: 'Database', url: '#' },
    { name: 'bilibili', icon: 'Video', url: 'https://bilibili.com' },
    { name: '推特', icon: 'Twitter', url: 'https://twitter.com' },
  ])

  const toggleCollapsed = () => {
    collapsed.value = !collapsed.value
  }

  const toggleMobileMenu = () => {
    mobileMenuOpen.value = !mobileMenuOpen.value
  }

  const closeMobileMenu = () => {
    mobileMenuOpen.value = false
  }

  return {
    collapsed,
    mobileMenuOpen,
    menuItems,
    onlineLinks,
    toggleCollapsed,
    toggleMobileMenu,
    closeMobileMenu,
  }
})
