---
layout: default
title: Re$^{\text{2}}$MaP: Macro Placement by Recursively Prototyping and Packing Tree-based Relocating
---

# Re$^{\text{2}}$MaP: Macro Placement by Recursively Prototyping and Packing Tree-based Relocating

**arXiv**: [2511.08054v1](https://arxiv.org/abs/2511.08054) | [PDF](https://arxiv.org/pdf/2511.08054.pdf)

**作者**: Yunqi Shi, Xi Lin, Zhiang Wang, Siyuan Xu, Shixiong Kai, Yao Lai, Chengrui Gao, Ke Xue, Mingxuan Yuan, Chao Qian, Zhi-Hua Zhou

---

## 💡 一句话要点

**提出Re²MaP方法，通过递归原型和树状重定位优化宏布局，提升芯片设计质量**

**关键词**: `宏布局优化` `芯片物理设计` `递归原型` `树状重定位` `PPA优化` `进化搜索`

## 📋 核心要点

1. 核心问题：优化宏布局以改善芯片性能、功耗和面积，应对复杂设计约束
2. 方法要点：结合多级分组、原型构建、角度优化和树状重定位，迭代改进布局
3. 实验效果：相比先进方法，WNS和TNS平均提升10.26%和33.97%，多项指标更优

## 📄 摘要（原文）

> This work introduces the Re$^{\text{2}}$MaP method, which generates expert-quality macro placements through recursively prototyping and packing tree-based relocating. We first perform multi-level macro grouping and PPA-aware cell clustering to produce a unified connection matrix that captures both wirelength and dataflow among macros and clusters. Next, we use DREAMPlace to build a mixed-size placement prototype and obtain reference positions for each macro and cluster. Based on this prototype, we introduce ABPlace, an angle-based analytical method that optimizes macro positions on an ellipse to distribute macros uniformly near chip periphery, while optimizing wirelength and dataflow. A packing tree-based relocating procedure is then designed to jointly adjust the locations of macro groups and the macros within each group, by optimizing an expertise-inspired cost function that captures various design constraints through evolutionary search. Re$^{\text{2}}$MaP repeats the above process: Only a subset of macro groups are positioned in each iteration, and the remaining macros are deferred to the next iteration to improve the prototype's accuracy. Using a well-established backend flow with sufficient timing optimizations, Re$^{\text{2}}$MaP achieves up to 22.22% (average 10.26%) improvement in worst negative slack (WNS) and up to 97.91% (average 33.97%) improvement in total negative slack (TNS) compared to the state-of-the-art academic placer Hier-RTLMP. It also ranks higher on WNS, TNS, power, design rule check (DRC) violations, and runtime than the conference version ReMaP, across seven tested cases. Our code is available at https://github.com/lamda-bbo/Re2MaP.

