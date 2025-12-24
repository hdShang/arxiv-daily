---
layout: default
title: "Grounding Everything: Emerging Localization Properties in Vision-Language Transformers"
---

# Grounding Everything: Emerging Localization Properties in Vision-Language Transformers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.00878" class="toolbar-btn" target="_blank">📄 arXiv: 2312.00878v3</a>
  <a href="https://arxiv.org/pdf/2312.00878.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.00878v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.00878v3', 'Grounding Everything: Emerging Localization Properties in Vision-Language Transformers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Walid Bousselham, Felix Petersen, Vittorio Ferrari, Hilde Kuehne

**分类**: cs.CV, cs.AI

**发布日期**: 2023-12-01 (更新: 2023-12-14)

**备注**: Code available at https://github.com/WalBouss/GEM

---

## 💡 一句话要点

**提出GEM模块以实现零-shot开放词汇物体定位**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言模型` `零-shot学习` `物体定位` `自我注意力` `开放词汇` `聚类` `正则化` `多模态学习`

## 📋 核心要点

1. 现有视觉-语言模型在零-shot物体定位任务中表现不佳，通常需要进行微调以适应特定任务。
2. 提出的GEM模块通过自我-自我注意力机制实现开放词汇物体定位，避免了微调的需求。
3. GEM在多个基准任务上表现优异，超越了其他无训练方法，并在OpenImagesV7上取得了最先进的结果。

## 📝 摘要（中文）

视觉-语言基础模型在图像检索、分类和描述等零-shot任务中表现出色，但在图像中定位指称表达和物体方面仍显不足。本文展示了预训练的视觉-语言模型能够在无需微调的情况下实现零-shot开放词汇物体定位。为此，提出了一个名为Grounding Everything Module（GEM）的模块，该模块将CLIPSurgery中提出的值-值注意力的思想推广到自我-自我注意力路径。研究表明，自我-自我注意力的概念与聚类相对应，从而使来自同一物体的令牌组保持相似，同时保持与语言空间的对齐。通过一系列正则化方法，模型能够在不同数据集和骨干网络之间进行泛化。实验结果表明，GEM在多个基准任务和数据集上超越了其他无训练的开放词汇定位方法，并在OpenImagesV7大规模分割基准上取得了最先进的结果。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉-语言模型在零-shot物体定位中的不足，尤其是在处理指称表达和物体时的局限性。现有方法通常需要针对特定任务进行微调，限制了其灵活性和适用性。

**核心思路**：论文提出的GEM模块通过自我-自我注意力机制，允许模型在无需微调的情况下实现开放词汇物体定位。该设计旨在通过聚类令牌来增强来自同一物体的令牌之间的相似性，同时保持与语言空间的对齐。

**技术框架**：GEM模块的整体架构包括自我-自我注意力机制和一系列正则化方法。自我-自我注意力机制用于聚类和对齐，而正则化方法则帮助模型在不同数据集和骨干网络之间进行泛化。

**关键创新**：GEM模块的核心创新在于将自我-自我注意力与聚类相结合，形成了一种新的注意力机制。这一机制与传统的值-值注意力方法不同，能够更好地处理开放词汇物体定位任务。

**关键设计**：在GEM模块中，设计了特定的正则化策略，以促进令牌的聚类和对齐。此外，模型的损失函数和网络结构经过精心设计，以确保在不同任务和数据集上的泛化能力。

## 📊 实验亮点

实验结果表明，GEM模块在多个基准任务上表现优异，超越了其他无训练的开放词汇定位方法。在OpenImagesV7大规模分割基准上，GEM取得了最先进的结果，展示了其在零-shot物体定位中的强大能力。

## 🎯 应用场景

该研究的潜在应用领域包括智能监控、自动驾驶、增强现实等场景，能够帮助系统更准确地理解和定位图像中的物体。未来，GEM模块有望在多模态学习和人机交互等领域发挥更大作用，提升系统的智能化水平。

## 📄 摘要（原文）

> Vision-language foundation models have shown remarkable performance in various zero-shot settings such as image retrieval, classification, or captioning. But so far, those models seem to fall behind when it comes to zero-shot localization of referential expressions and objects in images. As a result, they need to be fine-tuned for this task. In this paper, we show that pretrained vision-language (VL) models allow for zero-shot open-vocabulary object localization without any fine-tuning. To leverage those capabilities, we propose a Grounding Everything Module (GEM) that generalizes the idea of value-value attention introduced by CLIPSurgery to a self-self attention path. We show that the concept of self-self attention corresponds to clustering, thus enforcing groups of tokens arising from the same object to be similar while preserving the alignment with the language space. To further guide the group formation, we propose a set of regularizations that allows the model to finally generalize across datasets and backbones. We evaluate the proposed GEM framework on various benchmark tasks and datasets for semantic segmentation. It shows that GEM not only outperforms other training-free open-vocabulary localization methods, but also achieves state-of-the-art results on the recently proposed OpenImagesV7 large-scale segmentation benchmark.

