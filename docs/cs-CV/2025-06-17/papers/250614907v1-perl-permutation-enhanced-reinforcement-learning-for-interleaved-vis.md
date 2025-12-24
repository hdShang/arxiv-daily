---
layout: default
title: "PeRL: Permutation-Enhanced Reinforcement Learning for Interleaved Vision-Language Reasoning"
---

# PeRL: Permutation-Enhanced Reinforcement Learning for Interleaved Vision-Language Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14907" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14907v1</a>
  <a href="https://arxiv.org/pdf/2506.14907.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14907v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14907v1', 'PeRL: Permutation-Enhanced Reinforcement Learning for Interleaved Vision-Language Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yizhen Zhang, Yang Ding, Shuoshuo Zhang, Xinchen Zhang, Haoling Li, Zhong-zhi Li, Peijie Wang, Jie Wu, Lei Ji, Yelong Shen, Yujiu Yang, Yeyun Gong

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-17

---

## 💡 一句话要点

**提出PeRL以解决多图像推理中的空间关系理解问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `强化学习` `视觉-语言模型` `空间关系理解` `图像序列排列` `回滚过滤机制` `学习效率` `复杂场景`

## 📋 核心要点

1. 现有多模态强化学习方法主要局限于单图像的空间推理，难以处理多图像间的复杂关系。
2. 本文提出PeRL方法，通过引入图像序列的排列和回滚过滤机制，增强多模态任务的学习效率。
3. 实验结果显示，PeRL在5个多图像基准测试中显著优于现有基线，且在单图像任务中表现相当。

## 📝 摘要（中文）

受DeepSeek-R1等强化学习方法展示出的推理能力启发，近期研究开始探索利用强化学习增强视觉-语言模型（VLM）在多模态推理任务中的表现。然而，现有的多模态强化学习方法主要局限于单图像的空间推理，难以推广到涉及多图像位置推理的复杂现实场景。为此，本文提出了一种针对交错多模态任务的通用强化学习方法PeRL，并设计了多阶段策略以增强探索与利用的平衡，从而提高学习效率和任务表现。具体而言，我们引入图像序列的排列以模拟不同的空间关系，探索更多的空间和位置多样性。此外，我们设计了一种回滚过滤机制，重新采样以聚焦于对学习最优行为贡献最大的轨迹。实验结果表明，PeRL模型在多图像基准测试中表现优异，超越了相关基线，同时在单图像任务中保持了相当的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态强化学习方法在处理多图像位置推理时的局限性，尤其是在复杂场景中理解图像间关系的挑战。

**核心思路**：提出PeRL方法，通过引入图像序列的排列来模拟不同的空间关系，从而增强模型的空间和位置多样性，提升推理能力。

**技术框架**：PeRL的整体架构包括多个阶段，首先通过排列图像序列进行多样性探索，然后应用回滚过滤机制对轨迹进行重新采样，聚焦于最优行为的学习。

**关键创新**：最重要的创新在于引入图像序列的排列机制和回滚过滤策略，这与现有方法的单一空间推理方式形成鲜明对比，显著提升了多模态推理的能力。

**关键设计**：在参数设置上，PeRL采用了多阶段策略以优化探索与利用的平衡，损失函数设计上则注重对最优行为的强化学习，网络结构上结合了图像序列的排列与过滤机制。

## 📊 实验亮点

实验结果表明，PeRL模型在5个多图像基准测试中表现优异，超越了R1相关和交错VLM基线，达到了最先进的性能，提升幅度显著。同时，在3个单图像基准测试中保持了相当的性能。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、图像检索、以及多模态交互等场景。通过提升多图像推理能力，PeRL能够在复杂的现实任务中提供更准确的推理结果，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Inspired by the impressive reasoning capabilities demonstrated by reinforcement learning approaches like DeepSeek-R1, recent emerging research has begun exploring the use of reinforcement learning (RL) to enhance vision-language models (VLMs) for multimodal reasoning tasks. However, most existing multimodal reinforcement learning approaches remain limited to spatial reasoning within single-image contexts, yet still struggle to generalize to more complex and real-world scenarios involving multi-image positional reasoning, where understanding the relationships across images is crucial. To address this challenge, we propose a general reinforcement learning approach PeRL tailored for interleaved multimodal tasks, and a multi-stage strategy designed to enhance the exploration-exploitation trade-off, thereby improving learning efficiency and task performance. Specifically, we introduce permutation of image sequences to simulate varied positional relationships to explore more spatial and positional diversity. Furthermore, we design a rollout filtering mechanism for resampling to focus on trajectories that contribute most to learning optimal behaviors to exploit learned policies effectively. We evaluate our model on 5 widely-used multi-image benchmarks and 3 single-image benchmarks. Our experiments confirm that PeRL trained model consistently surpasses R1-related and interleaved VLM baselines by a large margin, achieving state-of-the-art performance on multi-image benchmarks, while preserving comparable performance on single-image tasks.

