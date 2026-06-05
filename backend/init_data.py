from database import SessionLocal, engine
import models


def init_db():
    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    # Articles
    if db.query(models.Article).count() == 0:
        articles = [
            models.Article(title="Vue3 性能优化实践指南", summary="从实际项目出发，深入探讨 Vue3 应用的性能优化策略", tags="Vue.js,性能优化,前端", views=2340, likes=156, comments=32, date="2024-01-15", read_time="12分钟"),
            models.Article(title="基于 Canvas 的编辑器架构设计", summary="探讨如何构建高性能的 Canvas 编辑器", tags="Canvas,编辑器,架构", views=1890, likes=128, comments=24, date="2024-01-10", read_time="15分钟"),
            models.Article(title="TypeScript 高级类型编程", summary="深入 TypeScript 类型系统，掌握高级特性", tags="TypeScript,类型系统", views=3200, likes=210, comments=45, date="2024-01-05", read_time="18分钟"),
            models.Article(title="AI 辅助编程工具对比评测", summary="对比 Cursor、GitHub Copilot 等主流 AI 编程助手", tags="AI,工具,效率", views=4560, likes=312, comments=67, date="2023-12-28", read_time="10分钟"),
        ]
        db.add_all(articles)

    # Photos
    if db.query(models.Photo).count() == 0:
        photos = [
            models.Photo(url="https://picsum.photos/400/300?random=1", title="山间晨雾", description="清晨的山间，云雾缭绕", likes=128, comments=12, date="2024-01-15"),
            models.Photo(url="https://picsum.photos/400/500?random=2", title="城市夜景", description="繁华都市的璀璨灯火", likes=256, comments=24, date="2024-01-10"),
            models.Photo(url="https://picsum.photos/400/300?random=3", title="海边日落", description="金色的夕阳洒在海面上", likes=189, comments=18, date="2024-01-05"),
            models.Photo(url="https://picsum.photos/400/400?random=4", title="樱花盛开", description="春天的粉色浪漫", likes=312, comments=32, date="2023-12-28"),
        ]
        db.add_all(photos)

    # Timeline
    if db.query(models.TimelineEvent).count() == 0:
        events = [
            models.TimelineEvent(date="2024-01-15", title="发布 Vue3 性能优化文章", description="总结了在实际项目中遇到的性能问题及解决方案", type="article"),
            models.TimelineEvent(date="2024-01-10", title="完成编辑器核心模块", description="基于 Canvas 的编辑器架构设计完成", type="project"),
            models.TimelineEvent(date="2024-01-01", title="2024 新年目标", description="计划学习 WebGL 和 AI 相关知识", type="milestone"),
            models.TimelineEvent(date="2023-12-20", title="学习 TypeScript 高级类型", description="深入理解了条件类型和映射类型", type="learning"),
        ]
        db.add_all(events)

    # Projects
    if db.query(models.Project).count() == 0:
        projects = [
            models.Project(name="Vue3 Blog", description="基于 Vue3 的个人博客系统", tech_stack="Vue3,TypeScript,Vite", stars=128, forks=32, url="https://github.com", demo_url="#", status="active"),
            models.Project(name="Canvas Editor", description="基于 Canvas 的图形编辑器", tech_stack="Canvas,TypeScript,Webpack", stars=256, forks=48, url="https://github.com", status="active"),
            models.Project(name="AI Chat Tool", description="集成 OpenAI API 的智能聊天工具", tech_stack="React,Node.js,OpenAI", stars=89, forks=15, url="https://github.com", status="completed"),
        ]
        db.add_all(projects)

    # Todos
    if db.query(models.Todo).count() == 0:
        todos = [
            models.Todo(title="完成 Vue3 博客项目", completed=False, priority="high", due_date="2024-01-20", category="项目"),
            models.Todo(title="学习 WebGL 基础", completed=False, priority="medium", due_date="2024-01-25", category="学习"),
            models.Todo(title="优化编辑器性能", completed=True, priority="high", due_date="2024-01-15", category="项目"),
            models.Todo(title="整理技术笔记", completed=False, priority="low", due_date="2024-01-30", category="文档"),
        ]
        db.add_all(todos)

    # Requirements
    if db.query(models.Requirement).count() == 0:
        reqs = [
            models.Requirement(title="CodeMirror的使用、数据结构配合网站设置中的数据", status="completed", priority="high", category="工作", date="12月31日", tech_stack="React,TS,skia & canvasKit", difficulty="有难点", description="图形学、节点树、从0-1、属性工具条", tags="编辑,方案,反思,开始,删除"),
            models.Requirement(title="编辑器核心架构设计与实现", status="completed", priority="high", category="工作", date="12月31日", tech_stack="React,TS,webpack,pnpm,skia & canvasKit", difficulty="有难点", description="图形学、编辑器、skia & canvasKit", tags="编辑,方案,反思,开始,删除"),
        ]
        db.add_all(reqs)

    # Friends
    if db.query(models.Friend).count() == 0:
        friends = [
            models.Friend(name="张三的博客", avatar="Z", description="全栈开发者，专注于 Node.js 和 Vue 生态", url="https://example.com", tags="全栈,Node.js"),
            models.Friend(name="李四的技术笔记", avatar="L", description="前端架构师，分享 React 和工程化实践", url="https://example.com", tags="React,架构"),
            models.Friend(name="王五的编程随想", avatar="W", description="独立开发者，探索 AI 与前端结合", url="https://example.com", tags="AI,独立开发"),
        ]
        db.add_all(friends)

    # Tech Categories & Items
    if db.query(models.TechCategory).count() == 0:
        cat1 = models.TechCategory(name="前端框架")
        cat2 = models.TechCategory(name="构建工具")
        db.add_all([cat1, cat2])
        db.flush()

        items = [
            models.TechItem(name="Vue.js", icon="V", proficiency=95, description="熟练掌握 Vue3 Composition API", category_id=cat1.id),
            models.TechItem(name="React", icon="R", proficiency=90, description="Hooks、Next.js 生态", category_id=cat1.id),
            models.TechItem(name="TypeScript", icon="TS", proficiency=92, description="类型系统、泛型编程", category_id=cat1.id),
            models.TechItem(name="Vite", icon="V", proficiency=88, description="快速构建、HMR", category_id=cat2.id),
            models.TechItem(name="Webpack", icon="W", proficiency=85, description="配置优化、Loader 开发", category_id=cat2.id),
        ]
        db.add_all(items)

    # Activities
    if db.query(models.Activity).count() == 0:
        activities = [
            models.Activity(content="发布了文章《Vue3 性能优化实践》", time_text="2小时前", type="article"),
            models.Activity(content="完成了项目需求 #11", time_text="昨天", type="requirement"),
            models.Activity(content="更新了技术栈页面", time_text="3天前", type="tech-stack"),
        ]
        db.add_all(activities)

    db.commit()
    db.close()
    print("Database initialized with sample data.")


if __name__ == "__main__":
    init_db()
