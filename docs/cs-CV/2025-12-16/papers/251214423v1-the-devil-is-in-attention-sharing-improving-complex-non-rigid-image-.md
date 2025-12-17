---
layout: default
title: The Devil is in Attention Sharing: Improving Complex Non-rigid Image Editing Faithfulness via Attention Synergy
---

# The Devil is in Attention Sharing: Improving Complex Non-rigid Image Editing Faithfulness via Attention Synergy

**arXiv**: [2512.14423v1](https://arxiv.org/abs/2512.14423) | [PDF](https://arxiv.org/pdf/2512.14423.pdf)

**作者**: Zhuo Chen, Fanyue Wei, Runze Xu, Jingjing Li, Lixin Duan, Angela Yao, Wen Li

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: Project page:https://synps26.github.io/

---

## 💡 一句话要点

**提出SynPS方法，通过注意力协同机制解决复杂非刚性图像编辑中的忠实性问题**

**关键词**: `图像编辑` `扩散模型` `注意力机制` `非刚性变换` `忠实性评估` `无训练方法` `计算机视觉` `人工智能`

## 📋 核心要点

1. 现有方法在复杂非刚性图像编辑中存在注意力崩溃问题，导致过度编辑或编辑不足，影响编辑忠实性。
2. 提出SynPS方法，通过动态调节位置嵌入和语义信息的协同作用，实现编辑幅度自适应控制。
3. 实验表明，SynPS在公共和新基准上显著提升编辑忠实性，有效平衡语义修改与保真度保持。

## 📝 摘要（中文）

基于大型扩散模型的无训练图像编辑已变得实用，但忠实执行复杂非刚性编辑（如姿态或形状变化）仍然极具挑战。我们发现一个关键根本原因：现有注意力共享机制中的注意力崩溃，其中位置嵌入或语义特征主导视觉内容检索，导致过度编辑或编辑不足。为解决此问题，我们引入SynPS，一种协同利用位置嵌入和语义信息以实现忠实非刚性图像编辑的方法。我们首先提出一种编辑度量，量化每个去噪步骤所需的编辑幅度。基于此度量，我们设计了一个注意力协同流程，动态调节位置嵌入的影响，使SynPS能够平衡语义修改和保真度保持。通过自适应整合位置和语义线索，SynPS有效避免过度编辑和编辑不足。在公共和新构建的基准测试上的大量实验证明了我们方法的优越性能和忠实性。

## 🔬 方法详解

SynPS的整体框架基于扩散模型的无训练图像编辑流程，核心创新在于注意力协同机制。该方法首先引入编辑度量来量化每个去噪步骤的编辑需求，然后设计动态调制模块，根据度量结果调整位置嵌入在注意力共享中的权重。关键技术创新点在于将位置嵌入和语义信息协同整合，避免单一因素主导内容检索。与现有方法的主要区别在于，传统方法往往固定位置或语义的贡献，而SynPS通过自适应调节实现更精细的编辑控制，从而提升复杂非刚性编辑的忠实性。

## 📊 实验亮点

在公共基准和新构建的数据集上，SynPS表现出优越性能，显著减少过度编辑和编辑不足现象。实验结果显示，该方法在复杂非刚性编辑任务中，编辑忠实性得到大幅提升，有效平衡语义修改与图像保真度，验证了注意力协同机制的有效性。

## 🎯 应用场景

该研究在计算机视觉和人工智能领域具有广泛潜在应用，如数字媒体创作中的图像编辑、虚拟现实内容生成、以及机器人视觉系统的场景理解与交互。通过提升复杂非刚性编辑的忠实性，可支持更精准的图像修改任务，例如人体姿态调整、物体形状变换等，为实际应用提供更可靠的技术基础。

## 📄 摘要（原文）

> Training-free image editing with large diffusion models has become practical, yet faithfully performing complex non-rigid edits (e.g., pose or shape changes) remains highly challenging. We identify a key underlying cause: attention collapse in existing attention sharing mechanisms, where either positional embeddings or semantic features dominate visual content retrieval, leading to over-editing or under-editing.To address this issue, we introduce SynPS, a method that Synergistically leverages Positional embeddings and Semantic information for faithful non-rigid image editing. We first propose an editing measurement that quantifies the required editing magnitude at each denoising step. Based on this measurement, we design an attention synergy pipeline that dynamically modulates the influence of positional embeddings, enabling SynPS to balance semantic modifications and fidelity preservation.By adaptively integrating positional and semantic cues, SynPS effectively avoids both over- and under-editing. Extensive experiments on public and newly curated benchmarks demonstrate the superior performance and faithfulness of our approach.

