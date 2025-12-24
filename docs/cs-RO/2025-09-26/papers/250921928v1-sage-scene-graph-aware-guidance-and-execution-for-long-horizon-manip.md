---
layout: default
title: "SAGE: Scene Graph-Aware Guidance and Execution for Long-Horizon Manipulation Tasks"
---

# SAGE: Scene Graph-Aware Guidance and Execution for Long-Horizon Manipulation Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21928" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21928v1</a>
  <a href="https://arxiv.org/pdf/2509.21928.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21928v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21928v1', 'SAGE: Scene Graph-Aware Guidance and Execution for Long-Horizon Manipulation Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jialiang Li, Wenzheng Wu, Gaojing Zhang, Yifan Han, Wenzhao Lian

**分类**: cs.RO, cs.AI

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**SAGE：基于场景图的长程操作任务引导与执行框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `长程操作` `场景图` `任务规划` `视觉运动控制` `图像编辑` `机器人` `语义推理`

## 📋 核心要点

1. 现有长程操作任务方法泛化性不足，语义推理能力有限，难以适应新任务。
2. SAGE利用场景图连接任务级语义推理和像素级视觉运动控制，实现可控的子目标图像合成。
3. 实验表明，SAGE在长程操作任务上达到了最先进的性能，验证了其有效性。

## 📝 摘要（中文）

成功解决长程操作任务仍然是一个根本性的挑战。这类任务涉及扩展的动作序列和复杂的对象交互，在高层符号规划和低层连续控制之间存在着关键差距。为了弥合这一差距，需要两种基本能力：鲁棒的长程任务规划和有效的以目标为条件的操控。现有的任务规划方法，包括传统方法和基于LLM的方法，通常表现出有限的泛化能力或稀疏的语义推理。同时，图像条件控制方法难以适应未见过的任务。为了解决这些问题，我们提出了SAGE，一种用于长程操作任务中场景图感知引导和执行的新框架。SAGE利用语义场景图作为场景状态的结构化表示。结构化场景图能够桥接任务级语义推理和像素级视觉运动控制。这也有助于可控地合成准确的、新的子目标图像。SAGE由两个关键组件组成：（1）一个基于场景图的任务规划器，它使用VLMs和LLMs来解析环境并推理物理上接地的场景状态转换序列，以及（2）一个解耦的结构化图像编辑管道，它通过图像修复和组合，可控地将每个目标子目标图转换为相应的图像。大量的实验表明，SAGE在不同的长程任务上实现了最先进的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决长程操作任务中，高层符号规划与低层连续控制之间的鸿沟。现有方法，如传统规划方法和基于LLM的方法，在泛化性和语义推理方面存在局限性。同时，图像条件控制方法难以适应未见过的任务，导致长程任务难以完成。

**核心思路**：论文的核心思路是利用语义场景图作为中间表示，连接任务级的语义推理和像素级的视觉运动控制。通过场景图，可以更好地理解环境状态，并规划出合理的动作序列。同时，利用场景图可以生成目标子图，并将其转化为图像，从而指导低层控制器的执行。

**技术框架**：SAGE框架包含两个主要模块：（1）基于场景图的任务规划器：该模块利用VLMs和LLMs解析环境，并推理出物理上可行的场景状态转换序列，生成一系列子目标场景图。（2）解耦的结构化图像编辑管道：该模块将每个子目标场景图转换为对应的图像，通过图像修复和组合等技术，生成高质量的子目标图像。这些图像作为低层控制器的目标，指导其执行操作。

**关键创新**：SAGE的关键创新在于使用场景图作为连接高层规划和低层控制的桥梁。场景图能够提供结构化的场景信息，方便进行语义推理和图像合成。此外，解耦的图像编辑管道使得子目标图像的生成更加可控和灵活。

**关键设计**：任务规划器使用VLM和LLM进行环境解析和状态推理，具体实现细节未知。图像编辑管道使用图像修复和组合技术，损失函数和网络结构等细节未知。论文中可能包含一些超参数的设置，但摘要中没有提及。

## 📊 实验亮点

论文通过大量实验验证了SAGE框架的有效性，并在不同的长程任务上取得了最先进的性能。具体的性能数据、对比基线和提升幅度在摘要中未提及，需要在论文正文中查找。

## 🎯 应用场景

SAGE框架可应用于各种长程操作任务，例如机器人组装、家庭服务机器人、自动化厨房等。该研究有助于提升机器人在复杂环境中的自主操作能力，降低人工干预的需求，提高生产效率和服务质量。未来，该技术有望应用于更广泛的机器人应用场景。

## 📄 摘要（原文）

> Successfully solving long-horizon manipulation tasks remains a fundamental challenge. These tasks involve extended action sequences and complex object interactions, presenting a critical gap between high-level symbolic planning and low-level continuous control. To bridge this gap, two essential capabilities are required: robust long-horizon task planning and effective goal-conditioned manipulation. Existing task planning methods, including traditional and LLM-based approaches, often exhibit limited generalization or sparse semantic reasoning. Meanwhile, image-conditioned control methods struggle to adapt to unseen tasks. To tackle these problems, we propose SAGE, a novel framework for Scene Graph-Aware Guidance and Execution in Long-Horizon Manipulation Tasks. SAGE utilizes semantic scene graphs as a structural representation for scene states. A structural scene graph enables bridging task-level semantic reasoning and pixel-level visuo-motor control. This also facilitates the controllable synthesis of accurate, novel sub-goal images. SAGE consists of two key components: (1) a scene graph-based task planner that uses VLMs and LLMs to parse the environment and reason about physically-grounded scene state transition sequences, and (2) a decoupled structural image editing pipeline that controllably converts each target sub-goal graph into a corresponding image through image inpainting and composition. Extensive experiments have demonstrated that SAGE achieves state-of-the-art performance on distinct long-horizon tasks.

