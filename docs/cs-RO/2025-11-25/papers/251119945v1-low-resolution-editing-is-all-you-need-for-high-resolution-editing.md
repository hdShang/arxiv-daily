---
layout: default
title: Low-Resolution Editing is All You Need for High-Resolution Editing
---

# Low-Resolution Editing is All You Need for High-Resolution Editing

**arXiv**: [2511.19945v1](https://arxiv.org/abs/2511.19945) | [PDF](https://arxiv.org/pdf/2511.19945.pdf)

**作者**: Junsung Lee, Hyunsoo Lee, Yong Jae Lee, Bohyung Han

---

## 💡 一句话要点

**提出高分辨率图像编辑框架，通过补丁优化和细节转移解决现有方法分辨率限制问题。**

**关键词**: `高分辨率图像编辑` `补丁优化` `细节转移` `测试时优化` `内容创建`

## 📋 核心要点

1. 核心问题：现有图像编辑方法仅支持低分辨率（如1K），无法满足高分辨率内容创建需求。
2. 方法要点：采用测试时优化、补丁级处理、细节转移模块和同步策略以保持一致性。
3. 实验或效果：广泛实验显示方法能生成高质量编辑，推动高分辨率内容创建发展。

## 📄 摘要（原文）

> High-resolution content creation is rapidly emerging as a central challenge in both the vision and graphics communities. While images serve as the most fundamental modality for visual expression, content generation that aligns with the user intent requires effective, controllable high-resolution image manipulation mechanisms. However, existing approaches remain limited to low-resolution settings, typically supporting only up to 1K resolution. In this work, we introduce the task of high-resolution image editing and propose a test-time optimization framework to address it. Our method performs patch-wise optimization on high-resolution source images, followed by a fine-grained detail transfer module and a novel synchronization strategy to maintain consistency across patches. Extensive experiments show that our method produces high-quality edits, facilitating the way toward high-resolution content creation.

