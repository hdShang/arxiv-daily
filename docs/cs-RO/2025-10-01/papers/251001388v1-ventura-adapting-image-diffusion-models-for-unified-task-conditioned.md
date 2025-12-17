---
layout: default
title: VENTURA: Adapting Image Diffusion Models for Unified Task Conditioned Navigation
---

# VENTURA: Adapting Image Diffusion Models for Unified Task Conditioned Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.01388" class="toolbar-btn" target="_blank">📄 arXiv: 2510.01388v1</a>
  <a href="https://arxiv.org/pdf/2510.01388.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01388v1" onclick="toggleFavorite(this, '2510.01388v1', 'VENTURA: Adapting Image Diffusion Models for Unified Task Conditioned Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arthur Zhang, Xiangyun Meng, Luca Calliari, Dong-Ki Kim, Shayegan Omidshafiei, Joydeep Biswas, Ali Agha, Amirreza Shaban

**分类**: cs.RO, cs.CV

**发布日期**: 2025-10-01

**备注**: 9 pages, 6 figures, 3 tables

---

## 💡 一句话要点

**提出VENTURA以解决机器人导航任务中的适应性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言模型` `路径规划` `机器人导航` `图像扩散模型` `行为克隆` `自监督学习` `任务适应性`

## 📋 核心要点

1. 现有的视觉-语言模型在导航任务中难以应用，主要由于行动空间和预训练目标的差异，导致模型的迁移能力不足。
2. VENTURA通过微调图像扩散模型生成路径掩码，结合轻量级行为克隆策略，将视觉计划转化为可执行轨迹，能够更好地执行自然语言指令。
3. 在实际评估中，VENTURA在多个任务上表现优异，成功率提高33%，碰撞率降低54%，并展现出对未见任务组合的良好泛化能力。

## 📝 摘要（中文）

机器人必须适应多样的人类指令，并在非结构化的开放世界环境中安全操作。近期的视觉-语言模型（VLMs）为语言和感知的结合提供了强有力的先验知识，但由于行动空间和预训练目标的差异，导致其在导航任务中的应用受到限制。为了解决这一问题，本文提出了VENTURA，一个通过微调互联网预训练的图像扩散模型进行路径规划的视觉-语言导航系统。VENTURA生成路径掩码（即视觉计划），并通过轻量级的行为克隆策略将这些视觉计划转化为可执行的轨迹。实验结果表明，VENTURA在物体到达、障碍物规避和地形偏好任务中超越了现有的基础模型基线，成功率提高了33%，碰撞率降低了54%。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人在复杂环境中执行导航任务时的适应性问题。现有方法在行动空间和预训练目标上存在差异，导致难以有效迁移到机器人任务中。

**核心思路**：VENTURA的核心思路是通过生成路径掩码来捕捉细粒度的上下文感知导航行为，而不是直接预测低级动作。这种方法使得机器人能够更自然地遵循人类指令。

**技术框架**：VENTURA的整体架构包括图像扩散模型的微调、路径掩码的生成和轻量级行为克隆策略的应用。首先，模型生成路径掩码，然后通过行为克隆将其转化为可执行的轨迹。

**关键创新**：VENTURA的主要创新在于其路径掩码生成机制，这与传统的直接动作预测方法有本质区别。通过这种方式，模型能够更好地理解和执行复杂的导航任务。

**关键设计**：在设计中，VENTURA使用自监督跟踪模型生成路径掩码，并结合VLM增强的描述进行监督，避免了手动像素级标注的需求。

## 📊 实验亮点

VENTURA在实际评估中表现出色，成功率提高了33%，碰撞率降低了54%。与现有基础模型相比，VENTURA在物体到达、障碍物规避和地形偏好任务上均取得了显著的性能提升，展现了良好的泛化能力。

## 🎯 应用场景

VENTURA的研究成果在机器人导航、智能家居、无人驾驶等领域具有广泛的应用潜力。通过提高机器人对人类指令的理解能力，能够实现更智能的交互和自主决策，推动智能机器人技术的发展。

## 📄 摘要（原文）

> Robots must adapt to diverse human instructions and operate safely in unstructured, open-world environments. Recent Vision-Language models (VLMs) offer strong priors for grounding language and perception, but remain difficult to steer for navigation due to differences in action spaces and pretraining objectives that hamper transferability to robotics tasks. Towards addressing this, we introduce VENTURA, a vision-language navigation system that finetunes internet-pretrained image diffusion models for path planning. Instead of directly predicting low-level actions, VENTURA generates a path mask (i.e. a visual plan) in image space that captures fine-grained, context-aware navigation behaviors. A lightweight behavior-cloning policy grounds these visual plans into executable trajectories, yielding an interface that follows natural language instructions to generate diverse robot behaviors. To scale training, we supervise on path masks derived from self-supervised tracking models paired with VLM-augmented captions, avoiding manual pixel-level annotation or highly engineered data collection setups. In extensive real-world evaluations, VENTURA outperforms state-of-the-art foundation model baselines on object reaching, obstacle avoidance, and terrain preference tasks, improving success rates by 33% and reducing collisions by 54% across both seen and unseen scenarios. Notably, we find that VENTURA generalizes to unseen combinations of distinct tasks, revealing emergent compositional capabilities. Videos, code, and additional materials: https://venturapath.github.io

