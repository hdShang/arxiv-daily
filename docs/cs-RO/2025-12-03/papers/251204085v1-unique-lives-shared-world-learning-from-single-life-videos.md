---
layout: default
title: Unique Lives, Shared World: Learning from Single-Life Videos
---

# Unique Lives, Shared World: Learning from Single-Life Videos

**arXiv**: [2512.04085v1](https://arxiv.org/abs/2512.04085) | [PDF](https://arxiv.org/pdf/2512.04085.pdf)

**作者**: Tengda Han, Sayna Ebrahimi, Dilara Gokay, Li Yang Ku, Maks Ovsjanikov, Iva Babukova, Daniel Zoran, Viorica Patraucean, Joao Carreira, Andrew Zisserman, Dima Damen

---

## 💡 一句话要点

**提出单一生学习范式，利用个人第一视角视频进行自监督视觉编码器训练。**

**关键词**: `单一生学习` `自监督学习` `第一视角视频` `几何表示学习` `跨注意力度量` `深度估计`

## 📋 核心要点

1. 核心问题：探索从单一生命视频中学习视觉表示的有效性，以应对数据多样性和泛化挑战。
2. 方法要点：基于多视角自监督学习，训练独立模型，并引入跨注意力度量评估表示对齐。
3. 实验或效果：模型在几何理解上对齐，能泛化到深度估计等任务，单周数据性能媲美多样网络数据。

## 📄 摘要（原文）

> We introduce the "single-life" learning paradigm, where we train a distinct vision model exclusively on egocentric videos captured by one individual. We leverage the multiple viewpoints naturally captured within a single life to learn a visual encoder in a self-supervised manner. Our experiments demonstrate three key findings. First, models trained independently on different lives develop a highly aligned geometric understanding. We demonstrate this by training visual encoders on distinct datasets each capturing a different life, both indoors and outdoors, as well as introducing a novel cross-attention-based metric to quantify the functional alignment of the internal representations developed by different models. Second, we show that single-life models learn generalizable geometric representations that effectively transfer to downstream tasks, such as depth estimation, in unseen environments. Third, we demonstrate that training on up to 30 hours from one week of the same person's life leads to comparable performance to training on 30 hours of diverse web data, highlighting the strength of single-life representation learning. Overall, our results establish that the shared structure of the world, both leads to consistency in models trained on individual lives, and provides a powerful signal for visual representation learning.

