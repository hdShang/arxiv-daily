---
layout: default
title: "FairyGen: Storied Cartoon Video from a Single Child-Drawn Character"
---

# FairyGen: Storied Cartoon Video from a Single Child-Drawn Character

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21272" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21272v2</a>
  <a href="https://arxiv.org/pdf/2506.21272.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21272v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21272v2', 'FairyGen: Storied Cartoon Video from a Single Child-Drawn Character')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiayi Zheng, Xiaodong Cun

**分类**: cs.GR, cs.CV, cs.MM

**发布日期**: 2025-06-26 (更新: 2025-06-27)

**备注**: Project Page: https://jayleejia.github.io/FairyGen/ ; Code: https://github.com/GVCLab/FairyGen

**🔗 代码/项目**: [GITHUB](https://github.com/GVCLab/FairyGen)

---

## 💡 一句话要点

**提出FairyGen以从单一儿童绘画生成故事驱动的卡通视频**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `卡通视频生成` `儿童绘画` `故事叙述` `风格一致性` `动画制作` `多模态学习` `运动定制`

## 📋 核心要点

1. 现有方法主要集中在角色一致性和基本动作上，缺乏对故事叙述的深度和视觉风格的保留。
2. FairyGen通过将角色建模与背景生成分离，并结合电影镜头设计，提升了故事叙述的表现力和连贯性。
3. 实验结果显示，FairyGen生成的动画在风格一致性和叙事结构上均优于现有基线，展示了显著的提升。

## 📝 摘要（中文）

我们提出了FairyGen，一个自动化系统，能够从单一儿童绘画生成故事驱动的卡通视频，同时忠实保留其独特的艺术风格。与以往主要关注角色一致性和基本动作的叙事方法不同，FairyGen明确将角色建模与风格化背景生成分离，并结合电影镜头设计以支持富有表现力和连贯的叙事。给定一幅角色草图，我们首先利用多模态大语言模型生成结构化的故事板，包含环境设置、角色动作和镜头视角的描述。为了确保视觉一致性，我们引入了风格传播适配器，捕捉角色的视觉风格并将其应用于背景，忠实保留角色的完整视觉身份，同时合成风格一致的场景。通过框架裁剪和基于故事板的多视图合成，镜头设计模块进一步增强了视觉多样性和电影质量。为了动画化故事，我们重建了角色的3D代理，以推导出物理上合理的运动序列，然后用于微调基于MMDiT的图像到视频扩散模型。我们还提出了两阶段的运动定制适配器：第一阶段从时间无序的帧中学习外观特征，解耦身份与运动；第二阶段使用时间步移位策略建模时间动态，冻结身份权重。一旦训练完成，FairyGen可以直接渲染与故事板对齐的多样化和连贯的视频场景。大量实验表明，我们的系统生成的动画在风格上忠实、叙事结构自然，突显了其在个性化和引人入胜的故事动画中的潜力。

## 🔬 方法详解

**问题定义**：本论文旨在解决从单一儿童绘画生成故事驱动卡通视频的挑战，现有方法在角色一致性和叙事深度方面存在不足。

**核心思路**：FairyGen的核心思路是将角色建模与背景生成明确分离，并引入电影镜头设计，以增强叙事的表现力和视觉连贯性。

**技术框架**：整体架构包括多个模块：首先利用多模态大语言模型生成结构化故事板；其次通过风格传播适配器确保角色与背景的视觉一致性；然后通过镜头设计模块增强视觉多样性；最后重建3D角色代理以生成动画。

**关键创新**：最重要的技术创新在于引入了风格传播适配器和两阶段运动定制适配器，前者确保了角色风格的保留，后者有效解耦了身份与运动，提升了动画的自然性。

**关键设计**：在技术细节上，采用了多模态大语言模型生成故事板，风格传播适配器通过捕捉角色特征进行背景合成，运动定制适配器则通过时间步移位策略建模动态，确保了动画的连贯性与多样性。

## 📊 实验亮点

实验结果表明，FairyGen在风格一致性和叙事结构上显著优于现有基线，生成的动画在视觉质量和自然运动方面有明显提升，展示出其在个性化故事动画中的巨大潜力。

## 🎯 应用场景

FairyGen的潜在应用场景包括儿童故事动画制作、个性化教育内容生成以及创意艺术项目。其能够将儿童的创意绘画转化为生动的动画，具有极大的实际价值和未来影响力，尤其在教育和娱乐领域。

## 📄 摘要（原文）

> We propose FairyGen, an automatic system for generating story-driven cartoon videos from a single child's drawing, while faithfully preserving its unique artistic style. Unlike previous storytelling methods that primarily focus on character consistency and basic motion, FairyGen explicitly disentangles character modeling from stylized background generation and incorporates cinematic shot design to support expressive and coherent storytelling. Given a single character sketch, we first employ an MLLM to generate a structured storyboard with shot-level descriptions that specify environment settings, character actions, and camera perspectives. To ensure visual consistency, we introduce a style propagation adapter that captures the character's visual style and applies it to the background, faithfully retaining the character's full visual identity while synthesizing style-consistent scenes. A shot design module further enhances visual diversity and cinematic quality through frame cropping and multi-view synthesis based on the storyboard. To animate the story, we reconstruct a 3D proxy of the character to derive physically plausible motion sequences, which are then used to fine-tune an MMDiT-based image-to-video diffusion model. We further propose a two-stage motion customization adapter: the first stage learns appearance features from temporally unordered frames, disentangling identity from motion; the second stage models temporal dynamics using a timestep-shift strategy with frozen identity weights. Once trained, FairyGen directly renders diverse and coherent video scenes aligned with the storyboard. Extensive experiments demonstrate that our system produces animations that are stylistically faithful, narratively structured natural motion, highlighting its potential for personalized and engaging story animation. The code will be available at https://github.com/GVCLab/FairyGen

