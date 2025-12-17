---
layout: default
title: SLIM-VDB: A Real-Time 3D Probabilistic Semantic Mapping Framework
---

# SLIM-VDB: A Real-Time 3D Probabilistic Semantic Mapping Framework

**arXiv**: [2512.12945v1](https://arxiv.org/abs/2512.12945) | [PDF](https://arxiv.org/pdf/2512.12945.pdf)

**作者**: Anja Sheppard, Parker Ewen, Joey Wilson, Advaith V. Sethuraman, Benard Adewole, Anran Li, Yuzhen Chen, Ram Vasudevan, Katherine A. Skinner

---

## 💡 一句话要点

**提出SLIM-VDB框架，利用OpenVDB数据结构实现实时3D概率语义建图，支持闭集和开集语义融合。**

**关键词**: `3D语义建图` `概率语义融合` `OpenVDB数据结构` `实时建图` `闭集与开集字典`

## 📋 核心要点

1. 现有语义建图系统缺乏统一框架支持固定类别和开放语言标签预测的集成。
2. 采用OpenVDB数据结构，结合贝叶斯更新框架，实现闭集和开集语义的概率融合。
3. 相比当前先进方法，显著减少内存占用和集成时间，同时保持可比建图精度。

## 📄 摘要（原文）

> This paper introduces SLIM-VDB, a new lightweight semantic mapping system with probabilistic semantic fusion for closed-set or open-set dictionaries. Advances in data structures from the computer graphics community, such as OpenVDB, have demonstrated significantly improved computational and memory efficiency in volumetric scene representation. Although OpenVDB has been used for geometric mapping in robotics applications, semantic mapping for scene understanding with OpenVDB remains unexplored. In addition, existing semantic mapping systems lack support for integrating both fixed-category and open-language label predictions within a single framework. In this paper, we propose a novel 3D semantic mapping system that leverages the OpenVDB data structure and integrates a unified Bayesian update framework for both closed- and open-set semantic fusion. Our proposed framework, SLIM-VDB, achieves significant reduction in both memory and integration times compared to current state-of-the-art semantic mapping approaches, while maintaining comparable mapping accuracy. An open-source C++ codebase with a Python interface is available at https://github.com/umfieldrobotics/slim-vdb.

