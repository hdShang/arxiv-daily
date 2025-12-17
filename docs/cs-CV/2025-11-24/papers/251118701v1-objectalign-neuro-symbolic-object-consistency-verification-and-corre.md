---
layout: default
title: ObjectAlign: Neuro-Symbolic Object Consistency Verification and Correction
---

# ObjectAlign: Neuro-Symbolic Object Consistency Verification and Correction

**arXiv**: [2511.18701v1](https://arxiv.org/abs/2511.18701) | [PDF](https://arxiv.org/pdf/2511.18701.pdf)

**作者**: Mustafa Munir, Harsh Goel, Xiwen Wei, Minkyu Choi, Sahil Shah, Kartikeya Bhardwaj, Paul Whatmough, Sandeep Chinchali, Radu Marculescu

---

## 💡 一句话要点

**提出ObjectAlign框架，通过神经符号方法检测和修正视频编辑中的对象不一致问题。**

**关键词**: `视频编辑一致性` `神经符号验证` `对象检测修正` `时间逻辑规范` `自适应帧修复`

## 📋 核心要点

1. 视频编辑常导致对象闪烁和身份漂移，降低感知质量。
2. 结合可学习指标阈值与神经符号验证器，确保对象一致性和时间保真度。
3. 在DAVIS和Pexels数据集上，CLIP分数和warp误差显著优于基线方法。

## 📄 摘要（原文）

> Video editing and synthesis often introduce object inconsistencies, such as frame flicker and identity drift that degrade perceptual quality. To address these issues, we introduce ObjectAlign, a novel framework that seamlessly blends perceptual metrics with symbolic reasoning to detect, verify, and correct object-level and temporal inconsistencies in edited video sequences. The novel contributions of ObjectAlign are as follows: First, we propose learnable thresholds for metrics characterizing object consistency (i.e. CLIP-based semantic similarity, LPIPS perceptual distance, histogram correlation, and SAM-derived object-mask IoU). Second, we introduce a neuro-symbolic verifier that combines two components: (a) a formal, SMT-based check that operates on masked object embeddings to provably guarantee that object identity does not drift, and (b) a temporal fidelity check that uses a probabilistic model checker to verify the video's formal representation against a temporal logic specification. A frame transition is subsequently deemed "consistent" based on a single logical assertion that requires satisfying both the learned metric thresholds and this unified neuro-symbolic constraint, ensuring both low-level stability and high-level temporal correctness. Finally, for each contiguous block of flagged frames, we propose a neural network based interpolation for adaptive frame repair, dynamically choosing the interpolation depth based on the number of frames to be corrected. This enables reconstruction of the corrupted frames from the last valid and next valid keyframes. Our results show up to 1.4 point improvement in CLIP Score and up to 6.1 point improvement in warp error compared to SOTA baselines on the DAVIS and Pexels video datasets.

