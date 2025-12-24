---
layout: default
title: "3DGS-IEval-15K: A Large-scale Image Quality Evaluation Database for 3D Gaussian-Splatting"
---

# 3DGS-IEval-15K: A Large-scale Image Quality Evaluation Database for 3D Gaussian-Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14642" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14642v2</a>
  <a href="https://arxiv.org/pdf/2506.14642.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14642v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14642v2', '3DGS-IEval-15K: A Large-scale Image Quality Evaluation Database for 3D Gaussian-Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuke Xing, Jiarui Wang, Peizhi Niu, Wenjie Huang, Guangtao Zhai, Yiling Xu

**分类**: cs.CV

**发布日期**: 2025-06-17 (更新: 2025-08-09)

**🔗 代码/项目**: [GITHUB](https://github.com/YukeXing/3DGS-IEval-15K)

---

## 💡 一句话要点

**提出3DGS-IEval-15K以解决3D高斯点云压缩评估问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D高斯点云` `图像质量评估` `数据集` `压缩技术` `视觉质量`

## 📋 核心要点

1. 现有的3D高斯点云方法在压缩后缺乏有效的质量评估框架，影响了其实际应用。
2. 本文提出了3DGS-IEval-15K数据集，专门用于评估压缩3DGS表示的图像质量。
3. 通过主观实验收集人类感知数据，建立了全面的基准，推动了3DGS质量评估的发展。

## 📝 摘要（中文）

3D高斯点云（3DGS）作为一种新兴的视图合成方法，具备实时渲染和高视觉保真度的优势。然而，其巨大的存储需求给实际应用带来了挑战。尽管最新的3DGS方法逐渐引入了专门的压缩模块，但缺乏全面评估其感知影响的框架。为此，本文提出了3DGS-IEval-15K，这是首个专为压缩3DGS表示设计的大规模图像质量评估（IQA）数据集。该数据集包含15,200张图像，来自10个真实场景，通过6种代表性的3DGS算法在20个选定视点下渲染，涵盖不同压缩级别及其引起的失真效果。通过控制的主观实验，我们收集了60名观众的感知数据，并通过场景多样性和MOS分布分析验证数据集质量，建立了涵盖多种类型的30个代表性IQA指标的综合基准。作为迄今为止最大规模的3DGS质量评估数据集，我们的工作为开发3DGS专用IQA指标奠定了基础，并提供了研究3DGS独特视图依赖质量分布模式的重要数据。

## 🔬 方法详解

**问题定义**：本文旨在解决现有3D高斯点云（3DGS）方法在压缩后缺乏有效的图像质量评估框架的问题。现有方法在实际应用中面临存储需求高和缺乏感知影响评估的挑战。

**核心思路**：论文提出的3DGS-IEval-15K数据集通过系统性地收集和分析压缩3DGS表示的图像质量，填补了这一领域的空白。该数据集的设计考虑了多样的场景和压缩级别，以便全面评估视觉质量。

**技术框架**：整体架构包括数据集的构建、主观实验的设计和质量评估指标的建立。数据集由15,200张图像组成，涵盖10个真实场景和6种3DGS算法，采用20个视点进行渲染。

**关键创新**：最重要的技术创新在于创建了一个专门针对压缩3DGS表示的图像质量评估数据集，首次系统性地分析了不同压缩级别对视觉质量的影响。

**关键设计**：数据集中的图像通过控制实验收集人类感知数据，使用30个代表性IQA指标进行评估，确保了数据集的多样性和质量。

## 📊 实验亮点

实验结果显示，3DGS-IEval-15K数据集在场景多样性和人类感知一致性方面表现优异，建立的基准指标能够有效反映不同压缩级别下的图像质量，为后续研究提供了可靠的数据支持。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、增强现实和计算机图形学等，能够为3D高斯点云技术的实际应用提供重要的质量评估依据。未来，该数据集将促进3DGS领域的研究和发展，推动新型质量评估指标的制定。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) has emerged as a promising approach for novel view synthesis, offering real-time rendering with high visual fidelity. However, its substantial storage requirements present significant challenges for practical applications. While recent state-of-the-art (SOTA) 3DGS methods increasingly incorporate dedicated compression modules, there is a lack of a comprehensive framework to evaluate their perceptual impact. Therefore we present 3DGS-IEval-15K, the first large-scale image quality assessment (IQA) dataset specifically designed for compressed 3DGS representations. Our dataset encompasses 15,200 images rendered from 10 real-world scenes through 6 representative 3DGS algorithms at 20 strategically selected viewpoints, with different compression levels leading to various distortion effects. Through controlled subjective experiments, we collect human perception data from 60 viewers. We validate dataset quality through scene diversity and MOS distribution analysis, and establish a comprehensive benchmark with 30 representative IQA metrics covering diverse types. As the largest-scale 3DGS quality assessment dataset to date, our work provides a foundation for developing 3DGS specialized IQA metrics, and offers essential data for investigating view-dependent quality distribution patterns unique to 3DGS. The database is publicly available at https://github.com/YukeXing/3DGS-IEval-15K.

