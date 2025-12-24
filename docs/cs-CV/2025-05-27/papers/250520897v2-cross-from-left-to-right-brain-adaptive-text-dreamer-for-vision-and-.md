---
layout: default
title: Cross from Left to Right Brain: Adaptive Text Dreamer for Vision-and-Language Navigation
---

# Cross from Left to Right Brain: Adaptive Text Dreamer for Vision-and-Language Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20897" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20897v2</a>
  <a href="https://arxiv.org/pdf/2505.20897.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20897v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20897v2', 'Cross from Left to Right Brain: Adaptive Text Dreamer for Vision-and-Language Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pingrui Zhang, Yifei Su, Pengyuan Wu, Dong An, Li Zhang, Zhigang Wang, Dong Wang, Yan Ding, Bin Zhao, Xuelong Li

**分类**: cs.CV, cs.AI, cs.CL, cs.RO

**发布日期**: 2025-05-27 (更新: 2025-06-22)

**🔗 代码/项目**: [GITHUB](https://github.com/zhangpingrui/Adaptive-Text-Dreamer)

---

## 💡 一句话要点

**提出自适应文本梦境生成器以解决视觉与语言导航问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉与语言导航` `自适应文本生成` `多模态学习` `逻辑推理` `场景想象` `深度学习` `智能导航`

## 📋 核心要点

1. 现有视觉与语言导航方法依赖于视觉合成，导致高计算成本和冗余细节，难以有效对齐感知与语言。
2. 本文提出的自适应文本梦境生成器（ATD）通过语言形式自适应想象环境语义，结合逻辑推理与想象预测。
3. 在R2R基准上，ATD实现了最先进的性能，且参数量更少，展示了其高效性和可靠性。

## 📝 摘要（中文）

视觉与语言导航（VLN）要求智能体在部分可观测的环境中根据自然语言指令进行导航，这使得感知与语言的对齐变得困难。近期的方法通过想象未来场景来缓解这一问题，但依赖于基于视觉的合成，导致计算成本高且细节冗余。为此，本文提出了一种自适应文本梦境生成器（ATD），通过语言形式自适应地想象关键环境语义，从而实现更可靠和高效的策略。ATD采用人类左脑-右脑架构，左脑专注于逻辑整合，右脑负责未来场景的想象预测。我们在R2R基准上进行了广泛实验，ATD以更少的参数实现了最先进的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉与语言导航中感知与语言对齐的困难，现有方法在想象未来场景时存在高计算成本和细节冗余的问题。

**核心思路**：提出自适应文本梦境生成器（ATD），通过语言形式自适应地想象关键环境语义，采用左脑-右脑架构，左脑负责逻辑整合，右脑进行未来场景的想象预测。

**技术框架**：ATD的整体架构包括两个主要分支：左脑分支专注于逻辑推理，右脑分支进行场景想象。通过对Q-former进行微调，激活领域特定知识，实现逻辑推理和想象的动态更新。

**关键创新**：ATD的创新在于其双分支自我引导的想象策略，结合了大型语言模型的推理能力与导航模型的专业知识，形成了有效的交互机制。

**关键设计**：在设计中，ATD通过微调Q-former来实现高效的知识激活，并引入交互机制以规范化想象输出，确保其与导航专家模块的有效结合。

## 📊 实验亮点

在R2R基准上，ATD实现了最先进的性能，参数量显著低于现有方法，展示了在视觉与语言导航任务中的高效性，具体性能数据未提供。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人导航、虚拟助手以及增强现实等场景，能够提升智能体在复杂环境中的自主导航能力。未来，ATD的设计理念可扩展至其他多模态任务，推动人机交互的进一步发展。

## 📄 摘要（原文）

> Vision-and-Language Navigation (VLN) requires the agent to navigate by following natural instructions under partial observability, making it difficult to align perception with language. Recent methods mitigate this by imagining future scenes, yet they rely on vision-based synthesis, leading to high computational cost and redundant details. To this end, we propose to adaptively imagine key environmental semantics via \textit{language} form, enabling a more reliable and efficient strategy. Specifically, we introduce a novel Adaptive Text Dreamer (ATD), a dual-branch self-guided imagination policy built upon a large language model (LLM). ATD is designed with a human-like left-right brain architecture, where the left brain focuses on logical integration, and the right brain is responsible for imaginative prediction of future scenes. To achieve this, we fine-tune only the Q-former within both brains to efficiently activate domain-specific knowledge in the LLM, enabling dynamic updates of logical reasoning and imagination during navigation. Furthermore, we introduce a cross-interaction mechanism to regularize the imagined outputs and inject them into a navigation expert module, allowing ATD to jointly exploit both the reasoning capacity of the LLM and the expertise of the navigation model. We conduct extensive experiments on the R2R benchmark, where ATD achieves state-of-the-art performance with fewer parameters. The code is \href{https://github.com/zhangpingrui/Adaptive-Text-Dreamer}{here}.

