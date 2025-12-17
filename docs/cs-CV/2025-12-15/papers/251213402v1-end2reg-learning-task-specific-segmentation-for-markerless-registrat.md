---
layout: default
title: End2Reg: Learning Task-Specific Segmentation for Markerless Registration in Spine Surgery
---

# End2Reg: Learning Task-Specific Segmentation for Markerless Registration in Spine Surgery

**arXiv**: [2512.13402v1](https://arxiv.org/abs/2512.13402) | [PDF](https://arxiv.org/pdf/2512.13402.pdf)

**作者**: Lorenzo Pettinari, Sidaty El Hadramy, Michael Wehrli, Philippe C. Cattin, Daniel Studer, Carol C. Hasler, Maria Licci

---

## 💡 一句话要点

**提出End2Reg端到端深度学习框架，以解决脊柱手术中无标记注册依赖弱分割标签的问题。**

**关键词**: `脊柱手术导航` `无标记注册` `端到端学习` `RGB-D注册` `分割优化` `深度学习框架`

## 📋 核心要点

1. 脊柱手术导航需毫米级精度，现有基于X光和骨锚标记的方法有创且干扰工作流。
2. End2Reg联合优化分割与注册，无需弱分割标签或手动步骤，仅通过注册目标指导学习。
3. 在离体和在体基准测试中，中位目标注册误差降低32%至1.83mm，均方根误差降低45%至3.95mm。

## 📄 摘要（原文）

> Purpose: Intraoperative navigation in spine surgery demands millimeter-level accuracy. Current systems based on intraoperative radiographic imaging and bone-anchored markers are invasive, radiation-intensive and workflow disruptive. Recent markerless RGB-D registration methods offer a promising alternative, but existing approaches rely on weak segmentation labels to isolate relevant anatomical structures, which can propagate errors throughout registration. Methods: We present End2Reg an end-to-end deep learning framework that jointly optimizes segmentation and registration, eliminating the need for weak segmentation labels and manual steps. The network learns segmentation masks specifically optimized for registration, guided solely by the registration objective without direct segmentation supervision. Results: The proposed framework achieves state-of-the-art performance on ex- and in-vivo benchmarks, reducing median Target Registration Error by 32% to 1.83mm and mean Root Mean Square Error by 45% to 3.95mm, respectively. An ablation study confirms that end-to-end optimization significantly improves registration accuracy. Conclusion: The presented end-to-end RGB-D registration pipeline removes dependency on weak labels and manual steps, advancing towards fully automatic, markerless intraoperative navigation. Code and interactive visualizations are available at: https://lorenzopettinari.github.io/end-2-reg/.

