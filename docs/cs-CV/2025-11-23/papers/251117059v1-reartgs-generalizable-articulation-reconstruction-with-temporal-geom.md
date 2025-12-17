---
layout: default
title: REArtGS++: Generalizable Articulation Reconstruction with Temporal Geometry Constraint via Planar Gaussian Splatting
---

# REArtGS++: Generalizable Articulation Reconstruction with Temporal Geometry Constraint via Planar Gaussian Splatting

**arXiv**: [2511.17059v1](https://arxiv.org/abs/2511.17059) | [PDF](https://arxiv.org/pdf/2511.17059.pdf)

**作者**: Di Wu, Liu Liu, Anran Huang, Yuyan Liu, Qiaoyu Jun, Shaofan Liu, Liangtu Song, Cewu Lu

---

## 💡 一句话要点

**提出REArtGS++以解决铰接物体重建中螺丝关节和多部件挑战，引入时间几何约束与平面高斯溅射**

**关键词**: `铰接物体重建` `高斯溅射` `时间几何约束` `关节参数估计` `部件级表面重建`

## 📋 核心要点

1. 核心问题：铰接物体如抽屉的重建在螺丝关节和多部件时困难，且缺乏未见状态的几何约束。
2. 方法要点：建模解耦螺丝运动，通过部件运动混合优化高斯与关节参数，并施加平面和时间一致正则化。
3. 实验或效果：在合成和真实铰接物体上优于现有方法，实现泛化部件级表面重建和关节参数估计。

## 📄 摘要（原文）

> Articulated objects are pervasive in daily environments, such as drawers and refrigerators. Towards their part-level surface reconstruction and joint parameter estimation, REArtGS~\cite{wu2025reartgs} introduces a category-agnostic approach using multi-view RGB images at two different states. However, we observe that REArtGS still struggles with screw-joint or multi-part objects and lacks geometric constraints for unseen states. In this paper, we propose REArtGS++, a novel method towards generalizable articulated object reconstruction with temporal geometry constraint and planar Gaussian splatting. We first model a decoupled screw motion for each joint without type prior, and jointly optimize part-aware Gaussians with joint parameters through part motion blending. To introduce time-continuous geometric constraint for articulated modeling, we encourage Gaussians to be planar and propose a temporally consistent regularization between planar normal and depth through Taylor first-order expansion. Extensive experiments on both synthetic and real-world articulated objects demonstrate our superiority in generalizable part-level surface reconstruction and joint parameter estimation, compared to existing approaches. Project Site: https://sites.google.com/view/reartgs2/home.

