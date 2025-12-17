---
layout: default
title: ImageGem: In-the-wild Generative Image Interaction Dataset for Generative Model Personalization
---

# ImageGem: In-the-wild Generative Image Interaction Dataset for Generative Model Personalization

**arXiv**: [2510.18433v1](https://arxiv.org/abs/2510.18433) | [PDF](https://arxiv.org/pdf/2510.18433.pdf)

**作者**: Yuanhe Guo, Linxi Xie, Zhuoran Chen, Kangrui Yu, Ryan Po, Guandao Yang, Gordon Wetztein, Hongyi Wen

---

## 💡 一句话要点

**提出ImageGem数据集以解决生成模型个性化中细粒度用户偏好标注缺失问题**

**关键词**: `生成模型个性化` `用户偏好数据集` `偏好对齐模型` `个性化图像检索` `扩散模型编辑`

## 📋 核心要点

1. 核心问题：缺乏真实世界细粒度用户偏好标注，阻碍生成模型个性化发展。
2. 方法要点：构建包含57K用户交互数据的数据集，支持偏好对齐模型训练。
3. 实验或效果：数据集提升偏好对齐模型性能，并探索个性化检索与推荐。

## 📄 摘要（原文）

> We introduce ImageGem, a dataset for studying generative models that
> understand fine-grained individual preferences. We posit that a key challenge
> hindering the development of such a generative model is the lack of in-the-wild
> and fine-grained user preference annotations. Our dataset features real-world
> interaction data from 57K users, who collectively have built 242K customized
> LoRAs, written 3M text prompts, and created 5M generated images. With user
> preference annotations from our dataset, we were able to train better
> preference alignment models. In addition, leveraging individual user
> preference, we investigated the performance of retrieval models and a
> vision-language model on personalized image retrieval and generative model
> recommendation. Finally, we propose an end-to-end framework for editing
> customized diffusion models in a latent weight space to align with individual
> user preferences. Our results demonstrate that the ImageGem dataset enables,
> for the first time, a new paradigm for generative model personalization.

