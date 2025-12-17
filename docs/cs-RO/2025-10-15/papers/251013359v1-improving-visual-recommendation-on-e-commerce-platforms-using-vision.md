---
layout: default
title: Improving Visual Recommendation on E-commerce Platforms Using Vision-Language Models
---

# Improving Visual Recommendation on E-commerce Platforms Using Vision-Language Models

**arXiv**: [2510.13359v1](https://arxiv.org/abs/2510.13359) | [PDF](https://arxiv.org/pdf/2510.13359.pdf)

**作者**: Yuki Yada, Sho Akiyama, Ryo Watanabe, Yuta Ueno, Yusuke Shido, Andre Rusli

---

## 💡 一句话要点

**提出基于视觉语言模型的视觉推荐方法，以提升电商平台产品发现效率。**

**关键词**: `视觉语言模型` `产品推荐` `SigLIP` `图像嵌入` `电商平台` `A/B测试`

## 📋 核心要点

1. 核心问题：电商平台需高效推荐视觉相似产品，以匹配用户偏好。
2. 方法要点：微调SigLIP模型，利用图像-标题对生成嵌入用于推荐系统。
3. 实验效果：离线nDCG@5提升9.1%，在线点击率增50%，转化率增14%。

## 📄 摘要（原文）

> On large-scale e-commerce platforms with tens of millions of active monthly
> users, recommending visually similar products is essential for enabling users
> to efficiently discover items that align with their preferences. This study
> presents the application of a vision-language model (VLM) -- which has
> demonstrated strong performance in image recognition and image-text retrieval
> tasks -- to product recommendations on Mercari, a major consumer-to-consumer
> marketplace used by more than 20 million monthly users in Japan. Specifically,
> we fine-tuned SigLIP, a VLM employing a sigmoid-based contrastive loss, using
> one million product image-title pairs from Mercari collected over a three-month
> period, and developed an image encoder for generating item embeddings used in
> the recommendation system. Our evaluation comprised an offline analysis of
> historical interaction logs and an online A/B test in a production environment.
> In offline analysis, the model achieved a 9.1% improvement in nDCG@5 compared
> with the baseline. In the online A/B test, the click-through rate improved by
> 50% whereas the conversion rate improved by 14% compared with the existing
> model. These results demonstrate the effectiveness of VLM-based encoders for
> e-commerce product recommendations and provide practical insights into the
> development of visual similarity-based recommendation systems.

