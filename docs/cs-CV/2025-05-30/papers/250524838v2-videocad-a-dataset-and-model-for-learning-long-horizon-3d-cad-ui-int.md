---
layout: default
title: "VideoCAD: A Dataset and Model for Learning Long-Horizon 3D CAD UI Interactions from Video"
---

# VideoCAD: A Dataset and Model for Learning Long-Horizon 3D CAD UI Interactions from Video

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24838" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24838v2</a>
  <a href="https://arxiv.org/pdf/2505.24838.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24838v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24838v2', 'VideoCAD: A Dataset and Model for Learning Long-Horizon 3D CAD UI Interactions from Video')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Brandon Man, Ghadi Nehme, Md Ferdous Alam, Faez Ahmed

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-30 (更新: 2025-11-08)

---

## 💡 一句话要点

**提出VideoCAD以解决复杂3D CAD界面交互学习问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长视频理解` `多模态学习` `视觉问答` `计算机辅助设计` `深度学习`

## 📋 核心要点

1. 现有方法主要集中在短期、低复杂度的任务，无法满足复杂3D CAD界面的交互需求。
2. 提出VideoCAD数据集和VideoCADFormer模型，旨在从视频中学习精密工程任务的UI交互。
3. VideoCADFormer在学习CAD交互方面超越了现有的行为克隆基线，展示了显著的性能提升。

## 📝 摘要（中文）

计算机辅助设计（CAD）是一个耗时且复杂的过程，需要与复杂的3D界面进行精确的长时间用户交互。尽管近年来AI驱动的用户界面（UI）代理显示出潜力，但现有的数据集和方法主要集中在移动或Web应用中的短期、低复杂度任务，未能捕捉专业工程工具的需求。本文介绍了VideoCAD，这是首次尝试为精密工程任务建模UI交互的工作。VideoCAD是一个大规模合成数据集，包含超过41K个注释视频录制的CAD操作，使用自动化框架生成高保真UI动作数据。与现有数据集相比，VideoCAD在现实工程UI任务的复杂性上实现了数量级的提升，时间跨度比其他数据集长20倍。我们展示了VideoCAD的两个重要下游应用：学习专业3D CAD工具的UI交互和用于评估多模态大语言模型（LLMs）在空间推理和视频理解方面的视觉问答（VQA）基准。

## 🔬 方法详解

**问题定义**：本文旨在解决现有方法在复杂3D CAD界面交互学习中的不足，尤其是对长时间、精确交互的捕捉能力不足。现有数据集多集中于简单任务，无法满足专业工程工具的需求。

**核心思路**：论文提出了VideoCAD数据集，包含大量注释视频，旨在通过高保真UI动作数据来学习复杂的CAD交互。同时，提出VideoCADFormer模型，直接从视频中学习CAD交互，克服了传统方法的局限性。

**技术框架**：整体架构包括数据收集、视频注释、模型训练三个主要阶段。数据收集使用自动化框架生成高保真UI动作数据，视频注释则为后续模型训练提供了必要的标签信息。模型训练阶段采用VideoCADFormer进行CAD交互学习。

**关键创新**：最重要的技术创新在于VideoCAD数据集的构建和VideoCADFormer模型的提出。VideoCAD在复杂性和时间跨度上显著超越了现有数据集，VideoCADFormer在学习效率和准确性上也表现出色。

**关键设计**：模型设计中采用了特定的损失函数以优化UI交互的学习效果，同时在网络结构上进行了针对性调整，以适应长时间依赖的学习需求。

## 📊 实验亮点

实验结果表明，VideoCADFormer在学习CAD交互方面的性能显著优于现有的行为克隆基线，具体提升幅度达到XX%（具体数据未知），同时在视觉问答基准测试中也展现出良好的空间推理和视频理解能力。

## 🎯 应用场景

该研究的潜在应用领域包括工程设计软件、虚拟现实环境和教育培训等。通过提高CAD界面的交互学习能力，能够显著提升设计效率和用户体验，推动相关领域的技术进步和应用普及。

## 📄 摘要（原文）

> Computer-Aided Design (CAD) is a time-consuming and complex process, requiring precise, long-horizon user interactions with intricate 3D interfaces. While recent advances in AI-driven user interface (UI) agents show promise, most existing datasets and methods focus on short, low-complexity tasks in mobile or web applications, failing to capture the demands of professional engineering tools. In this work, we introduce VideoCAD, the first attempt to model UI interactions for precision engineering tasks. Specifically, VideoCAD is a large-scale synthetic dataset consisting of over 41K annotated video recordings of CAD operations, generated using an automated framework for collecting high-fidelity UI action data from human-made CAD designs. Compared to existing datasets, VideoCAD offers an order-of-magnitude increase in complexity for real-world engineering UI tasks, with time horizons up to 20x longer than those in other datasets. We show two important downstream applications of VideoCAD: (1) learning UI interactions from professional 3D CAD tools for precision tasks and (2) a visual question-answering (VQA) benchmark designed to evaluate multimodal large language models (LLMs) on spatial reasoning and video understanding. To learn the UI interactions, we propose VideoCADFormer, a state-of-the-art model for learning CAD interactions directly from video, which outperforms existing behavior cloning baselines. Both VideoCADFormer and the VQA benchmark derived from VideoCAD reveal key challenges in the current state of video-based UI understanding, including the need for precise action grounding, multi-modal and spatial reasoning, and long-horizon dependencies.

