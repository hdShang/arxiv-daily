---
layout: default
title: Relational Visual Similarity
---

# Relational Visual Similarity

**arXiv**: [2512.07833v1](https://arxiv.org/abs/2512.07833) | [PDF](https://arxiv.org/pdf/2512.07833.pdf)

**作者**: Thao Nguyen, Sicheng Mo, Krishna Kumar Singh, Yilin Wang, Jing Shi, Nicholas Kolkin, Eli Shechtman, Yong Jae Lee, Yuheng Li

---

## 💡 一句话要点

**提出关系视觉相似性度量方法，通过匿名化数据集微调视觉语言模型以捕捉图像间关系逻辑。**

**关键词**: `关系视觉相似性` `匿名化数据集` `视觉语言模型微调` `图像关系逻辑` `相似性度量`

## 📋 核心要点

1. 核心问题：现有视觉相似性度量（如LPIPS、CLIP）仅关注感知属性相似性，无法捕捉人类感知的关系相似性。
2. 方法要点：构建114k匿名化图像-描述数据集，描述场景关系逻辑而非表面内容，并微调视觉语言模型以测量关系相似性。
3. 实验或效果：模型能连接图像底层关系结构，揭示现有模型在关系相似性捕捉上的关键差距，具有实际应用潜力。

## 📄 摘要（原文）

> Humans do not just see attribute similarity -- we also see relational similarity. An apple is like a peach because both are reddish fruit, but the Earth is also like a peach: its crust, mantle, and core correspond to the peach's skin, flesh, and pit. This ability to perceive and recognize relational similarity, is arguable by cognitive scientist to be what distinguishes humans from other species. Yet, all widely used visual similarity metrics today (e.g., LPIPS, CLIP, DINO) focus solely on perceptual attribute similarity and fail to capture the rich, often surprising relational similarities that humans perceive. How can we go beyond the visible content of an image to capture its relational properties? How can we bring images with the same relational logic closer together in representation space? To answer these questions, we first formulate relational image similarity as a measurable problem: two images are relationally similar when their internal relations or functions among visual elements correspond, even if their visual attributes differ. We then curate 114k image-caption dataset in which the captions are anonymized -- describing the underlying relational logic of the scene rather than its surface content. Using this dataset, we finetune a Vision-Language model to measure the relational similarity between images. This model serves as the first step toward connecting images by their underlying relational structure rather than their visible appearance. Our study shows that while relational similarity has a lot of real-world applications, existing image similarity models fail to capture it -- revealing a critical gap in visual computing.

