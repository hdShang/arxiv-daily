---
layout: default
title: "GeoSketch: A Neural-Symbolic Approach to Geometric Multimodal Reasoning with Auxiliary Line Construction and Affine Transformation"
---

# GeoSketch: A Neural-Symbolic Approach to Geometric Multimodal Reasoning with Auxiliary Line Construction and Affine Transformation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22460" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22460v2</a>
  <a href="https://arxiv.org/pdf/2509.22460.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22460v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22460v2', 'GeoSketch: A Neural-Symbolic Approach to Geometric Multimodal Reasoning with Auxiliary Line Construction and Affine Transformation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shichao Weng, Zhiqiang Wang, Yuhua Zhou, Rui Lu, Ting Liu, Zhiyang Teng, Xiaozhang Liu, Hanmeng Liu

**分类**: cs.AI

**发布日期**: 2025-09-26 (更新: 2025-09-30)

---

## 💡 一句话要点

**GeoSketch：提出一种神经-符号几何多模态推理框架，支持辅助线构造和仿射变换。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `几何问题求解` `多模态推理` `神经-符号方法` `辅助线构造` `仿射变换`

## 📋 核心要点

1. 现有几何问题求解方法难以动态操作图表，限制了其解决复杂几何问题的能力。
2. GeoSketch将几何推理建模为感知-推理-行动的交互循环，通过神经-符号方法实现动态图表操作。
3. GeoSketch在GeoSketch基准测试中显著提高了逐步推理准确性和问题解决成功率。

## 📝 摘要（中文）

几何问题求解(GPS)对多模态大语言模型(MLLM)提出了独特的挑战，它不仅需要对文本和图表进行联合解释，还需要迭代的视觉空间推理。现有的方法将图表视为静态图像进行处理，缺乏动态操作的能力，而动态操作是人类几何推理的核心，包括辅助线构造和仿射变换。我们提出了GeoSketch，一个神经-符号框架，它将几何推理重塑为一个交互式的感知-推理-行动循环。GeoSketch集成了：（1）一个感知模块，将图表抽象成结构化的逻辑形式；（2）一个符号推理模块，应用几何定理来决定下一个演绎步骤；（3）一个草图行动模块，执行诸如绘制辅助线或应用变换等操作，从而在一个闭环中更新图表。为了训练这个智能体，我们开发了一个两阶段的流程：在2000个符号化管理的轨迹上进行监督微调，然后使用密集的符号奖励进行强化学习，以提高鲁棒性和战略探索。为了评估这种范式，我们引入了GeoSketch基准，这是一个高质量的包含390个几何问题的集合，这些问题需要辅助构造或仿射变换。在强大的MLLM基线上的实验表明，GeoSketch显著提高了逐步推理的准确性和解决问题的成功率，优于静态感知方法。通过统一分层决策、可执行的视觉动作和符号验证，GeoSketch将多模态推理从静态解释提升到动态、可验证的交互，为解决复杂的视觉空间问题奠定了新的基础。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大语言模型在几何问题求解中，缺乏动态操作图表能力的问题。现有方法将图表视为静态图像，无法进行辅助线构造和仿射变换等操作，导致在需要复杂几何推理的问题上表现不佳。

**核心思路**：论文的核心思路是将几何推理过程建模为一个交互式的感知-推理-行动循环。通过让模型能够动态地修改和更新图表，模拟人类解决几何问题的方式，从而提高解决复杂问题的能力。这种交互式的方法允许模型在推理过程中逐步探索和验证不同的几何关系。

**技术框架**：GeoSketch框架包含三个主要模块：感知模块、符号推理模块和草图行动模块。感知模块负责将图表抽象成结构化的逻辑形式；符号推理模块应用几何定理来决定下一步的演绎步骤；草图行动模块则执行绘制辅助线或应用变换等操作，更新图表。整个框架通过一个闭环进行迭代，直到找到问题的解。训练过程分为两个阶段：首先进行监督微调，然后在强化学习阶段使用密集的符号奖励来提高模型的鲁棒性和探索能力。

**关键创新**：GeoSketch的关键创新在于其神经-符号的交互式框架，它将神经模型的感知能力与符号推理的精确性相结合，实现了动态的图表操作。与现有方法相比，GeoSketch不再局限于对静态图像的分析，而是能够通过执行动作来改变图表，从而进行更深入的几何推理。

**关键设计**：在训练过程中，论文采用了两阶段的训练策略。首先，使用2000个符号化管理的轨迹进行监督微调，使模型学习基本的几何推理和操作。然后，使用强化学习，通过密集的符号奖励来鼓励模型进行有效的探索和决策。这种训练策略能够提高模型的鲁棒性和解决复杂问题的能力。具体的网络结构和损失函数等细节未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

GeoSketch在GeoSketch基准测试中表现出色，该基准包含390个需要辅助线构造或仿射变换的几何问题。实验结果表明，GeoSketch显著提高了逐步推理的准确性和问题解决的成功率，优于静态感知方法。具体的性能数据和提升幅度未在摘要中给出，属于未知信息。

## 🎯 应用场景

GeoSketch框架具有广泛的应用前景，可应用于智能教育、CAD设计、机器人视觉等领域。在智能教育中，可以帮助学生更好地理解几何概念和解决几何问题。在CAD设计中，可以辅助设计师进行复杂的几何建模和分析。在机器人视觉中，可以提高机器人对几何环境的理解和操作能力。

## 📄 摘要（原文）

> Geometric Problem Solving (GPS) poses a unique challenge for Multimodal Large Language Models (MLLMs), requiring not only the joint interpretation of text and diagrams but also iterative visuospatial reasoning. While existing approaches process diagrams as static images, they lack the capacity for dynamic manipulation - a core aspect of human geometric reasoning involving auxiliary line construction and affine transformations. We present GeoSketch, a neural-symbolic framework that recasts geometric reasoning as an interactive perception-reasoning-action loop. GeoSketch integrates: (1) a Perception module that abstracts diagrams into structured logic forms, (2) a Symbolic Reasoning module that applies geometric theorems to decide the next deductive step, and (3) a Sketch Action module that executes operations such as drawing auxiliary lines or applying transformations, thereby updating the diagram in a closed loop. To train this agent, we develop a two-stage pipeline: supervised fine-tuning on 2,000 symbolic-curated trajectories followed by reinforcement learning with dense, symbolic rewards to enhance robustness and strategic exploration. To evaluate this paradigm, we introduce the GeoSketch Benchmark, a high-quality set of 390 geometry problems requiring auxiliary construction or affine transformations. Experiments on strong MLLM baselines demonstrate that GeoSketch significantly improves stepwise reasoning accuracy and problem-solving success over static perception methods. By unifying hierarchical decision-making, executable visual actions, and symbolic verification, GeoSketch advances multimodal reasoning from static interpretation to dynamic, verifiable interaction, establishing a new foundation for solving complex visuospatial problems.

