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

**提出SynPS方法，通过注意力协同机制解决复杂非刚性图像编辑中的过编辑与欠编辑问题**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `图像编辑` `扩散模型` `注意力机制` `非刚性编辑` `位置嵌入` `语义信息` `编辑忠实性` `去噪过程`

## 📋 核心要点

1. 现有方法在复杂非刚性编辑中存在注意力崩溃问题，位置嵌入或语义特征主导导致过编辑或欠编辑
2. 提出SynPS方法，通过编辑度量动态调节位置嵌入影响，协同利用位置和语义信息
3. 实验表明SynPS在公共和新基准上表现优越，有效提升编辑忠实性，避免过编辑和欠编辑

## 📝 摘要（中文）

基于大型扩散模型的无训练图像编辑已变得实用，但忠实执行复杂非刚性编辑（如姿态或形状变化）仍然极具挑战。我们发现一个关键根本原因：现有注意力共享机制中的注意力崩溃，其中位置嵌入或语义特征主导视觉内容检索，导致过编辑或欠编辑。为解决这一问题，我们引入了SynPS方法，该方法协同利用位置嵌入和语义信息进行忠实的非刚性图像编辑。我们首先提出一种编辑度量，量化每个去噪步骤所需的编辑幅度。基于此度量，我们设计了一个注意力协同流程，动态调节位置嵌入的影响，使SynPS能够平衡语义修改和保真度保持。通过自适应整合位置和语义线索，SynPS有效避免了过编辑和欠编辑。在公共和新策划的基准测试上的大量实验证明了我们方法的优越性能和忠实性。

## 🔬 方法详解

SynPS的整体框架是一个基于扩散模型的注意力协同编辑流程。首先，提出编辑度量来量化每个去噪步骤的编辑需求，这是关键创新点，使编辑过程可测量。然后，设计注意力协同机制，动态调制位置嵌入的影响，平衡语义修改与保真度保持。与现有方法的主要区别在于：现有方法往往固定依赖位置或语义信息，导致注意力崩溃；而SynPS通过自适应整合两者，实现更精细的控制，避免过编辑和欠编辑，提升复杂非刚性编辑的忠实性。

## 📊 实验亮点

在公共基准和新策划数据集上的实验显示，SynPS在复杂非刚性编辑任务中显著优于现有方法，有效避免过编辑和欠编辑，编辑忠实性得到大幅提升，证明了注意力协同机制的有效性和优越性。

## 🎯 应用场景

该研究在计算机视觉和图像处理领域有广泛应用，特别适用于需要高保真度的复杂非刚性图像编辑，如人物姿态调整、物体形状变换、艺术创作和影视后期制作。其实际价值在于提供更可靠、可控的编辑工具，提升自动化编辑的质量和效率。

## 📄 摘要（原文）

> Training-free image editing with large diffusion models has become practical, yet faithfully performing complex non-rigid edits (e.g., pose or shape changes) remains highly challenging. We identify a key underlying cause: attention collapse in existing attention sharing mechanisms, where either positional embeddings or semantic features dominate visual content retrieval, leading to over-editing or under-editing.To address this issue, we introduce SynPS, a method that Synergistically leverages Positional embeddings and Semantic information for faithful non-rigid image editing. We first propose an editing measurement that quantifies the required editing magnitude at each denoising step. Based on this measurement, we design an attention synergy pipeline that dynamically modulates the influence of positional embeddings, enabling SynPS to balance semantic modifications and fidelity preservation.By adaptively integrating positional and semantic cues, SynPS effectively avoids both over- and under-editing. Extensive experiments on public and newly curated benchmarks demonstrate the superior performance and faithfulness of our approach.

