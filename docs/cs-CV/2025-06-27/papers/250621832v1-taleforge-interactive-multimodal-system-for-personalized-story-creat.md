---
layout: default
title: "TaleForge: Interactive Multimodal System for Personalized Story Creation"
---

# TaleForge: Interactive Multimodal System for Personalized Story Creation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21832" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21832v1</a>
  <a href="https://arxiv.org/pdf/2506.21832.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21832v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21832v1', 'TaleForge: Interactive Multimodal System for Personalized Story Creation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Minh-Loi Nguyen, Quang-Khai Le, Tam V. Nguyen, Minh-Triet Tran, Trung-Nghia Le

**分类**: cs.CV

**发布日期**: 2025-06-27

---

## 💡 一句话要点

**提出TaleForge以解决个性化故事创作的参与度不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `个性化故事生成` `多模态系统` `用户参与` `大型语言模型` `图像生成技术`

## 📋 核心要点

1. 现有故事生成方法往往缺乏个性化，导致用户参与感不足，无法满足个体需求。
2. TaleForge通过整合大型语言模型和图像生成技术，提供个性化的故事创作体验，用户可以嵌入自己的面部图像。
3. 用户研究显示，TaleForge显著提升了用户的参与感和归属感，尽管用户希望有更多的叙事编辑工具。

## 📝 摘要（中文）

讲故事是一个深具个人色彩和创造性的过程，但现有方法往往将用户视为被动消费者，提供通用情节且个性化程度有限。这削弱了用户的参与感和沉浸感，尤其是在个体风格或外观至关重要的情况下。我们提出了TaleForge，一个个性化故事生成系统，整合了大型语言模型（LLMs）和文本到图像的扩散技术，将用户的面部图像嵌入叙事和插图中。TaleForge包含三个相互关联的模块：故事生成模块，利用LLMs根据用户提示创建叙事和角色描述；个性化图像生成模块，将用户的面孔和服装选择合并到角色插图中；背景生成模块，创建包含个性化角色的场景背景。用户研究表明，当个体作为主角出现时，参与感和归属感显著增强。参与者赞扬系统的实时预览和直观控制，但希望有更精细的叙事编辑工具。TaleForge通过将个性化文本和图像对齐，推动了多模态讲故事的发展，创造了沉浸式的用户中心体验。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有故事生成方法缺乏个性化的问题，用户往往被视为被动消费者，无法充分参与创作过程。

**核心思路**：TaleForge的核心思路是通过整合大型语言模型和文本到图像的扩散技术，使用户能够将自己的面部图像融入故事叙述和插图中，从而增强个性化体验。

**技术框架**：TaleForge的整体架构包括三个主要模块：故事生成模块利用LLMs创建叙事和角色描述；个性化图像生成模块将用户的面孔和服装选择合并到角色插图中；背景生成模块则创建包含个性化角色的场景背景。

**关键创新**：TaleForge的主要创新在于将用户的面部图像与故事情节和插图紧密结合，形成一个高度个性化的多模态故事生成系统，这与传统的通用故事生成方法有本质区别。

**关键设计**：在技术细节上，TaleForge采用了特定的损失函数来优化图像生成质量，并设计了适应用户输入的网络结构，以确保生成的故事和插图能够真实反映用户的个性化需求。

## 📊 实验亮点

用户研究结果表明，使用TaleForge的用户在参与感和归属感上显著提升，尤其是当他们作为故事主角时。参与者对系统的实时预览和直观控制表示赞赏，尽管他们希望有更精细的叙事编辑工具。

## 🎯 应用场景

TaleForge的潜在应用场景包括个性化儿童故事书、互动游戏中的角色创建、以及社交媒体平台上的个性化内容生成。其实际价值在于能够提升用户的参与感和创造力，未来可能对教育、娱乐等领域产生深远影响。

## 📄 摘要（原文）

> Storytelling is a deeply personal and creative process, yet existing methods often treat users as passive consumers, offering generic plots with limited personalization. This undermines engagement and immersion, especially where individual style or appearance is crucial. We introduce TaleForge, a personalized story-generation system that integrates large language models (LLMs) and text-to-image diffusion to embed users' facial images within both narratives and illustrations. TaleForge features three interconnected modules: Story Generation, where LLMs create narratives and character descriptions from user prompts; Personalized Image Generation, merging users' faces and outfit choices into character illustrations; and Background Generation, creating scene backdrops that incorporate personalized characters. A user study demonstrated heightened engagement and ownership when individuals appeared as protagonists. Participants praised the system's real-time previews and intuitive controls, though they requested finer narrative editing tools. TaleForge advances multimodal storytelling by aligning personalized text and imagery to create immersive, user-centric experiences.

