---
layout: default
title: "UniDiffGrasp: A Unified Framework Integrating VLM Reasoning and VLM-Guided Part Diffusion for Open-Vocabulary Constrained Grasping with Dual Arms"
---

# UniDiffGrasp: A Unified Framework Integrating VLM Reasoning and VLM-Guided Part Diffusion for Open-Vocabulary Constrained Grasping with Dual Arms

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06832" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06832v1</a>
  <a href="https://arxiv.org/pdf/2505.06832.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06832v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06832v1', 'UniDiffGrasp: A Unified Framework Integrating VLM Reasoning and VLM-Guided Part Diffusion for Open-Vocabulary Constrained Grasping with Dual Arms')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xueyang Guo, Hongwei Hu, Chengye Song, Jiale Chen, Zilin Zhao, Yu Fu, Bowen Guan, Zhenze Liu

**分类**: cs.RO

**发布日期**: 2025-05-11

**备注**: 8 pages, 5 figures

---

## 💡 一句话要点

**提出UniDiffGrasp以解决双臂开放词汇约束抓取问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `开放词汇抓取` `双臂机器人` `视觉语言模型` `部件引导扩散` `抓取生成` `任务导向` `几何约束` `高效协作`

## 📋 核心要点

1. 现有方法在开放词汇抓取中面临精确抓取生成和双臂协调的挑战，导致抓取成功率低。
2. UniDiffGrasp通过将VLM推理与部件引导扩散结合，提供了一种新的抓取生成方法，能够在不重训练的情况下实现高效抓取。
3. 在实地测试中，UniDiffGrasp在单臂和双臂任务中分别达到了0.876和0.767的抓取成功率，显著提高了抓取性能。

## 📝 摘要（中文）

开放词汇、任务导向的特定功能部件抓取，尤其是双臂抓取，仍然是一个关键挑战。现有的视觉语言模型（VLM）在增强任务理解方面表现良好，但在精确抓取生成和有效的双臂协调方面存在不足。为此，本文提出了UniDiffGrasp，一个将VLM推理与引导部件扩散相结合的统一框架。UniDiffGrasp利用VLM解释用户输入并识别语义目标，通过开放词汇分割进行定位。识别的部件为受限抓取扩散场（CGDF）提供几何约束，支持高效、高质量的六自由度抓取。通过广泛的实地部署，UniDiffGrasp在单臂和双臂场景中分别实现了0.876和0.767的抓取成功率，显著超越现有最先进的方法。

## 🔬 方法详解

**问题定义**：本文旨在解决开放词汇、任务导向的双臂抓取问题。现有的视觉语言模型在抓取生成和双臂协调方面存在不足，导致抓取成功率低下。

**核心思路**：UniDiffGrasp通过结合VLM推理与部件引导扩散，能够有效识别语义目标并生成高质量的抓取方案，特别是在双臂协作中。

**技术框架**：该框架包括用户输入的VLM解释、语义目标的开放词汇分割、部件引导扩散生成几何约束，以及针对双臂任务的稳定合作抓取选择。

**关键创新**：UniDiffGrasp的主要创新在于其受限抓取扩散场（CGDF）和部件引导扩散的结合，使得抓取生成过程更加高效且无需重训练。

**关键设计**：在设计中，UniDiffGrasp采用了特定的参数设置和损失函数，以优化抓取质量和稳定性，同时确保双臂的协调性。具体的网络结构和训练细节在论文中进行了详细描述。

## 📊 实验亮点

在实验中，UniDiffGrasp在单臂抓取任务中实现了0.876的成功率，而在双臂任务中达到了0.767，显著超越了现有的最先进方法，展示了其在复杂场景中的有效性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、工业自动化和人机协作等场景。通过实现高效的双臂抓取，UniDiffGrasp能够在复杂环境中执行多种任务，提高工作效率和安全性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Open-vocabulary, task-oriented grasping of specific functional parts, particularly with dual arms, remains a key challenge, as current Vision-Language Models (VLMs), while enhancing task understanding, often struggle with precise grasp generation within defined constraints and effective dual-arm coordination. We innovatively propose UniDiffGrasp, a unified framework integrating VLM reasoning with guided part diffusion to address these limitations. UniDiffGrasp leverages a VLM to interpret user input and identify semantic targets (object, part(s), mode), which are then grounded via open-vocabulary segmentation. Critically, the identified parts directly provide geometric constraints for a Constrained Grasp Diffusion Field (CGDF) using its Part-Guided Diffusion, enabling efficient, high-quality 6-DoF grasps without retraining. For dual-arm tasks, UniDiffGrasp defines distinct target regions, applies part-guided diffusion per arm, and selects stable cooperative grasps. Through extensive real-world deployment, UniDiffGrasp achieves grasp success rates of 0.876 in single-arm and 0.767 in dual-arm scenarios, significantly surpassing existing state-of-the-art methods, demonstrating its capability to enable precise and coordinated open-vocabulary grasping in complex real-world scenarios.

