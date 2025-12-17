---
layout: default
title: NoPe-NeRF++: Local-to-Global Optimization of NeRF with No Pose Prior
---

# NoPe-NeRF++: Local-to-Global Optimization of NeRF with No Pose Prior

**arXiv**: [2511.17322v1](https://arxiv.org/abs/2511.17322) | [PDF](https://arxiv.org/pdf/2511.17322.pdf)

**作者**: Dongbo Shi, Shen Cao, Bojian Wu, Jinhui Guo, Lubin Fan, Renjie Chen, Ligang Liu, Jieping Ye

---

## 💡 一句话要点

**提出NoPe-NeRF++，通过局部到全局优化在无姿态先验下训练NeRF。**

**关键词**: `神经辐射场` `相机姿态估计` `局部优化` `全局优化` `束调整` `新视角合成`

## 📋 核心要点

1. 核心问题：现有方法在复杂场景中难以恢复准确相机姿态。
2. 方法要点：结合局部联合优化与全局束调整，提升姿态估计。
3. 实验或效果：在基准数据集上优于先进方法，验证鲁棒性。

## 📄 摘要（原文）

> In this paper, we introduce NoPe-NeRF++, a novel local-to-global optimization algorithm for training Neural Radiance Fields (NeRF) without requiring pose priors. Existing methods, particularly NoPe-NeRF, which focus solely on the local relationships within images, often struggle to recover accurate camera poses in complex scenarios. To overcome the challenges, our approach begins with a relative pose initialization with explicit feature matching, followed by a local joint optimization to enhance the pose estimation for training a more robust NeRF representation. This method significantly improves the quality of initial poses. Additionally, we introduce global optimization phase that incorporates geometric consistency constraints through bundle adjustment, which integrates feature trajectories to further refine poses and collectively boost the quality of NeRF. Notably, our method is the first work that seamlessly combines the local and global cues with NeRF, and outperforms state-of-the-art methods in both pose estimation accuracy and novel view synthesis. Extensive evaluations on benchmark datasets demonstrate our superior performance and robustness, even in challenging scenes, thus validating our design choices.

