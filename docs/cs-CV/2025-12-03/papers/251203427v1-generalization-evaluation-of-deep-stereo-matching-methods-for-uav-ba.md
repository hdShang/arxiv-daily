---
layout: default
title: Generalization Evaluation of Deep Stereo Matching Methods for UAV-Based Forestry Applications
---

# Generalization Evaluation of Deep Stereo Matching Methods for UAV-Based Forestry Applications

**arXiv**: [2512.03427v1](https://arxiv.org/abs/2512.03427) | [PDF](https://arxiv.org/pdf/2512.03427.pdf)

**作者**: Yida Lin, Bing Xue, Mengjie Zhang, Sam Schofield, Richard Green

---

## 💡 一句话要点

**评估八种深度立体匹配方法在无人机林业应用中的零样本泛化性能**

**关键词**: `立体匹配` `无人机林业` `零样本泛化` `深度估计` `跨域评估` `植被场景`

## 📋 核心要点

1. 核心问题：现有立体匹配方法在植被密集的林业场景中缺乏跨域泛化评估，存在研究空白。
2. 方法要点：系统评估八种先进方法，涵盖迭代优化、基础模型和零样本适应范式，使用Scene Flow训练并在多个基准上零样本测试。
3. 实验或效果：发现方法性能依赖场景，基础模型在结构化场景表现优，迭代方法跨域稳健，DEFOM在林业数据上表现最佳。

## 📄 摘要（原文）

> Autonomous UAV forestry operations require robust depth estimation methods with strong cross-domain generalization. However, existing evaluations focus on urban and indoor scenarios, leaving a critical gap for specialized vegetation-dense environments. We present the first systematic zero-shot evaluation of eight state-of-the-art stereo methods--RAFT-Stereo, IGEV, IGEV++, BridgeDepth, StereoAnywhere, DEFOM (plus baseline methods ACVNet, PSMNet, TCstereo)--spanning iterative refinement, foundation model, and zero-shot adaptation paradigms. All methods are trained exclusively on Scene Flow and evaluated without fine-tuning on four standard benchmarks (ETH3D, KITTI 2012/2015, Middlebury) plus a novel 5,313-pair Canterbury forestry dataset captured with ZED Mini camera (1920x1080). Performance reveals scene-dependent patterns: foundation models excel on structured scenes (BridgeDepth: 0.23 px on ETH3D, 0.83-1.07 px on KITTI; DEFOM: 0.35-4.65 px across benchmarks), while iterative methods maintain cross-domain robustness (IGEV++: 0.36-6.77 px; IGEV: 0.33-21.91 px). Critical finding: RAFT-Stereo exhibits catastrophic ETH3D failure (26.23 px EPE, 98 percent error rate) due to negative disparity predictions, while performing normally on KITTI (0.90-1.11 px). Qualitative evaluation on Canterbury forestry dataset identifies DEFOM as the optimal gold-standard baseline for vegetation depth estimation, exhibiting superior depth smoothness, occlusion handling, and cross-domain consistency compared to IGEV++, despite IGEV++'s finer detail preservation.

