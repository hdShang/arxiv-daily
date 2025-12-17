---
layout: default
title: MVAFormer: RGB-based Multi-View Spatio-Temporal Action Recognition with Transformer
---

# MVAFormer: RGB-based Multi-View Spatio-Temporal Action Recognition with Transformer

**arXiv**: [2511.02473v1](https://arxiv.org/abs/2511.02473) | [PDF](https://arxiv.org/pdf/2511.02473.pdf)

**作者**: Taiga Yamane, Satoshi Suzuki, Ryo Masumura, Shotaro Tora

---

## 💡 一句话要点

**提出MVAFormer以解决多视角时空动作识别中的协作问题**

**关键词**: `多视角动作识别` `时空动作识别` `Transformer` `特征图协作` `自注意力机制`

## 📋 核心要点

1. 核心问题：现有多视角动作识别方法不适用于时空动作识别设置，无法处理序列化个人动作识别。
2. 方法要点：引入基于Transformer的协作模块，利用特征图保留空间信息，并分视图自注意力建模关系。
3. 实验或效果：在新数据集上，F-measure比基线提升约4.4点，验证方法有效性。

## 📄 摘要（原文）

> Multi-view action recognition aims to recognize human actions using multiple
> camera views and deals with occlusion caused by obstacles or crowds. In this
> task, cooperation among views, which generates a joint representation by
> combining multiple views, is vital. Previous studies have explored promising
> cooperation methods for improving performance. However, since their methods
> focus only on the task setting of recognizing a single action from an entire
> video, they are not applicable to the recently popular spatio-temporal action
> recognition~(STAR) setting, in which each person's action is recognized
> sequentially. To address this problem, this paper proposes a multi-view action
> recognition method for the STAR setting, called MVAFormer. In MVAFormer, we
> introduce a novel transformer-based cooperation module among views. In contrast
> to previous studies, which utilize embedding vectors with lost spatial
> information, our module utilizes the feature map for effective cooperation in
> the STAR setting, which preserves the spatial information. Furthermore, in our
> module, we divide the self-attention for the same and different views to model
> the relationship between multiple views effectively. The results of experiments
> using a newly collected dataset demonstrate that MVAFormer outperforms the
> comparison baselines by approximately $4.4$ points on the F-measure.

