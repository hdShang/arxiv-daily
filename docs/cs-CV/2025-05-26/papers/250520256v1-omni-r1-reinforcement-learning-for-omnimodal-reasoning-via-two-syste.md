---
layout: default
title: Omni-R1: Reinforcement Learning for Omnimodal Reasoning via Two-System Collaboration
---

# Omni-R1: Reinforcement Learning for Omnimodal Reasoning via Two-System Collaboration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20256" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20256v1</a>
  <a href="https://arxiv.org/pdf/2505.20256.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20256v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20256v1', 'Omni-R1: Reinforcement Learning for Omnimodal Reasoning via Two-System Collaboration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Zhong, Muzhi Zhu, Zongze Du, Zheng Huang, Canyu Zhao, Mingyu Liu, Wen Wang, Hao Chen, Chunhua Shen

**分类**: cs.CV

**发布日期**: 2025-05-26

**备注**: Project page: https://aim-uofa.github.io/OmniR1

---

## 💡 一句话要点

**提出Omni-R1以解决长视频音频推理与细粒度像素理解的矛盾问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长视频理解` `音频推理` `细粒度像素理解` `强化学习` `多模态模型` `关键帧选择` `层次奖励机制`

## 📋 核心要点

1. 现有方法在长视频音频推理与细粒度像素理解之间存在矛盾，难以同时满足低分辨率和高分辨率的需求。
2. 论文提出的Omni-R1通过双系统架构，利用强化学习优化关键帧选择和任务重写，解决了这一矛盾。
3. 实验结果显示，Omni-R1在多个基准测试中超越了现有的监督和专门模型，提升了模型的泛化能力。

## 📝 摘要（中文）

长时间的视频音频推理与细粒度像素理解对全模态模型提出了相互矛盾的要求：密集的时间覆盖需要许多低分辨率帧，而精确的定位则需要高分辨率输入。为了解决这一权衡，本文提出了一种双系统架构：全球推理系统选择信息丰富的关键帧并以低空间成本重写任务，而细节理解系统则在选定的高分辨率片段上执行像素级的定位。由于“最佳”关键帧选择和重构模糊且难以监督，本文将其形式化为强化学习问题，并提出了Omni-R1，一个基于组相对策略优化的端到端强化学习框架。实验结果表明，Omni-R1在RefAVS和REVOS两个基准上超越了强大的监督基线，并在领域外泛化和多模态幻觉的缓解方面显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决长视频音频推理与细粒度像素理解之间的矛盾，现有方法在处理低分辨率和高分辨率输入时存在局限性，难以同时满足两者的需求。

**核心思路**：论文提出的Omni-R1采用双系统架构，全球推理系统负责选择关键帧并重写任务，而细节理解系统则在高分辨率片段上进行像素级定位，通过强化学习优化关键帧选择和任务重写。

**技术框架**：Omni-R1的整体架构分为两个主要模块：全球推理系统和细节理解系统。全球推理系统通过低空间成本选择关键帧，细节理解系统则在这些关键帧上进行高精度的像素级分析。

**关键创新**：Omni-R1首次将强化学习应用于大规模全模态推理，利用在线协作的层次奖励训练全球推理系统，显著提升了模型的性能和泛化能力。

**关键设计**：在参数设置上，Omni-R1采用了组相对策略优化方法，损失函数设计上结合了层次奖励机制，确保了在小任务分割上仅需一轮强化学习即可完成训练。

## 📊 实验亮点

在RefAVS和REVOS两个基准测试中，Omni-R1不仅超越了强大的监督基线，还在多个专门模型上取得了更好的性能，显著提升了领域外的泛化能力，减少了多模态幻觉现象。

## 🎯 应用场景

该研究的潜在应用领域包括视频监控、自动驾驶、智能家居等场景，能够有效提升系统在复杂环境下的理解和决策能力。未来，Omni-R1有望为多模态基础模型的发展提供新的思路，推动更广泛的应用落地。

## 📄 摘要（原文）

> Long-horizon video-audio reasoning and fine-grained pixel understanding impose conflicting requirements on omnimodal models: dense temporal coverage demands many low-resolution frames, whereas precise grounding calls for high-resolution inputs. We tackle this trade-off with a two-system architecture: a Global Reasoning System selects informative keyframes and rewrites the task at low spatial cost, while a Detail Understanding System performs pixel-level grounding on the selected high-resolution snippets. Because ``optimal'' keyframe selection and reformulation are ambiguous and hard to supervise, we formulate them as a reinforcement learning (RL) problem and present Omni-R1, an end-to-end RL framework built on Group Relative Policy Optimization. Omni-R1 trains the Global Reasoning System through hierarchical rewards obtained via online collaboration with the Detail Understanding System, requiring only one epoch of RL on small task splits.
>   Experiments on two challenging benchmarks, namely Referring Audio-Visual Segmentation (RefAVS) and Reasoning Video Object Segmentation (REVOS), show that Omni-R1 not only surpasses strong supervised baselines but also outperforms specialized state-of-the-art models, while substantially improving out-of-domain generalization and mitigating multimodal hallucination. Our results demonstrate the first successful application of RL to large-scale omnimodal reasoning and highlight a scalable path toward universally foundation models.

