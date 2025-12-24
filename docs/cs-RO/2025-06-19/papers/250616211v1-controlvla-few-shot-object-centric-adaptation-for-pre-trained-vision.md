---
layout: default
title: "ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models"
---

# ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16211" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16211v1</a>
  <a href="https://arxiv.org/pdf/2506.16211.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16211v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16211v1', 'ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Puhao Li, Yingying Wu, Ziheng Xi, Wanlin Li, Yuzhe Huang, Zhiyuan Zhang, Yinghan Chen, Jianan Wang, Song-Chun Zhu, Tengyu Liu, Siyuan Huang

**分类**: cs.RO

**发布日期**: 2025-06-19

**备注**: Website: https://controlvla.github.io

---

## 💡 一句话要点

**提出ControlVLA以解决少量示例下的机器人操作适应问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `少量示例学习` `机器人操作` `视觉-语言-动作` `对象中心表示` `微调技术` `ControlNet`

## 📋 核心要点

1. 现有的少量示例机器人操作方法在模拟与现实之间存在显著差距，且缺乏对特定任务的适应能力。
2. ControlVLA通过零初始化投影层，将预训练的操作策略与对象中心表示相结合，实现高效的微调。
3. 在六个不同的真实任务中，ControlVLA在仅需10-20个示例的情况下达到了76.7%的成功率，显著提升了操作效率。

## 📝 摘要（中文）

学习现实世界的机器人操作具有挑战性，尤其是在可用示例有限的情况下。现有的少量示例操作方法通常依赖于模拟增强数据或预构建模块，如抓取和姿态估计，这些方法在模拟与现实之间存在差距且缺乏扩展性。尽管大规模模仿预训练显示出潜力，但在数据稀缺的环境中将这些通用策略适应于特定任务仍未被充分探索。为此，我们提出了ControlVLA，一个通过ControlNet风格架构将预训练的视觉-语言-动作模型与以对象为中心的表示相结合的框架，以实现高效的微调。在六个不同任务的真实实验中，我们的方法在仅需10-20个示例的情况下实现了76.7%的成功率，显著优于传统方法所需的100多个示例。额外实验表明ControlVLA在长时间任务中的扩展性和对未见对象及背景的鲁棒性。

## 🔬 方法详解

**问题定义**：本论文旨在解决在有限示例下，如何有效地将预训练的视觉-语言-动作模型适应于特定的机器人操作任务。现有方法往往依赖于大量示例，导致在数据稀缺情况下的适应性不足。

**核心思路**：ControlVLA的核心思想是通过零初始化一组投影层，使其能够逐步适应预训练的操作策略，从而引入对象中心条件而不覆盖已有知识。这种设计旨在提高模型在少量示例下的适应能力。

**技术框架**：ControlVLA采用ControlNet风格的架构，主要包括预训练的视觉-语言-动作模型和对象中心表示的结合。该框架通过逐步微调投影层，实现对特定任务的适应。

**关键创新**：ControlVLA的最大创新在于其零初始化的投影层设计，使得模型能够在不丢失预训练知识的情况下，灵活适应新的操作任务。这与传统方法的直接重训练方式形成了明显对比。

**关键设计**：在技术细节上，ControlVLA的投影层采用了特定的损失函数和网络结构，以确保在微调过程中能够有效捕捉对象特征，并保持对预训练策略的依赖。

## 📊 实验亮点

在六个不同的真实任务中，ControlVLA在仅需10-20个示例的情况下实现了76.7%的成功率，相较于传统方法所需的100多个示例，提升幅度显著。这一结果展示了ControlVLA在少量示例学习中的有效性和实用性。

## 🎯 应用场景

ControlVLA的研究成果在机器人操作、智能家居、自动化生产等领域具有广泛的应用潜力。通过减少对示例的依赖，该方法能够加速机器人在新环境中的学习和适应，提升其在复杂任务中的操作能力，未来可能推动更智能的机器人系统的发展。

## 📄 摘要（原文）

> Learning real-world robotic manipulation is challenging, particularly when limited demonstrations are available. Existing methods for few-shot manipulation often rely on simulation-augmented data or pre-built modules like grasping and pose estimation, which struggle with sim-to-real gaps and lack extensibility. While large-scale imitation pre-training shows promise, adapting these general-purpose policies to specific tasks in data-scarce settings remains unexplored. To achieve this, we propose ControlVLA, a novel framework that bridges pre-trained VLA models with object-centric representations via a ControlNet-style architecture for efficient fine-tuning. Specifically, to introduce object-centric conditions without overwriting prior knowledge, ControlVLA zero-initializes a set of projection layers, allowing them to gradually adapt the pre-trained manipulation policies. In real-world experiments across 6 diverse tasks, including pouring cubes and folding clothes, our method achieves a 76.7% success rate while requiring only 10-20 demonstrations -- a significant improvement over traditional approaches that require more than 100 demonstrations to achieve comparable success. Additional experiments highlight ControlVLA's extensibility to long-horizon tasks and robustness to unseen objects and backgrounds.

