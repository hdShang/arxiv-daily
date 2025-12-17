---
layout: default
title: Few-Shot Remote Sensing Image Scene Classification with CLIP and Prompt Learning
---

# Few-Shot Remote Sensing Image Scene Classification with CLIP and Prompt Learning

**arXiv**: [2510.24321v1](https://arxiv.org/abs/2510.24321) | [PDF](https://arxiv.org/pdf/2510.24321.pdf)

**作者**: Ivica Dimitrovski, Vlatko Spasev, Ivan Kitanovski

---

## 💡 一句话要点

**提出提示学习以解决遥感图像少样本场景分类中的领域差距问题**

**关键词**: `遥感图像分类` `少样本学习` `提示学习` `CLIP模型` `领域适应` `多模态学习`

## 📋 核心要点

1. 核心问题：遥感图像场景分类受限于标注数据稀缺和领域差距，导致CLIP模型直接应用效果不佳。
2. 方法要点：系统评估多种提示学习方法，包括上下文优化和多模态提示，以轻量级方式适应语义。
3. 实验或效果：在多个数据集上，提示学习优于零样本CLIP和线性探针，尤其在跨域场景中表现稳健。

## 📄 摘要（原文）

> Remote sensing applications increasingly rely on deep learning for scene
> classification. However, their performance is often constrained by the scarcity
> of labeled data and the high cost of annotation across diverse geographic and
> sensor domains. While recent vision-language models like CLIP have shown
> promise by learning transferable representations at scale by aligning visual
> and textual modalities, their direct application to remote sensing remains
> suboptimal due to significant domain gaps and the need for task-specific
> semantic adaptation. To address this critical challenge, we systematically
> explore prompt learning as a lightweight and efficient adaptation strategy for
> few-shot remote sensing image scene classification. We evaluate several
> representative methods, including Context Optimization, Conditional Context
> Optimization, Multi-modal Prompt Learning, and Prompting with Self-Regulating
> Constraints. These approaches reflect complementary design philosophies: from
> static context optimization to conditional prompts for enhanced generalization,
> multi-modal prompts for joint vision-language adaptation, and semantically
> regularized prompts for stable learning without forgetting. We benchmark these
> prompt-learning methods against two standard baselines: zero-shot CLIP with
> hand-crafted prompts and a linear probe trained on frozen CLIP features.
> Through extensive experiments on multiple benchmark remote sensing datasets,
> including cross-dataset generalization tests, we demonstrate that prompt
> learning consistently outperforms both baselines in few-shot scenarios.
> Notably, Prompting with Self-Regulating Constraints achieves the most robust
> cross-domain performance. Our findings underscore prompt learning as a scalable
> and efficient solution for bridging the domain gap in satellite and aerial
> imagery, providing a strong foundation for future research in this field.

