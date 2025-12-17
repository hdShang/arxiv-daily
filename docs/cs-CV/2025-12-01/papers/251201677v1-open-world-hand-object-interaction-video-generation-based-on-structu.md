---
layout: default
title: Open-world Hand-Object Interaction Video Generation Based on Structure and Contact-aware Representation
---

# Open-world Hand-Object Interaction Video Generation Based on Structure and Contact-aware Representation

**arXiv**: [2512.01677v1](https://arxiv.org/abs/2512.01677) | [PDF](https://arxiv.org/pdf/2512.01677.pdf)

**作者**: Haodong Yan, Hang Yu, Zhide Zhong, Weilin Yuan, Xin Gong, Zehang Luo, Chengxi Heyu, Junfeng Li, Wenxuan Song, Shunbo Zhou, Haoang Li

---

## 💡 一句话要点

**提出结构-接触感知表示以解决开放世界手物交互视频生成中物理约束建模的难题**

**关键词**: `手物交互视频生成` `结构-接触感知表示` `开放世界泛化` `物理约束建模` `联合生成范式`

## 📋 核心要点

1. 核心问题：手物交互视频生成中，现有2D与3D表示难以兼顾可扩展性和交互保真度
2. 方法要点：设计无3D标注的结构-接触感知表示，捕获接触、遮挡和整体结构，并采用共享-专业化联合生成范式
3. 实验或效果：在真实数据集上超越先进方法，生成物理真实且时序连贯的视频，并展示对开放世界场景的强泛化能力

## 📄 摘要（原文）

> Generating realistic hand-object interactions (HOI) videos is a significant challenge due to the difficulty of modeling physical constraints (e.g., contact and occlusion between hands and manipulated objects). Current methods utilize HOI representation as an auxiliary generative objective to guide video synthesis. However, there is a dilemma between 2D and 3D representations that cannot simultaneously guarantee scalability and interaction fidelity. To address this limitation, we propose a structure and contact-aware representation that captures hand-object contact, hand-object occlusion, and holistic structure context without 3D annotations. This interaction-oriented and scalable supervision signal enables the model to learn fine-grained interaction physics and generalize to open-world scenarios. To fully exploit the proposed representation, we introduce a joint-generation paradigm with a share-and-specialization strategy that generates interaction-oriented representations and videos. Extensive experiments demonstrate that our method outperforms state-of-the-art methods on two real-world datasets in generating physics-realistic and temporally coherent HOI videos. Furthermore, our approach exhibits strong generalization to challenging open-world scenarios, highlighting the benefit of our scalable design. Our project page is https://hgzn258.github.io/SCAR/.

