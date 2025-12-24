---
layout: default
title: "FaSTA$^*$: Fast-Slow Toolpath Agent with Subroutine Mining for Efficient Multi-turn Image Editing"
---

# FaSTA$^*$: Fast-Slow Toolpath Agent with Subroutine Mining for Efficient Multi-turn Image Editing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20911" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20911v1</a>
  <a href="https://arxiv.org/pdf/2506.20911.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20911v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20911v1', 'FaSTA$^*$: Fast-Slow Toolpath Agent with Subroutine Mining for Efficient Multi-turn Image Editing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Advait Gupta, Rishie Raj, Dang Nguyen, Tianyi Zhou

**分类**: cs.CV

**发布日期**: 2025-06-26

---

## 💡 一句话要点

**提出FaSTA$^*$以解决高效的多轮图像编辑问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多轮图像编辑` `神经符号代理` `工具路径优化` `大型语言模型` `A$^*$搜索` `子程序重用` `计算机视觉`

## 📋 核心要点

1. 现有的图像编辑方法在处理复杂的多轮任务时效率低下，尤其是在需要多次调用不同工具的情况下。
2. 论文提出了一种结合快速高层次规划与慢速精确搜索的FaSTA$^*$代理，通过重用成功的工具路径来提高效率。
3. 实验结果表明，FaSTA$^*$在计算效率上显著优于现有方法，同时在成功率上与最先进的基线保持竞争力。

## 📝 摘要（中文）

我们开发了一种成本高效的神经符号代理，以应对复杂的多轮图像编辑任务，如“检测图像中的长椅并将其重新着色为粉色，同时移除猫以获得更清晰的视图，并将墙壁重新着色为黄色。”该方法结合了大型语言模型（LLMs）进行快速高层次子任务规划与逐步准确的工具使用和局部A$^*$搜索，以找到成本高效的工具路径。通过对先前成功工具路径的归纳推理，FaSTA$^*$能够提取和优化常用子程序，并在未来任务中重用，从而显著降低相似子任务的探索成本。

## 🔬 方法详解

**问题定义**：本论文旨在解决复杂的多轮图像编辑任务，现有方法在处理此类任务时往往面临效率低下和工具调用成本高的问题。

**核心思路**：FaSTA$^*$通过结合大型语言模型进行快速高层次子任务规划和局部A$^*$搜索来优化工具路径，旨在通过重用成功的子程序来降低成本。

**技术框架**：该方法的整体架构包括两个主要阶段：首先利用LLMs进行快速的子任务规划，其次在高层次规划失败时，激活低层次的A$^*$搜索以确保任务的完成。

**关键创新**：FaSTA$^*$的核心创新在于通过归纳推理提取和重用符号子程序，这种方法与传统的逐步搜索方法相比，显著提高了效率和适应性。

**关键设计**：在设计中，FaSTA$^*$采用了高层次的规则选择机制，并在相似图像的相同类型子任务中重用先前成功的工具路径，从而减少了探索成本。具体的参数设置和损失函数设计尚未详细披露。

## 📊 实验亮点

实验结果显示，FaSTA$^*$在计算效率上比现有图像编辑方法提高了显著的性能，成功率与最先进的基线相当，表明其在处理复杂多轮任务时的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括图像处理、计算机视觉和人机交互等，能够显著提升多轮图像编辑的效率和用户体验。未来，FaSTA$^*$可能在自动化设计、虚拟现实和游戏开发等领域发挥重要作用。

## 📄 摘要（原文）

> We develop a cost-efficient neurosymbolic agent to address challenging multi-turn image editing tasks such as "Detect the bench in the image while recoloring it to pink. Also, remove the cat for a clearer view and recolor the wall to yellow.'' It combines the fast, high-level subtask planning by large language models (LLMs) with the slow, accurate, tool-use, and local A$^*$ search per subtask to find a cost-efficient toolpath -- a sequence of calls to AI tools. To save the cost of A$^*$ on similar subtasks, we perform inductive reasoning on previously successful toolpaths via LLMs to continuously extract/refine frequently used subroutines and reuse them as new tools for future tasks in an adaptive fast-slow planning, where the higher-level subroutines are explored first, and only when they fail, the low-level A$^*$ search is activated. The reusable symbolic subroutines considerably save exploration cost on the same types of subtasks applied to similar images, yielding a human-like fast-slow toolpath agent "FaSTA$^*$'': fast subtask planning followed by rule-based subroutine selection per subtask is attempted by LLMs at first, which is expected to cover most tasks, while slow A$^*$ search is only triggered for novel and challenging subtasks. By comparing with recent image editing approaches, we demonstrate FaSTA$^*$ is significantly more computationally efficient while remaining competitive with the state-of-the-art baseline in terms of success rate.

