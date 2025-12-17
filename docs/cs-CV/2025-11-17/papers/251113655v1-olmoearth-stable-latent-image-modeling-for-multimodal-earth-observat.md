---
layout: default
title: OlmoEarth: Stable Latent Image Modeling for Multimodal Earth Observation
---

# OlmoEarth: Stable Latent Image Modeling for Multimodal Earth Observation

**arXiv**: [2511.13655v1](https://arxiv.org/abs/2511.13655) | [PDF](https://arxiv.org/pdf/2511.13655.pdf)

**作者**: Henry Herzog, Favyen Bastani, Yawen Zhang, Gabriel Tseng, Joseph Redmon, Hadrien Sablon, Ryan Park, Jacob Morrison, Alexandra Buraczynski, Karen Farley, Joshua Hansen, Andrew Howe, Patrick Alan Johnson, Mark Otterlee, Ted Schmitt, Hunter Pitelka, Stephen Daspit, Rachel Ratner, Christopher Wilhelm, Sebastian Wood, Mike Jacobi, Hannah Kerner, Evan Shelhamer, Ali Farhadi, Ranjay Krishna, Patrick Beukema

---

## 💡 一句话要点

**提出OlmoEarth多模态时空基础模型以解决地球观测数据挑战**

**关键词**: `多模态学习` `时空建模` `自监督学习` `地球观测` `基础模型` `掩码策略`

## 📋 核心要点

1. 地球观测数据具有空间、时序和多模态特性，带来独特建模挑战。
2. 采用自监督学习、掩码策略和损失函数，专为地球观测领域设计。
3. 在多个基准测试和实际任务中，性能优于12个其他基础模型。

## 📄 摘要（原文）

> Earth observation data presents a unique challenge: it is spatial like images, sequential like video or text, and highly multimodal. We present OlmoEarth: a multimodal, spatio-temporal foundation model that employs a novel self-supervised learning formulation, masking strategy, and loss all designed for the Earth observation domain. OlmoEarth achieves state-of-the-art performance compared to 12 other foundation models across a variety of research benchmarks and real-world tasks from external partners. When evaluating embeddings OlmoEarth achieves the best performance on 15 out of 24 tasks, and with full fine-tuning it is the best on 19 of 29 tasks. We deploy OlmoEarth as the backbone of an end-to-end platform for data collection, labeling, training, and inference of Earth observation models. The OlmoEarth Platform puts frontier foundation models and powerful data management tools into the hands of non-profits and NGOs working to solve the world's biggest problems. OlmoEarth source code, training data, and pre-trained weights are available at $\href{https://github.com/allenai/olmoearth_pretrain}{\text{https://github.com/allenai/olmoearth_pretrain}}$.

