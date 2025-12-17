---
layout: default
title: Light-Weight Benchmarks Reveal the Hidden Hardware Cost of Zero-Shot Tabular Foundation Models
---

# Light-Weight Benchmarks Reveal the Hidden Hardware Cost of Zero-Shot Tabular Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.00888" class="toolbar-btn" target="_blank">📄 arXiv: 2512.00888</a>
  <a href="https://arxiv.org/pdf/2512.00888.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.00888" onclick="toggleFavorite(this, '2512.00888', 'Light-Weight Benchmarks Reveal the Hidden Hardware Cost of Zero-Shot Tabular Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ishaan Gangwani, Aayam Bansal

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**轻量级基准测试揭示零样本表格数据基础模型隐藏的硬件成本**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `零样本学习` `表格数据` `基础模型` `硬件资源消耗` `基准测试`

## 📋 核心要点

1. 现有零样本表格数据基础模型硬件资源消耗评估不足，缺乏统一的性能基准。
2. 构建可复现的基准测试，同时评估模型精度、推理延迟、CPU RAM和GPU VRAM占用。
3. 实验表明，传统树模型在精度和效率上优于现有零样本模型，揭示了硬件与精度之间的权衡。

## 📝 摘要（中文）

零样本基础模型(FMs)承诺在表格数据上进行免训练预测，但它们的硬件占用仍然缺乏充分的表征。本文提出了一个完全可复现的基准测试，报告了在四个公共数据集（Adult-Income、Higgs-100k、Wine-Quality和California-Housing）上的测试精度以及实际延迟、峰值CPU RAM和峰值GPU VRAM。在单个NVIDIA T4 GPU上，将两个开放的FM（TabPFN-1.0和TabICL-base）与经过调整的XGBoost、LightGBM和Random Forest基线进行比较。树集成模型在三个数据集上达到或超过了FM的精度，同时在<= 0.40秒内完成完整测试批次，并使用<= 150 MB的RAM，且不使用VRAM。TabICL在Higgs上实现了0.8个百分点的增益，但需要大约40,000倍的延迟（960秒）和9 GB的VRAM。TabPFN在Wine和Housing上匹配了树模型的精度，但峰值达到4 GB VRAM，并且无法处理完整的10万行Higgs表。这些结果量化了当前表格数据FM中显著的硬件与精度之间的权衡，并为未来面向效率的研究提供了一个开放的基线。

## 🔬 方法详解

**问题定义**：论文旨在解决零样本表格数据基础模型（FMs）的硬件资源消耗评估问题。现有研究主要关注FMs的预测精度，而忽略了其在实际应用中所需的计算资源，如延迟、CPU RAM和GPU VRAM。这使得难以评估FMs在资源受限环境下的适用性，也缺乏一个统一的基准来比较不同FMs的效率。

**核心思路**：论文的核心思路是通过构建一个全面的、可复现的基准测试，同时评估FMs的预测精度和硬件资源消耗。通过对比FMs与传统机器学习模型（如树集成模型）在不同数据集上的性能，量化FMs在精度和效率之间的权衡。这种方法能够更全面地评估FMs的实用性，并为未来的效率优化研究提供参考。

**技术框架**：该研究的技术框架主要包括以下几个部分：1) 选择具有代表性的表格数据集（Adult-Income, Higgs-100k, Wine-Quality, California-Housing）；2) 选择具有代表性的零样本FMs（TabPFN-1.0, TabICL-base）和传统机器学习模型（XGBoost, LightGBM, Random Forest）作为对比；3) 在统一的硬件平台上（NVIDIA T4 GPU）运行所有模型，并记录测试精度、推理延迟、峰值CPU RAM和峰值GPU VRAM；4) 对比不同模型在精度和硬件资源消耗方面的表现，分析FMs的优缺点。

**关键创新**：论文的关键创新在于构建了一个全面的、可复现的基准测试，能够同时评估零样本FMs的预测精度和硬件资源消耗。该基准测试不仅提供了具体的性能数据，还揭示了FMs在精度和效率之间的权衡，为未来的效率优化研究提供了重要的参考。此外，论文还强调了硬件资源消耗在评估FMs实用性中的重要性，这有助于推动FMs在资源受限环境下的应用。

**关键设计**：论文的关键设计包括：1) 选择具有代表性的表格数据集，覆盖不同规模和特征类型；2) 选择具有代表性的零样本FMs和传统机器学习模型，进行公平的对比；3) 使用统一的硬件平台和评估指标，确保结果的可比性；4) 详细记录和分析硬件资源消耗数据，揭示FMs的优缺点。论文没有特别提及损失函数或网络结构等细节，因为重点在于评估现有模型的性能，而不是提出新的模型。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.00888/acc_vs_latency.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.00888/ram_bar.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.00888/vram_bar.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，在三个数据集上，经过调优的树集成模型在精度上与零样本FM相当甚至超过，同时延迟远低于FM（<= 0.40秒 vs. 960秒），RAM占用也远低于FM（<= 150 MB vs. 9 GB VRAM）。TabICL虽然在Higgs数据集上精度略有提升（0.8个百分点），但延迟和VRAM占用显著增加。TabPFN无法处理完整的Higgs数据集，且VRAM占用较高（4GB）。

## 🎯 应用场景

该研究成果可应用于评估和选择适用于资源受限环境的表格数据预测模型。例如，在边缘计算设备或移动设备上部署模型时，需要考虑模型的硬件资源消耗。该研究提供的基准测试可以帮助用户选择在精度和效率之间取得平衡的模型。此外，该研究还可以促进对现有零样本模型的效率优化，推动其在实际应用中的落地。

## 📄 摘要（原文）

> Zero-shot foundation models (FMs) promise training-free prediction on tabular data, yet their hardware footprint remains poorly characterized. We present a fully reproducible benchmark that reports test accuracy together with wall-clock latency, peak CPU RAM, and peak GPU VRAM on four public datasets: Adult-Income, Higgs-100k, Wine-Quality, and California-Housing. Two open FMs (TabPFN-1.0 and TabICL-base) are compared against tuned XGBoost, LightGBM, and Random Forest baselines on a single NVIDIA T4 GPU. The tree ensembles equal or surpass FM accuracy on three datasets while completing full-test batches in <= 0.40 s and <= 150 MB RAM, using zero VRAM. TabICL achieves a 0.8 percentage-point gain on Higgs but requires roughly 40,000 times more latency (960 s) and 9 GB VRAM. TabPFN matches tree-model accuracy on Wine and Housing but peaks at 4 GB VRAM and cannot process the full 100k-row Higgs table. These results quantify the substantial hardware-versus-accuracy trade-offs in current tabular FMs and provide an open baseline for future efficiency-oriented research.

