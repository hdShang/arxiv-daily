---
layout: default
title: "Human-MME: A Holistic Evaluation Benchmark for Human-Centric Multimodal Large Language Models"
---

# Human-MME: A Holistic Evaluation Benchmark for Human-Centric Multimodal Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26165" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26165v3</a>
  <a href="https://arxiv.org/pdf/2509.26165.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26165v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26165v3', 'Human-MME: A Holistic Evaluation Benchmark for Human-Centric Multimodal Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuansen Liu, Haiming Tang, Jinlong Peng, Jiangning Zhang, Xiaozhong Ji, Qingdong He, Wenbin Wu, Donghao Luo, Zhenye Gan, Junwei Zhu, Yunhang Shen, Chaoyou Fu, Chengjie Wang, Xiaobin Hu, Shuicheng Yan

**分类**: cs.CV

**发布日期**: 2025-09-30 (更新: 2025-10-15)

**🔗 代码/项目**: [GITHUB](https://github.com/Yuan-Hou/Human-MME)

---

## 💡 一句话要点

**提出Human-MME基准，用于全面评估以人为中心的多模态大语言模型**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `以人为中心` `评估基准` `场景理解` `人体感知` `因果推理` `数据标注`

## 📋 核心要点

1. 现有MLLM在理解以人为中心的场景方面能力不足，缺乏同时考虑细粒度和高维推理的全面评估基准。
2. 提出Human-MME基准，通过多样化的人类场景、渐进的评估维度和高质量的标注，实现更全面的评估。
3. 实验结果揭示了现有MLLM在以人为中心的图像理解方面的局限性，为未来研究提供了指导。

## 📝 摘要（中文）

多模态大语言模型(MLLMs)在视觉理解任务中取得了显著进展。然而，它们理解以人为中心的场景的能力很少被探索，这主要是由于缺乏全面的评估基准，这些基准既考虑了以人为本的细粒度级别，又考虑了更高维度的因果推理能力。鉴于人体的物理复杂性和标注细粒度结构的难度，这种高质量的评估基准面临着严峻的挑战。在本文中，我们提出了Human-MME，一个精心设计的基准，旨在为MLLM在以人为中心的场景理解中提供更全面的评估。与其他现有基准相比，我们的工作提供了三个关键特征：1. 人类场景的多样性，跨越4个主要视觉领域，包含15个二级领域和43个子领域，以确保广泛的场景覆盖。2. 渐进和多样化的评估维度，从以人为本的细粒度感知到更高维度的推理，逐步评估基于人类的活动，包括八个维度，包含19,945个真实世界的图像问题对和一个评估套件。3. 高质量的注释与丰富的数据范式，构建自动化注释管道和人工注释平台，支持严格的人工标注，以促进精确和可靠的模型评估。我们的基准通过构建选择、简答、定位、排序和判断问题组件以及它们的组合的复杂问题，将单目标理解扩展到多人和多图像的相互理解。对17个最先进的MLLM的广泛实验有效地揭示了局限性，并指导未来的MLLM研究朝着更好的人类中心图像理解发展。所有数据和代码都可以在https://github.com/Yuan-Hou/Human-MME上找到。

## 🔬 方法详解

**问题定义**：现有的大型多模态模型在理解以人为中心的场景时面临挑战，缺乏一个综合性的评估基准来衡量模型在细粒度人体感知和高层次因果推理方面的能力。现有的基准数据集通常关注通用场景，忽略了人体姿态、动作、交互等复杂因素，导致模型在实际应用中表现不佳。

**核心思路**：Human-MME的核心思路是构建一个全面、多样、高质量的评估基准，覆盖各种以人为中心的场景，并设计多维度的评估任务，从细粒度感知到高层次推理，逐步评估模型的能力。通过自动化标注和人工标注相结合的方式，保证数据的准确性和可靠性。

**技术框架**：Human-MME基准的构建包含以下几个主要阶段：1. 数据收集：收集涵盖4个主要视觉领域（如日常生活、医疗保健、体育运动等）和15个二级领域、43个子领域的图像数据，确保场景的多样性。2. 问题设计：设计八个维度的评估任务，包括人体感知、动作识别、关系推理、因果推理等，涵盖选择题、简答题、定位题、排序题和判断题等多种题型。3. 数据标注：构建自动化标注管道和人工标注平台，对图像数据进行细致的标注，包括人体姿态、动作、对象关系等信息。4. 基准评估：使用Human-MME基准评估现有的MLLM模型，分析其在不同维度上的表现，并揭示其局限性。

**关键创新**：Human-MME的关键创新在于其全面性和多样性。它不仅覆盖了广泛的以人为中心的场景，还设计了多维度的评估任务，能够更全面地评估MLLM在人体感知和推理方面的能力。此外，Human-MME还采用了自动化标注和人工标注相结合的方式，保证了数据的质量和可靠性。

**关键设计**：Human-MME的关键设计包括：1. 多样化的场景选择：覆盖4个主要视觉领域、15个二级领域和43个子领域，确保场景的多样性。2. 多维度的评估任务：设计八个维度的评估任务，从细粒度感知到高层次推理，逐步评估模型的能力。3. 混合标注策略：采用自动化标注和人工标注相结合的方式，保证数据的准确性和可靠性。4. 多种题型设计：涵盖选择题、简答题、定位题、排序题和判断题等多种题型，更全面地评估模型的能力。

## 📊 实验亮点

对17个最先进的MLLM进行了广泛的实验，结果表明现有模型在以人为中心的图像理解方面存在局限性。例如，在因果推理任务中，模型的准确率明显低于人类水平。Human-MME基准的评估结果为未来的MLLM研究提供了重要的参考。

## 🎯 应用场景

Human-MME基准可广泛应用于评估和提升多模态大语言模型在以人为中心的场景理解能力，例如智能监控、人机交互、医疗诊断、运动分析等领域。该基准能够促进相关技术的发展，提高模型在实际应用中的性能和可靠性，为人们的生活带来便利。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) have demonstrated significant advances in visual understanding tasks. However, their capacity to comprehend human-centric scenes has rarely been explored, primarily due to the absence of comprehensive evaluation benchmarks that take into account both the human-oriented granular level and higher-dimensional causal reasoning ability. Such high-quality evaluation benchmarks face tough obstacles, given the physical complexity of the human body and the difficulty of annotating granular structures. In this paper, we propose Human-MME, a curated benchmark designed to provide a more holistic evaluation of MLLMs in human-centric scene understanding. Compared with other existing benchmarks, our work provides three key features: 1. Diversity in human scene, spanning 4 primary visual domains with 15 secondary domains and 43 sub-fields to ensure broad scenario coverage. 2. Progressive and diverse evaluation dimensions, evaluating the human-based activities progressively from the human-oriented granular perception to the higher-dimensional reasoning, consisting of eight dimensions with 19,945 real-world image question pairs and an evaluation suite. 3. High-quality annotations with rich data paradigms, constructing the automated annotation pipeline and human-annotation platform, supporting rigorous manual labeling to facilitate precise and reliable model assessment. Our benchmark extends the single-target understanding to the multi-person and multi-image mutual understanding by constructing the choice, short-answer, grounding, ranking and judgment question components, and complex questions of their combination. The extensive experiments on 17 state-of-the-art MLLMs effectively expose the limitations and guide future MLLMs research toward better human-centric image understanding. All data and code are available at https://github.com/Yuan-Hou/Human-MME.

