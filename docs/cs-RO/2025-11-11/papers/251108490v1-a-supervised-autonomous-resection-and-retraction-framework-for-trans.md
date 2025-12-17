---
layout: default
title: A Supervised Autonomous Resection and Retraction Framework for Transurethral Enucleation of the Prostatic Median Lobe
---

# A Supervised Autonomous Resection and Retraction Framework for Transurethral Enucleation of the Prostatic Median Lobe

**arXiv**: [2511.08490v1](https://arxiv.org/abs/2511.08490) | [PDF](https://arxiv.org/pdf/2511.08490.pdf)

**作者**: Mariana Smith, Tanner Watts, Susheela Sharma Stern, Brendan Burkhart, Hao Li, Alejandro O. Chara, Nithesh Kumar, James Ferguson, Ayberk Acar, Jesse F. d'Almeida, Lauren Branscombe, Lauren Shepard, Ahmed Ghazi, Ipek Oguz, Jie Ying Wu, Robert J. Webster, Axel Krieger, Alan Kuntz

---

## 💡 一句话要点

**提出基于模型规划与学习网络的半自主切除框架，用于经尿道前列腺中叶机器人手术**

**关键词**: `同心管机器人` `半自主手术` `图像引导规划` `学习网络` `前列腺切除` `机器人控制`

## 📋 核心要点

1. 核心问题：实现经尿道机器人手术中前列腺中叶的精确半自主切除
2. 方法要点：结合模型规划器生成工具轨迹与学习网络执行牵拉操作
3. 实验效果：在前列腺模型上实现97.1%目标体积切除，验证可行性

## 📄 摘要（原文）

> Concentric tube robots (CTRs) offer dexterous motion at millimeter scales, enabling minimally invasive procedures through natural orifices. This work presents a coordinated model-based resection planner and learning-based retraction network that work together to enable semi-autonomous tissue resection using a dual-arm transurethral concentric tube robot (the Virtuoso). The resection planner operates directly on segmented CT volumes of prostate phantoms, automatically generating tool trajectories for a three-phase median lobe resection workflow: left/median trough resection, right/median trough resection, and median blunt dissection. The retraction network, PushCVAE, trained on surgeon demonstrations, generates retractions according to the procedural phase. The procedure is executed under Level-3 (supervised) autonomy on a prostate phantom composed of hydrogel materials that replicate the mechanical and cutting properties of tissue. As a feasibility study, we demonstrate that our combined autonomous system achieves a 97.1% resection of the targeted volume of the median lobe. Our study establishes a foundation for image-guided autonomy in transurethral robotic surgery and represents a first step toward fully automated minimally-invasive prostate enucleation.

