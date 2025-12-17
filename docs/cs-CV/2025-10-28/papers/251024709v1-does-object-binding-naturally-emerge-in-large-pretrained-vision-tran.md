---
layout: default
title: Does Object Binding Naturally Emerge in Large Pretrained Vision Transformers?
---

# Does Object Binding Naturally Emerge in Large Pretrained Vision Transformers?

**arXiv**: [2510.24709v1](https://arxiv.org/abs/2510.24709) | [PDF](https://arxiv.org/pdf/2510.24709.pdf)

**作者**: Yihao Li, Saeed Salehi, Lyle Ungar, Konrad P. Kording

---

## 💡 一句话要点

**揭示自监督ViT中自然涌现对象绑定能力，提升下游任务性能**

**关键词**: `视觉Transformer` `对象绑定` `自监督学习` `注意力机制` `补丁嵌入` `下游任务`

## 📋 核心要点

1. 核心问题：预训练ViT是否自然具备对象绑定能力，即识别图像补丁是否属于同一对象。
2. 方法要点：使用相似性探针从ViT补丁嵌入解码IsSameObject属性，分析其编码与注意力引导。
3. 实验效果：自监督ViT对象绑定准确率超90%，优于监督模型，消融实验显示其服务于预训练目标。

## 📄 摘要（原文）

> Object binding, the brain's ability to bind the many features that
> collectively represent an object into a coherent whole, is central to human
> cognition. It groups low-level perceptual features into high-level object
> representations, stores those objects efficiently and compositionally in
> memory, and supports human reasoning about individual object instances. While
> prior work often imposes object-centric attention (e.g., Slot Attention)
> explicitly to probe these benefits, it remains unclear whether this ability
> naturally emerges in pre-trained Vision Transformers (ViTs). Intuitively, they
> could: recognizing which patches belong to the same object should be useful for
> downstream prediction and thus guide attention. Motivated by the quadratic
> nature of self-attention, we hypothesize that ViTs represent whether two
> patches belong to the same object, a property we term IsSameObject. We decode
> IsSameObject from patch embeddings across ViT layers using a similarity probe,
> which reaches over 90% accuracy. Crucially, this object-binding capability
> emerges reliably in self-supervised ViTs (DINO, MAE, CLIP), but markedly weaker
> in ImageNet-supervised models, suggesting that binding is not a trivial
> architectural artifact, but an ability acquired through specific pretraining
> objectives. We further discover that IsSameObject is encoded in a
> low-dimensional subspace on top of object features, and that this signal
> actively guides attention. Ablating IsSameObject from model activations
> degrades downstream performance and works against the learning objective,
> implying that emergent object binding naturally serves the pretraining
> objective. Our findings challenge the view that ViTs lack object binding and
> highlight how symbolic knowledge of "which parts belong together" emerges
> naturally in a connectionist system.

