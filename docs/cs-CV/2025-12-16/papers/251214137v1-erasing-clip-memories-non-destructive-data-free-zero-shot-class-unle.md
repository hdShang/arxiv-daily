---
layout: default
title: Erasing CLIP Memories: Non-Destructive, Data-Free Zero-Shot class Unlearning in CLIP Models
---

# Erasing CLIP Memories: Non-Destructive, Data-Free Zero-Shot class Unlearning in CLIP Models

**arXiv**: [2512.14137v1](https://arxiv.org/abs/2512.14137) | [PDF](https://arxiv.org/pdf/2512.14137.pdf)

**作者**: Ashish Mishra, Tarun Kumar, Gyanaranjan Nayak, Arpit Shah, Suparna Bhattacharya, Martin Foltin

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出基于零空间投影的非破坏性数据无关零样本类别遗忘方法，以解决CLIP模型选择性遗忘问题。**

**关键词**: `选择性遗忘` `零空间投影` `多模态模型` `CLIP模型` `零样本学习` `模型去污` `隐私保护` `闭式方法`

## 📋 核心要点

1. 现有方法依赖迭代微调和大量数据整理，计算成本高且难以精确控制遗忘过程。
2. 提出基于零空间投影的闭式方法，通过正交基投影擦除目标类别信息，无需重新训练或数据。
3. 实验显示目标类别零样本性能显著下降，同时整体多模态知识得以保留，部分投影实现平衡。

## 📝 摘要（中文）

我们提出了一种新颖的闭式方法，用于多模态模型中的选择性遗忘，特别针对如CLIP这样的预训练模型。该方法利用零空间投影来擦除嵌入在最终投影层中的目标类别信息，无需任何重新训练或使用遗忘集中的图像。通过计算目标文本嵌入所张成子空间的正交基并投影这些方向，我们显著降低了图像特征与不需要类别之间的对齐。与依赖迭代微调和大量数据整理的传统遗忘技术不同，我们的方法既计算高效又具有外科手术般的精确性。这导致目标类别的零样本性能显著下降，同时保留了模型的整体多模态知识。实验表明，即使是部分投影也能在完全遗忘和保留有用信息之间取得平衡，解决了模型去污和隐私保护中的关键挑战。

## 🔬 方法详解

该方法整体框架基于CLIP模型的最终投影层，通过计算目标类别文本嵌入的正交基，构建零空间投影矩阵来擦除这些方向上的信息。关键技术创新点在于利用闭式零空间投影实现非破坏性、数据无关的类别遗忘，无需微调或访问遗忘集图像。与现有方法的主要区别在于避免了迭代优化和数据依赖，提供了一种计算高效且精确的解决方案，直接操作嵌入空间而非修改模型参数。

## 📊 实验亮点

实验结果表明，该方法能显著降低目标类别的零样本性能，同时保持模型对其他类别的识别能力；部分投影策略在完全遗忘和知识保留之间取得平衡，验证了方法的有效性和灵活性。

## 🎯 应用场景

该研究在模型去污和隐私保护领域具有重要应用价值，例如在需要移除敏感或错误类别信息的场景中，如医疗图像分析、内容过滤和合规性调整，能高效实现选择性遗忘而不损害模型整体性能。

## 📄 摘要（原文）

> We introduce a novel, closed-form approach for selective unlearning in multimodal models, specifically targeting pretrained models such as CLIP. Our method leverages nullspace projection to erase the target class information embedded in the final projection layer, without requiring any retraining or the use of images from the forget set. By computing an orthonormal basis for the subspace spanned by target text embeddings and projecting these directions, we dramatically reduce the alignment between image features and undesired classes. Unlike traditional unlearning techniques that rely on iterative fine-tuning and extensive data curation, our approach is both computationally efficient and surgically precise. This leads to a pronounced drop in zero-shot performance for the target classes while preserving the overall multimodal knowledge of the model. Our experiments demonstrate that even a partial projection can balance between complete unlearning and retaining useful information, addressing key challenges in model decontamination and privacy preservation.

