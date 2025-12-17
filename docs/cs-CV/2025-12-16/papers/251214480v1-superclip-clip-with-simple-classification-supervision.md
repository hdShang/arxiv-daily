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

**关键词**: `对比学习` `多模态对齐` `细粒度语义` `零样本分类` `图像-文本检索` `轻量级监督` `视觉-语言模型` `预训练框架`

## 📋 核心要点

1. CLIP模型仅优化全局图像-文本相似性，忽略词元级监督，导致细粒度语义信号利用不足，尤其在处理长描述时表现更差。
2. SuperCLIP通过添加轻量级线性层，引入基于分类的监督，增强对比学习，以词元级线索提升视觉-文本对齐，无需额外数据。
3. 实验显示SuperCLIP在零样本分类、图像-文本检索和视觉任务上均提升性能，并缓解小批量训练的性能下降问题。

## 📝 摘要（中文）

对比语言-图像预训练（CLIP）通过在共享嵌入空间中对齐图像和文本来实现视觉-语言任务的强泛化能力。然而，最近的研究发现，CLIP类模型在处理文本时仍未能充分利用细粒度语义信号，这一问题在处理长而详细的描述时尤为明显。这源于CLIP的训练目标仅优化全局图像-文本相似性，而忽略了词元级监督，限制了其实现细粒度视觉-文本对齐的能力。为解决这一问题，我们提出了SuperCLIP，一个简单而有效的框架，通过基于分类的监督来增强对比学习。仅需在视觉编码器上添加一个轻量级线性层，SuperCLIP就能利用词元级线索来提升视觉-文本对齐，总FLOPs仅增加0.077%，且无需额外标注数据。实验表明，SuperCLIP在零样本分类、图像-文本检索和纯视觉任务上均能持续提升性能。这些增益无论模型是在原始网络数据还是丰富的重新描述数据上训练都成立，证明了SuperCLIP在两种情况下恢复文本监督的能力。此外，SuperCLIP通过基于分类的监督减轻了CLIP在小批量情况下的性能下降，避免了依赖大批量训练。代码和模型将开源。

## 🔬 方法详解

SuperCLIP的整体框架基于CLIP，通过增强对比学习来实现。关键技术创新点是在视觉编码器上添加一个轻量级线性层，用于生成分类预测，从而引入基于分类的监督。这种方法利用文本中的词元级信息（如名词或短语）作为监督信号，通过分类损失函数优化视觉特征与文本细粒度语义的对齐。与现有方法的主要区别在于，SuperCLIP不依赖复杂的架构或额外标注数据，而是通过简单的分类监督直接提升CLIP的细粒度对齐能力，总计算开销仅微增0.077%。

## 📊 实验亮点

SuperCLIP在零样本分类任务上显著提升准确率，图像-文本检索性能优于基线CLIP，同时纯视觉任务如目标检测也有改进。实验还表明，该方法能有效缓解小批量训练的性能下降，总FLOPs仅增加0.077%，无需额外数据。

## 🎯 应用场景

SuperCLIP可应用于多模态人工智能领域，如零样本图像分类、图像-文本检索、视觉问答和内容生成任务。其提升的细粒度对齐能力有助于在医疗影像分析、自动驾驶视觉理解和智能内容推荐等实际场景中实现更精准的语义理解。

## 📄 摘要（原文）

> Contrastive Language-Image Pretraining (CLIP) achieves strong generalization in vision-language tasks by aligning images and texts in a shared embedding space. However, recent findings show that CLIP-like models still underutilize fine-grained semantic signals in text, and this issue becomes even more pronounced when dealing with long and detailed captions. This stems from CLIP's training objective, which optimizes only global image-text similarity and overlooks token-level supervision - limiting its ability to achieve fine-grained visual-text alignment. To address this, we propose SuperCLIP, a simple yet effective framework that augments contrastive learning with classification-based supervision. By adding only a lightweight linear layer to the vision encoder, SuperCLIP leverages token-level cues to enhance visual-textual alignment - with just a 0.077% increase in total FLOPs, and no need for additional annotated data. Experiments show that SuperCLIP consistently improves zero-shot classification, image-text retrieval, and purely visual tasks. These gains hold regardless of whether the model is trained on original web data or rich re-captioned data, demonstrating SuperCLIP's ability to recover textual supervision in both cases. Furthermore, SuperCLIP alleviates CLIP's small-batch performance drop through classification-based supervision that avoids reliance on large batch sizes. Code and models will be made open source.

