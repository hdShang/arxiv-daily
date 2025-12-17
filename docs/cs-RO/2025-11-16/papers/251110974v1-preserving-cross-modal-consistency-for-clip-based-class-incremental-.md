---
layout: default
title: Preserving Cross-Modal Consistency for CLIP-based Class-Incremental Learning
---

# Preserving Cross-Modal Consistency for CLIP-based Class-Incremental Learning

**arXiv**: [2511.10974v1](https://arxiv.org/abs/2511.10974) | [PDF](https://arxiv.org/pdf/2511.10974.pdf)

**作者**: Haoran Chen, Houze Xu, Micah Goldblum, Daoguo Dong, Zuxuan Wu

---

## 💡 一句话要点

**提出DMC框架以解决CLIP类增量学习中的跨模态对齐问题**

**关键词**: `类增量学习` `跨模态对齐` `软提示优化` `最优传输校准` `视觉语言模型` `生成式回放`

## 📋 核心要点

1. 核心问题：CLIP类增量学习中文本原型过拟合新类导致分类器偏差
2. 方法要点：两阶段框架解耦视觉编码器和文本软提示优化以保持跨模态一致性
3. 实验或效果：在多个数据集上实现SOTA，DMC-OT平均提升准确率1.80%

## 📄 摘要（原文）

> Class-incremental learning (CIL) enables models to continuously learn new categories from sequential tasks without forgetting previously acquired knowledge. While recent advances in vision-language models such as CLIP have demonstrated strong generalization across domains, extending them to continual settings remains challenging. In particular, learning task-specific soft prompts for newly introduced classes often leads to severe classifier bias, as the text prototypes overfit to recent categories when prior data are unavailable. In this paper, we propose DMC, a simple yet effective two-stage framework for CLIP-based CIL that decouples the adaptation of the vision encoder and the optimization of textual soft prompts. Each stage is trained with the other frozen, allowing one modality to act as a stable semantic anchor for the other to preserve cross-modal alignment. Furthermore, current CLIP-based CIL approaches typically store class-wise Gaussian statistics for generative replay, yet they overlook the distributional drift that arises when the vision encoder is updated over time. To address this issue, we introduce DMC-OT, an enhanced version of DMC that incorporates an optimal-transport guided calibration strategy to align memory statistics across evolving encoders, along with a task-specific prompting design that enhances inter-task separability. Extensive experiments on CIFAR-100, Imagenet-R, CUB-200, and UCF-101 demonstrate that both DMC and DMC-OT achieve state-of-the-art performance, with DMC-OT further improving accuracy by an average of 1.80%.

