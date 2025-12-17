---
layout: default
title: LoMix: Learnable Weighted Multi-Scale Logits Mixing for Medical Image Segmentation
---

# LoMix: Learnable Weighted Multi-Scale Logits Mixing for Medical Image Segmentation

**arXiv**: [2510.22995v1](https://arxiv.org/abs/2510.22995) | [PDF](https://arxiv.org/pdf/2510.22995.pdf)

**作者**: Md Mostafijur Rahman, Radu Marculescu

---

## 💡 一句话要点

**提出LoMix模块，通过可学习加权多尺度logits融合提升医学图像分割性能。**

**关键词**: `医学图像分割` `多尺度融合` `可学习权重` `U形网络` `零推理开销`

## 📋 核心要点

1. U形网络多尺度logits训练时孤立处理，未充分利用粗-细预测融合互补信息。
2. LoMix使用四种轻量融合算子混合logits，并学习软加损失权重，实现零推理开销。
3. 在多个基准测试中，DICE提升达+13.5%，数据稀缺时优势更显著。

## 📄 摘要（原文）

> U-shaped networks output logits at multiple spatial scales, each capturing a
> different blend of coarse context and fine detail. Yet, training still treats
> these logits in isolation - either supervising only the final,
> highest-resolution logits or applying deep supervision with identical loss
> weights at every scale - without exploring mixed-scale combinations.
> Consequently, the decoder output misses the complementary cues that arise only
> when coarse and fine predictions are fused. To address this issue, we introduce
> LoMix (Logits Mixing), a NAS-inspired, differentiable plug-and-play module that
> generates new mixed-scale outputs and learns how exactly each of them should
> guide the training process. More precisely, LoMix mixes the multi-scale decoder
> logits with four lightweight fusion operators: addition, multiplication,
> concatenation, and attention-based weighted fusion, yielding a rich set of
> synthetic mutant maps. Every original or mutant map is given a softplus loss
> weight that is co-optimized with network parameters, mimicking a one-step
> architecture search that automatically discovers the most useful scales,
> mixtures, and operators. Plugging LoMix into recent U-shaped architectures
> (i.e., PVT-V2-B2 backbone with EMCAD decoder) on Synapse 8-organ dataset
> improves DICE by +4.2% over single-output supervision, +2.2% over deep
> supervision, and +1.5% over equally weighted additive fusion, all with zero
> inference overhead. When training data are scarce (e.g., one or two labeled
> scans), the advantage grows to +9.23%, underscoring LoMix's data efficiency.
> Across four benchmarks and diverse U-shaped networks, LoMiX improves DICE by up
> to +13.5% over single-output supervision, confirming that learnable weighted
> mixed-scale fusion generalizes broadly while remaining data efficient, fully
> interpretable, and overhead-free at inference. Our code is available at
> https://github.com/SLDGroup/LoMix.

