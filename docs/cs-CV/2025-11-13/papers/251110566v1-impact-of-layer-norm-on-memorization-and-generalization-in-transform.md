---
layout: default
title: Impact of Layer Norm on Memorization and Generalization in Transformers
---

# Impact of Layer Norm on Memorization and Generalization in Transformers

**arXiv**: [2511.10566v1](https://arxiv.org/abs/2511.10566) | [PDF](https://arxiv.org/pdf/2511.10566.pdf)

**作者**: Rishi Singhal, Jung-Eun Kim

---

## 💡 一句话要点

**分析LayerNorm在Pre-与Post-LayerNorm Transformer中对记忆化和学习的影响**

**关键词**: `LayerNorm` `Transformer架构` `记忆化分析` `学习稳定性` `视觉语言数据集` `梯度流优化`

## 📋 核心要点

1. 核心问题：LayerNorm在Pre-和Post-LayerNorm Transformer中对记忆化和学习的作用机制不明确。
2. 方法要点：比较Pre-和Post-LayerNorm架构，移除LayerNorm参数以分析其对稳定性和记忆化的影响。
3. 实验或效果：在6个视觉和语言数据集上验证，发现早期层LayerNorm最关键，影响因架构而异。

## 📄 摘要（原文）

> Layer Normalization (LayerNorm) is one of the fundamental components in transformers that stabilizes training and improves optimization. In recent times, Pre-LayerNorm transformers have become the preferred choice over Post-LayerNorm transformers due to their stable gradient flow. However, the impact of LayerNorm on learning and memorization across these architectures remains unclear. In this work, we investigate how LayerNorm influences memorization and learning for Pre- and Post-LayerNorm transformers. We identify that LayerNorm serves as a key factor for stable learning in Pre-LayerNorm transformers, while in Post-LayerNorm transformers, it impacts memorization. Our analysis reveals that eliminating LayerNorm parameters in Pre-LayerNorm models exacerbates memorization and destabilizes learning, while in Post-LayerNorm models, it effectively mitigates memorization by restoring genuine labels. We further precisely identify that early layers LayerNorm are the most critical over middle/later layers and their influence varies across Pre and Post LayerNorm models. We have validated it through 13 models across 6 Vision and Language datasets. These insights shed new light on the role of LayerNorm in shaping memorization and learning in transformers.

