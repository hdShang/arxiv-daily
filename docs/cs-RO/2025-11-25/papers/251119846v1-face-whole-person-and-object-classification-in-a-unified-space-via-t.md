---
layout: default
title: Face, Whole-Person, and Object Classification in a Unified Space Via The Interleaved Multi-Domain Identity Curriculum
---

# Face, Whole-Person, and Object Classification in a Unified Space Via The Interleaved Multi-Domain Identity Curriculum

**arXiv**: [2511.19846v1](https://arxiv.org/abs/2511.19846) | [PDF](https://arxiv.org/pdf/2511.19846.pdf)

**作者**: Thomas M Metz, Matthew Q Hill, Alice J O'Toole

---

## 💡 一句话要点

**提出交错多域身份课程以在统一嵌入空间中实现多任务分类，避免灾难性遗忘**

**关键词**: `多任务学习` `灾难性遗忘` `嵌入空间统一` `基础模型微调` `交错训练`

## 📋 核心要点

1. 核心问题：视觉基础模型微调后易发生灾难性遗忘，难以同时处理多任务
2. 方法要点：引入交错多域身份课程，同步微调基础模型于四个任务
3. 实验或效果：在EVA-02和CLIP上表现媲美专家，优于人类多任务能力

## 📄 摘要（原文）

> Vision foundation models can perform generalized object classification in zero-shot mode, and face/person recognition when they are fine-tuned. However, fine-tuned models suffer from catastrophic forgetting. We create models that perform four tasks (object recognition, face recognition from high- and low-quality images, and person recognition from whole-body images) in a single embedding space -- without incurring substantial catastrophic forgetting. To accomplish this, we introduce two variants of the Interleaved Multi-Domain Identity Curriculum (IMIC): a gradient-coupled, interleaving training schedule that fine-tunes a foundation backbone simultaneously on all four tasks. The IMIC method proved effective with three foundation model bases: DINOv3, CLIP, and EVA-02. Two of these (EVA-02 and CLIP) performed comparably with domain experts on all four tasks concurrently and were more accurate than humans at multi-tasking across face, body, and object datasets. Further, we demonstrate that our approach does not substantially harm out-of-distribution generalization, thus maintaining a key property of foundation models. Analysis of the most accurate model variants (EVA-02 + IMIC A and B) showed linearly separable representations of the four tasks in the unified embedding space, but with substantial sharing of features across tasks. Fewer than 100 PCs calculated from any one task could perform all other tasks with nearly zero performance degradation.

