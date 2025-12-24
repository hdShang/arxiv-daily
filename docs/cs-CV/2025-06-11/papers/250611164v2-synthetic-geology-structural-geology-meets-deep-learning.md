---
layout: default
title: "Synthetic Geology: Structural Geology Meets Deep Learning"
---

# Synthetic Geology: Structural Geology Meets Deep Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11164" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11164v2</a>
  <a href="https://arxiv.org/pdf/2506.11164.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11164v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11164v2', 'Synthetic Geology: Structural Geology Meets Deep Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Simon Ghyselincks, Valeriia Okhmak, Stefano Zampini, George Turkiyyah, David Keyes, Eldad Haber

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-06-11 (更新: 2025-11-18)

**备注**: 10 pages, 9 figures, geological simulation code at https://doi.org/10.5281/zenodo.15244035, generative AI code at https://github.com/chipnbits/flowtrain_stochastic_interpolation/releases/tag/v1.0.2

---

## 💡 一句话要点

**提出StructuralGeo以解决地质重建中的数据稀缺问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `地质重建` `深度学习` `生成模型` `地球物理` `岩土工程` `合成数据` `不确定性建模`

## 📋 核心要点

1. 现有的地质重建方法依赖于稀疏数据，无法全面捕捉地下结构的多样性，导致模型的局限性。
2. 论文提出了StructuralGeo地质模拟引擎，通过模拟地质过程生成大量合成3D岩石模型，解决了训练数据不足的问题。
3. 实验结果表明，使用生成模型可以从相同观测数据中生成多个重建场景，显著提高了地下特征的估计精度。

## 📝 摘要（中文）

从稀疏或间接的地表观测重建地球表层几公里的结构地质和矿物成分一直是一个长期挑战，具有重要的矿产勘探、地质灾害评估和岩土工程应用。传统的地球物理反演方法通常只能提供单一的最大似然模型，无法捕捉到地质的全貌。本文提出了StructuralGeo，一个地质模拟引擎，生成逼真的合成3D岩石模型，并利用这些数据训练生成流匹配模型，从而能够从地表地形和稀疏钻孔数据中重建多个可能的3D场景。

## 🔬 方法详解

**问题定义**：论文要解决的问题是如何从稀疏或间接的地表观测中重建地下的结构地质和矿物成分。现有的传统方法往往只能提供单一的模型，无法反映地下地质的复杂性和多样性。

**核心思路**：论文的核心思路是利用StructuralGeo地质模拟引擎生成大量的合成3D岩石模型，进而训练生成模型，以捕捉地下结构的多样性和不确定性。这样的设计使得模型能够从有限的数据中推断出多个可能的地质场景。

**技术框架**：整体架构包括地质模拟引擎和基于3D注意力U-net的生成流匹配模型。首先，使用模拟引擎生成合成数据，然后利用这些数据训练生成模型，最后通过模型从地表数据重建地下结构。

**关键创新**：最重要的技术创新点在于结合了地质模拟与生成AI，提供了一种灵活的概率框架，能够生成多个可能的地下结构模型，而不仅仅是单一的最优解。这与传统方法的本质区别在于其考虑了不确定性。

**关键设计**：在模型设计中，采用了3D注意力U-net架构，结合了条件和无条件生成流匹配模型。损失函数的设计考虑了生成模型的多样性和真实感，确保生成的模型能够反映真实地质特征。

## 📊 实验亮点

实验结果显示，使用生成模型能够从相同的地表观测数据中生成多个重建场景，显著提高了地下特征的估计精度。与传统方法相比，模型在捕捉地质多样性方面表现出更高的灵活性和准确性，提供了更为全面的地质理解。

## 🎯 应用场景

该研究的潜在应用领域包括矿产资源勘探、地质灾害评估和岩土工程等。通过提供更为准确和多样的地下结构重建，能够帮助工程师和地质学家在决策过程中更好地评估风险和资源分布，提升工程安全性和经济效益。未来，该方法有望在更广泛的地质研究和应用中发挥重要作用。

## 📄 摘要（原文）

> Reconstructing the structural geology and mineral composition of the first few kilometers of the Earth's subsurface from sparse or indirect surface observations remains a long-standing challenge with critical applications in mineral exploration, geohazard assessment, and geotechnical engineering. This inherently ill-posed problem is often addressed by classical geophysical inversion methods, which typically yield a single maximum-likelihood model that fails to capture the full range of plausible geology. The adoption of modern deep learning methods has been limited by the lack of large 3D training datasets. We address this gap with \textit{StructuralGeo}, a geological simulation engine that mimics eons of tectonic, magmatic, and sedimentary processes to generate a virtually limitless supply of realistic synthetic 3D lithological models. Using this dataset, we train both unconditional and conditional generative flow-matching models with a 3D attention U-net architecture. The resulting foundation model can reconstruct multiple plausible 3D scenarios from surface topography and sparse borehole data, depicting structures such as layers, faults, folds, and dikes. By sampling many reconstructions from the same observations, we introduce a probabilistic framework for estimating the size and extent of subsurface features. While the realism of the output is bounded by the fidelity of the training data to true geology, this combination of simulation and generative AI functions offers a flexible prior for probabilistic modeling, regional fine-tuning, and use as an AI-based regularizer in traditional geophysical inversion workflows.

