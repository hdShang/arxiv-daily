---
layout: default
title: WithAnyone: Towards Controllable and ID Consistent Image Generation
---

# WithAnyone: Towards Controllable and ID Consistent Image Generation

**arXiv**: [2510.14975v1](https://arxiv.org/abs/2510.14975) | [PDF](https://arxiv.org/pdf/2510.14975.pdf)

**作者**: Hengyuan Xu, Wei Cheng, Peng Xing, Yixiao Fang, Shuhan Wu, Rui Wang, Xianfang Zeng, Daxin Jiang, Gang Yu, Xingjun Ma, Yu-Gang Jiang

---

## 💡 一句话要点

**提出WithAnyone模型以解决身份一致图像生成中的复制粘贴问题**

**关键词**: `身份一致生成` `扩散模型` `复制粘贴缓解` `可控图像生成` `对比学习` `多身份数据集`

## 📋 核心要点

1. 核心问题：现有模型因依赖重建训练，易产生复制粘贴，限制姿态和表情可控性。
2. 方法要点：构建MultiID-2M数据集，引入对比身份损失，平衡身份保真与多样性。
3. 实验或效果：模型显著减少复制粘贴，提升可控性，保持高身份相似和感知质量。

## 📄 摘要（原文）

> Identity-consistent generation has become an important focus in text-to-image
> research, with recent models achieving notable success in producing images
> aligned with a reference identity. Yet, the scarcity of large-scale paired
> datasets containing multiple images of the same individual forces most
> approaches to adopt reconstruction-based training. This reliance often leads to
> a failure mode we term copy-paste, where the model directly replicates the
> reference face rather than preserving identity across natural variations in
> pose, expression, or lighting. Such over-similarity undermines controllability
> and limits the expressive power of generation. To address these limitations, we
> (1) construct a large-scale paired dataset MultiID-2M, tailored for
> multi-person scenarios, providing diverse references for each identity; (2)
> introduce a benchmark that quantifies both copy-paste artifacts and the
> trade-off between identity fidelity and variation; and (3) propose a novel
> training paradigm with a contrastive identity loss that leverages paired data
> to balance fidelity with diversity. These contributions culminate in
> WithAnyone, a diffusion-based model that effectively mitigates copy-paste while
> preserving high identity similarity. Extensive qualitative and quantitative
> experiments demonstrate that WithAnyone significantly reduces copy-paste
> artifacts, improves controllability over pose and expression, and maintains
> strong perceptual quality. User studies further validate that our method
> achieves high identity fidelity while enabling expressive controllable
> generation.

