---
layout: default
title: MatchAttention: Matching the Relative Positions for High-Resolution Cross-View Matching
---

# MatchAttention: Matching the Relative Positions for High-Resolution Cross-View Matching

**arXiv**: [2510.14260v1](https://arxiv.org/abs/2510.14260) | [PDF](https://arxiv.org/pdf/2510.14260.pdf)

**作者**: Tingman Yan, Tao Liu, Xilian Yang, Qunfei Zhao, Zeyang Xia

---

## 💡 一句话要点

**提出MatchAttention机制以解决高分辨率跨视图匹配的效率和精度问题**

**关键词**: `跨视图匹配` `注意力机制` `立体匹配` `高分辨率图像处理` `实时推理`

## 📋 核心要点

1. 核心问题：高分辨率图像跨视图匹配存在二次复杂度和缺乏显式匹配约束的挑战
2. 方法要点：通过BilinearSoftmax实现连续可微滑动窗口注意力采样，迭代更新相对位置
3. 实验或效果：在多个基准数据集上达到SOTA，支持实时高分辨率处理，如4K图像0.1秒推理

## 📄 摘要（原文）

> Cross-view matching is fundamentally achieved through cross-attention
> mechanisms. However, matching of high-resolution images remains challenging due
> to the quadratic complexity and lack of explicit matching constraints in the
> existing cross-attention. This paper proposes an attention mechanism,
> MatchAttention, that dynamically matches relative positions. The relative
> position determines the attention sampling center of the key-value pairs given
> a query. Continuous and differentiable sliding-window attention sampling is
> achieved by the proposed BilinearSoftmax. The relative positions are
> iteratively updated through residual connections across layers by embedding
> them into the feature channels. Since the relative position is exactly the
> learning target for cross-view matching, an efficient hierarchical cross-view
> decoder, MatchDecoder, is designed with MatchAttention as its core component.
> To handle cross-view occlusions, gated cross-MatchAttention and a
> consistency-constrained loss are proposed. These two components collectively
> mitigate the impact of occlusions in both forward and backward passes, allowing
> the model to focus more on learning matching relationships. When applied to
> stereo matching, MatchStereo-B ranked 1st in average error on the public
> Middlebury benchmark and requires only 29ms for KITTI-resolution inference.
> MatchStereo-T can process 4K UHD images in 0.1 seconds using only 3GB of GPU
> memory. The proposed models also achieve state-of-the-art performance on KITTI
> 2012, KITTI 2015, ETH3D, and Spring flow datasets. The combination of high
> accuracy and low computational complexity makes real-time, high-resolution, and
> high-accuracy cross-view matching possible. Code is available at
> https://github.com/TingmanYan/MatchAttention.

