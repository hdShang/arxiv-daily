---
layout: default
title: MedBridge: Bridging Foundation Vision-Language Models to Medical Image Diagnosis in Chest X-Ray
---

# MedBridge: Bridging Foundation Vision-Language Models to Medical Image Diagnosis in Chest X-Ray

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21698" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21698v2</a>
  <a href="https://arxiv.org/pdf/2505.21698.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21698v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21698v2', 'MedBridge: Bridging Foundation Vision-Language Models to Medical Image Diagnosis in Chest X-Ray')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yitong Li, Morteza Ghahremani, Christian Wachinger

**分类**: cs.CV

**发布日期**: 2025-05-27 (更新: 2025-11-24)

**🔗 代码/项目**: [GITHUB](https://github.com/ai-med/MedBridge)

---

## 💡 一句话要点

**提出MedBridge以解决医学影像诊断中的领域适应问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学影像诊断` `视觉-语言模型` `领域适应` `多模态学习` `深度学习`

## 📋 核心要点

1. 现有视觉-语言模型在医学图像诊断中面临领域转移的挑战，导致性能下降。
2. MedBridge通过Focal Sampling、Query-Encoder和Mixture of Experts机制，灵活适应医学图像诊断。
3. 在五个胸部放射影像基准测试中，MedBridge在多标签胸部疾病诊断中AUC提升6-15%。

## 📝 摘要（中文）

近年来，视觉-语言基础模型在自然图像分类中取得了最先进的结果，但在医学图像领域由于显著的领域转移而表现不佳。训练医学基础模型需要大量的标注数据和高计算能力。为此，我们提出了MedBridge，一个轻量级的多模态适应框架，旨在以最小的开销灵活地重新利用任意预训练的基础视觉-语言模型进行医学图像诊断。MedBridge包含三个核心组件：Focal Sampling模块、Query-Encoder模型和Mixture of Experts机制。我们在五个胸部放射影像基准测试上评估了MedBridge，结果显示其在跨领域和领域内适应任务中均表现优越，AUC提升6-15%。

## 🔬 方法详解

**问题定义**：本论文旨在解决医学影像诊断中视觉-语言模型因领域转移而导致的性能不足问题。现有方法通常需要大量标注数据和高计算资源，限制了其在医学领域的应用。

**核心思路**：MedBridge的核心思路是通过轻量级的适应框架，利用预训练的视觉-语言模型进行医学图像诊断，而无需对基础模型进行重训练。

**技术框架**：MedBridge的整体架构包括三个主要模块：Focal Sampling模块用于提取高分辨率局部区域，Query-Encoder模型用于对齐特征图与医学语义，Mixture of Experts机制则通过可学习查询整合多种模型的优势。

**关键创新**：MedBridge的创新点在于其Focal Sampling和Query-Encoder设计，使得在不重训练基础层的情况下，能够有效捕捉医学图像中的细微病理特征。

**关键设计**：在Focal Sampling模块中，采用了高分辨率局部区域提取技术；Query-Encoder使用了一小组可学习的查询来对齐特征图；Mixture of Experts机制则通过可学习的查询动态选择最优模型组合。具体的损失函数和参数设置在论文中详细描述。

## 📊 实验亮点

在五个胸部放射影像基准测试中，MedBridge在多标签胸部疾病诊断任务中，相较于最先进的视觉-语言模型适应方法，AUC提升了6-15%。这一结果表明MedBridge在跨领域和领域内适应任务中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括医学影像诊断、临床辅助决策和医疗数据分析。MedBridge的设计使其能够在资源有限的情况下，利用现有的视觉-语言模型进行高效的医学图像分析，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent vision-language foundation models deliver state-of-the-art results in natural image classification, but falter in medical images due to pronounced domain shifts. Training a medical foundation model also requires substantial resources, including extensive annotated data and high computational capacity. To bridge this gap with minimal overhead, we introduce MedBridge, a lightweight multimodal adaptation framework that flexibly re-purposes arbitrary pre-trained foundation VLMs for medical image diagnosis. MedBridge comprises three novel core components. First, a Focal Sampling module that subsamples and extracts high-resolution local regions to capture subtle pathological features, compensating for the limited input resolution of foundation VLMs. Second, a Query-Encoder model with a small set of learnable queries to align the feature maps of frozen VLMs with medical semantics, without requiring retraining of the backbone layers. Third, a Mixture of Experts mechanism, driven by learnable queries, harnesses the complementary strength of various VLMs to maximize diagnostic performance. We evaluate MedBridge on five chest radiograph benchmarks in three key adaptation tasks, demonstrating its superior performance in both cross-domain and in-domain adaptation settings under varying levels of training data availability. MedBridge achieved an improvement of 6-15% in AUC compared to state-of-the-art VLM adaptation methods in multi-label thoracic disease diagnosis, underscoring its effectiveness in leveraging diverse foundation models for accurate and data-efficient medical diagnosis. Our project and code are available at https://github.com/ai-med/MedBridge.

