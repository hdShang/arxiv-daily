---
layout: default
title: Verifying Rumors via Stance-Aware Structural Modeling
---

# Verifying Rumors via Stance-Aware Structural Modeling

**arXiv**: [2512.13559v1](https://arxiv.org/abs/2512.13559) | [PDF](https://arxiv.org/pdf/2512.13559.pdf)

**作者**: Gibson Nkhata, Uttamasha Anjally Oyshi, Quan Mai, Susan Gauch

---

## 💡 一句话要点

**提出基于立场感知的结构建模方法，以增强社交媒体谣言验证的准确性。**

**关键词**: `社交媒体谣言验证` `立场感知建模` `对话结构分析` `Transformer编码器` `跨平台泛化`

## 📋 核心要点

1. 核心问题：现有模型难以同时捕捉语义内容、立场信息和对话结构，尤其在Transformer编码器的序列长度限制下。
2. 方法要点：通过编码帖子及其立场信号，按立场类别聚合回复嵌入，并引入立场分布和层次深度作为协变量，以增强结构感知。
3. 实验或效果：在基准数据集上显著优于先前方法，验证了模型在谣言真实性预测、早期检测和跨平台泛化方面的有效性。

## 📄 摘要（原文）

> Verifying rumors on social media is critical for mitigating the spread of false information. The stances of conversation replies often provide important cues to determine a rumor's veracity. However, existing models struggle to jointly capture semantic content, stance information, and conversation strructure, especially under the sequence length constraints of transformer-based encoders. In this work, we propose a stance-aware structural modeling that encodes each post in a discourse with its stance signal and aggregates reply embedddings by stance category enabling a scalable and semantically enriched representation of the entire thread. To enhance structural awareness, we introduce stance distribution and hierarchical depth as covariates, capturing stance imbalance and the influence of reply depth. Extensive experiments on benchmark datasets demonstrate that our approach significantly outperforms prior methods in the ability to predict truthfulness of a rumor. We also demonstrate that our model is versatile for early detection and cross-platfrom generalization.

