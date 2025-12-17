---
layout: default
title: Unsupervised Domain Adaptation via Similarity-based Prototypes for Cross-Modality Segmentation
---

# Unsupervised Domain Adaptation via Similarity-based Prototypes for Cross-Modality Segmentation

**arXiv**: [2510.20596v1](https://arxiv.org/abs/2510.20596) | [PDF](https://arxiv.org/pdf/2510.20596.pdf)

**作者**: Ziyu Ye, Chen Ju, Chaofan Ma, Xiaoyun Zhang

---

## 💡 一句话要点

**提出基于相似性原型的无监督域适应方法以解决跨模态分割问题**

**关键词**: `无监督域适应` `跨模态分割` `原型学习` `相似性约束` `对比学习`

## 📋 核心要点

1. 核心问题：深度学习模型在未见数据上性能下降，因域偏移敏感。
2. 方法要点：学习类原型于嵌入空间，引入相似性约束增强代表性与可分性。
3. 实验或效果：使用字典存储原型，避免类缺失，实验显示优于现有方法。

## 📄 摘要（原文）

> Deep learning models have achieved great success on various vision
> challenges, but a well-trained model would face drastic performance degradation
> when applied to unseen data. Since the model is sensitive to domain shift,
> unsupervised domain adaptation attempts to reduce the domain gap and avoid
> costly annotation of unseen domains. This paper proposes a novel framework for
> cross-modality segmentation via similarity-based prototypes. In specific, we
> learn class-wise prototypes within an embedding space, then introduce a
> similarity constraint to make these prototypes representative for each semantic
> class while separable from different classes. Moreover, we use dictionaries to
> store prototypes extracted from different images, which prevents the
> class-missing problem and enables the contrastive learning of prototypes, and
> further improves performance. Extensive experiments show that our method
> achieves better results than other state-of-the-art methods.

