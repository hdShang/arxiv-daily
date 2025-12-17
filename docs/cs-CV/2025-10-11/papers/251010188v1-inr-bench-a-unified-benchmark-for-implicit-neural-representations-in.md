---
layout: default
title: INR-Bench: A Unified Benchmark for Implicit Neural Representations in Multi-Domain Regression and Reconstruction
---

# INR-Bench: A Unified Benchmark for Implicit Neural Representations in Multi-Domain Regression and Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.10188" class="toolbar-btn" target="_blank">📄 arXiv: 2510.10188v1</a>
  <a href="https://arxiv.org/pdf/2510.10188.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10188v1" onclick="toggleFavorite(this, '2510.10188v1', 'INR-Bench: A Unified Benchmark for Implicit Neural Representations in Multi-Domain Regression and Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Linfei Li, Fengyi Zhang, Zhong Wang, Lin Zhang, Ying Shen

**分类**: cs.LG, cs.CV

**发布日期**: 2025-10-11

**🔗 代码/项目**: [GITHUB](https://github.com/lif314/INR-Bench)

---

## 💡 一句话要点

**提出INR-Bench：多领域回归与重建的隐式神经表示统一基准**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `隐式神经表示` `基准测试` `多模态学习` `神经正切核` `模型评估`

## 📋 核心要点

1. 现有隐式神经表示(INR)研究缺乏对模型架构、位置编码等因素影响的系统性分析，限制了其发展。
2. 论文提出INR-Bench，一个综合性的多模态INR基准，旨在通过系统评估不同模型和配置来理解其性能。
3. INR-Bench包含多种模型变体和任务，涵盖正向和逆向问题，为未来INR研究提供坚实的基础。

## 📝 摘要（中文）

隐式神经表示(INRs)因其连续性和无限分辨率的优势，在各种信号处理任务中取得了成功。然而，影响其有效性和局限性的因素仍未被充分探索。为了更好地理解这些因素，我们利用神经正切核(NTK)理论的见解，分析了模型架构（经典MLP和新兴KAN）、位置编码和非线性原语如何影响对不同频率信号的响应。在此分析的基础上，我们推出了INR-Bench，这是第一个专门为多模态INR任务设计的综合基准。它包括56种Coordinate-MLP模型变体（具有4种位置编码和14种激活函数）和22种具有不同基函数的Coordinate-KAN模型，并在9个隐式多模态任务中进行了评估。这些任务涵盖了正向和逆向问题，提供了一个强大的平台来突出不同神经模型的优势和局限性，从而为未来的研究奠定坚实的基础。代码和数据集可在https://github.com/lif314/INR-Bench获得。

## 🔬 方法详解

**问题定义**：现有隐式神经表示(INR)方法在不同任务和数据集上的性能表现差异较大，缺乏一个统一的评估标准来比较不同模型和配置的优劣。此外，影响INR性能的关键因素，如模型架构、位置编码和激活函数等，尚未得到充分研究，阻碍了INR的进一步发展。

**核心思路**：论文的核心思路是构建一个全面的基准测试平台，通过系统地评估不同INR模型在各种任务上的性能，来揭示影响INR性能的关键因素。该基准包括多种模型变体（MLP和KAN）、位置编码和激活函数，以及涵盖正向和逆向问题的多个任务，从而提供一个公平和全面的比较平台。

**技术框架**：INR-Bench基准测试平台主要包含以下几个模块：1) **模型库**：包含多种Coordinate-MLP和Coordinate-KAN模型变体，涵盖不同的位置编码和激活函数。2) **任务库**：包含9个隐式多模态任务，涵盖图像、音频、视频等多种数据类型，以及正向和逆向问题。3) **评估指标**：采用标准化的评估指标，如PSNR、SSIM等，来衡量模型的性能。4) **自动化评估流程**：提供自动化的评估流程，方便研究人员快速评估和比较不同模型的性能。

**关键创新**：INR-Bench的关键创新在于其综合性和系统性。它是第一个专门为多模态INR任务设计的综合基准，涵盖了多种模型变体、位置编码、激活函数和任务类型。通过系统地评估不同模型在各种任务上的性能，INR-Bench可以帮助研究人员更好地理解影响INR性能的关键因素，并为未来的研究提供指导。

**关键设计**：在模型设计方面，论文考虑了经典的MLP和新兴的KAN架构，并针对每种架构设计了多种变体，例如不同的层数、神经元数量、位置编码和激活函数。在任务设计方面，论文选择了涵盖图像、音频、视频等多种数据类型的9个隐式多模态任务，并涵盖了正向和逆向问题。在评估指标方面，论文采用了标准化的评估指标，如PSNR、SSIM等，以确保评估结果的公平性和可比性。

## 📊 实验亮点

实验结果表明，不同的模型架构、位置编码和激活函数对INR的性能有显著影响。例如，KAN模型在某些任务上优于MLP模型，而某些位置编码可以提高模型的收敛速度和精度。INR-Bench提供了一个平台，可以系统地评估这些因素的影响，并为未来的研究提供指导。

## 🎯 应用场景

INR-Bench可广泛应用于计算机视觉、音频处理、机器人等领域。通过该基准，研究人员可以更好地理解不同INR模型在各种任务上的性能，从而选择合适的模型和配置，提高相关应用的性能。此外，INR-Bench还可以促进新的INR模型和技术的开发，推动相关领域的发展。

## 📄 摘要（原文）

> Implicit Neural Representations (INRs) have gained success in various signal processing tasks due to their advantages of continuity and infinite resolution. However, the factors influencing their effectiveness and limitations remain underexplored. To better understand these factors, we leverage insights from Neural Tangent Kernel (NTK) theory to analyze how model architectures (classic MLP and emerging KAN), positional encoding, and nonlinear primitives affect the response to signals of varying frequencies. Building on this analysis, we introduce INR-Bench, the first comprehensive benchmark specifically designed for multimodal INR tasks. It includes 56 variants of Coordinate-MLP models (featuring 4 types of positional encoding and 14 activation functions) and 22 Coordinate-KAN models with distinct basis functions, evaluated across 9 implicit multimodal tasks. These tasks cover both forward and inverse problems, offering a robust platform to highlight the strengths and limitations of different neural models, thereby establishing a solid foundation for future research. The code and dataset are available at https://github.com/lif314/INR-Bench.

