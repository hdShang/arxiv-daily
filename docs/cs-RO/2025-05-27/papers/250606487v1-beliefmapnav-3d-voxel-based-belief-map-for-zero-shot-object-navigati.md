---
layout: default
title: "BeliefMapNav: 3D Voxel-Based Belief Map for Zero-Shot Object Navigation"
---

# BeliefMapNav: 3D Voxel-Based Belief Map for Zero-Shot Object Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06487" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06487v1</a>
  <a href="https://arxiv.org/pdf/2506.06487.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06487v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06487v1', 'BeliefMapNav: 3D Voxel-Based Belief Map for Zero-Shot Object Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zibo Zhou, Yue Hu, Lingkai Zhang, Zonglin Li, Siheng Chen

**分类**: cs.RO

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出BeliefMapNav以解决零-shot物体导航问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `零-shot导航` `3D体素` `信念图` `语义推理` `路径规划` `机器人导航` `视觉-语言模型`

## 📋 核心要点

1. 现有的零-shot物体导航方法在空间推理和全局环境理解方面存在不足，导致导航效率低下。
2. 本文提出了一种基于3D体素的信念图，通过整合语义先验和实时观察，构建目标位置的全局后验信念。
3. 实验结果显示，BeliefMapNav在多个基准测试中取得了最先进的性能，显著提升了导航成功率和效率。

## 📝 摘要（中文）

零-shot物体导航（ZSON）使机器人能够在不熟悉的环境中根据自然语言指令找到目标物体，而无需依赖预构建的地图或特定任务的训练。现有的通用模型，如大型语言模型（LLMs）和视觉-语言模型（VLMs），虽然赋予了代理语义推理能力，但在环境的全局理解和空间推理方面存在局限。为了解决这些问题，本文提出了一种新颖的基于3D体素的信念图，能够在体素化的3D空间中估计目标的先验存在分布。基于这一信念图，我们引入了BeliefMapNav，一个高效的导航系统，能够实现精确的目标位置估计和高效的全局导航决策。实验结果表明，BeliefMapNav在HM3D、MP3D和HSSD基准测试中达到了最先进的成功率（SR）和路径长度加权成功率（SPL），在SPL上比之前的最佳方法提高了46.4%。

## 🔬 方法详解

**问题定义**：本文旨在解决零-shot物体导航中的空间推理不足和全局环境理解缺失的问题。现有方法通常无法有效整合语义信息与环境信息，导致导航决策不够精准。

**核心思路**：提出基于3D体素的信念图，利用大型语言模型的语义推理能力和视觉嵌入，结合分层空间结构和实时观察，构建目标位置的全局后验信念。

**技术框架**：整体架构包括信念图的构建模块和导航决策模块。信念图模块负责整合语义信息和环境信息，而导航模块则基于信念图进行路径规划和目标定位。

**关键创新**：最重要的创新在于将LLM的语义推理与3D层次语义体素空间相结合，使得目标位置估计更加精准，同时引入顺序路径规划以提升全局导航决策的效率。

**关键设计**：在设计中，采用了体素化的3D空间表示，结合了多层次的语义信息，并在损失函数中考虑了路径长度和成功率的加权，确保了模型的高效性和准确性。

## 📊 实验亮点

实验结果表明，BeliefMapNav在HM3D、MP3D和HSSD基准测试中达到了最先进的成功率（SR）和成功加权路径长度（SPL），在SPL上比之前的最佳方法提高了46.4%，验证了其有效性和高效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动驾驶、虚拟现实和增强现实等。通过提升机器人在复杂环境中的导航能力，BeliefMapNav有望在实际应用中实现更高的自主性和灵活性，推动智能系统的进一步发展。

## 📄 摘要（原文）

> Zero-shot object navigation (ZSON) allows robots to find target objects in unfamiliar environments using natural language instructions, without relying on pre-built maps or task-specific training. Recent general-purpose models, such as large language models (LLMs) and vision-language models (VLMs), equip agents with semantic reasoning abilities to estimate target object locations in a zero-shot manner. However, these models often greedily select the next goal without maintaining a global understanding of the environment and are fundamentally limited in the spatial reasoning necessary for effective navigation. To overcome these limitations, we propose a novel 3D voxel-based belief map that estimates the target's prior presence distribution within a voxelized 3D space. This approach enables agents to integrate semantic priors from LLMs and visual embeddings with hierarchical spatial structure, alongside real-time observations, to build a comprehensive 3D global posterior belief of the target's location. Building on this 3D voxel map, we introduce BeliefMapNav, an efficient navigation system with two key advantages: i) grounding LLM semantic reasoning within the 3D hierarchical semantics voxel space for precise target position estimation, and ii) integrating sequential path planning to enable efficient global navigation decisions. Experiments on HM3D, MP3D, and HSSD benchmarks show that BeliefMapNav achieves state-of-the-art (SOTA) Success Rate (SR) and Success weighted by Path Length (SPL), with a notable 46.4% SPL improvement over the previous best SR method, validating its effectiveness and efficiency.

