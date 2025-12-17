---
layout: default
title: SuperCLIP: CLIP with Simple Classification Supervision
---

# SuperCLIP: CLIP with Simple Classification Supervision

**arXiv**: [2512.14480v1](https://arxiv.org/abs/2512.14480) | [PDF](https://arxiv.org/pdf/2512.14480.pdf)

**作者**: Weiheng Zhao, Zilong Huang, Jiashi Feng, Xinggang Wang

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: Accepted by NeurIPS 2025. Code: https://github.com/hustvl/SuperCLIP

---

## 💡 一句话要点

**提出SuperCLIP框架，通过分类监督增强对比学习，解决CLIP模型细粒度语义利用不足的问题。**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `对比学习` `多模态对齐` `细粒度语义` `零样本分类` `图像-文本检索` `轻量级监督` `视觉-语言模型` `分类监督`

## 📋 核心要点

1. CLIP模型仅优化全局图像-文本相似性，忽略词元级监督，导致细粒度语义信号利用不足，尤其在处理长描述时表现更差。
2. SuperCLIP通过添加轻量级线性层，引入基于分类的监督，增强对比学习，利用词元级线索提升视觉-文本对齐，无需额外数据。
3. 实验显示SuperCLIP在零样本分类、图像-文本检索和视觉任务上均提升性能，并缓解小批量性能下降，适用于多种训练数据。

## 📝 摘要（中文）

对比语言-图像预训练（CLIP）通过在共享嵌入空间中对齐图像和文本来实现视觉-语言任务的强泛化能力。然而，最近的研究发现，CLIP类模型在处理文本时仍未能充分利用细粒度语义信号，这一问题在处理长而详细的描述时尤为突出。这源于CLIP的训练目标仅优化全局图像-文本相似性，而忽略了词元级监督，限制了其实现细粒度视觉-文本对齐的能力。为解决这一问题，我们提出了SuperCLIP，一个简单而有效的框架，通过基于分类的监督来增强对比学习。仅通过在视觉编码器上添加一个轻量级线性层，SuperCLIP利用词元级线索来增强视觉-文本对齐，总FLOPs仅增加0.077%，且无需额外标注数据。实验表明，SuperCLIP在零样本分类、图像-文本检索和纯视觉任务上均能持续提升性能。这些增益无论模型是在原始网络数据还是丰富的重新描述数据上训练都成立，证明了SuperCLIP在两种情况下恢复文本监督的能力。此外，SuperCLIP通过基于分类的监督减轻了CLIP在小批量情况下的性能下降，避免了依赖大批量大小。代码和模型将开源。

## 🔬 方法详解

SuperCLIP是一个增强CLIP的框架，整体基于对比学习，但引入分类监督。关键创新在于在视觉编码器后添加一个轻量级线性层，用于生成词元级分类预测，从而利用文本中的细粒度语义信号。与现有方法的主要区别在于，它不依赖额外标注数据或复杂架构，仅通过简单分类监督弥补CLIP的全局对齐不足，实现更精细的视觉-文本对齐，同时保持计算效率。

## 📊 实验亮点

SuperCLIP在零样本分类、图像-文本检索和纯视觉任务上均实现性能提升，总FLOPs仅增加0.077%，且能缓解CLIP的小批量性能下降，适用于原始和重新描述数据。

## 🎯 应用场景

该研究可应用于多模态人工智能领域，如零样本图像分类、图像-文本检索、视觉问答和机器人视觉理解，提升模型在细粒度语义任务上的性能，具有实际价值。

## 📄 摘要（原文）

> Contrastive Language-Image Pretraining (CLIP) achieves strong generalization in vision-language tasks by aligning images and texts in a shared embedding space. However, recent findings show that CLIP-like models still underutilize fine-grained semantic signals in text, and this issue becomes even more pronounced when dealing with long and detailed captions. This stems from CLIP's training objective, which optimizes only global image-text similarity and overlooks token-level supervision - limiting its ability to achieve fine-grained visual-text alignment. To address this, we propose SuperCLIP, a simple yet effective framework that augments contrastive learning with classification-based supervision. By adding only a lightweight linear layer to the vision encoder, SuperCLIP leverages token-level cues to enhance visual-textual alignment - with just a 0.077% increase in total FLOPs, and no need for additional annotated data. Experiments show that SuperCLIP consistently improves zero-shot classification, image-text retrieval, and purely visual tasks. These gains hold regardless of whether the model is trained on original web data or rich re-captioned data, demonstrating SuperCLIP's ability to recover textual supervision in both cases. Furthermore, SuperCLIP alleviates CLIP's small-batch performance drop through classification-based supervision that avoids reliance on large batch sizes. Code and models will be made open source.

