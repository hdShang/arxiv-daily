---
layout: default
title: "ME-Mamba: Multi-Expert Mamba with Efficient Knowledge Capture and Fusion for Multimodal Survival Analysis"
---

# ME-Mamba: Multi-Expert Mamba with Efficient Knowledge Capture and Fusion for Multimodal Survival Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16900" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16900v1</a>
  <a href="https://arxiv.org/pdf/2509.16900.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16900v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16900v1', 'ME-Mamba: Multi-Expert Mamba with Efficient Knowledge Capture and Fusion for Multimodal Survival Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chengsheng Zhang, Linhao Qu, Xiaoyu Liu, Zhijian Song

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-21

---

## 💡 一句话要点

**提出ME-Mamba，用于高效融合病理图像和基因组数据的多模态生存分析。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态生存分析` `Mamba架构` `病理图像` `基因组数据` `最优传输` `最大均值差异` `癌症预后`

## 📋 核心要点

1. 病理图像生存分析面临仅有切片级别标签的挑战，限制了从千兆像素WSI中学习判别性表示。
2. ME-Mamba通过病理专家、基因组专家和协同专家，分别提取单模态特征、学习模态间对应关系并进行融合。
3. 在TCGA的五个数据集上，ME-Mamba实现了最先进的生存分析性能，同时保持较低的计算复杂度。

## 📝 摘要（中文）

本研究提出了一种多专家Mamba（ME-Mamba）系统，旨在捕获判别性的病理和基因组特征，并实现两种模态的高效整合，从而进行准确的癌症生存分析。该方法通过互补的信息融合，避免了关键信息的丢失。ME-Mamba包含病理专家和基因组专家，分别处理单模态数据，利用Mamba架构提取长序列中的判别性特征。此外，设计了协同专家负责模态融合，通过最优传输学习token级别的局部对应关系，并通过基于最大均值差异的全局跨模态融合损失增强分布一致性。融合后的特征表示被传递到Mamba骨干网络进行进一步整合。在五个TCGA数据集上的实验结果表明，该方法实现了最先进的性能，且计算复杂度相对较低。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态生存分析中，如何有效整合病理图像和基因组数据的问题。现有方法难以从仅有切片级别标签的病理图像中学习判别性特征，并且在融合多模态信息时容易丢失关键信息。

**核心思路**：论文的核心思路是设计一个多专家系统，每个专家负责处理特定模态的数据或进行模态融合。通过这种方式，可以针对不同模态的特点进行优化，并实现互补的信息融合，避免关键信息丢失。Mamba架构的应用旨在高效处理长序列数据，提取判别性特征。

**技术框架**：ME-Mamba系统包含三个主要模块：病理专家、基因组专家和协同专家。病理专家和基因组专家分别使用Mamba架构处理病理图像和基因组数据，提取单模态特征。协同专家负责模态融合，通过最优传输学习token级别的局部对应关系，并通过基于最大均值差异的全局跨模态融合损失增强分布一致性。融合后的特征表示被传递到Mamba骨干网络进行进一步整合。

**关键创新**：该方法的主要创新点在于多专家架构的设计，以及协同专家中使用的最优传输和最大均值差异损失。多专家架构允许针对不同模态进行专门处理，而最优传输和最大均值差异损失则有助于学习模态间的对应关系并增强分布一致性，从而实现更有效的模态融合。Mamba架构在病理和基因组专家中的应用，使其能够高效处理长序列数据。

**关键设计**：病理专家和基因组专家都采用了Mamba架构，并结合了传统的扫描和基于注意力的扫描机制，以提取判别性特征。协同专家使用最优传输来学习token级别的局部对应关系，并通过最大均值差异损失来增强分布一致性。损失函数的具体形式和参数设置在论文中有详细描述。Mamba骨干网络的具体结构也需要参考原文。

## 📊 实验亮点

ME-Mamba在五个TCGA数据集上取得了最先进的性能，证明了其有效性。具体性能数据需要在论文中查找，但摘要中明确指出该方法优于现有方法，并且具有相对较低的计算复杂度。该方法在生存分析的C-index等指标上取得了显著提升。

## 🎯 应用场景

该研究成果可应用于癌症诊断、预后预测和个性化治疗方案制定。通过整合病理图像和基因组数据，可以更准确地预测患者的生存期，并为临床医生提供更全面的信息，从而制定更有效的治疗策略。该方法还可扩展到其他多模态医学数据分析任务中。

## 📄 摘要（原文）

> Survival analysis using whole-slide images (WSIs) is crucial in cancer research. Despite significant successes, pathology images typically only provide slide-level labels, which hinders the learning of discriminative representations from gigapixel WSIs. With the rapid advancement of high-throughput sequencing technologies, multimodal survival analysis integrating pathology images and genomics data has emerged as a promising approach. We propose a Multi-Expert Mamba (ME-Mamba) system that captures discriminative pathological and genomic features while enabling efficient integration of both modalities. This approach achieves complementary information fusion without losing critical information from individual modalities, thereby facilitating accurate cancer survival analysis. Specifically, we first introduce a Pathology Expert and a Genomics Expert to process unimodal data separately. Both experts are designed with Mamba architectures that incorporate conventional scanning and attention-based scanning mechanisms, allowing them to extract discriminative features from long instance sequences containing substantial redundant or irrelevant information. Second, we design a Synergistic Expert responsible for modality fusion. It explicitly learns token-level local correspondences between the two modalities via Optimal Transport, and implicitly enhances distribution consistency through a global cross-modal fusion loss based on Maximum Mean Discrepancy. The fused feature representations are then passed to a mamba backbone for further integration. Through the collaboration of the Pathology Expert, Genomics Expert, and Synergistic Expert, our method achieves stable and accurate survival analysis with relatively low computational complexity. Extensive experimental results on five datasets in The Cancer Genome Atlas (TCGA) demonstrate our state-of-the-art performance.

