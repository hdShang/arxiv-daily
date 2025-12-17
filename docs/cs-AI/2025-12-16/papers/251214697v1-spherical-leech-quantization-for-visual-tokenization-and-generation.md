---
layout: default
title: Spherical Leech Quantization for Visual Tokenization and Generation
---

# Spherical Leech Quantization for Visual Tokenization and Generation

**arXiv**: [2512.14697v1](https://arxiv.org/abs/2512.14697) | [PDF](https://arxiv.org/pdf/2512.14697.pdf)

**作者**: Yue Zhao, Hanwen Jiang, Zhenlin Xu, Chutong Yang, Ehsan Adeli, Philipp Krähenbühl

**分类**: cs.CV, cs.AI, cs.LG, eess.SP

**发布日期**: 2025-12-16

**备注**: Tech report; project page: https://zhaoyue-zephyrus.github.io/npq/

---

## 💡 一句话要点

**提出基于Leech晶格的球形量化方法，以改进视觉标记化与生成中的重建-压缩权衡。**

**关键词**: `非参数量化` `晶格编码` `Leech晶格` `图像标记化` `图像压缩` `自回归生成` `视觉量化` `重建-压缩权衡`

## 📋 核心要点

1. 现有非参数量化方法（如BSQ）在训练自编码器时需辅助损失项，导致流程复杂且重建-压缩权衡不佳。
2. 提出基于Leech晶格的球形量化（Λ24-SQ），利用其高对称性和超球面均匀分布简化训练并优化性能。
3. 在图像标记化、压缩和生成任务中，Λ24-SQ在重建质量上全面超越BSQ，同时比特消耗更低。

## 📝 摘要（中文）

非参数量化因其参数效率和在大码本上的可扩展性而备受关注。本文通过晶格编码的视角，提出了不同非参数量化方法的统一表述。晶格码的几何结构解释了在训练自编码器时，对于某些现有的无查找量化变体（如BSQ）需要辅助损失项的必要性。作为进一步探索，我们研究了几种可能的候选方案，包括随机晶格、广义斐波那契晶格和最密球堆积晶格。其中，我们发现基于Leech晶格的量化方法（称为球形Leech量化，Λ24-SQ）由于其高对称性和超球面上的均匀分布，既能简化训练流程，又能改善重建与压缩之间的权衡。在图像标记化和压缩任务中，该量化方法在所有指标上均优于先前最佳方法BSQ，同时消耗的比特数略少。这一改进也延伸到了最先进的自回归图像生成框架中。

## 🔬 方法详解

论文提出一种统一的非参数量化框架，基于晶格编码理论。核心方法是球形Leech量化（Λ24-SQ），它利用Leech晶格（Λ24）的高对称性和在24维超球面上的均匀分布特性。该方法通过晶格点直接量化特征向量，无需复杂的查找操作或辅助损失，简化了自编码器的训练流程。与现有方法（如BSQ）的主要区别在于：Λ24-SQ基于数学上优化的晶格结构，提供了更均匀的量化点分布，从而在压缩效率和重建质量之间达到更好平衡，避免了训练中的不稳定性。

## 📊 实验亮点

实验显示，Λ24-SQ在图像标记化和压缩任务中，所有重建质量指标（如PSNR、SSIM）均优于先前最佳方法BSQ，同时比特率略有降低；在自回归图像生成框架中也能带来性能提升，验证了其广泛适用性。

## 🎯 应用场景

该研究主要应用于计算机视觉领域，特别是图像和视频的压缩、标记化以及生成任务。潜在价值包括提升图像编码效率、支持高质量图像生成模型（如自回归框架），并可能扩展到其他模态的数据压缩和生成场景。

## 📄 摘要（原文）

> Non-parametric quantization has received much attention due to its efficiency on parameters and scalability to a large codebook. In this paper, we present a unified formulation of different non-parametric quantization methods through the lens of lattice coding. The geometry of lattice codes explains the necessity of auxiliary loss terms when training auto-encoders with certain existing lookup-free quantization variants such as BSQ. As a step forward, we explore a few possible candidates, including random lattices, generalized Fibonacci lattices, and densest sphere packing lattices. Among all, we find the Leech lattice-based quantization method, which is dubbed as Spherical Leech Quantization ($Λ_{24}$-SQ), leads to both a simplified training recipe and an improved reconstruction-compression tradeoff thanks to its high symmetry and even distribution on the hypersphere. In image tokenization and compression tasks, this quantization approach achieves better reconstruction quality across all metrics than BSQ, the best prior art, while consuming slightly fewer bits. The improvement also extends to state-of-the-art auto-regressive image generation frameworks.

